from collections import Counter
from utils import process_files
import numpy as np
import time
import decimal


def obtain_exact_counter(stream):

    # Start timer
    start = time.time()

    # Count the frequency of each letter
    return Counter(stream), time.time() - start


def obtain_approximate_counter(stream):

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


def obtain_frequent_count(stream, k):

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


def handle_exact_counter(stream, stats_time):

    # Obtain exact counters
    counter, processing_time = obtain_exact_counter(stream)
    save_stats_time(stats_time, "Exact Counter", processing_time)

    # Store the exact counters
    with open("exact_counters/" + title + ".txt", "w", encoding="utf8") as file:
        for letter in counter:
            file.write(letter + " - " + str(counter[letter]) + "\n")

    return counter


def handle_approximate_counter(stream, stats_time):

    # Set number of trials
    n_trials = 2

    counters = []

    for trial in range(n_trials):

        # Obtain approximate counters
        counter, processing_time = obtain_approximate_counter(stream)
        save_stats_time(stats_time, "Approximate Counter", processing_time)

        # Store the approximate counters
        with open("approximate_counters/" + title + "_trial" + str(trial + 1) + ".txt", "w", encoding="utf8") as file:
            for letter in counter:
                file.write(letter + " - " + str(counter[letter]) + "\n")

        counters.append(counter)

    return counters


def handle_frequent_count(stream, stats_time):

    # Set all possible k
    all_k = [3, 5, 10]

    counters = []

    for k in all_k:

        counter, processing_time = obtain_frequent_count(stream, k)
        save_stats_time(stats_time, f"Data Stream Counter (k = {k})", processing_time)

        # Store the frequent counters
        with open("frequent_counters/" + title + "_K" + str(k) + ".txt", "w", encoding="utf8") as file:
            for letter in counter:
                file.write(letter + " - " + str(counter[letter]) + "\n")

        counters.append(counter)

    return counters


def save_stats_time(file, algorithm, processing_time):
    file.write(f'{algorithm + ":":<30} {processing_time:<25} seconds\n')


if __name__ == "__main__":

    np.random.seed(98039)

    stats = open("statistics/time.txt", "w", encoding="utf-8")

    streams = process_files()
    for title in streams:

        stats.write(title + "\n")
        stats.write("------------------------------------------\n")

        # Exact Counter
        exact_counter = handle_exact_counter(streams[title], stats)

        # Approximate Counter
        approximate_counters = handle_approximate_counter(streams[title], stats)

        # Data Stream Counter
        data_stream_counters = handle_frequent_count(streams[title], stats)

        stats.write("\n")

    stats.close()
