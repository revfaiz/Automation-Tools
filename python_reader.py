from gtts import gTTS
from pypdf import PdfReader
from tqdm import tqdm

# Insert the name of your PDF file
pdf_reader = PdfReader('book.pdf')

# Initialize a variable to accumulate all the extracted text
full_text = ""

# Loop through all pages in the PDF with a progress bar
for page_num in tqdm(range(len(pdf_reader.pages)), desc="Processing pages"):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    if text:  # If text is extracted
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + "\n"  # Append the clean text of the current page

# Convert the accumulated text to speech using gTTS
# You can specify the language (e.g., 'en' for English, 'es' for Spanish, etc.)
tts = gTTS(text=full_text, lang='en-uk', slow=False)  # slow=False means the speech will be normal speed

# Save the speech to an MP3 file
tts.save("th.mp3")

# The audio will be saved in the current directory with the name 'complete_story.mp3'
