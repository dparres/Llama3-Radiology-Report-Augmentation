import random

def reorder_sentences(paragraph):

    # Split the string into sentences
    sentences = paragraph.split('. ')

    # Remove empty strings from the list (resulting from the split)
    sentences = [sentence.strip() for sentence in sentences if sentence]

    # Shuffle the order of the sentences
    random.shuffle(sentences)

    # Join the sentences back into a string
    output_string = '. '.join(sentences)

    # Add a period at the end of the string if it's missing
    if not output_string.endswith('.'):
        output_string += '.'

    return output_string
