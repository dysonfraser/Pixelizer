from PIL import Image
import os
from collections import defaultdict

print("______________++______________")

size_of_pixel = 3

img1 = Image.open('F:\Dev\Python\Pixelizer\dtumblr_05a58f1f8433b57c67570142de24661e_168271ba_540.jpg').convert("RGB")
img = img1.copy()
width, height = img.size

print(width)
print(height)

x = 0

width = width - (width % size_of_pixel)
height = height - (height % size_of_pixel)
pixel_color = defaultdict(lambda: 0)

while x < width:
 
    y = 0
    while y < height:

        i = x
        while i < x + size_of_pixel:
            
            j = y

            while j < y + size_of_pixel:

                pixel_color[img.getpixel((i,j))] += 1

                j += 1 

            i += 1
    
        i = x
        while i < x + size_of_pixel:
            j = y
            while j < y + size_of_pixel:
                img.putpixel((i,j), max(pixel_color, key=pixel_color.get))
                
                j += 1 
            i += 1
        
        pixel_color.clear()
        print(i,end="\r");      

        y += size_of_pixel  
    x += size_of_pixel


img = img.crop((0,0,width,height))


print("done")
img.show()

img.save("rotated3.jpg")
width, height = img.size

