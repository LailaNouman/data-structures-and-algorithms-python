def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

if __name__ == "__main__":
    arr = [5,4,8,2,1]
    insertion_sort(arr)
    print(arr)