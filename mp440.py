#Global variables
computedStatistics = null

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
            print("row: " + str(row) + "\tcolumn: " + str(column) + "\nwidth: " + str(width) + "\theight: " + str(height))
            if(digit_data[row][column] == '#' or digit_data[row][column] == '+'):
                features[row].append(True)
            else:
                features[row].append(False)
    # Your code ends here #
    #_raise_not_defined()
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

    #Get percentage of data
    partialDataSize = int(len(data)*percentage)
    partialData = data[0:modifiedDataSize]

    #Calculate prior distribution
    numberOccurrence = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    priorDistribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    dataSize = len(data)

    for number in label:
        numberOccurrence[number] += 1.0

    int index = 0
    for occurrenceCount in numberOccurrence:
        priorDistribution[index] = numberOccurrence / dataSize

    #Calculate conditional distribution
    #Possibly need to calculate this in for loop below for each individual image?
        

    for image in partialData:
        extractedFeatures = feature_extractor(image, width, height)

        

    

    # Your code ends here #
    #_raise_not_defined()

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = -1

    # Your code starts here #
    # Your code ends here #
    _raise_not_defined()

    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]

    # Your code starts here #
    # Your code ends here #
    _raise_not_defined()

    return predicted







        
    
