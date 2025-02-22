def find_smallest_missing_sum(numbers):
    """
    Daily Coding Problem #224

    Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

    For example, for the input [1, 2, 3, 10], you should return 7.

    Do this in O(N) time.

    Determines the smallest positive integer that is not the sum of a subset.

    Args:
        numbers: A sorted list of positive integers. 

    Returns:
        The smallest missing sum.
    """


    result = 1 #Start with 1 as potential missing sum
    for number in numbers: #Looks at each number in list
            if number <= result:
                  result += number #Adds number to result if it is small enough
            else: #Otherwise, gap exists
                return result #Returns the result
    return result #If whole list is moved through under above conditions, return result



#Example Usage:
my_list = [1,3,8,14]
missing_sum = find_smallest_missing_sum(my_list)
print("The smallest missing sum is: {missing_sum}") #Prints result
