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
    features = []
    rowIsEmpty = 0
    pixelBlock = 0
    foundHole = 0
    topHole = 0
    bottomHole = 0
    for row in range(height):
        features.append([]);
        print
        "Features after append in row: " + str(features)
        if (row > 0):
            for column in range(width):
                if (digit_data[row - 1][column] != '#' or digit_data[row - 1][column] != '+' or digit_data[row - 1][
                    column] != 1 or digit_data[row - 1][column] != 2):
                    print
                    "Features after insert in column: " + str(features)
                    rowIsEmpty = 1
                else:
                    rowIsEmpty = 0
        for column in range(width):
            if (rowIsEmpty == 1 and (digit_data[row][column] == '#' or digit_data[row][column] == '+' or digit_data[row][column] == 1 or
                    digit_data[row][column] == 2)):
                features[row].append(4)
            if (digit_data[row][column] == '#' or digit_data[row][column] == '+' or digit_data[row][column] == 1 or digit_data[row][column] == 2):
                pixelBlock += 1
            if(pixelBlock > 0 and (digit_data[row][column] != '#' or digit_data[row][column] != '+' or digit_data[row][column] != 1 or digit_data[row][column] != 2)):
                foundHole += 1
            if(pixelBlock > 0 and foundHole > 0):
                if(row < height/2):
                    topHole = 1
                if(row >= height/2):
                    bottomHole = 1
                pixelBlock = 0
                foundHole = 0
            if(topHole > 0 and bottomHole > 0):
                features[row].append(8)
                topHole = 0
                bottomHole = 0
                break
            if (topHole == 0 and bottomHole > 0):
                features[row].append(6)
                topHole = 0
                bottomHole = 0
                break
            if (topHole > 0 and bottomHole == 0):
                features[row].append(9)
                topHole = 0
                bottomHole = 0
                break
            else:
                features[row].append(0)

    '''
    for row in range(height / 2):
        print "row no." + str(row)
        features.append([]);
        width = 0
        innerCounter = 0
        rowCounter = 0
        if (digit_data[row][0] == '#' or digit_data[row][0] == '+'):
            for column in range(width):
                innerCounter = 1
                x = row
                if (digit_data[row][column] == '+' and digit_data[row][column + 1] == '0' and digit_data[row][
                    column + 2] == '0'):
                    rowCounter += 1
                    print " " + str(rowCounter)
                    break
            if (innerCounter > 0 and rowCounter > 0):
                topHole = 1
                x = row
                features[row].append(9)
                break
            else:
                topHole = 0
                x = row
                features[row].append(0)


    for row in range(height/2, height):
        width = 0
        innerCounter = 0
        rowCounter = 0
        if (digit_data[row][0] == '#' and digit_data[row][1] == '+'):
            for column in range(width):
                innerCounter += 1
                x = row
                if (digit_data[row][column] == '+' and digit_data[row][column + 1] == 0 and digit_data[row][
                    column + 2] == 0):
                    for x in range(height / 2, height):
                        if (digit_data[0][column] != '0' and digit_data[x][column] == 0):
                            rowCounter += 1
                        else:
                            break
                    break
            if (innerCounter > 0 and rowCounter > 0):
                bottomHole = 1
                if(topHole == 1):
                    features[row].append(8)
                else:
                    features[row].append(6)
                break
            else:
                bottomHole = 0
                features[row].append(0)

    '''
    print str(features)
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
    k = 1
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
        if(index >= partialDataSize):
            break
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

    #Go through numbers 0 to 9, get and store number of times number occurs in partial data set
    for number in indexLists:
        numberInstanceCount = len(number)
        dataLength = len(partialData[number[0]])
        trueCount = np.zeros((dataLength, dataLength))
        #Go through each instance of a number (e.g. all 1's)
        for instanceIndex in number:
            pixelInstanceCount = 0
            #Get image object
            numberImage = partialData[instanceIndex]
            extractedFeatures = feature_extractor(numberImage, width, height)

            if(isinstance(extractedFeatures[0][0], bool)):
                #Extracting basic features
                #Go through each pixel in the image and increment trueCount if it is a feature
                for row in range(0, len(extractedFeatures)):
                    for column in range(0, len(extractedFeatures[row])):
                        if(extractedFeatures[row][column]):
                            trueCount[row][column] += 1
            else:
                #Extracting advanced features. Should be integers
                for row in range(0, len(extractedFeatures)):
                    for column in range(0, len(extractedFeatures[row])):
                        if(extractedFeatures[row][column] >= 0):
                            trueCount[row][column] += extractedFeatures[row][column] + 1




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
    #print str(min(computedStatistics[1][0][0]))
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
    element = 0
    for numberImage in data:
        print "Working on element " + str(element)
        extraction = feature_extractor(numberImage, width, height)
        predicted.append(compute_class(extraction))
        element += 1
    # Your code ends here #
    return predicted
