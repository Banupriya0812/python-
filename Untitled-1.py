def bubble_sort(arr):
    for n in range(length(arr)-1,0,-1):
        swapped False

    for i in range(n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True

    if not swapped:
        break
arr =[6,6,2]
print("unsorted list is :")
print(arr)

bubble_sort(arr)
print("sorted list is :")
print(arr)

