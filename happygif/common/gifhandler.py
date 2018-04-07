from PIL import Image
from .subtitler import SubTitler
import imageio


class GifHandler():
    def __init__(self, giffn):
        self.imreader = imageio.get_reader(giffn)
        self.duration = self.imreader.get_meta_data()['duration']
        self.subtitler = SubTitler()
        self.frames = []
        for frame in self.imreader.iter_data():
            self.frames.append(frame.copy())

    def getsize(self):
        return (len(self.frames[0][0]), len(self.frames[0]))

    def getinfo(self):
        return self.imreader.get_meta_data()

    def getlength(self):
        return len(self.frames)

    def get_frame(self, index):
        return Image.fromarray(self.frames[index])

    def show_frame(self, index):
        im = Image.fromarray(self.frames[index])
        im.show()
        del im

    def set_font(self, fontfile, size=10, index=0):
        self.subtitler.set_font(fontfile, size, index)

    def write_text_to_frame(self, index, text, pos=(0, 0),
                            color=(255, 255, 255), anchor="left"):
        res = self.subtitler.write_text_to_img(self.frames[index],
                                               text, pos, color, anchor)
        self.frames[index] = res

    def write_text_to_frames(self, index_range, text, pos=(0, 0),
                             color=(255, 255, 255), anchor="left"):
        for index in index_range:
            self.write_text_to_frame(index, text, pos, color, anchor)

    def write_gif(self, new_fn):
        framenum = 0
        self.imwriter = imageio.get_writer(new_fn)
        for frame in self.frames:
            data = self.imreader.get_meta_data(index=framenum)
            self.imwriter.append_data(frame, data)
            frame += 1
        self.imwriter.close()
