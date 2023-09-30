class Calculation1:
    def sum(selfself,a,b):
        return a+b
class Calculation2:
    def mul(selfself,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def div(selfself,a,b):
        return a/b

d = Derived()
print(issubclass(Derived,Calculation2))
print(isinstance(d,Calculation1))