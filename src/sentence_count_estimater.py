import fitz  # PyMuPDF
import re


def count_sentences_and_words_in_pdf(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    text = ""

    # Extract text from each page
    for page in doc:
        text += page.get_text()

    # Count sentences using a regular expression
    # This regex considers sentences to end with '.', '?', or '!'
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    sentence_count = len(sentences)

    # Split the text into words and count
    words = text.split()
    word_count = len(words)

    return sentence_count, word_count


pdf_path = '/Users/eliasstrauss/Downloads/Thesis__Feature_Engineering_for_Multimodal_Machine_Learning (13).pdf'
sentence_count, word_count = count_sentences_and_words_in_pdf(pdf_path)
print(f'Estimated Number of Sentences: {sentence_count}')
print(f'Estimated Number of Words: {word_count}')