import pygsheets

from sheet2linkml.source.gsheetmodel.entity import Entity


class GSheetModel:
    """
    A GSheetModel represents a single, coherent model represented as a series of worksheets
    in Google Sheets. This representation is currently being developed by all the CCDH workstreams,
    and so it needs to be flexible enough to be modified extensively on the fly.

    If we ever extend sheet2linkml beyond Google Sheets, we should create a top-level Model
    class that generically represents a single, coherent model, and then make GSheetModel a
    subclass of that. But that's for another day.
    """

    """ The Google API scopes that are necessary to query this sheet. """
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly',
              'https://www.googleapis.com/auth/drive.metadata.readonly']

    def __init__(
            self,
            google_sheet_oath2_credentials: str,
            google_sheet_id: str
        ):
        """
        Create a new Google Sheet Model. This will create a model that uses the specified
        Google Sheet as an input.

        Note that creating a GSheetModel will kick off the Google Sheets authentication
        process, which will ask you to visit a website, log in with a Google account, and
        then to enter the provided code into this Python script. See
        https://pygsheets.readthedocs.io/en/stable/authorization.html for information on
        creating and downloading OAuth2 credentials from the Google Developers Console.
        Once you authenticate yourself, this script will create a file with your
        authentication token in your working directory, so you will not need to log in
        again from the same working directory.

        :param google_sheet_oath2_credentials: A file containing OAuth2 credential files.
        :param google_sheet_id: The Google Sheet ID containing the model.
        """

        self.client = pygsheets.authorize(client_secret=google_sheet_oath2_credentials, scopes=self.SCOPES)
        self.sheet = self.client.open_by_key(google_sheet_id)

    def entities(self) -> list:
        """
        A list of entities available in this model.

        We identify an entity based on having 'Status' as the first column header title.

        :return: A list of entities available in this model.
        """

        def is_sheet_entity(worksheet: pygsheets.worksheet):
            return worksheet.get_value('A1') == 'Status'

        worksheets = self.sheet.worksheets()
        entity_worksheets = filter(is_sheet_entity, worksheets)
        return [Entity(self, worksheet) for worksheet in entity_worksheets]

    def __str__(self) -> str:
        """
        :return: A string representation of this Google Sheet model.
        """

        return f'{self.__class__.__name__} with an underlying Google Sheet titled "{self.sheet.title}" containing {len(self.sheet.worksheets())} worksheets'