#fp = open('data.txt')
#read() reads the whole data from file..but as curser moves..we have to reset the curser
#Using fp.seek(0);
# print(fp.read())
# fp.seek(0)
# print(fp.readline())

# print(fp.readlines())
# fp.close()


#We can also use "with" , "as"..So , we don't have to close the file

#
    
# For writing mode = "w" , but it will delete all previous data
# For Both reading and writing mode="r+" then it will reset the seek and start from starting

#

# with open('data.txt','r+') as fr:
#     text = fr.write('smileee')
#     print(text)

#With append we can do all right'
with open('data.txt','a') as fr:
    text = fr.write('\nsmileee')
    print(text)