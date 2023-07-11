from OCRiser import *
import shutil
import os

INPUT_PATH = "../DATA/INPUT"
OUTPUT_PATH = "../DATA/OUTPUT"

for files in os.listdir(INPUT_PATH):
    if files.endswith(".pdf"):
        filename = files.replace(".pdf","") # Retrieve filename

        if not os.path.exists(os.path.join(OUTPUT_PATH,filename)):
            os.makedirs(os.path.join(OUTPUT_PATH,filename)) # Create the output directory if it does not exist

        shutil.move(os.path.join(INPUT_PATH,f"{filename}.pdf"),os.path.join(os.path.join(OUTPUT_PATH,filename),f"{filename}.pdf")) # Move file to OUTPUT directory


        PDF_OCRiser(os.path.join(OUTPUT_PATH,filename),f"{filename}.pdf")