import numpy as np
import time

#Global variables
computedStatistics = None

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    # Your code starts here #
    for row in range(height):
        features.append([]);
        for column in range(width):
            if(digit_data[row][column] == '#' or digit_data[row][column] == '+' or digit_data[row][column] == 1 or digit_data[row][column] == 2):
                features[row].append(True)
            else:
                features[row].append(False)
    # Your code ends here #
    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    # Your code starts here #
    # Your code ends here #
    _raise_not_defined()
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here #
    # Your code ends here #
    _raise_not_defined()
    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=1.0):
    # Your code starts here #
    global computedStatistics

    #k = smoothing factor. Currently choosing arbitrary k
    k = 1.0
    #Get percentage of data
    partialDataSize = int(len(data)*percentage)
    partialData = data[0:partialDataSize]

    #Calculate smoothed prior distribution and store indices of each occurrence of each number in indexLists
    numberOccurrence = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    priorDistribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    indexLists = [[], [], [], [], [], [], [], [], [], []]
    dataSize = len(partialData)

    index = 0
    for number in label:
        numberOccurrence[number] += 1.0
        indexLists[number].append(index)
        index += 1

    #Reset index counter
    index = 0
    for occurrenceCount in numberOccurrence:
        priorDistribution[index] = (k + occurrenceCount) / (k + dataSize)
        index += 1
    priorDistribution = np.log(priorDistribution)

    #Calculate conditional distribution
    conditionalProbabilitiesList = [[], [], [], [], [], [], [], [], [], []]
    cplIndex = 0
    #Go through numbers 0 to 9, get and store number of times number occurs in data set
    for number in indexLists:
        numberInstanceCount = len(number)
        trueCount = np.zeros((len(data[number[0]]), len(data[number[0]])))

        #Go through each instance of a number (e.g. all 1's)
        for instanceIndex in number:
            pixelInstanceCount = 0
            #Get image object
            numberImage = data[instanceIndex]
            extractedFeatures = feature_extractor(numberImage, width, height)
            #Go through each pixel in the image and increment trueCount if it is a feature
            for row in range(0, len(extractedFeatures)):
                for column in range(0, len(extractedFeatures[row])):
                    if(extractedFeatures[row][column]):
                        trueCount[row][column] += 1

        #Calculate smoothed conditional probabilities of each pixel for this number
        conditionalProbabilities = np.zeros((len(trueCount), len(trueCount)))
        for row in range(0, len(conditionalProbabilities)):
            for column in range(0, len(conditionalProbabilities[row])):
                conditionalProbabilities[row][column] = (k + trueCount[row][column]) / (k + numberInstanceCount)
        #Now have 2D array for conditional probabilities of each pixel for a number
        conditionalProbabilities = np.log(conditionalProbabilities)
        conditionalProbabilitiesList[cplIndex] = conditionalProbabilities
        cplIndex += 1
    #Should now have list of 2D arrays containing smoothed conditional probabilities for each pixel for each number in conditionalProbabilitiesList

    computedStatistics = [priorDistribution, conditionalProbabilitiesList]
    '''
    print
    print "Printing computedStatistics"
    print str(computedStatistics)
    '''
    # Your code ends here #
    return

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = -1
    #features is the list of lists of True/False that represent the number image
    # Your code starts here #
    global computedStatistics
    classifierSum = []

    #min(computedStatistics[1 (conditional probabilities)][0 (number to look at)][0 (row number)])) should always be the computed statistic of a zero value
    print str(min(computedStatistics[1][0][0]))
    zeroValue = min(computedStatistics[1][0][0])
    priorIndex = 0

    for number in computedStatistics[1]:
        sumCp = computedStatistics[0][priorIndex]
        row = 0
        for rowElement in number:
            column = 0
            for columnElement in rowElement:
                if(features[row][column] == 0):
                    oneProbability = np.exp(columnElement)
                    zeroProbability = 1 - oneProbability
                    loggedZeroProbability = np.log(zeroProbability)
                    sumCp += loggedZeroProbability
                else:
                    sumCp += columnElement
                column += 1
            row += 1
        classifierSum.append(sumCp)
        priorIndex += 1
    
    maxP = max(classifierSum)
    predicted = classifierSum.index(maxP)
    # Your code ends here #
    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):
    #Calls compute_class
    predicted=[]

    # Your code starts here #

    # Your code ends here #
    _raise_not_defined()
    return predicted







        
    
