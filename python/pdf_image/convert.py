# Sources : https://stackoverflow.com/questions/69643954/converting-pdf-to-png-with-python-without-pdf2image
#           https://datatofish.com/images-to-pdf-python/

import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
import os
from PIL import Image
from os import listdir
from os.path import isfile, join

def pdf_2_images(pdf_file, dir_images):
    doc = fitz.open(pdf_file)  # open document
    if not os.path.isdir(dir_images):
        os.makedirs(dir_images)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=200)  # render page to an image
        image_file = os.path.join(dir_images, f"page_{i:03d}.png")
        pix.save(image_file)


def get_img_files(dir_path):
    '''Returns all the png files of a directory'''
    onlyfiles = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return onlyfiles

def imgdir_2_pdf(dir_images, pdf_file):
    img_files = get_img_files(dir_images)
    
    if len(img_files) == 0:
        print("No images to convert...")
        return
    
    image_1 = Image.open(img_files[0])
    im_1 = image_1.convert('RGB')

    image_list = [ ]
    for i in range(1, len(img_files) - 1):
        image = Image.open(img_files[i])
        im = image.convert('RGB')
        image_list.append(im)

    im_1.save(pdf_file, save_all=True, append_images=image_list)
