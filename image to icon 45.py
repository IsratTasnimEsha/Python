'''
from PIL import Image, ImageEnhance
old_initial_block=Image.open('C:\\Users\\Asus\\Documents\\Screenshot (278).png')
new_initial_block=old_initial_block.resize((200, 200))
new_initial_block.save('C:\\Users\\Asus\\Documents\\Screenshot (278).copy.png')
'''



from PIL import Image
img=Image.open('C:\\Users\\Asus\\Documents\\Result.png')
img.save('C:\\Users\\Asus\\Documents\\StoreMeIcon.ico')
