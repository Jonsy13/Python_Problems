my_list = [1,2,3]
ur_list = [10,20,30]
hii = [4,5]

def multiply_by2(item):
    return item*2


def odd_check(item):
    return (item % 2 !=0)



print(list(filter(odd_check , my_list)))
print(list(map(multiply_by2, my_list)))
print(list(zip(my_list , ur_list)))
