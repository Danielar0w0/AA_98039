from utils import process_files, load_exact_counter
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
        if np.random.uniform(0, 1) <= 1 / prob:
            counter[letter] += 1

    return counter, time.time() - start


def compare_counters(exact, other):

    # Number of letters in the exact counter
    n = len(exact.keys())

    # Number of letters in the other counter
    m = len(other.keys())

    # Number of correct counters
    correct_counters = len([c for c in other.items() if c in exact.items()])

    for letter in exact:

        # Number of events
        n = exact[letter]

        # Decreasing probability counter : 1 / sqrt(2)^k
        p = 1 / np.sqrt(2)
        q = 1 - p

        # Estimated value
        estimated_value = n * p

        # True value
        true_value = exact[letter]

        # Absolute error
        absolute_error = abs(estimated_value - true_value)

        # Relative error
        relative_error = absolute_error / true_value * 100

        # Variance
        variance = n * p * q

    # TODO: Mean absolute error
    mean_absolute_error = 0

    # TODO: Mean relative error
    mean_relative_error = 0

    # TODO: Mean Accuracy Ratio
    mean_accuracy_ratio = 0

    # TODO: Variance
    variance = 0

    # TODO: Standard deviation
    standard_deviation = 0

    # TODO: Mean Counter Value
    mean_counter_value = 0

    # TODO: Mean absolute deviation
    mean_absolute_deviation = 0

    # TODO: Standard Deviation
    standard_deviation = 0

    # TODO: Maximum Deviation
    maximum_deviation = 0

    # TODO: Variance again?

    # print(f"Expected value: {estimated_value}")
    print(f"Variance: {variance}")
    print(f"Standard deviation: {standard_deviation}")
    print()
    print(f"Mean absolute error: {mean_absolute_error}")
    print(f"Mean relative error: {mean_relative_error}")
    print(f"Mean accuracy ratio: {mean_accuracy_ratio}")
    print()
    print(f"Smallest counter value: {min(other.values())}")
    print(f"Largest counter value: {max(other.values())}")
    print()
    print(f"Mean counter value: {mean_counter_value}")
    print(f"Mean absolute deviation: {mean_absolute_deviation}")
    print(f"Standard deviation: {standard_deviation}")
    print(f"Maximum deviation: {maximum_deviation}")
    # print(f"Variance: {variance}")
    print("-----------------------------------")


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

        # counters = []
        exact_counter = load_exact_counter(title)

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

            # counters.append(counter)
            compare_counters(exact_counter, counter)

        # Compare the counters


    stats.close()

