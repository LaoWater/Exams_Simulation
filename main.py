from pathlib import Path


DATA_FILE = Path(__file__).with_name("transmission.txt")


def load_clean_lines(filepath):
    # TODO 1:
    # Open the file and read it line by line.
    # Strip each line.
    # Ignore blank lines.
    # Ignore lines that start with "STATIC:".
    # Return a list of the remaining cleaned lines.
    return []


class BeaconBoard:
    def __init__(self, lighthouse_name):
        self.lighthouse_name = lighthouse_name
        self.lines = []

    def add_line(self, line):
        # TODO 2:
        # Add the cleaned line to self.lines.
        pass

    def full_message(self):
        # TODO 3:
        # Join every line in self.lines into one string and return it.
        return ""

    def count_help_calls(self):
        # TODO 4:
        # Count how many stored lines contain the word "help".
        return 0

    def show_message(self):
        # TODO 5:
        # Print the lighthouse name and the final message clearly.
        pass


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


if __name__ == "__main__":
    main()
