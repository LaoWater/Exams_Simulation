# Exam 6: School Trip Registration

## Story
The school is planning an outing. Teachers need to register participants, avoid overbooking, and calculate the money collected from tickets. A guided trip also has a minimum age rule.

Complete the six numbered TODOs in `main.py`. The structure, sample participants, and demo are provided. No input(), external files, packages, or menu are needed.

## Exam Style
- Time target: 90–120 minutes.
- Focus: attributes, inheritance, `super()`, list appending, conditions, and simple loops.
- Work only in `main.py`. The bonus is independent of the main tasks.
- Assume valid Participant objects, nonnegative integer capacities and ages, and nonnegative ticket prices. Each participant is registered at most once per trip; duplicate detection is not required.
- For this exercise, a **student** is a participant aged **under 18**. Ticket prices are already provided: no discounts or taxes need to be calculated.

## Main Tasks
1. **`Trip.available_seats()`** — return capacity minus the number of registered participants.
2. **`Trip.register(participant)`** — if a seat is available, append the participant and return `True`. Otherwise return `False` without changing the list.
3. **`Trip.total_income()`** — use a loop to sum `ticket_price` for accepted participants. An empty trip returns `0`.
4. **`GuidedTrip.__init__(destination, capacity, min_age)`** — call the parent constructor, then store `min_age`.
5. **`GuidedTrip.register(participant)`** — reject anyone younger than `min_age`; otherwise use and return the parent registration method's result. Age equal to the minimum is allowed. A regular Trip has no age restriction.
6. **`count_students(participants)`** — return how many participants are under `18`, using a loop. An empty list returns `0`.

## Example
After completing the TODOs:

```python
ana = Participant("Ana", 12, 30)
elena = Participant("Elena", 18, 50)
luca = Participant("Luca", 10, 20)
radu = Participant("Radu", 16, 30)
trip = GuidedTrip("Mountain Observatory", capacity=2, min_age=12)

print(trip.register(luca))       # False: too young
print(trip.available_seats())    # 2: rejection uses no seat
print(trip.register(ana))        # True: exactly the minimum age
print(trip.register(elena))      # True
print(trip.register(radu))       # False: full
print(trip.available_seats())    # 0
print(trip.total_income())       # 80
print(count_students(trip.participants))  # 1
```

Only Ana and Elena are registered. Their tickets contribute `30 + 50 = 80`. Elena is exactly 18, so she is not counted as a student under the exercise rule.

## Run and Try the Example
Open a terminal **inside this exam's folder** and run `python main.py` for the introduction.
After completing the main TODOs, run the small demo:

```bash
python -c "from main import run_demo; run_demo()"
```

Compare the printed values with the expected values alongside them. The demo is a short usage example, not a complete test suite. It may fail or show unfinished results until you complete the TODOs. The optional task is separate.

## Optional Task
Complete `count_by_ticket_price(participants)`. Return a dictionary counting participants at each ticket price, using numbers as keys. For `[ana, elena, radu]`, return `{30: 2, 50: 1}`. For an empty list, return `{}`. Test this separately after finishing the main tasks.

## Suggested Session Flow
Use this as the independent exam simulation after the library recap. Complete TODOs 1–3, then 4–6, and reserve the last 10–15 minutes for the demo. Attempt the bonus only after the main tasks work.
