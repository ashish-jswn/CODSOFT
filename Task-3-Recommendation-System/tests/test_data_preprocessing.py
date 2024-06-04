import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_preprocessing import load_data

class TestDataPreprocessing(unittest.TestCase):
    def test_load_data(self):
        ratings, movies = load_data()
        self.assertFalse(ratings.empty)
        self.assertFalse(movies.empty)
        self.assertIn('userId', ratings.columns)
        self.assertIn('movieId', ratings.columns)
        self.assertIn('rating', ratings.columns)
        self.assertIn('title', movies.columns)

if __name__ == '__main__':
    unittest.main()


