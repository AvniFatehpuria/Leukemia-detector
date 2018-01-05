# Leukemia Predictor

A classification program implementing k-nearest neighbours to analyse csv files of gene data and determine the prognosis of leukemia patients. Uses n-fold cross validation. 
Main is in leukemia.py
The input file, leukemiaPatients.csv, is sourced from this paper: http://science.sciencemag.org/content/286/5439/531.long
Each line describes the expression values of one patient. Each column (except the last) is the expression value for one gene. 
The last column is the class for the sample: -1 for acute lymphoblastic leukemia (ALL) and 1 for acute myeloid leukemia (AML).

## Usage
To use, write: python leukemia.py k filename
(where k is the number of neighbours to consider)

example: python leukemia.py 3 input/leukemiaPatients.csv
