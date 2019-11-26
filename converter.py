import sys
import os
from PIL import Image

fromJpg = sys.argv[1]
toPng = sys.argv[2]

if not os.path.isdir(toPng):
    os.mkdir(toPng)
for filename in os.listdir(fromJpg):
    if filename.endswith(".jpg"):
        im = Image.open(f'{fromJpg}/{filename}')
        """
            # another way to remove the extension from the filename
            # By using --> os.path.splitext(filename)[0]
        """

        im.save(f'{toPng}/{filename[:-4]}.png')
    else:
        continue
