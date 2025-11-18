# print from 1 to n

class Recursion:
    def f_of_n(i,n):
        # base case
        if i<1:
            return
        
        print(i)
        Recursion.f_of_n(i-1,n)

Recursion.f_of_n(100,1)
