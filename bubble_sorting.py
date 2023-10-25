def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """

    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps are made in a pass
        swapped = False

        # Last i elements are already in place, so no need to check them again
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in inner loop, the array is already sorted
        if not swapped:
            break

    return arr

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("Sorted array is:", sorted_list)
