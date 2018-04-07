import os
import sys


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


def test_gif_info():
    from common.gifhandler import GifHandler
    rect = GifHandler('test/rect.gif')
    assert rect.getinfo()['duration'] == 0
    assert rect.getsize() == (1000, 500)
    assert rect.getlength() == 1


def test_gif_text():
    from common.gifhandler import GifHandler
    rect = GifHandler('test/rect.gif')
    rect.set_font('test/Arial.ttf', size=100)
    rect.write_text_to_frames(range(0, 1), 'test', (500, 250),
                              color=(255, 0, 0), anchor="center")
    from test_write_static_img import pixel_match
    rect.show_frame(0)
    rect.write_gif('test/result.gif')
    rect = GifHandler('test/result.gif')
    testimage = rect.get_frame(0)
    basey = 250
    found_red = False
    for x in range(1000):
        if pixel_match(testimage, x, basey, 255, 0, 0, 10):
            found_red = True
    assert found_red
    del rect
    os.remove('test/result.gif')
