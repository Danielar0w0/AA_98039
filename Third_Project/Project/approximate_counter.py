from utils import process_files
import numpy as np
import time
import json


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
        prob = 1 / np.sqrt(2) ** k

        # Increment with previous probability
        if np.random.uniform(0, 1) <= prob:
            counter[letter] += 1

    return counter, time.time() - start


if __name__ == '__main__':

    # Open file to store time statistics
    stats = open("statistics/time_approximate_counter.txt", "w", encoding="utf-8")
    stats.write(f'{"Title":<40} {"Time":<25}\n')

    # Set number of trials
    n_trials = 10000

    # Set seed with nMec
    np.random.seed(98039)

    streams = process_files()
    for title in streams:

        file = open("counters/approximate_counters/" + title + ".txt", "w", encoding="utf-8")
        avg_time = 0

        for trial in range(n_trials):

            # Obtain approximate counters
            counter, processing_time = approximate_counter(streams[title])

            # Store processing time
            # stats.write(f'{title + ":":<40} {processing_time:<25}\n')

            # Store the approximate counters
            file.write(json.dumps(counter) + "\n")

            # Update average processing time
            avg_time += processing_time

        # Store average processing time
        stats.write(f'{title + ":":<40} {avg_time / n_trials:<25}\n')

        file.close()

    stats.close()

