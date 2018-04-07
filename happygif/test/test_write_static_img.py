import os
import sys


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


def pixel_match(im, target_x, target_y, target_r, target_g, target_b, diff):
    pixel = im.getpixel((target_x, target_y))
    pixel_diff = abs(pixel[0]-target_r)
    +abs(pixel[1]-target_g)+abs(pixel[2]-target_b)
    if pixel_diff <= diff:
        return True
    else:
        return False


def test_write_jpg_left():
    from PIL import Image
    testimage = Image.open('test/black.jpg')
    size = testimage.size
    assert size == (1000, 500)
    from common.subtitler import SubTitler
    subtitler = SubTitler()
    subtitler.set_font('test/Arial.ttf', size=100)
    subtitler.write_text_to_img(testimage, 'test text', pos=(0, 0),
                                color=(255, 0, 0), anchor="left")
    basey = 40
    found_red = False
    for x in range(1000):
        if pixel_match(testimage, x, basey, 255, 0, 0, 10):
            found_red = True
    assert found_red


def test_write_jpg_mid():
    from PIL import Image
    testimage = Image.open('test/black.jpg')
    size = testimage.size
    assert size == (1000, 500)
    from common.subtitler import SubTitler
    subtitler = SubTitler()
    subtitler.set_font('test/Arial.ttf', size=100)
    subtitler.write_text_to_img(testimage, 'test text', pos=(0, 0),
                                color=(255, 0, 0), anchor="center")
    basey = 40
    found_red = False
    for x in range(1000):
        if pixel_match(testimage, x, basey, 255, 0, 0, 10):
            found_red = True
    assert found_red


def test_write_jpg_right():
    from PIL import Image
    testimage = Image.open('test/black.jpg')
    size = testimage.size
    assert size == (1000, 500)
    from common.subtitler import SubTitler
    subtitler = SubTitler()
    subtitler.set_font('test/Arial.ttf', size=100)
    subtitler.write_text_to_img(testimage, 'test text', pos=(0, 0),
                                color=(255, 0, 0), anchor="right")
    basey = 40
    found_red = False
    for x in range(1000):
        if pixel_match(testimage, x, basey, 255, 0, 0, 10):
            found_red = True
    assert not found_red  # align to the right so it should go out of the image
