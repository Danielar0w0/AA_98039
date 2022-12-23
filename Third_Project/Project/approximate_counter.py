from utils import process_files
import numpy as np
import time
import decimal


def approximate_counter(stream):

    # Start timer
    start = time.time()

    # Initialize the counter
    counter = {}

    for letter in stream:

        if letter not in counter:
            counter[letter] = 0

        # Counter has value k
        k = counter[letter]

        # Decreasing probability counter : 1 / sqrt(2)^k
        prob = 1 / (decimal.Decimal(np.sqrt(2)) ** k)

        # Increment with previous probability
        if np.random.uniform(0, 1) < 1 / prob:
            counter[letter] += 1

    return counter, time.time() - start


if __name__ == '__main__':

    # Open file to store time statistics
    stats = open("statistics/time_approximate_counter.txt", "w", encoding="utf-8")
    stats.write(f'{"Title":<40} {"Time":<25}\n')

    # Set number of trials
    n_trials = 2

    # Set seed with nMec
    np.random.seed(98039)

    streams = process_files()
    for title in streams:

        for trial in range(n_trials):

            # Obtain approximate counters
            counter, processing_time = approximate_counter(streams[title])

            # Store processing time
            stats.write(f'{title + ":":<40} {processing_time:<25}\n')

            # Store the approximate counters
            with open("approximate_counters/" + title + "_trial" + str(trial + 1) + ".txt", "w", encoding="utf8") as file:
                file.write(f'{"Letter":<10} {"Counter":<10}\n')
                for letter in counter:
                    file.write(f'{letter:<10} {counter[letter]:<10}\n')

    stats.close()
