from PIL import image
import os

descargas = "/data/data/com.termux/files/home/storage/shared/Download"

scream = "/data/data/com.termux/files/home/storage/shared/DCIM/Screenshots"

if __name__ == "__main__" :
    for filename in os.listdir(descargas, scream + filename):

        if extension in ["jpg", "png", "jpeg", "mp4"]:

            picture = image.open(descargas, scream + filename)
            picture.save(descargas, scream + "compressed_"+ filename, optimize=True, quality=60)

