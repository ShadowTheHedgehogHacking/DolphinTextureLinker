import os
import shutil

import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def mse(imageA, imageB):
    e = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    e /= float(imageA.shape[0] * imageA.shape[1])
    return e


DFDTX_PATH = "analyzepool\\DFDTX\\"
DTX_PATH = "analyzepool\\DTX\\"
OTX_PATH = "analyzepool\\OTX\\"

DFDTX = []
DTX = []
OTX = []

TOTAL_MATCHES = []
NO_MATCHES = []
LOW_SCORE = []

for filename in glob.glob(DFDTX_PATH + '*.png'):
    DFDTX.append(filename)

for filename in glob.glob(DTX_PATH + '*.png'):
    DTX.append(filename)

for filename in glob.glob(OTX_PATH + '*.png'):
    OTX.append(filename)

for index, dolphin_texture in enumerate(DFDTX):
    CURRENT_TEXTURE_SCORES = []
#    if index < 20:
    print("Analyzing: " + dolphin_texture[len(DFDTX_PATH):])
    dolphin_image = cv2.imread(dolphin_texture)
    best_score = -1
    closest_match = ""
    for magic_texture in DTX:

        magic_image = cv2.imread(magic_texture)
        try:
            (score, diff) = ssim(dolphin_image, magic_image, full=True, multichannel=True)
            if score > best_score:
                closest_match = (magic_texture[len(DTX_PATH):], score)
                best_score = score
        except ValueError:
            diff = -1


    if best_score > 0.8:
        TOTAL_MATCHES.append((dolphin_texture[len(DFDTX_PATH):], closest_match))

    # if best_score == -1:
    #     NO_MATCHES.append(dolphin_texture[len(DFDTX_PATH):])
    # elif best_score > 0.8:
    #     TOTAL_MATCHES.append((dolphin_texture[len(DFDTX_PATH):], closest_match))
    # else:
    #     LOW_SCORE.append((dolphin_texture[len(DFDTX_PATH):], closest_match))


print("MATCHES:")
print(TOTAL_MATCHES)
# print("LOW SCORE:")
# print(LOW_SCORE)
# print("NO MATCHES:")
# print(NO_MATCHES)

# PHASE 2
if not os.path.exists("OUTPUT"):
    os.makedirs("OUTPUT")

for match in TOTAL_MATCHES:
    newName = match[0]
    fileToUse = OTX_PATH + match[1][0]
    shutil.copyfile(fileToUse, "OUTPUT\\"+newName)


# print("MSE: {}".format(mse(dolphinVer, magicVer)))
# (score, diff) = ssim(dolphinVer, magicVer, full=True, multichannel=True)
# diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))
