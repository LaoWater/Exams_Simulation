from pathlib import Path


DATA_FILE = Path(__file__).with_name("transmission.txt")


def load_clean_lines(filepath):
    # Open the file and read all lines
    with open(filepath, 'r') as f:
        lines = f.readlines()
    cleaned = []
    for line in lines:
        line = line.strip()  # Remove whitespace
        if not line:
            continue  # Skip blank lines
        if line.startswith("STATIC:"):
            continue  # Skip lines starting with STATIC:
        cleaned.append(line)
    return cleaned


class BeaconBoard:
    def __init__(self, lighthouse_name):
        self.lighthouse_name = lighthouse_name
        self.lines = []

    def add_line(self, line):
        # Add the cleaned line to the list
        self.lines.append(line)

    def full_message(self):
        # Join all lines into a single string separated by spaces
        return ' '.join(self.lines)

    def count_help_calls(self):
        # Count lines containing the word 'help'
        return sum('help' in line for line in self.lines)

    def show_message(self):
        # Print the lighthouse name and the full message
        print(f"Lighthouse: {self.lighthouse_name}")
        print("Message:")
        print(self.full_message())


def word_count(message):
    # OPTIONAL TASK:
    # Return a dictionary that counts each word in the message.
    counts = {}
    return counts


def print_story_setup():
    print("=== Harbor Distress Log ===")
    print("A damaged lighthouse radio log must be cleaned before the harbor team can act.\n")
    print("Use transmission.txt to rebuild the message.")


def print_checklist():
    print("\nFinish the TODOs, then test these checks:")
    print("1. load_clean_lines() should skip STATIC lines and blank lines.")
    print("2. add_line() should store every cleaned line.")
    print("3. full_message() should join the stored lines into one message.")
    print("4. count_help_calls() should count lines containing 'help'.")
    print("5. show_message() should print a readable result.")
    print("6. Optional: word_count() should build a frequency dictionary.")


def run_quick_checks():
    board = BeaconBoard("North Point")
    clean_lines = load_clean_lines(DATA_FILE)
    for line in clean_lines:
        board.add_line(line)

    # What is 'assert'?
    # 'assert' is used to auto-test your answers.
    # If your load_clean_lines() function correctly filters out the junk lines,
    # the length of the list will be exactly 4, and the assert passes.
    # Otherwise, it crashes to let you know something is wrong.
    assert len(clean_lines) == 4
    assert board.count_help_calls() == 2
    assert "help" in board.full_message()


def main():
    print_story_setup()
    print_checklist()
    print("\nAfter finishing the TODOs, run run_quick_checks() to self-test.")



    lines = load_clean_lines(DATA_FILE)
    # Create a BeaconBoard for a sample lighthouse
    board = BeaconBoard("Sulina Lighthouse")
    # Add each cleaned line to the board
    for line in lines:
        board.add_line(line)
    # Show the full message
    board.show_message()
    # Print the number of help calls
    print(f"Number of help calls: {board.count_help_calls()}")


if __name__ == "__main__":
    main()
