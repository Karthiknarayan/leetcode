# print from 1 to n

class Recursion:
    def f_of_n(i,n):
        # base case
        if i>n:
            return
        
        print(i)
        Recursion.f_of_n(i+1,n)

Recursion.f_of_n(1,100)
