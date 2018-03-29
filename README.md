# Nearest Neighbor
One of the simplest decision procedures that can be used for classification is the nearest neighbour(NN) rule. It classifies a sample based on the category of its nearest neighbour. The nearest neighbour based classifiers use some or all the patterns available in the training set to classify a test pattern. These classifiers essentially involve finding the similarity between the test pattern and every pattern in the training set.

## iris.txt (Data Set)
This is perhaps the best known database to be found in the pattern recognition literature. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 
Predicted attribute: class of iris plant. 
This is an exceedingly simple domain. 

### Attribute Information:

1 sepal length in cm 
2 sepal width in cm 
3 petal length in cm 
4 petal width in cm 
5 class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica

## train.txt (Train data set )
Contains 90 out of 150 instances of iris data set 

## test.txt (Test data set )
Contains 60 out of 150 instances of iris data set

## nearestNeighbor2.py (File to be executed)
This is the file that contains the code for nearest neighbour rule.

## k-nearestNeighbor3.py (File to be executed)
This is the file that contains the code for k-nearest neighbour rule.
K nearest neighbors is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure. A case is classified by a majority vote of its neighbors, with the case being assigned to the class most common amongst its K nearest neighbors measured by a distance function.
If K = 1, then the case is simply assigned to the class of its nearest neighbor. 

## condensedNearestNeighbor.py (File to be executed)
This is the file that contains the code for condensed nearest neighbour rule.
A single pattern is put in the condensed set first. Then each pattern is considered and its nearest neighbour in the condensed set is found. If it's label is the same as that of the pattern in the condensed set, it is left out, Otherwise the new pattern is included in the condensed set.

## modifiedCondensedNearestNeighbor.py (File to be executed)
This is the file that contains the code for modified condensed nearest neighbour rule. 
The modified condensed nearest neighbour(MCNN) algorithm attempts to partition the region of a class into simpler non-overlapping regions. This is done in an incremental manner, adding prototypes to a representative set till finally all training patterns are classified correctly.

##### Language used - Python
##### Software used - Anaconda  