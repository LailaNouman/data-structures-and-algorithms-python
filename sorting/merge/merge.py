def merge_sort(array):
    n = len(array)

    if n > 1:
        mid = n//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)

def merge(left, right, array):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = [8, 4, 23, 42, 16, 15]
    merge_sort(arr)
    print(arr)
