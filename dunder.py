class Student():
    
    def __del__(self):
        print("Deleted")
    
    def __dir__(self):
        print("Added")
        
        
S = Student()

dir S
del S
