from PIL import Image , ImageFilter

img = Image.open('./Screenshot (23).png')
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

# #With filter We can add filters to the image
filtered_img = img.filter(ImageFilter.SHARPEN)

# #We can Convert File to different Modes
filtered_img = img.convert('L')

# #For rotating the image
# #crroked = filtered_img.rotate(180)

# #For resizing the image
# #resize = filtered_img.resize((300 , 300))

# #For showing the image
# #filtered_img.show()

# #For croping the image
# box = (100,100,400,400)
# region = filtered_img.crop(box)

# #For Saving the processed Image
filtered_img.save("blur.png",'png')


#For REsizing a image..but also want to aspect ratio to be same...Use Thumbnail
# img = Image.open('./Screenshot (23).png')
# img.thumbnail((400,200))
# img.save('thumbnail.jpg')
# print(img.size)