import random
import numpy as np
import skimage.io as io


def denoise(filename):
    d = 0
    nnoise = np.array(io.imread(f"input/{filename}_{0}.png"), dtype=np.int64)
    maxx, maxy, _ = list(nnoise.shape)
    for a in range(1, 20):
        img = io.imread(f"input/{filename}_{a}.png")
        nnoise += img
        """for x in range(maxx):
            for y in range(maxy):
                nnoise[x, y] += img[x, y]"""
    nnoise //= 20
    io.imsave("output/f.png", nnoise)

denoise('f.png')
