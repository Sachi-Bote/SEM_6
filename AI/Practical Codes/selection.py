#Implement Greedy Search Algorithm for any of the following application
#1. Selection Sort

def input_array(array):
	n = int(input("Enter the number of elements in the array: "))
	for i in range(0, n):
		a = int(input("Enter the number: "))
		array.append(a)
	print("Input Array: ",array)	

def selection_sort(array):
	n = len(array)
	
	for i in range(0, n):
		min = i
		for j in range (i+1, n):
			if(array[j] < array[min]):
				min = j
		array[i], array[min] = array[min], array[i]
		print("Pass", i+1, "array: ", array)
	print("Sorted array: ", array)

array = []
input_array(array)
selection_sort(array)	
