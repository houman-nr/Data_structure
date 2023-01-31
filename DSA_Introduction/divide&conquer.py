#this is a divide and conquer approach to sorting problem
def mergeSort(array, start, end):
    if start < end:
        return
    middle = int(end + start/2)
    mergeSort(array, start, middle)
    mergeSort(array, middle+1, end)
    merge(array, start, middle, end)

def merge(array, start, middle, end):
    leftHalf = array[start:middle]
    rightHalf = array[middle+1:end]
    print("left half:")
    print("left half:")
    j ,k = 0
    for i in range(array):
        if leftHalf[j] > rightHalf[k]:
            array[i] = leftHalf[j]
            j = j + 1
        else:
            array[i] = rightHalf[k]
            k = k + 1
#this is a divide and conquer approach to sorting problem

if __name__ == "__main__":
    first_array = [5, 3, 9, 2, 7]
    mergeSort(first_array, 0, 4)
    print(first_array)