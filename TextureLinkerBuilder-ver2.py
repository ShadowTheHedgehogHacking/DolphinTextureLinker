import pickle
import time
import cv2
import glob
from skimage.metrics import structural_similarity as ssim

start_time = time.time()

DFDTX_PATH = "analyzepool\\DFDTX\\"
DTX_PATH = "analyzepool\\DTX\\"
OTX_PATH = "analyzepool\\OTX\\"

DFDTX = []
DTX = []

DFDTX_IMAGES = []
DTX_IMAGES = []

TOTAL_MATCHES = []

for filename in glob.glob(DFDTX_PATH + '**/*.png', recursive=True):
    DFDTX.append(filename)
    DFDTX_IMAGES.append(cv2.imread(filename))

for filename in glob.glob(DTX_PATH + '**/*.png', recursive=True):
    DTX.append(filename)
    DTX_IMAGES.append(cv2.imread(filename))

TOTAL_IMG = len(DFDTX)

for index, dolphin_texture in enumerate(DFDTX):
    # if index < 2:
    SHARED_TEXTURE = []
    print("Analyzing: " + dolphin_texture[len(DFDTX_PATH):])
    print("Total progress: {0:.2%}".format(index/TOTAL_IMG))
    best_score = -1
    closest_match = ""
    for jindex, magic_texture in enumerate(DTX):
        try:
            (score, diff) = ssim(DFDTX_IMAGES[index], DTX_IMAGES[jindex], full=True, multichannel=True)
            if score > best_score:
                closest_match = (magic_texture[len(DTX_PATH):], score)
                best_score = score
                # Destroy old list, add current texture
                SHARED_TEXTURE = [magic_texture[len(DTX_PATH):]]
            elif score == best_score:
                # Shared texture scenario
                SHARED_TEXTURE.append(magic_texture[len(DTX_PATH):])

        except ValueError:
            diff = -1
    if best_score > 0.8:
        TOTAL_MATCHES.append((dolphin_texture[len(DFDTX_PATH):], closest_match, SHARED_TEXTURE))

print("Saved pairs to resumable file")
pickle.dump(TOTAL_MATCHES, open('resumable_matched_results.txt', 'wb'))
x = pickle.load(open('resumable_matched_results.txt', 'rb'))
assert x == TOTAL_MATCHES

print("Process took:\n%s seconds" % (time.time() - start_time))