arr = []
for i in range(9):
    arr.append(int(input()))

max = 0 # �ִ�
index = 0 # �ڸ�

for i in range(len(arr)):
    if(max<=arr[i]):
        max = arr[i]
        index = i+1

print(max)
print(index)