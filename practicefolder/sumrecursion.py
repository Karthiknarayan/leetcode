def sumr(i,sum):
    if i<1:
        print(sum)
        return
    sumr(i-1,sum+i)
sumr(100,0)


# sum=0
# for i in range(0,100):
#     sum+=i
# print(sum)