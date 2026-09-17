class Participant:
    def __init__(self, name, age, ticket_price):
        self.name = name
        self.age = age
        self.ticket_price = ticket_price


class Trip:
    def __init__(self, destination, capacity):
        self.destination = destination
        self.capacity = capacity
        self.participants = []

    def available_seats(self):
        # TODO 1: Return capacity minus the number of registered participants.
        return self.capacity - len(self.participants)

    def register(self, participant):
        # TODO 2: If no seats remain, return False without changing the list.
        # Otherwise append participant to self.participants and return True.
        # Hint: use self.available_seats().
        print(f"{self.participants}, {self.available_seats()}")

        if self.available_seats() > 0:
            self.participants.append(participant)
            return True
        return False

    def total_income(self):
        # TODO 3: Loop through self.participants and sum their ticket_price.
        # Return 0 for an empty trip. There are no taxes or discounts.
        total = 0
        for participant in self.participants:
            total += participant.ticket_price
        return total


class GuidedTrip(Trip):
    def __init__(self, destination, capacity, min_age):
        # TODO 4: Use super().__init__() with destination and capacity.
        # Then store min_age in self.min_age.
        super().__init__(destination, capacity)
        self.min_age = min_age

    def register(self, participant):
        # TODO 5: If participant.age is below self.min_age, return False.
        # Otherwise return the result of super().register(participant).
        # A participant whose age equals min_age IS allowed.
        print(f"Participant {participant.name}, {participant.age}")
        if participant.age < self.min_age:
            return False
        return super().register(participant)


def count_students(participants):
    # TODO 6: Loop through participants and count those with age < 18.
    # For this exercise, "student" means anyone under 18. Empty list -> 0.
    count = 0
    for participant in participants:
        if participant.age < 18:
            count += 1
    return count                


def count_by_ticket_price(participants):
    # OPTIONAL: Count participants for each ticket price in a dictionary.
    # Example: {30: 2, 50: 1}. Use numbers as keys. Empty list -> {}.
    count = {}
    for participant in participants:
        price = participant.ticket_price
        count[price] = count.get(price, 0) + 1
    return count


# Small example to run after completing the main TODOs.
def run_demo():
    trip = GuidedTrip("Mountain Observatory", capacity=1, min_age=12)
    print("Register age 10:", trip.register(Participant("Luca", 10, 20)), "| Expected: False")
    print("Register age 12:", trip.register(Participant("Ana", 12, 30)), "| Expected: True")
    print("Register when full:", trip.register(Participant("Radu", 16, 30)), "| Expected: False")
    print("Income:", trip.total_income(), "| Expected: 30")


def main():
    print("=== School Trip Registration ===")
    print("Help teachers organize the next school outing.")
    print("Complete TODOs 1-6 in this file:")
    print("1. Count free seats.  2. Register a participant.  3. Sum ticket prices.")
    print("4. Initialize a guided trip.  5. Check minimum age.  6. Count students.")
    print("Optional: count participants by ticket price.")
    print('\nAfter completing the TODOs, run: python -c "from main import run_demo; run_demo()"')


if __name__ == "__main__":
    main()
