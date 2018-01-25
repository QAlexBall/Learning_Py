from PIL import Image
im = Image.open('1.jpg')
print(im.format, im.size, im.mode)
# 保存缩略图
im.thumbnail((200, 100))
im.save('1thumb.jpg', 'JPEG')
im1 = Image.open('1thumb.jpg')
im1.show()