from classifiers import *
from sys import *

def parse():
    """ parses command line arguments and returns k and the data in the input file as a list of lists"""
    if len(argv)!= 3:
         print "wrong number of arguments; correct usage: python leukemia-detector k filename"
         exit(1)
    try:
        num_neighbours = int(argv[1])
        infile = open(argv[2], "r")
        plist = []
        for entry in infile:
            line = entry.strip()
            line = line.split(",")
            plist.append(line)
        return num_neighbours, plist

    except:
        print "failed to process input file"
        exit(1)

def output(predictions):
    """takes a list of predictions across folds and calculates _ prints the accuracy, sensitivity and specificity of the prediction"""
    truePositives = 0.0
    trueNegatives = 0.0
    falsePositives = 0.0
    falseNegatives = 0.0
    num_predictions = 0
    for fold in predictions:
        for data in fold:
            num_predictions+=1
            if data[0][-1] == '+1' or data[0][-1] == '1':
                if data[1] == 1:
                    truePositives += 1.0
                else:
                    falseNegatives += 1.0
            else:
                if data[1] == 1:
                    falsePositives += 1.0
                else:
                    trueNegatives += 1.0
    accuracy = float((trueNegatives + truePositives)/num_predictions)
    sensitivity = float(truePositives/(truePositives+falseNegatives))
    specificity = float(trueNegatives/(trueNegatives+falsePositives))
    print "Results:\n\nAccuracy: %.2f \nSensitivity: %.2f \nSpecificity: %.2f" % (accuracy, sensitivity, specificity)
    return

def main():
    numFolds = 5
    (num_neighbours, plist) = parse()
    (trainingFolds, testFolds) = generateFolds(numFolds, plist)
    prediction_list = []
    for i in range(len(trainingFolds)):
        prediction_list.append(kNearestNeighbours(trainingFolds[i], testFolds[i], num_neighbours))
    output(prediction_list)
    #print prediction_list
main()
