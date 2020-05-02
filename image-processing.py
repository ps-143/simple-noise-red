import random
import numpy as np
import skimage.io as io


def denoise(filename):
    d = 0
    nnoise = np.array(io.imread(f"input/{filename}_{0}.png"), dtype=np.int64)
    maxx, maxy, _ = list(nnoise.shape)
    print(maxx)
    print(maxy)
    for a in range(1, 20):
        img = io.imread(f"input/{filename}_{a}.png")
        print(img[0,0])
        nnoise += img
        """for x in range(maxx):
            for y in range(maxy):
                nnoise[x, y] += img[x, y]"""
        print(nnoise[0,0])
    nnoise //= 20
    print(nnoise[0,0])
    io.imsave("ouput/f.png", nnoise)

denoise('f.png')
