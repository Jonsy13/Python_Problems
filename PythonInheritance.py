class User():
    
    def __init__(self,email):
        self.email = email
        
    def run(self):
        print("Logged In")
        
    def attack(self):
        print("Do Nothingg")
        
class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name=name
        self.power=power
        
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows
        
    def attack(self):
        print(f'attacking with arrows of {self.num_arrows}')


Wizard1 = Wizard('Merlin',50,'Hii')
archer1 = Archer('Jane',100)

Wizard1.attack()
print(Wizard1.email)
print(isinstance(Wizard1 , Wizard))
print(isinstance(Wizard1 , object))
print(dir(Wizard1)) 