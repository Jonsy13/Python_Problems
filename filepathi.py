try:
    with open('daa.txt','r') as fr:
         print(fr.read())
except FileNotFoundError as err:
    print('U beti Pushpa')
    #raise err