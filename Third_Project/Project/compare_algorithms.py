import json

import numpy as np


def obtain_exact_counters(title):

    with open("counters/exact_counters/" + title + ".txt", "r", encoding="utf8") as file:
        line = file.readline()
        counters = dict(json.loads(line))

        return dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))


def compare_approximate_counters(title, exact_counters):

    # Keep track of all counters (for n trials)
    total_letters = []

    # Keep track of all orders (for n trials)
    total_orders = {}

    # Keep track of first 5 letters order
    first_5_letters = {}

    # Obtain all counters
    with open("counters/approximate_counters/" + title + ".txt", "r", encoding="utf8") as file:

        while True:

            line = file.readline()

            # If EOF, break
            if not line:
                break

            # Obtain counters
            counters = dict(json.loads(line))
            counters = dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))

            total = sum(counters.values())
            total_letters.append(total)

            # Obtain letters order
            order = "".join(counters)
            if order not in total_orders:
                total_orders[order] = 0

            total_orders[order] += 1

            # Obtain first 5 letters order
            order = order[:5]

            if order not in first_5_letters:
                first_5_letters[order] = 0

            first_5_letters[order] += 1

    # ----------------------------

    real_total = sum(exact_counters.values())
    real_order = "".join(exact_counters.keys())

    n = real_total

    # Decreasing probability counter : 1 / sqrt(2)^k
    p = 1 / np.sqrt(2)
    q = 1 - p

    # Expected value
    expected_value = n * p

    # Expected value of each counter
    expected_value_dict = {letter: n * p for letter, n in counters.items()}

    # Real Variance
    real_variance = n * p * q

    # Real standard deviation
    real_standard_deviation = np.sqrt(real_variance)

    # -----------------------------

    n = len(total_letters)
    mean = sum(total_letters) / n

    # Maximum deviation
    maximum_deviation = max([abs(total - mean) for total in total_letters])

    # Mean absolute deviation
    mean_absolute_deviation = sum([abs(total - mean) for total in total_letters]) / n

    # Variance
    variance = sum([(total - mean) ** 2 for total in total_letters]) / n

    # Standard deviation (variance ** 0.5)
    standard_deviation = np.sqrt(sum([(total - mean) ** 2 for total in total_letters]) / n)

    # Mean absolute error
    mean_absolute_error = sum([abs(total - real_total) for total in total_letters]) / n

    # Mean relative error
    mean_relative_error = sum([abs(total - real_total) / real_total * 100 for total in total_letters]) / n

    # Mean accuracy ratio
    # mean_accuracy_ratio = len([total for total in total_letters if total == real_total]) / n
    mean_accuracy_ratio = mean / expected_value

    # -----------------------------

    # Smallest counter value
    smallest_value = min(total_letters)

    # Largest counter value
    largest_value = max(total_letters)

    # -----------------------------

    # Orders sorted by frequency
    total_orders = {letter: counter for letter, counter in sorted(total_orders.items(), key=lambda item: item[1], reverse=True)}

    # First 5 letters sorted by frequency
    first_5_letters = {letter: counter for letter, counter in sorted(first_5_letters.items(), key=lambda item: item[1], reverse=True)}

    # Order Accuracy
    order_accuracy = total_orders[real_order] / n if real_order in total_orders else 0

    # First 5 letters Accuracy
    first_5_letters_accuracy = first_5_letters[real_order[:5]] / n if real_order[:5] in first_5_letters else 0

    with open("statistics/approximate_counters/" + title + ".txt", "w", encoding="utf8") as stats:

        stats.write(f"Expected value: {expected_value}\n")
        stats.write(f"Variance: {real_variance}\n")
        stats.write(f"Standard deviation: {real_standard_deviation}\n\n")

        stats.write(f"Mean absolute error: {mean_absolute_error}\n")
        stats.write(f"Mean relative error: {mean_relative_error * 100}%\n")
        stats.write(f"Mean accuracy ratio: {mean_accuracy_ratio * 100}%\n\n")

        stats.write(f"Smallest counter value: {smallest_value}\n")
        stats.write(f"Largest counter value: {largest_value}\n\n")

        stats.write(f"Mean counter value: {mean}\n")
        stats.write(f"Mean absolute deviation: {mean_absolute_deviation}\n")
        stats.write(f"Standard deviation: {standard_deviation}\n")
        stats.write(f"Maximum deviation: {maximum_deviation}\n")
        stats.write(f"Variance: {variance}\n\n")

        stats.write(f'Real Char Frequency Order: {real_order}\n')
        stats.write(f'Letter Order Accuracy: {order_accuracy * 100}%\n')
        stats.write('10 Most Common Orders:\n')

        for i, order in enumerate(total_orders):
            if i >= 10:
                break
            stats.write(f'{order}: {total_orders[order]}\n')

        stats.write("\n")

        stats.write(f'Top 5 Char Order Accuracy: {first_5_letters_accuracy * 100}%\n')
        stats.write('10 Most Common Orders:\n')
        for i, order in enumerate(first_5_letters):
            if i >= 10:
                break
            stats.write(f'{order}: {first_5_letters[order]}\n')

        stats.write("\n")

        stats.write('Mean Counter Values per letter:\n')
        stats.write(f'Letter : Counter Value : Expected Value\n')
        for letter, counter in counters.items():
            stats.write(f'{letter} : {counter} : {expected_value_dict[letter]}\n')


if __name__ == "__main__":

    # All books
    books = ["Alice’s Adventures in Wonderland", "Alice's Abenteuer im Wunderland", "Aventures d'Alice au pays"]

    for book in books:

        exact_counters = obtain_exact_counters(book)

        # Compare approximate counters
        compare_approximate_counters(book, exact_counters)
