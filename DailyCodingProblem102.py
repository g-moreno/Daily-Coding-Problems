def find_contiguous_sum(nums, k):
  """
  Finds a contiguous subarray of the given list whose elements sum to k.

  Args:
    nums: A list of integers.
    k: The target sum.

  Returns:
    A list of integers representing the contiguous subarray, or None if no such subarray exists.
  """

  # Initialize a dictionary to store the cumulative sum and its corresponding index.
  cum_sum = {0: -1}

  # Initialize the current cumulative sum to 0.
  curr_sum = 0

  # Iterate through the list.
  for i, num in enumerate(nums):
    # Update the current cumulative sum.
    curr_sum += num

    # Check if the difference between the current cumulative sum and the target sum exists in the dictionary.
    # If it exists, it means we found a contiguous subarray whose sum is equal to the target sum.
    if curr_sum - k in cum_sum:
      # Return the subarray starting from the index stored in the dictionary and ending at the current index.
      return nums[cum_sum[curr_sum - k] + 1: i + 1]

    # Update the dictionary with the current cumulative sum and its corresponding index.
    cum_sum[curr_sum] = i

  # If no contiguous subarray is found, return None.
  return None

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 9
result = find_contiguous_sum(nums, k)
print(result)  # Output: [2, 3, 4]
