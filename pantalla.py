#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
thisdir=os.path.dirname(os.path.realpath(__file__))
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import epd1in54_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

class Pantalla():
    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
        self.epd = epd1in54_V2.EPD()
        logging.info("epd1in54_V2 screen initialized")
        self.epd.init(0)
        # self.epd.Clear(0xFF)
        self.Font = ImageFont.truetype(os.path.join(thisdir, 'arial.ttf'), 24)
        # time.sleep(1)
    def show(self, text):
        # split text in strings of max 16 characters
        # and put them in a list
        text_list = [text[i:i+17] for i in range(0, len(text), 16)]
        logging.info("1.Drawing on the image...")
        image = Image.new('1', (self.epd.width, self.epd.height), 255)
        self.draw = ImageDraw.Draw(image)
        y=8
        for line in text_list:
            self.draw.text((4, y), line, font = self.Font, fill = 0)
            y+=24
        # self.draw.rectangle((0, 10, 200, 34), fill = 0)
        # self.draw.text((8, 12), 'hello world', font = self.Font, fill = 255)
        # self.draw.text((8, 36), u'微雪电子', font = self.Font, fill = 0)
        # self.draw.line((16, 60, 56, 60), fill = 0)
        # self.draw.line((56, 60, 56, 110), fill = 0)
        # self.draw.line((16, 110, 56, 110), fill = 0)
        # self.draw.line((16, 110, 16, 60), fill = 0)
        # self.draw.line((16, 60, 56, 110), fill = 0)
        # self.draw.line((56, 60, 16, 110), fill = 0)
        # self.draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
        # self.draw.rectangle((16, 130, 56, 180), fill = 0)
        # self.draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
        self.epd.display(self.epd.getbuffer(image.rotate(90)))


# logging.basicConfig(level=logging.DEBUG)

# try:
#     logging.info("epd1in54_V2 Demo")
    
#     epd = epd1in54_V2.EPD()
    
#     logging.info("init and Clear")
#     epd.init(0)
#     epd.Clear(0xFF)
#     time.sleep(1)
    
#     # Drawing on the image
#     logging.info("1.Drawing on the image...")
#     image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
#     draw.rectangle((0, 10, 200, 34), fill = 0)
#     draw.text((8, 12), 'hello world', font = font, fill = 255)
#     draw.text((8, 36), u'微雪电子', font = font, fill = 0)
#     draw.line((16, 60, 56, 60), fill = 0)
#     draw.line((56, 60, 56, 110), fill = 0)
#     draw.line((16, 110, 56, 110), fill = 0)
#     draw.line((16, 110, 16, 60), fill = 0)
#     draw.line((16, 60, 56, 110), fill = 0)
#     draw.line((56, 60, 16, 110), fill = 0)
#     draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
#     draw.rectangle((16, 130, 56, 180), fill = 0)
#     draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
#     epd.display(epd.getbuffer(image.rotate(90)))
#     time.sleep(2)
    
#     # read bmp file 
#     logging.info("2.read bmp file...")
#     # open image file bmp from same directory where this script is
#     image = Image.open(os.path.join(thisdir, 'pic/robot.bmp'))
#     logging.info("image size: %s", image.size)
    
#     epd.display(epd.getbuffer(image))
#     logging.info('show image')
#     time.sleep(1)
    
#     # # read bmp file on window
#     # logging.info("3.read bmp file on window...")
#     # epd.Clear(0xFF)
#     # image1 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#     # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
#     # image1.paste(bmp, (50,50))    
#     # epd.display(epd.getbuffer(image1))
#     # time.sleep(2)
    
#     # # partial update
#     # logging.info("4.show time...")
#     # time_image = image1
#     # # Image.new('1', (epd.width, epd.height), 255)
#     # epd.displayPartBaseImage(epd.getbuffer(time_image))
    
#     # epd.init(1) # into partial refresh mode
#     # time_draw = ImageDraw.Draw(time_image)
#     # num = 0
#     # while (True):
#     #     time_draw.rectangle((10, 10, 120, 50), fill = 255)
#     #     time_draw.text((10, 10), time.strftime('%H:%M:%S'), font = font, fill = 0)
#     #     newimage = time_image.crop([10, 10, 120, 50])
#     #     time_image.paste(newimage, (10,10))  
#     #     epd.displayPart(epd.getbuffer(time_image))
#     #     num = num + 1
#     #     if(num == 20):
#     #         break
    
#     # logging.info("Clear...")
#     # epd.init(0)
#     # epd.Clear(0xFF)
    
#     logging.info("Goto Sleep...")
#     epd.sleep()
        
# except IOError as e:
#     logging.info(e)
    
# except KeyboardInterrupt:    
#     logging.info("ctrl + c:")
#     epd1in54_V2.epdconfig.module_exit()
#     exit()
