"""#Selection sort
def selectionSort(array, size):
	for ind in range(size):
		min_index = ind
		print("ind")
		print(ind)
		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
				print("j")
				print(j)
		(array[ind], array[min_index]) = (array[min_index], array[ind])
		print(array[min_index],"::",array[ind])
arr = list(map(int,input("enter the element with sepoarated space: ").split()))
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
"""

def selection_sort(n, arr):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)
    
print("Array before Sorting:")
for i in arr:
    print(i,end=" ")
    
selection_sort(n, arr)
    
print("\nArray after Sorting in Ascending Order:")
for i in arr:
    print(i,end=" ")
