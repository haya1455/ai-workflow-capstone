#!/usr/bin/env python
"""
model tests
"""

import sys, os
import unittest
sys.path.insert(1, os.path.join('..', os.getcwd()))

from pathlib import Path
sys.path.append(str(Path(os.getcwd()).parent))
## import model specific functions and variables
from src.model import *

import numpy as np

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """
        from src.config import MODEL_DIR
        ## train the model
        model_train('data/cs-train/', test=True)
        
        self.assertTrue(os.path.exists(os.path.join(MODEL_DIR, "test-all-0_1.joblib")))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## train the model
        all_data, all_models = model_load(prefix='test')
        
        countries = ['portugal', 'united_kingdom', 'hong_kong', 'eire', 'spain', 'france', 'singapore', 'all', 'norway', 'germany', 'netherlands']
        self.assertTrue(list(all_data.keys())[0] in countries)
        self.assertTrue(list(all_models.keys())[0] in countries)

       
    def test_03_predict(self):
        """
        test the predict function input
        """

        ## load model first
        model = model_load(prefix='test')
    
        ## ensure that a list can be passed
        country='all'
        year='2018'
        month='01'
        day='05'

        result = model_predict(country,year,month,day, test=True)
        y_pred = result['y_pred']
        
        self.assertTrue(type(y_pred[0]) == np.float64)
        
          
### Run the tests
if __name__ == '__main__':
    unittest.main()
