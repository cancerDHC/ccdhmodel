import os
import unittest

from linkml_runtime.loaders import  json_loader, rdf_loader

from crdch_model.crdch_model import AlcoholExposureObservation

CWD = os.path.abspath(os.path.dirname(__file__))

INPUT_DIR = os.path.join(CWD, 'secondary_inputs')


class InputFileTestCase(unittest.TestCase):
    def test_alcohol_file(self):
        nyaml, njson, nttl = 0, 0, 0
        pyaml, pjson, pttl = 0, 0, 0
        nread, nfailures = 0, 0
        print("AlcoholExposureObservation test")
        alcohol_data_filename = 'test_AlcoholExposureObservation.json'
        alcohol_data_filepath = os.path.join(INPUT_DIR, alcohol_data_filename)
        print("Attempting to load " + alcohol_data_filepath + " as one or more AlcoholExposureObservation(s)")

        try:
            njson += 1
            Diagnosis = json_loader.load(alcohol_data_filepath, AlcoholExposureObservation)
            pjson += 1
            print("Successfully parsed:")
            print(Diagnosis)
        except Exception as e:
            print(e)
            nfailures += 1
        self.assertEqual(0, nfailures)

if __name__ == '__main__':
    unittest.main()
