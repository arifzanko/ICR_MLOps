import os
import matplotlib.pyplot as plt
from pathlib import Path
import configparser

confp = configparser.RawConfigParser()
confp.read(os.path.abspath(os.path.join(Path(__file__).absolute(), os.pardir)) + '/config.ini')
datasets_test = confp.get("explore","datasets_test")
datasets_train = confp.get("explore","datasets_train")
datasets_valid = confp.get("explore","datasets_valid")

def counts_plot(folder_path, save_path):
    text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    # Dictionary to store the frequency of each character (0-9 and A-Z) across all files
    character_counts = {str(i): 0 for i in range(10)}
    character_counts.update({chr(ord('A') + i): 0 for i in range(26)})

    for txt_file in text_files:
        file_path = os.path.join(folder_path, txt_file)

        # Open and read the content of each text file
        with open(file_path, 'r') as file:
            file_content = file.read()

        lines = file_content.split('\n')  # Split the text into lines

        for line in lines:
            values = line.split()  # Split each line into individual values
            if values:
                number = int(values[0])  # Convert the first value to an integer
                if 0 <= number <= 9:
                    character = str(number)
                    character_counts[character] += 1
                elif 10 <= number <= 35:
                    character = chr(ord('A') + (number - 10))
                    character_counts[character] += 1

    # Create a bar chart to visualize the counts of characters
    characters = list(character_counts.keys())
    counts = list(character_counts.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(characters, counts)
    plt.xlabel('Character (0-9 and A-Z)')
    plt.ylabel('Count')
    plt.title('Character Counts 0-9 and A-Z')

    # Add text annotations to each bar
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() + 0.1, str(count), ha='center', va='bottom')

    # Save the figure to the specified path
    plt.savefig(save_path)


def data_explore():
    current_path = os.getcwd()
    train_file_path = os.path.join(current_path, datasets_train)
    save_train_file_path = os.path.join(current_path, 'data_train_analysis.png')
    counts_plot(train_file_path, save_train_file_path)

    test_file_path = os.path.join(current_path, datasets_test)
    save_test_file_path = os.path.join(current_path, 'data_test_analysis.png')
    counts_plot(test_file_path, save_test_file_path)

    valid_file_path = os.path.join(current_path, datasets_valid)
    save_valid_file_path = os.path.join(current_path, 'data_valid_analysis.png')
    counts_plot(valid_file_path, save_valid_file_path)




