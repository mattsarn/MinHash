"""

Matthew Sarni
Module used -- https://github.com/ekzhu/datasketch

MinHash Element Estimator--
These functions will provide cardinality estimations via MinHash for a list and 
a list of lists. The last function will provide the accuracy of your estimation.

"""

from hashlib import sha1
from datasketch import MinHash

        
def estimateDistinctElements(items, num_perm):
    """This function will estimate the number of distinct elements in a list.
       The default number of hash function permutations is num_perm(128), but 
       I asjusted after researching more-
       http://blog.cluster-text.com/tag/minhash/"""
    h = MinHash(num_perm)  # creates a minhash object with the parameter 
    for item in items:     # being the number of hash permutations
        h.digest(sha1(item.encode('utf8')))  # digests the minhash signatures 
    print("Estimated number of elements: ", h.count())

estimateDistinctElements(items, 200)



estimate = []
def estimateDistinctElementParallel(listOfItems, num_perm):
    """Same as above, except here we have a nested for loop to iterate through the 
       lists in the list. This function will also append the estimation result 
       to a list for use in the following accuracy function."""
    h = MinHash(num_perm)
    for item in listOfItems:
        for i in item:  # nested for loop to iterate over lists within a list
            h.digest(sha1(i.encode('utf8')))
    estimate.append(h.count())
    print("Estimated number of elements: ", h.count())

estimateDistinctElementParallel(listOfItems, 200)



def calculateEmpiricalAccuracy(items, estimate):
	"""This function calculates the empirical accuracy of the previous. The goal
	   is to get a returned result as close to zero as possible."""
    s1 = set(items)
    actual = len(s1)  # to count unique elements
    accuracy = float(actual) - float(estimate[0])
    print("Empirical accuracy: ", accuracy)
    
calculateEmpiricalAccuracy(items, estimate)