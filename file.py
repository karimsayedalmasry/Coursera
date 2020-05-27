import PIL
from PIL import Image
from PIL import ImageEnhance
import cv2 
import numpy as np 
from IPython.display import display
from PIL import ImageFont, ImageDraw
    

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
for q in [0.1, 0.5, 0.9]:
    r, g, b = image.split()
    r = r.point(lambda i: i * q)
    result = Image.merge('RGB', (r, g, b)) 
    images.append(result)
for q in [0.1, 0.5, 0.9]:
    r, g, b = image.split()
    g = g.point(lambda i: i * q)
    result = Image.merge('RGB', (r, g, b)) 
    images.append(result)
for q in [0.1, 0.5, 0.9]:
    r, g, b = image.split()
    b = b.point(lambda i: i * q)
    result = Image.merge('RGB', (r, g, b)) 
    images.append(result)
fon1 = ImageFont.truetype("readonly/fanwood-webfont.ttf",75)   
    
# create a contact sheet from different color
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+3*85))
x=0
y=0
draw = ImageDraw.Draw(contact_sheet)
for i,img in enumerate(images):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    if i in [0,3,6]:
         draw.text((x,y+first_image.height+5),"Intensity: 0.1", font=fon1)
    if i in [1,4,7]:
         draw.text((x,y+first_image.height+5),"Intensity: 0.5", font=fon1)
    if i in [2,5,8]:
         draw.text((x,y+first_image.height+5),"Intensity: 0.9", font=fon1)
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+85
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

