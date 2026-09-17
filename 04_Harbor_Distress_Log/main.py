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
        # Join self.lines with one space between lines and return the string.
        # Hint: " ".join(self.lines)
        return ""

    def count_help_calls(self):
        # TODO 4:
        # Count lines where "help" is a separate word in line.lower().split().
        # Count each matching line once. The supplied text has no punctuation.
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


# Small example to run after completing the main TODOs.
def run_demo():
    board = BeaconBoard("North Point")
    lines = load_clean_lines(DATA_FILE)
    for line in lines:
        board.add_line(line)
    print("Clean lines:", len(lines), "| Expected: 4")
    print("Help calls:", board.count_help_calls(), "| Expected: 2")
    print("Message:", board.full_message())
    print("Expected:", "help fishing boat mara near south breakwater engine failed after taking water help request tow to sulina harbor before dark crew safe waiting with anchor down")


def main():
    print_story_setup()
    print_checklist()
    print("\nAfter finishing the TODOs, run run_demo() to compare your results with the expected values.")


if __name__ == "__main__":
    main()
