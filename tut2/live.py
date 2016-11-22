from  PIL import Image


im = Image.open('eye.jpg')
im.show()

img2 = im.copy()
width, height = img2.size

img3 = im.copy()
width2, height2 = img3.size

def change_pixels(width, height, img, fun):
    for i in range(width):
       for j in range(height):
           val = img.getpixel((i,j))
           new_val = fun(val)
           img.putpixel((i, j), new_val)

def grey_px(px):
    new_px = int(sum(px)/3)
    return (new_px, new_px, new_px)

def inverted_px(px):
    return tuple(map(lambda x: 255-x, px))

change_pixels(width, height, img2, grey_px)
change_pixels(width, height, img3, inverted_px)
img2.show()
img3.show()
