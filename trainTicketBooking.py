import random

class TrainTicket:
    def __init__(self, passenger_name):
        """Initialize a ticket with random train number, ticket number, start and end time"""
        self.passenger_name = passenger_name
        self.train_number = random.randint(1000, 9999)      # Random 4-digit train number
        self.ticket_number = random.randint(100000, 999999) # Random 6-digit ticket number
        self.start_time = random.randint(1, 23)            # Start hour (1–23)
        self.duration = random.randint(1, 8)               # Travel duration in hours
        self.end_time = self.start_time + self.duration    # End hour

    def display_ticket(self):
        """Display ticket information"""
        print("----- TRAIN TICKET -----")
        print(f"Passenger Name : {self.passenger_name}")
        print(f"Train Number   : {self.train_number}")
        print(f"Ticket Number  : {self.ticket_number}")
        print(f"Start Time     : {self.start_time}:00 hrs")
        print(f"End Time       : {self.end_time}:00 hrs")
        print(f"Duration       : {self.duration} hours")
        print("------------------------\n")


def main():
    tickets = []  # List to store booked tickets

    print("Welcome to the Train Booking System!")
    
    while True:
        name = input("Enter passenger name (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            break

        ticket = TrainTicket(name)
        tickets.append(ticket)
        print("Ticket booked successfully!\n")
        ticket.display_ticket()

    # Optionally show all tickets booked during this session
    if tickets:
        print("All tickets booked in this session:")
        for t in tickets:
            t.display_ticket()
    else:
        print("No tickets were booked.")


if __name__ == "__main__":
    main()
