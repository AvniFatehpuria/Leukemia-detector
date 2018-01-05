# Leukemia Predictor

A classification program implementing k-nearest neighbours to analyse csv files of gene data and determine the prognosis of leukemia patients. Uses n-fold cross validation. 
Main is in leukemia.py

## Usage
To use, write: python leukemiaPredictor.py k filename
(where k is the number of neighbours to consider)

example: python leukemiaPredictor.py 3 input/leukemiaPatients.csv
