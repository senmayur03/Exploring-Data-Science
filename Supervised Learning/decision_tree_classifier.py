# classifier.py
# Lin Li/26-dec-2021
#
# Use the skeleton below for the classifier and insert your code here.

from collections import Counter

# A class for creating tree nodes 
# This node will hold the best feature for splitting for the current data
class TreeNode:
    def __init__(self, feature, parent, left, right):
        self.feature = feature
        self.parent = parent
        self.left = left
        self.right = right

# A class for creating tree leaves
# This leaf will hold the value to be returned after traversing the decision tree
class TreeLeaf:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

class Classifier:
    def __init__(self):
        pass

    # Returns the most common element in the data array
    def highestNumber(self, data):
        return Counter(data).most_common(1)

    # Converts a test set into a dictionary of data and target elements
    # Each data is split into another dictionary holding key value pairs for each feature
    # i.e. 
    #{Sample Number : [{Feature 1 : A, Feature 2 : B}, Target]}
    def dataToDict(self, dataSet, targetSet):
        featureSet = list(range(len(dataSet[0])))
        dataSetDict = {}
        counter = 0
        for data in dataSet:
            dataDict = {}
            for feature in featureSet:
                dataDict[str(feature)] = data[feature]
            dataSetDict[counter] = [dataDict, targetSet[counter]]
            counter = counter + 1
        return dataSetDict      

    # Calculates the gini value for a specific set of data
    def gini(self, target):
        classes = list(set(target))
        squaredValues = 0
        for class_ in classes:
            squaredValues = squaredValues + ((target.count(class_) / len(target)) ** 2)
        return 1 - squaredValues

    # Calculates the gini impurity of the data with a specific feature
    def giniImpurity(self, dataDict, feature):
        positiveSize = 0
        negativeSize = 0
        total = len(dataDict.keys())

        positiveTarget = []
        negativeTarget = []

        for key in dataDict.keys():
            if dataDict[key][0][feature] == 1:
                positiveSize = positiveSize + 1
                positiveTarget.append(dataDict[key][1])
            else:
                negativeSize = negativeSize + 1
                negativeTarget.append(dataDict[key][1])
        
        positiveGini = (positiveSize / total) * self.gini(positiveTarget)
        negativeGini = (negativeSize / total) * self.gini(negativeTarget)

        return positiveGini + negativeGini

    # Returns the feature that gives the lowest gini impurity
    def lowestGiniImpurity(self, dataDict):
        featureWithGini = {}
        featureSet = dataDict[list(dataDict.keys())[0]][0].keys()
        for feature in featureSet:
            featureWithGini[feature] = self.giniImpurity(dataDict, feature)
        return min(featureWithGini, key = featureWithGini.get)

    # Creates a decision tree. Based on the pseudocode given in Week 2 Lecture 1
    def decisionTree(self, dataSetDict, parentDataSetDict, parent):
        
        # Get a list of all targets from the data set dictionary
        dataSetTargets = []
        for value in dataSetDict.values():
            dataSetTargets.append(value[1])
        
        # If there are no more training examples left, return the most common target from the parent examples
        if bool(dataSetDict) == False:
            parentTargets = []
            for key in parentDataSetDict.keys():
                parentTargets.append(parentDataSetDict[key][1])
            return TreeLeaf(self.highestNumber(parentTargets)[0][0], parent)
        
        # Else if the training examples only have one target, return that target value
        elif len(list(set(dataSetTargets))) == 1:
            return TreeLeaf(list(set(dataSetTargets))[0], parent)
        
        # Else if there are no more features left to split on, return the most common target from the current examples
        elif bool(dataSetDict[list(dataSetDict.keys())[0]][0]) == False:
            return TreeLeaf(self.highestNumber(dataSetTargets)[0][0], parent)

        # Else build a new Tree Node for the decision tree
        else:
            bestAttribute = self.lowestGiniImpurity(dataSetDict)
            tree_ = TreeNode(bestAttribute, parent, None, None)

            # Create two dictionaries for which the feature is either 0 or 1 (negative or positive respectively)
            positiveDataDict = {}
            negativeDataDict = {}

            counter = 0
            # Deletes the best feature from all training examples and puts them into their respective dictionaries
            for key in dataSetDict.keys():
                data = dataSetDict[key]
                if data[0][bestAttribute] == 1:
                    del data[0][bestAttribute]
                    positiveDataDict[counter] = data
                else:
                    del data[0][bestAttribute]
                    negativeDataDict[counter] = data
                counter = counter + 1
            
            # Recursively call the method for the two children of this decision tree node
            # Left child holds examples where the best feature is 0 (negative)
            # Right child holds the examples where the best feature is 1 (positive)
            tree_.left = self.decisionTree(negativeDataDict, dataSetDict, tree_)
            tree_.right = self.decisionTree(positiveDataDict, dataSetDict, tree_)

        return tree_

    def reset(self):   
         pass

    def fit(self, data, target):
        dataSetDict = self.dataToDict(data, target)
        self.tree_ = self.decisionTree(dataSetDict, None, None)

    def predict(self, data, legal=None):
        currentNode = self.tree_
        # If the current node is not a tree leaf, using the feature of this Tree Node
        # traverse left or right depending if this specific feature is 0 or 1
        # Once a Tree Leaf has reached, return the value stored in it
        while type(currentNode) != TreeLeaf:
            currentFeature = currentNode.feature
            value = data[int(currentFeature)]
            if value == 0:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return currentNode.value