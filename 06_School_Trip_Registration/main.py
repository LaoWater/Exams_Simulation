class Participant:
    def __init__(self, name: str, age: int, ticket_price: int):
        self.name = name
        self.age = age
        self.ticket_price = ticket_price


class Trip:
    def __init__(self, destination: str, capacity: int):
        self.destination = destination
        self.capacity = capacity
        self.participants = []  # Lista în care salvăm participanții acceptați

    def available_seats(self) -> int:
        # TODO 1: Returnează capacitatea minus numărul participanților înscriși
        return self.capacity - len(self.participants)

    def register(self, participant: Participant) -> bool:
        # TODO 2: Dacă există un loc liber, adaugă participantul și returnează True. Altfel False.
        if self.available_seats() > 0:
            self.participants.append(participant)
            return True
        return False

    def total_income(self) -> int:
        # TODO 3: Folosește o buclă pentru a aduna ticket_price pentru participanții acceptați
        suma_totala = 0
        for persoana in self.participants:
            suma_totala += persoana.ticket_price
        return suma_totala


# TODO 4: Moștenire din clasa părinte Trip
class GuidedTrip(Trip):
    def __init__(self, destination: str, capacity: int, min_age: int):
        # Apelez constructorul clasei părinte Trip pentru a salva destination și capacity
        super().__init__(destination, capacity)
        # Salvez min_age ca atribut specific acestei clase
        self.min_age = min_age

    def register(self, participant: Participant) -> bool:
        # TODO 5: Respinge participanții cu vârsta sub min_age.
        # Pentru ceilalți, folosește metoda părinte de înscriere.
        if participant.age < self.min_age:
            return False
        return super().register(participant)


def count_students(participants: list) -> int:
    # TODO 6: Folosește o buclă pentru a număra participanții cu vârsta sub 18 ani
    numar_elevi = 0
    for persoana in participants:
        if persoana.age < 18:
            numar_elevi += 1
    return numar_elevi


# --- SARCINĂ OPȚIONALĂ (BONUS) ---
def count_by_ticket_price(participants: list) -> dict:
    # Returnează un dicționar cu numărul participanților pentru fiecare preț de bilet
    dictionar_preturi = {}
    for persoana in participants:
        pret = persoana.ticket_price
        if pret in dictionar_preturi:
            dictionar_preturi[pret] += 1
        else:
            dictionar_preturi[pret] = 1
    return dictionar_preturi


# Funcție demonstrativă pentru a verifica dacă totul rulează ca în cerință
def run_demo():
    ana = Participant("Ana", 12, 30)
    elena = Participant("Elena", 18, 50)
    luca = Participant("Luca", 10, 20)
    radu = Participant("Radu", 16, 30)
    trip = GuidedTrip("Mountain Observatory", capacity=2, min_age=12)

    print(trip.register(luca))       # Ar trebui să afișeze: False
    print(trip.available_seats())    # Ar trebui să afișeze: 2
    print(trip.register(ana))        # Ar trebui să afișeze: True
    print(trip.register(elena))      # Ar trebui să afișeze: True
    print(trip.register(radu))       # Ar trebui să afișeze: False
    print(trip.available_seats())    # Ar trebui să afișeze: 0
    print(trip.total_income())       # Ar trebui să afișeze: 80
    print(count_students(trip.participants))  # Ar trebui să afișeze: 1

    # Verificare bonus
    print("\n--- Test Bonus ---")
    print(count_by_ticket_price([ana, elena, radu]))  # Ar trebui să afișeze: {30: 2, 50: 1}


if __name__ == "__main__":
    run_demo()
