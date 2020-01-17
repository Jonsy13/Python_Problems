class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    
    
    def run(self):
        print('run')
        
    @classmethod
    def adding_num(cls,n1,n2):
        return cls('Teddy',(n1+n2))
    
    @staticmethod
    def add_statadd(n1,n2):
        return (n1+n2)
        
player1 = PlayerCharacter('Jon',18)

print(player1)
print(player1.name)

player2=PlayerCharacter.adding_num(2,3)
player3 = PlayerCharacter.add_statadd(2,3)
player1.run()


print(player2.age)
print(player3)
# help([])