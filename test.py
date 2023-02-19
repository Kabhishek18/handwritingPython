# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap,math

# gfg_logo.jpeg image opened using open
# function and assigned to variable named img
def textWrapper(texts,limit):
    wrapper = textwrap.TextWrapper(width=limit)
    word_list = wrapper.wrap(text = texts)
    txt ='\n'.join(word_list)
    return txt

def textLimiter(fontsize):
    fontset = 55 / 20 
    limit = math.ceil(fontset* fontsize)
    return limit

def handWriting(paper,fontname,fontsize,colorText,texts):
    img = Image.open(paper)
    fontLocation = 'fonts/'
    fontname = fontLocation + fontname
    colorOutline = "red"
    colorBackground = "white"

    font = ImageFont.truetype(fontname, fontsize)
    limit = textLimiter(fontsize)
    txt = textWrapper(texts,limit)
    # Image is converted into editable form using
    # Draw function and assigned to d1
    width, height = 720,1080
    # img = Image.new('RGB', (width+4, height+4), colorBackground)

    d1 = ImageDraw.Draw(img)
    # d1.text((2, height/2), txt, fill=colorText, font=font)
    d1.text((128,100), txt, fill=colorText, font=font)
    # d1.rectangle((0, 0, width+3, height+3), outline=colorOutline)

    # Font selection from the downloaded file
    # myFont = ImageFont.truetype('C:\\Users\KUMABHIS\Desktop\py\Tomatoes-O8L8.ttf', 20)
    # myFont = ImageFont.truetype('C:\\Users\KUMABHIS\Desktop\py\Spicy_Chicken.otf', 20)
    # Decide the text location, color and font
    # d1.text((70, 63),txt, fill =(255, 0, 0),font=myFont)
    
    # show and save the image
    img.show()
    img.save("results.jpeg")

texts ="Whereas disregard and contempt for human rights have resulted Whereas disregard and contempt for human rights have resultedWhereas disregard and contempt for human rights have resulted " 
handWriting('paper4.jpg',"GloriaHallelujah-Regular.ttf",20,"Black",texts)