from sheet2linkml.model import ModelElement
from linkml_model.meta import Element
from linkml_model.types import Uriorcurie
import re
import urllib
import csv
import logging
from enum import Enum
from dataclasses import dataclass


class MappingRelations(Enum):
    SKOS_BROAD_MATCH = "skos:broadMatch"
    SKOS_NARROW_MATCH = "skos:narrowMatch"
    SKOS_EXACT_MATCH = "skos:exactMatch"
    SKOS_CLOSE_MATCH = "skos:closeMatch"
    SKOS_RELATED_MATCH = "skos:relatedMatch"


class Mappings:
    """
    In our Google Sheets document, mappings are stored within a single cell in the following format:
        "LINKML:String (exact match)
        XML:string  (exact match)
        JSON:string  (exact match)
        FHIR:string (does not allow zero-length strings and limits the length of the string to 1024x1024 characters)"

    Thus, each mapping consists of:
        - The URI being mapped to
        - The relation of the map

    In LinkML, mappings (https://linkml.github.io/linkml-model/docs/mappings/) are of five kinds, all of which are of the
    UriORCURIE type and which are subproperties of `mappings` (:B is mapped to :A somehow -- the parent concept of the
    other five mappings)
    1. broad mappings (:B is a broader concept than :A)
    2. narrow mappings (:B is a narrower concept than :A)
    3. exact mappings (:B and :A can be used interchangeably across a wide range of information retrieval applications)
    4. close mappings (:B and :A are sufficiently similar that they can be used interchangeably in some applications)
    5. related mapping (:B and :A are related in some way -- "used to state an associative mapping link between two concepts")

    In order to fit the one into the other, things that can have mappings (entities and types, to begin with) will
    invoke Mappings() to wrap over their mapping fields. Mappings() can provide a list of individual mappings to various
    concepts. However, the most likely way of using this would be to pass it a LinkML Element, to which it will add the
    appropriate mappings in the most appropriate category. Since there is no space for metadata in LinkML, we will
    necessary lose some information -- however, to reaccess that information, you can iterate over all Mappings() objects,
    which can provide a method to create a CSV containing *all* of the mapping information in the original file.
    """

    def __init__(self, mapping_from: ModelElement):
        """
        Read sets of mappings from around a single text, presumably from a Google Sheet.
        """
        self.source_element = mapping_from
        self.mappings = []

    @dataclass
    class Mapping:
        """
        An individual mapping represents the mapping between one ModelElement (such as a type or an entity)
        and some URIorCURIE, with an enum representating a relation and a textual description of the relationship.
        """

        source: ModelElement
        target: Uriorcurie
        description: str
        relation: MappingRelations

    def add_mappings(
        self,
        mapping_string: str,
        default_relation: MappingRelations = MappingRelations.SKOS_RELATED_MATCH,
    ) -> list[Mapping]:
        """
        Add mappings from the provided mapping string with the specified default relation.
        """

        if mapping_string is None or len(mapping_string.strip()) == 0:
            return

        rows = re.split(r"\s*[\r\n\|]+\s*", mapping_string)

        for row in rows:
            # Is the row empty? If so, ignore it.
            if row.strip() == "":
                continue

            # There are three kinds of rows:
            #   - [mapping target]
            #   - [mapping target]([description])
            #   - [mapping target]([relation type])
            # We can use regular expression to differentiate between them.
            mapping_target = row
            description = None
            relation = default_relation

            match = re.match(r"^\s*(.*?)\s*\(\s*(.*)\s*\)\s*$", row)
            if match:
                mapping_target = match.group(1)
                description = match.group(2)

            lower_desc = (description or "").lower()
            if (
                lower_desc == "skos:exactMatch"
                or lower_desc == "exact"
                or lower_desc.startswith("exact match")
            ):
                relation = MappingRelations.SKOS_EXACT_MATCH
            elif (
                lower_desc == "skos:closeMatch"
                or lower_desc == "close"
                or lower_desc.startswith("close match")
            ):
                relation = MappingRelations.SKOS_CLOSE_MATCH
            elif (
                lower_desc == "skos:relatedMatch"
                or lower_desc == "related"
                or lower_desc.startswith("related match")
            ):
                relation = MappingRelations.SKOS_RELATED_MATCH
            elif (
                lower_desc == "skos:broadMatch"
                or lower_desc == "broad"
                or lower_desc.startswith("broad match")
            ):
                relation = MappingRelations.SKOS_BROAD_MATCH
            elif (
                lower_desc == "skos:narrowMatch"
                or lower_desc == "narrow"
                or lower_desc.startswith("narrow match")
            ):
                relation = MappingRelations.SKOS_NARROW_MATCH
            elif lower_desc.strip() == "":
                # If no description is given, we'll use the default relation instead.
                relation = default_relation
            else:
                logging.warning(
                    f"In entity {self.source_element.name}: mapping type '{lower_desc}' could not be mapped to LinkML, "
                    + "assuming it is a description."
                )

            # TODO: Eventually, we should enforce that the input is already a Uriorcurie.
            # But for now, we need to support two formats:
            #   - (GDC|PDC|ICDC|...).(Entity).(property)...
            #   - Any other kind of string
            # For the former, we will map it to `GDC:(Entity).(property)...`.
            # For the latter, we will map it to `example:(URL-encoded string)`.
            uri_or_curie = None
            match = re.match(r"^([A-Z]+)(?:\.|:)(.*)$", mapping_target)
            if match:
                # Note that in this case we don't sanitize the CURIE at all -- if there any spaces, they'll remain here!
                uri_or_curie = Uriorcurie(f"{match.group(1)}:{match.group(2).strip()}")
            else:
                uri_or_curie = Uriorcurie(
                    f"example:{urllib.parse.quote_plus(mapping_target.strip())}"
                )

            self.mappings.append(
                Mappings.Mapping(
                    source=self.source_element,
                    target=uri_or_curie,
                    description=description,
                    relation=relation,
                )
            )

    def set_mappings_on_element(self, element: Element):
        """
        This method will append the mappings in this Mappings object to the specified element.
        """

        for mapping in self.mappings:
            if mapping.relation == MappingRelations.SKOS_BROAD_MATCH:
                element.broad_mappings.append(mapping.target)
            elif mapping.relation == MappingRelations.SKOS_NARROW_MATCH:
                element.narrow_mappings.append(mapping.target)
            elif mapping.relation == MappingRelations.SKOS_EXACT_MATCH:
                element.exact_mappings.append(mapping.target)
            elif mapping.relation == MappingRelations.SKOS_CLOSE_MATCH:
                element.close_mappings.append(mapping.target)
            elif mapping.relation == MappingRelations.SKOS_RELATED_MATCH:
                element.related_mappings.append(mapping.target)
            else:
                element.mappings.append(mapping.target)

    @classmethod
    def write_to_file(cls, mappings: list[Mapping], filename: str, model):
        """
        Write the list of mappings to a filename, provided as a string.

        mapping: A list of Mappings.Mapping objects to write.
        filename: A filename to write to. If None, no file will be written.
        model: The GSheetModel these mappings are a part of.
        """
        if filename is None:
            raise RuntimeError(
                "Mappings.write_to_file() needs a `filename` parameter with the output file to write."
            )

        if model is None:
            raise RuntimeError(
                "Mappings.write_to_file() needs a `model` parameter with the GSheetModel being used."
            )

        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile, dialect="excel-tab")
            writer.writerow(
                [
                    "subject_id",
                    "subject_category",
                    "predicate_id",
                    "object_id",
                    "comment",
                    "match_type",
                    "mapping_set_id",
                    "mapping_set_version",
                    "creator_id",
                    "mapping_date",
                ]
            )

            for mapping in mappings:
                # See if we can figure out the range of this datatype/entity/attribute.
                source_range = None
                if hasattr(mapping.source, "range"):
                    source_range = mapping.source.range

                writer.writerow(
                    [
                        mapping.source.full_name,
                        source_range,
                        mapping.relation.value,
                        mapping.target,
                        mapping.description,
                        "SSSOMC:HumanCurated",
                        model.full_name,
                        model.version,
                        model.last_updated,
                    ]
                )
