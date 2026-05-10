def twosum(array, target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                print(array[i],',',array[j])
                
array=list(map(int,input().split()))
target=int(input())
print(twosum(array,target))