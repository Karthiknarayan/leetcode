class Recursion:
    def __init__(self):
        pass

    def recurfunction(self, val):
        print(val)
        if (val<100):
            self.recurfunction(val+1)
        else:
            exit()
    
class A:
    r = Recursion()
    r.recurfunction(1)