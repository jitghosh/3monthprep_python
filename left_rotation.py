def rotateLeft(d, arr):
    arr_rotated = [0] * len(arr)
    for idx in range(0,len(arr)):
        arr_rotated[idx - d] = arr[idx]
    return arr_rotated


print(rotateLeft(2,[1,2,3,4,5]))