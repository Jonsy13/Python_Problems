my_list = [ item for item in 'hello' ]
my_list2 = [ (2*item) for item in range(1,21)]
print(my_list)
print(my_list2)

m = { item for item in range(20,1,-1)}
print(m)

sim = {
    'a':1,
    'b':2
}
my_dict = { key:value**2 for key,value in sim.items()}
print(my_dict)

my_dict1 = { num: num*2 for num in [1,2,3]}
print(my_dict1)