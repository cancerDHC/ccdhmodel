import os
import unittest

from linkml_runtime.loaders import  json_loader, rdf_loader

from crdch_model.crdch_model import TobaccoExposureObservation

CWD = os.path.abspath(os.path.dirname(__file__))

INPUT_DIR = os.path.join(CWD, 'secondary_inputs')


class InputFileTestCase(unittest.TestCase):
    def test_tobacco_file(self):
        nyaml, njson, nttl = 0, 0, 0
        pyaml, pjson, pttl = 0, 0, 0
        nread, nfailures = 0, 0
        print("TobaccoExposureObservation test")
        toboacco_data_filename = 'test_TobaccoExposureObservation.json'
        toboacco_data_filepath = os.path.join(INPUT_DIR, toboacco_data_filename)
        print("Attempting to load " + toboacco_data_filepath + " as one or more TobaccoExposureObservation(s)")

        try:
            njson += 1
            Diagnosis = json_loader.load(toboacco_data_filepath, TobaccoExposureObservation)
            pjson += 1
            print("Successfully parsed:")
            print(Diagnosis)
        except Exception as e:
            print(e)
            nfailures += 1
        self.assertEqual(0, nfailures)

if __name__ == '__main__':
    unittest.main()
