
import sys
import os
import unittest


# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model_training import train_model
from src.data_preprocessing import load_data

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        ratings, _ = load_data()
        model, testset = train_model(ratings)
        self.assertIsNotNone(model)
        self.assertIsNotNone(testset)

if __name__ == '__main__':
    unittest.main()
