import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr1=np.array(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr1[j][i]=arr[i][j]
print(arr1)
