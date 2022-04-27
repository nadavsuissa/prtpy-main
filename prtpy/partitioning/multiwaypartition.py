"""
Algorithm for an Optimal solution to the multiway number partitioning problem

Based on: Search Strategies for Optimal Multi-Way Number Partitioning Michael D. Moffitt

https://www.ijcai.org/Proceedings/13/Papers/099.pdf
"""
import logging
logger = logging.getLogger(__name__)

# Function to check if all subsets are filled or not
def validateS(sumLeft:list, k:int)-> bool:
    return r


# Helper function for solving `k` partition problem.
# It returns true if there exist `k` subsets with the given sum
def sSum(S, n, sumLeft, A, k)-> bool:
    return result


# Function for solving k–partition problem. It prints the subsets if
# set `S[0…n-1]` can be divided into `k` subsets with equal sum
def multiwaypartition(
        S:list,
        k:int)-> list:
    """
    Main Function - Given Set on Int and K PArtiotions 
    :param S: Set of Integers
    :param k: Int - Num of Partitions
    :return: List of K Lists partiotions of sets that match Criteria

    Examples that have been precalculated:

    >>> multiwaypartition([2,3,4,5,1,2,4], 3)
    [[2, 1, 4], [2, 5], [3, 4]]
    >>> multiwaypartition([4,3,6,8,2,4,9], 3)
    [[3, 9], [4, 8], [4, 6, 2]]
    >>> multiwaypartition([5,3,6,8], 2)
    [[6, 5], [8, 3]]
    >>> multiwaypartition([5,3,6,8,2,2,8], 2)
    [[8, 3, 6], [8, 2, 2, 5]]
    >>> multiwaypartition([5,3,6,7], 1)
    [5,3,6,7]
    >>> multiwaypartition([1,2,3,4], 2)
    [[3, 2], [4, 1]]
    >>> multiwaypartition([4,4,4,4,4,4,4,4,4], 3)
    [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
    >>> multiwaypartition([4,2,3,7,4,5,9,2,4,9,1,2,9,7,4,7,8,3,2,3,4,5,7,1,3,1,1,1,1,1], 10)
    [[1, 2, 9], [1, 2, 9], [3, 4, 5], [3, 9], [2, 7, 3], [1, 3, 8], [1, 2, 5, 4], [1, 7, 4], [1, 7, 4], [1, 7, 4]]
    """
    return []

if __name__ == '__main__':
    logger.addHandler(logging.StreamHandler())
    # logger.setLevel(logging.INFO)

    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

