import random
import csv
import sys
import time

def generate_dataset(n, filename):
    start_time = time.time()  # Start the timer

    with open(f"../dataset/{filename}", "w", newline="") as file:
        writer = csv.writer(file)
        for i in range(1, n + 1):
            integer = random.randint(0, 1000000000)
            string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            writer.writerow([integer, string])

            # Print the progress every 100,000 records to reduce console clutter
            if i % 100000 == 0:
                elapsed_time = time.time() - start_time
                print(f"Generated: {i}/{n} records | Time Elapsed: {elapsed_time:.2f} seconds", end="\r")
                sys.stdout.flush()

    total_time = time.time() - start_time  # Calculate total time
    print(f"\nDataset generation completed: {n} records in {total_time:.2f} seconds.")

generate_dataset(1000000000, "dataset_sample_1000000000.csv")
