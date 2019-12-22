#!/usr/bin/python
import unicodedata
import fontforge
from televideo_912_mapping import codepoints
import numpy as np

img = np.frombuffer(open('A3-2.bin','rb').read(),dtype=np.uint8)

fnt = fontforge.font()

fnt.fontname = 'Televideo 912'
fnt.familyname = 'Televideo 912'
fnt.weight = 'Medium'
fnt.version = '1.0'
fnt.descent = 100
fnt.ascent = 700

fnt.copyright = 'please visit https://github.com/vogelchr/wargames_font_televideo_912'

def add_pixel(pen, x, y) :
        x = x*100 + 50
        y = 100*(7-y)

        pen.moveTo((x, y))
        pen.lineTo((x+100, y))
        pen.lineTo((x+100, y-100))
        pen.lineTo((x, y-100))
        pen.closePath()

for offset, charnum in codepoints :
        glyphname = unicodedata.name(chr(charnum))
        glyph = fnt.createChar(charnum, )

        pen = glyph.glyphPen();     # Create a pen to draw into glyph "B"

        ###
        # pixels are stored in the following order:
        #  byte0: char0, 8th line
        #  byte1: char0, 1st line
        #   ...
        #  byte7: char0, 7th line
        #  byte8: char1, 8th line
        #  byte9: char1, 1st line
        #   ..
        #  byte15: char1, 1st line
        #
        # the 6 MSB bits are containing pixel data with the
        # two lower bits being control signals that can shift
        # the pixels to the left
        ###
        for line in range(8) :
                if line == 7 :
                        d = img[offset*8]
                else :
                        d = img[offset*8 + (line+1)]

                for bit in range(6) :
                        bitoffs = 0
                        if bit >= 4 : # bit 0x01 shifts left for the left 4 pixels
                                if d & 0x01 :
                                        bitoffs = -0.5
                        else :  # bit 0x02 shifts left for the right 2 pixels
                                if d & 0x02 :
                                        bitoffs = -0.5

                        x = float(bit + bitoffs)
                        y = float(line)
                        if d & (1<<(7-bit)) :
                                add_pixel(pen, x, y)

        glyph.width = 600

fnt.save('Televideo_912.sfd')
fnt.generate('Televideo_912.ttf')