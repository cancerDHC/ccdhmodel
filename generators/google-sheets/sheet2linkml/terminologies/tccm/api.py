from sheet2linkml.terminologies.service import TerminologyService

import requests
from functools import cache
import logging
from datetime import datetime, timezone
import yaml


class TCCMService(TerminologyService):
    """
    Provides methods for accessing information in a TCCM Terminology Service.
    """

    def __init__(self, base_url: str):
        """Set up a TCCM Terminology Service access system based around the provided base_url."""
        self.base_url = base_url

    # This is unlikely to change during a run and is quite expensive (since we download it from the network), so
    # we memoize it.
    @cache
    def get_enum_values_for_field(self, field_name: str):
        """
        Returns information on the enum fields for a particular field.

        TODO: This is very vaguely specified right now in the interests of getting stuff out the door;
        I'll come back to this and clean this up later and make it a proper API method later.
        """

        # Construct the URL we need to access the enumeration information.
        url = f"{self.base_url}/enumerations/{field_name}"
        logging.debug(f"Querying TCCM for attribute info: {url}")

        # Query the URL.
        # We use ?value_only=false because "the value_only param sets whether the mapped ncit code is used".
        time_of_request = datetime.now(timezone.utc).isoformat()
        response = requests.get(
            url, headers={"accept": "application/x-yaml"}, params={"value_only": "true"}
        )
        if not response.ok:
            logging.debug(f"Error accessing TCCM Terminology Service: {response}")
            return {}

        # The output we receive is currently in YAML, so we need to convert that into Python dicts so we can
        # access them.
        enum_info = yaml.safe_load(response.text)

        # If there is no 'last_updated' field, assume that it was last updated when we made the request.
        if "last_updated" not in enum_info:
            enum_info["last_updated"] = time_of_request

        return enum_info
