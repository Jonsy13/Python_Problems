class A:
    num=10
    
class B(A):
    num=2

class C(A):
    num=1
    
class D(B,C):
    pass
# try to cooment lines
# print(D.mro())

print(D.num)