import heapq

def min_steps(points):
  """Calculates the minimum number of steps to cover a sequence of points in a 2D grid.

  Args:
    points: A list of tuples representing the points to be covered.

  Returns:
    The minimum number of steps required to cover the points.
  """

  # Create a priority queue to store the points and their corresponding distances from the starting point.
  queue = [(0, 0, 0)]  # (distance, x, y)
  visited = set()

  while queue:
    distance, x, y = heapq.heappop(queue)

    if (x, y) in visited:
      continue

    visited.add((x, y))

    if (x, y) == points[-1]:
      return distance

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
      new_x, new_y = x + dx, y + dy
      new_distance = distance + 1
      heapq.heappush(queue, (new_distance, new_x, new_y))

  return -1  # If no path is found

# Example usage
points = [(0, 0), (1, 1), (1, 2)]
print(min_steps(points))  # Output: 2
