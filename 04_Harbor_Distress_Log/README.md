# Exam 4: Harbor Distress Log

## Story
During a storm on the coast, a harbor coordination point receives a damaged text log from a lighthouse radio system. The log was saved in `transmission.txt`, but some lines are only static. Your job is to clean the log and rebuild the final distress message.

This exam keeps everything simple and readable. The main work lives in `main.py`, and the text file is your only extra input.

## Exam Style
- Time target: 90 to 120 minutes
- Main file: `main.py`
- Extra file: `transmission.txt`
- Focus: file reading, string cleaning, list appending, joining strings, loops, basic counting

## Main Tasks
1. Complete `load_clean_lines(filepath)`:
   - open the file
   - strip newlines
   - skip blank lines
   - skip lines that start with `STATIC:`
2. Complete `BeaconBoard.add_line()` so it stores cleaned lines.
3. Complete `BeaconBoard.full_message()` so it returns one sentence made from all stored lines.
4. Complete `BeaconBoard.count_help_calls()` so it counts how many lines contain the word `help`.
5. Complete `BeaconBoard.show_message()` so it prints the final message neatly.

## What Is Already Given
- The story setup
- A sample log file
- Starter code in one file
- A test checklist printed when you run the file

## Example Input and Expected Output

**Input (transmission.txt content):**
```text
STATIC: zzzzzzt
send help immediately
STATIC: kkkrrhhh
we need help now

```

**Action:**
```python
lines = load_clean_lines("transmission.txt")
board = BeaconBoard("South Harbor")
for line in lines:
    board.add_line(line)
```

**Expected Results:**
- `load_clean_lines()` should return exactly `["send help immediately", "we need help now"]` (skipping the "STATIC:" lines and blank lines).
- `board.full_message()` should return `"send help immediately we need help now"` (joined with one space).
- `board.count_help_calls()` should return `2`.

## Optional Task
At the bottom of `main.py`, complete `word_count(message)`.

This is optional. It asks you to build a dictionary that counts each word in the final message.

## Run
```bash
python main.py
```

## Try the Example
After completing the main TODOs, run this command from this exam folder. Compare actual and expected values; this is a short demo, not a full test suite.

```bash
python -c "from main import run_demo; run_demo()"
```

Count `help` as a separate word using `line.lower().split()`, once per matching line. The supplied text has no punctuation.
