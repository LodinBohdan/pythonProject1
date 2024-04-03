import re

def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Підрахунок слів
    words = re.findall(r'\w+', text)
    word_count = len(words)

    # Підрахунок речень
    sentences = re.split(r'[.!?…]', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    sentence_count = len(sentences)

    return word_count, sentence_count
