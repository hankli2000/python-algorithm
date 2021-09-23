
'''
merge sort

MergeSort(arr[], l, r)
if r > l
	1. find the middle point to divide the array into two halves:
		middle m = l + (r-1)/2
	2. call mergesort for first half
		mergesort(arr, l, m)
	3. call mergsort for second half
		mergesort(arr, m+1, r)
	4. merge the two halves sorted in step 2 and 3
		merge(arr, l, m, r)
'''

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		larr = arr[:mid]
		rarr = arr[mid:]
		mergeSort(larr)
		mergeSort(rarr)

		i = j = k = 0

		# merge
		while i<len(larr) and j<len(rarr):
			if larr[i] < rarr[j]:
				arr[k] = larr[i]
				i+=1
			else:
				arr[k] = rarr[j]
				j+=1
			k += 1

		#left part, just copy
		while i<len(larr):
			arr[k] = larr[i]
			i+=1
			k+=1
		while j<len(rarr):
			arr[k] = rarr[j]
			j+=1
			k+=1



