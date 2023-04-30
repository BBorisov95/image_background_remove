import os
from rembg import remove
from PIL import Image

path_to_imgs = input('Please select the folder of images for background removal: ')
path_to_output = input('Please select the folder of output images: ')

for file_type in [path_to_imgs]:
    for img in os.listdir(file_type):
        input_img = Image.open(path_to_imgs + "\\" + img)
        output_img = remove(input_img)
        output_img.save(path_to_output + "\\" + img.split('.jpg')[0] + ".png")
