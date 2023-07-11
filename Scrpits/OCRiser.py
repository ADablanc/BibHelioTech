from pdf2image import convert_from_path
from tqdm import tqdm
from PIL import Image
import pytesseract
import os




def PDF_OCRiser(current_OCR_folder,PDF_file):
    '''
    Part #1 : Converting PDF to images
    '''

    # Store all the pages of the PDF in a variable
    pages = convert_from_path(os.path.join(current_OCR_folder,PDF_file), dpi=600)

    # Iterate through all the pages stored above
    for i,page in tqdm(enumerate(pages),total=len(pages), colour="green", unit=" pages", desc="\tconverting"):
        # Save the image of the page in system
        page.save(os.path.join(current_OCR_folder, f"page_{i+1}.jpg"), 'JPEG')

    '''
    Part #2 - Recognizing text from the images using OCR
    '''

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    with open(os.path.join(current_OCR_folder,"out_text.txt"), "a", encoding="UTF-8") as buffer:
        # Iterate from 1 to total number of pages
        for i in tqdm(range(1, len(pages) + 1),total=len(pages), colour="green", unit=" pages", desc="\t       ocr"):
            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(Image.open(os.path.join(current_OCR_folder, f"page_{i}.jpg"))))))

            text = text.replace('-\n', '')

            buffer.write(text)