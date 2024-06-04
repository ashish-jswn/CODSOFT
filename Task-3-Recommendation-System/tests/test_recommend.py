
import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.recommend import recommend
from src.data_preprocessing import load_data

class TestRecommend(unittest.TestCase):
    def test_recommend(self):
        ratings, _ = load_data()
        user_id = ratings['userId'].iloc[0]
        recommendations = recommend(user_id)
        self.assertIsNotNone(recommendations)

if __name__ == '__main__':
    unittest.main()
