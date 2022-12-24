import string


def load_stopwords():
    with open("stopwords.txt", encoding="utf8") as file:
        return file.read().split("\n")


def process_files():

    # Load stopwords
    stopwords = load_stopwords()

    # All books
    books = ["Alice’s Adventures in Wonderland", "Alice's Abenteuer im Wunderland", "Aventures d'Alice au pays"]
    processed_books = {}

    # File to keep track of text processing
    stats = open("statistics/text_processing.txt", "w", encoding="utf8")
    stats.write(f'{"Title":<40} {"Initial Length":<25} {"Final Length"}\n')

    # Open Project Gutenberg files
    for book in books:

        with open("Project_Gutenberg/" + book + ".txt", encoding="utf8") as file:
            text = file.read()

            # print("Title: " + book)
            # print("Initial length of text: ", len(text))

            # Keep track of initial length (before processing)
            initial_length = len(text)

            # Remove header and footer
            header = f"*** START OF THE PROJECT GUTENBERG EBOOK {book.upper()} ***"
            start = text.find(header) + len(header)

            footer = f"*** END OF THE PROJECT GUTENBERG EBOOK {book.upper()} ***"
            end = text.find(footer)

            text = text[start:end]

            # Remove Illustrations
            text = text.replace("[Illustration]", "")

            # Remove punctuation
            punctuation = string.punctuation
            for char in punctuation:
                text = text.replace(char, "")

            # Remove all stopwords and whitespaces with nltk
            # text = "".join([word for word in text.split() if word not in stopwords.words("english")])

            # Remove all stopwords and whitespaces without nltk
            text = "".join([word for word in text.split() if word.lower() not in stopwords])

            # Keep only letters
            text = "".join([char for char in text if char.isalpha()])

            # Convert all letters to uppercase
            text = text.upper()

            # print("Final length of text: ", len(text))
            # print("------------------------")

            # Keep track of final length (after processing)
            final_length = len(text)

            processed_books[book] = text

        # Store length of text before and after processing
        stats.write(f'{book:<40} {initial_length:<25} {final_length}\n')

    stats.close()

    return processed_books


def load_exact_counter(title):

    exact_counter = {}
    try:
        with open("exact_counters/" + title + ".txt", encoding="utf8") as file:

            # Skip the first line
            file.readline()

            # Read all letters - counters
            for line in file:
                letter, counter = line.split()
                exact_counter[letter] = int(counter)

        return exact_counter

    except FileNotFoundError:
        return None
