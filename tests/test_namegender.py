""" 

@copyright: 2018 samuorous <samuorous@gmail.com>
@licence: GPLv3
"""
import namegender
import os
import pkg_resources
from unittest import TestCase

MAPPING_PICKLE = pkg_resources.resource_filename('namegender', 'data/mapping.pickle')
here = os.path.abspath(os.path.dirname(__file__))


class TestNamegender(TestCase):
    def test_reload_mapping(self):
        namegender.reload_mapping()
        self.assertTrue(os.path.exists(MAPPING_PICKLE))
        self.assertTrue(os.path.isfile(MAPPING_PICKLE))

    def test_get_mapping(self):
        mapping = namegender.get_mapping()
        self.assertEqual(type(mapping), dict)
        self.assertTrue('otto' in mapping)
        self.assertEqual(type(mapping['otto']), dict)
        self.assertTrue(any(key in mapping['otto'] for key in ['male', 'female']))

    def test_predict(self):
        # Predict name in data
        prediction = namegender.predict('Otto')
        self.assertEqual(prediction['gender'], 'male')
        # Predict using explicit mapping
        prediction = namegender.predict('jane', {'jane': {'female': 75, 'male': 25}})
        self.assertEqual(prediction['gender'], 'female')
        self.assertEqual(prediction['probability'], 75)
        self.assertEqual(prediction['samples'], 100)
        # Predict name not in data.
        prediction = namegender.predict('Oofewefowqidqnxcqoenwoqiw')
        self.assertEqual(prediction['gender'], 'unknown')

    def test_predict_list(self):
        prediction = namegender.predict_list(['Jhon', 'Jane'])
        self.assertEqual(type(prediction), list)
        self.assertEqual(len(prediction), 2)
        self.assertEqual(prediction[0]['gender'], 'male')
        self.assertEqual(prediction[1]['gender'], 'female')

    def test_corrupted_data(self):
        namegender.MAPPING_TXT = os.path.join(here, 'data', 'corrupted_mapping_text.txt')
        namegender.reload_mapping()
        # Prediction should still work for correct lines.
        prediction = namegender.predict('aadarsh')
        self.assertEqual(prediction['gender'], 'male')
        # Set back to correct data.
        namegender.MAPPING_TXT = pkg_resources.resource_filename('namegender', 'data/gender_name_mapping.txt')
        namegender.reload_mapping()
