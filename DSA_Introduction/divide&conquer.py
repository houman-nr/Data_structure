#this is a divide and conquer approach to sorting problem
def mergeSort(array, start, end):
    if start == end:
        return
    middle = int((end + start)/2)
    mergeSort(array, start, middle)
    mergeSort(array, middle+1, end)
    merge(array, start, middle+1, end)

def merge(array, start, middle, end):
    
    leftHalf = array[start:middle]
    rightHalf = array[middle:end+1]
    i = start
    
    j ,k = int(0), int(0)
    
    print("lefthalft:",leftHalf)
    print("righthalf:",rightHalf)

    while i < len(array):
        if j < len(leftHalf) and k < len(rightHalf):
            if leftHalf[j] < rightHalf[k]:
                array[i] = leftHalf[j]
                leftHalf.pop(j)
                i += 1
            else:
                array[i] = rightHalf[k]
                rightHalf.pop(k)
                i += 1
        else:
            if len(leftHalf) > 0:
                array[i] = leftHalf[j]
                leftHalf.pop(j)
                i += 1
            elif len(rightHalf) > 0:
                array[i] = rightHalf[k]
                rightHalf.pop(k)
                i += 1
            else:
                return
            print("array:", array)
#this is a divide and conquer approach to sorting problem

if __name__ == "__main__":
    first_array = [5, 3, 9, 2, 7]
    i = int(0)
    mergeSort(first_array, 0, 4)
    print(first_array)