from utils import process_files
import time


def frequent_count(stream, k):

    # Start timer
    start = time.time()

    # Initialize the counter
    counter = {}

    # Count the frequency of each element
    for letter in stream:

        # If the letter is in the counter
        if letter in counter:
            # Increment the counter
            counter[letter] += 1

        # If the letter is not in the counter
        elif len(counter.keys()) < k - 1:
            counter[letter] = 1

        else:
            # Decrement all counters
            for key in counter:
                counter[key] -= 1

            # Remove the letter from the counter if its counter is 0
            counter = {key: value for key, value in counter.items() if value != 0}

    return counter, time.time() - start


if __name__ == "__main__":

    # Open file to store time statistics
    stats = open("statistics/time_data_stream_counter.txt", "w", encoding="utf-8")
    stats.write(f'{"Title":<40} {"Time":<25} {"k":<10}\n')

    # Set all possible k
    all_k = [3, 5, 10]

    streams = process_files()
    for title in streams:

        counters = []

        for k in all_k:

            counter, processing_time = frequent_count(streams[title], k)
            stats.write(f'{title + ":":<40} {processing_time:<25} {k:<10}\n')

            # Store the frequent counters
            with open("data_stream_counters/" + title + "_K" + str(k) + ".txt", "w", encoding="utf8") as file:
                file.write(f'{"Letter":<10} {"Counter":<10}\n')
                for letter in counter:
                    file.write(f'{letter:<10} {counter[letter]:<10}\n')

            counters.append(counter)
