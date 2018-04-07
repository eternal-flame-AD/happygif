from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import imageio
import os


class SubTitler():
    def __init__(self):
        self.font = None

    def set_font(self, font_file, size=10, index=0):
        self.font = ImageFont.truetype(font_file, size, index)

    def _align_text(self, draw, pos, text, anchor):
        if anchor == "left":
            return pos
        elif anchor == "center":
            x, y = pos
            x1, y1 = draw.textsize(text, font=self.font)
            return (x-x1/2, y-y1/2)
        elif anchor == "right":
            x, y = pos
            x1, y1 = draw.textsize(text, font=self.font)
            return (x-x1, y-y1)

    def write_text_to_img(self, im, text, pos=(0, 0),
                          color=(255, 255, 255), anchor="left"):
        try:
            im = Image.fromarray(im)
        except TypeError:
            pass
        draw = ImageDraw.Draw(im)
        pos = self._align_text(draw, pos, text, anchor)
        draw.text(pos, text, fill=color, font=self.font)
        im.save('temp.bmp')  # VERY DIRTY SOLUTION
        res = imageio.imread('temp.bmp')
        os.remove('temp.bmp')
        return res
