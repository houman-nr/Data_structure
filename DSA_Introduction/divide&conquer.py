#this is a divide and conquer approach to sorting problem
def mergeSort(array, start, end):
    if start < end:
        return
    mergeSort(array, start, int(end + start/2))
    mergeSort(array, int(end + start/2)+1, end)

def merge(array, start, middle, end):
    pass
#this is a divide and conquer approach to sorting problem

if __name__ == "__main__":
    first_array = [5, 3, 9, 2, 7]
    mergeSort(first_array, 0, 5)
    print(first_array)