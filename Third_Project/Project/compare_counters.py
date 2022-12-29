import json
import numpy as np


def obtain_exact_counters(title):

    with open("counters/exact_counters/" + title + ".txt", "r", encoding="utf8") as file:
        line = file.readline()
        counters = dict(json.loads(line))

        return dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))


def compare_approximate_counters(title, exact_counters):

    # Keep track of mean counter values
    avg_counts = {}

    # Keep track of total number of letters (for n trials)
    total_letters = []

    # Keep track of all orders (for n trials)
    total_orders = {}

    # Keep track of order for first 3 letters
    first_3_letters = {}

    # Keep track of most frequent letter
    most_frequent_letters = {}

    # Obtain all trials
    with open("counters/approximate_counters/" + title + ".txt", "r", encoding="utf8") as file:

        while True:

            line = file.readline()

            # If EOF, break
            if not line:
                break

            # Obtain counters
            counters = dict(json.loads(line))
            counters = dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))

            # Obtain total number of letters
            total = sum(counters.values())
            total_letters.append(total)

            # Obtain mean counter values
            for letter, count in counters.items():
                if letter not in avg_counts:
                    avg_counts[letter] = 0
                avg_counts[letter] += count

            # Obtain letters order
            order = "".join(counters)
            if order not in total_orders:
                total_orders[order] = 0

            total_orders[order] += 1

            # Obtain first 3 letters order
            order = order[:3]

            if order not in first_3_letters:
                first_3_letters[order] = 0

            first_3_letters[order] += 1

            # Obtain most frequent letter
            most_frequent_letter = order[0]

            if most_frequent_letter not in most_frequent_letters:
                most_frequent_letters[most_frequent_letter] = 0

            most_frequent_letters[most_frequent_letter] += 1

    avg_counts = {letter: count/len(total_letters) for letter, count in avg_counts.items()}
    avg_counts = dict(sorted(avg_counts.items(), key=lambda item: item[1], reverse=True))

    # ----------------------------

    real_total = sum(exact_counters.values())
    real_order = "".join(exact_counters.keys())

    n = real_total

    # Decreasing probability counter : 1 / a^k = 1 / sqrt(2)^k
    a = np.sqrt(2)

    # n = (a**k – a + 1) / (a – 1) =>
    # => k = log_a(n_events * (a – 1) + a – 1) =>
    # => k = log(n_events * (a – 1) + a – 1)/log(a)

    # Expected value of each counter
    expected_value_dict = {letter: np.log(count * (a - 1) + a - 1) / np.log(a)
                           for letter, count in exact_counters.items()}

    # Expected value
    expected_value = sum(expected_value_dict.values())

    # Real Variance
    real_variance = expected_value / 2

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

    # Expected value of each counter sorted by frequency
    expected_value_dict = {letter: counter for letter, counter in sorted(expected_value_dict.items(), key=lambda item: item[1], reverse=True)}

    # First 3 letters sorted by frequency
    first_3_letters = {letter: counter for letter, counter in sorted(first_3_letters.items(), key=lambda item: item[1], reverse=True)}

    # Most frequent letters sorted by frequency
    most_frequent_letters = {letter: counter for letter, counter in sorted(most_frequent_letters.items(), key=lambda item: item[1], reverse=True)}

    # Order Accuracy
    order_accuracy = total_orders[real_order] / n if real_order in total_orders else 0

    # First 3 letters Accuracy
    first_3_letters_accuracy = first_3_letters[real_order[:3]] / n if real_order[:3] in first_3_letters else 0

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

        stats.write(f"Real Char Frequency Order: {real_order}\n")
        stats.write(f"Letter Order Accuracy: {order_accuracy * 100}%\n")
        stats.write("10 Most Common Orders:\n")

        for i, order in enumerate(total_orders):
            if i >= 10:
                break
            stats.write(f'{order}: {total_orders[order]}\n')

        stats.write("\n")

        stats.write(f'Top 3 Char Order Accuracy: {first_3_letters_accuracy * 100}%\n')
        stats.write('10 Most Common Orders:\n')
        for i, order in enumerate(first_3_letters):
            if i >= 10:
                break
            stats.write(f'{order}: {first_3_letters[order]}\n')

        stats.write("\n")

        stats.write(f"Most Frequent Letter: {real_order[0]}\n")
        stats.write(f"Letter Accuracy: {most_frequent_letters[real_order[0]]/n * 100}%\n")
        stats.write("10 Most Common Letters:\n")

        for i, letter in enumerate(most_frequent_letters):
            if i >= 10:
                break
            stats.write(f'{letter} ')

        stats.write("\n\n")

        stats.write('Mean Counter Values per letter:\n')
        stats.write(f'Letter : Counter Value : Expected Value\n')
        for letter, counter in avg_counts.items():
            stats.write(f'{letter:<6} : {counter:<13} : {expected_value_dict[letter]}\n')


def compare_data_stream_counters(title, exact_counters):

    # Set all possible k
    all_k = [3, 5, 10]

    for k in all_k:

        with open("counters/data_stream_counters/" + title + "_K" + str(k) + ".txt", "r", encoding="utf8") as file:
            line = file.readline()
            counters = dict(json.loads(line))

        top_k_letters = sorted(exact_counters.items(), key=lambda x: x[1], reverse=True)[:k-1]

        with open("statistics/data_stream_counters/" + title + "_K" + str(k) + ".txt", "w", encoding="utf8") as stats:

            stats.write(f"Top {k-1} letters (Exact Counter):\n")
            for letter, counter in top_k_letters:
                stats.write(f"{letter}: {counter}\n")

            stats.write("\n")

            stats.write(f"Top {k-1} letters (Frequent-Count):\n")
            for letter, counter in counters.items():
                stats.write(f"{letter}: {counter}\n")

            stats.write("\n")

            # Accurate letters
            accurate_letters = len([letter for letter, counter in top_k_letters if letter in counters])

            # Accuracy
            accuracy = accurate_letters/(k-1)

            stats.write(f"Accurate letters: {accurate_letters}/{k-1}\n")
            stats.write(f"Accuracy: {accuracy * 100}%\n")


if __name__ == "__main__":

    # All books
    books = ["Alice’s Adventures in Wonderland", "Alice's Abenteuer im Wunderland", "Aventures d'Alice au pays"]

    for book in books:

        exact_counters = obtain_exact_counters(book)

        # Compare approximate counters
        compare_approximate_counters(book, exact_counters)

        # Compare data stream counters
        compare_data_stream_counters(book, exact_counters)
