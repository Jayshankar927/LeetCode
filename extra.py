def heapifyDown(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapifyDown(arr,n,largest)

def heapsort(arr,n):
    for i in range(n//2 - 1,-1,-1):
        heapifyDown(arr,n,i)
    
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapifyDown(arr,i,0)
    
arr = [1,3,2,5,4,8,6,7,9]
n = len(arr)

heapsort(arr,n)
print(arr)