from collections import Iterable,Iterator,Generator
class Iter_obj:
    def __init__(self):
        self.a=[1,2,3,4,5]
    def __getitem__(self,i):
        return self.a[i]
it=Iter_obj()
print(isinstance(it, Iterable))
print(isinstance(it, Iterator)) 
print(isinstance(it, Generator)) 
print(hasattr(it, "__iter__")) 
print(next(iter(it)))