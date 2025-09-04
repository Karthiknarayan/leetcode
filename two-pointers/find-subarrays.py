arr=[1,2,3,4]
#trial
# subarray=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         subarray.append(arr[i:j+1])

# print(subarray)

#practice
sub=[]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sub.append(arr[i:j+1])
print(sub)