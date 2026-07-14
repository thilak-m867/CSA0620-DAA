print("192572046\nShree Thilak Muthukrishna\n")

arr = [5, 10, 15, 20 , 25]
key = 20

def binary_search(array, low, high , key):

    if low>high:
        return -1
    
    mid = low + (high-low)//2

    if array[mid] == key:
        return mid
    
    elif array[mid] > key:
        return binary_search(array, low, mid-1, key)

    else:
        return binary_search(array, mid+1, high, key)

index = binary_search(arr, 0, len(arr)-1, key)

print(f"Key is found at index {index}")
