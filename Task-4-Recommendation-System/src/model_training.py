
import sys
import os
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle


# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_preprocessing import load_data

def train_model(ratings):
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings, reader)
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    return model, testset

# Load data
ratings, movies = load_data()

# Train the SVD algorithm on the training set and get the testset
model, testset = train_model(ratings)

# Save the model
with open('models/recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Evaluate the model
predictions = model.test(testset)
from surprise import accuracy
accuracy.rmse(predictions)
