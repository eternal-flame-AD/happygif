import sys
import os
from common.gifhandler import GifHandler


def _percentage2pixel(x, scale):
    return int(x[:-1])*scale//100


def _pos_trans(x, y, size):
    if "%" in x:
        x = _percentage2pixel(x, size[0])
    else:
        x = int(x)
    if "%" in y:
        y = _percentage2pixel(y, size[1])
    else:
        y = int(y)
    return (x, y)


def _prompt(prompt):
    print(prompt, end="")
    return input()


def main():
    gif = GifHandler(sys.argv[1])
    color = (255, 255, 255)
    anchor = "center"
    font = os.path.split(os.path.realpath(__file__))[0]+'/Arial.ttf'
    gif.set_font(font)
    print('frames:', gif.getlength())
    print('size:', gif.getsize())
    pos = (0, 0)
    while True:
        cmd = _prompt('?')

        if cmd.startswith('show'):
            index = int(cmd[4:])
            gif.show_frame(index)

        if cmd.startswith('drawframes'):
            start = int(_prompt('start?'))
            end = int(_prompt('end?'))
            text = _prompt('text?')
            try:
                gif.write_text_to_frames(range(start, end+1), text, pos, color,
                                         anchor)
            except Exception as e:
                print(e)

        if cmd.startswith('setpos'):
            x = _prompt('x?')
            y = _prompt('y?')
            pos = _pos_trans(x, y, gif.getsize())

        if cmd.startswith('setcolor'):
            r = _prompt('r?')
            g = _prompt('g?')
            b = _prompt('b?')
            color = (int(r), int(g), int(b))

        if cmd.startswith('setanchor'):
            anchor = _prompt('anchor?')

        if cmd.startswith('setfont'):
            font = _prompt('font?')
            size = _prompt('size?')
            gif.set_font(font, int(size))

        if cmd.startswith('write'):
            fn = _prompt('fn?')
            gif.write_gif(fn)

        if cmd.startswith('exit'):
            break


if __name__ == "__main__":
    main()
