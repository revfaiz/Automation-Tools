import pyttsx3
from pypdf import PdfReader

# Insert the name of your PDF file
pdf_reader = PdfReader('book2.pdf')
speaker = pyttsx3.init()

# Initialize a variable to accumulate all the extracted text
full_text = ""

# Loop through all pages in the PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    if text:  # If text is extracted
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + "\n"  # Append the clean text of the current page

# Save the accumulated text as one MP3 file
# Name the MP3 file whatever you would like
speaker.save_to_file(full_text, 'Mlops.mp3')

# Run the speech synthesis and wait until it's done
speaker.runAndWait()

# Stop the speaker after finishing
speaker.stop()
