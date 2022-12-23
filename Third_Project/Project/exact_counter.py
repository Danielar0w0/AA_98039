from collections import Counter
from utils import process_files
import time


def exact_counter(stream):

    # Start timer
    start = time.time()

    # Count the frequency of each letter
    return Counter(stream), time.time() - start


if __name__ == '__main__':

    # Open file to store time statistics
    stats = open("statistics/time_exact_counter.txt", "w", encoding="utf-8")
    stats.write(f'{"Title":<40} {"Time":<25}\n')

    streams = process_files()
    for title in streams:

        # Obtain exact counters
        counter, processing_time = exact_counter(streams[title])

        # Store processing time
        stats.write(f'{title + ":":<40} {processing_time:<25}\n')

        # Store the exact counters
        with open("exact_counters/" + title + ".txt", "w", encoding="utf8") as file:
            file.write(f'{"Letter":<10} {"Counter":<10}\n')
            for letter in counter:
                file.write(f'{letter:<10} {counter[letter]:<10}\n')

    stats.close()
