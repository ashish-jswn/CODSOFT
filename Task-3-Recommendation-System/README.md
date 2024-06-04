# Movie Recommendation System

This is a movie recommendation system built using collaborative filtering techniques with the `surprise` library. The system recommends movies to users based on their past ratings.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)


## Project Overview

The Movie Recommendation System is designed to suggest movies to users based on their preferences. It uses the SVD algorithm from the `surprise` library to predict user ratings for movies they have not yet rated, and then recommends the top-rated movies.

## Features

- Load and preprocess movie rating data
- Train a recommendation model using collaborative filtering
- Generate movie recommendations for a given user
- Simple GUI to input user ID and display recommendations
- Handle invalid user IDs gracefully

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ashish-nitrr-aws/movie-recommendation-system.git
   cd movie-recommendation-system

2. Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    pip install -r requirements.txt

## Usage

1. Train the Model:
    
    python src/model_training.py

2. Run the Recommendation System:

    python app.py

3. Use the GUI:

   i. Enter a user ID in the input field.
   ii. Click the "Get Recommendations" button.
   iii. The recommended movies will be displayed in a table.

## Project Structure

movie-recommendation-system/
│
├── data/
│   ├── ml-latest-small/
│   │   ├── links.csv
│   │   ├── movies.csv
│   │   ├── ratings.csv
│   │   └── tags.csv
│
├── models/
│   └── recommendation_model.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── recommend.py
│
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_model_training.py
│   └── test_recommend.py
│
├── notebooks/
│   ├── model_training.ipynb
│   └── data_exploration.ipynb
│
├── app.py
├── requirements.txt
└── README.md

## Testing

To run the tests, use the following command:

python -m unittest discover tests

