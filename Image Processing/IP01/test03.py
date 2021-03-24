import numpy as np

'''
arr1 = np.array([1,2,3], dtype = np.uint8)
print(arr1, type(arr1))

#start부터 stop까지 2의 간격으로 생성
arr2 = np.arange(0, 12, 2)
print(arr2)
#start부터 stop까지 5개의 균등한 값으로 나누기
arr3 = np.linspace(0, 10, 5)
print(arr3)

#shape크기의 배열을 생성(모든 값은 0)
arr4 = np.zeros((2,3), dtype = float)
print(arr4, type(arr4), type(arr4[0,0]))

#shape크기의 배열을 생성(모든 값은 1)
arr5 = np.ones((3,2,2), dtype = np.uint8)
print(arr5, type(arr5[0][0]), type(arr5[0][0]), type(arr5[0][0][0]))

'''

#shape의 크기를 가지는 value로 채워진 배열 생성
arr6 = np.full((2, 2), 5, dtype = np.uint8)
print(arr6)

#n,m의 단위행렬 생성
eye = np.eye(3, 4, dtype = np.uint8)
print(eye)

list = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(list)

print(list[1][1]) #list[1, 1]
print(arr[1][1], arr[1, 1])


