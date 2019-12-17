import os
import pickle
import shutil
import time

import cv2
import glob
from skimage.metrics import structural_similarity as ssim

OTX_PATH = "analyzepool\\OTX\\"

start_time = time.time()

TOTAL_MATCHES = pickle.load(open('resumable_matched_results.txt', 'rb'))

# Perform copy with filestruct matching game
for match in TOTAL_MATCHES:
    newName = match[0]
    fileToUse = OTX_PATH + match[1][0]
    newFileSet = match[1][0].rsplit('\\', 1)
    if not os.path.exists("OUTPUT\\"+newFileSet[0]):
        os.makedirs("OUTPUT\\"+newFileSet[0])
    shutil.copyfile(fileToUse, "OUTPUT\\"+newFileSet[0] + "\\" + newName)

    # Multi-match case output flag
    if len(match[2]) > 1:
        for element in match[2]:
            if not os.path.exists("OUTPUT\\" + element.rsplit('\\', 1)[0]):
                os.makedirs("OUTPUT\\" + element.rsplit('\\', 1)[0])
            f = open("OUTPUT\\" + element.rsplit('\\', 1)[0] + "\\" + "POSSIBLE_OVERRIDES.txt", 'a')
            f.write(element + " possibly overwritten by " + newFileSet[0] + "\\" + newName + '\n')
            f.close()

print("Process took:\n%s seconds" % (time.time() - start_time))