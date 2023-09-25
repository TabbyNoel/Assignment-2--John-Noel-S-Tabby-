def main_menu():
    """
    Displays the main menu and handles user input.
    """
    participants = []

    while True:
        print("1. Add Raffle Participant")
        print("2. Draw Winner")
        print("3. Quit Program")
        choice = input("Please select an option: ")

        if choice == "1":
            add_participant(participants)
        elif choice == "2":
            draw_winner(participants)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def add_participant(participants):
    """
    Adds a new participant to the list.
    """
    first_name = input("Enter participant's first name: ").strip()
    while not first_name:
        print("First name can't be empty.")
        first_name = input("Enter participant's first name: ").strip()

    last_name = input("Enter participant's last name: ").strip()
    while not last_name:
        print("Last name can't be empty.")
        last_name = input("Enter participant's last name: ").strip()

    address = input("Enter participant's address: ").strip()
    while not address:
        print("Address can't be empty.")
        address = input("Enter participant's address: ").strip()

    while True:
        try:
            entry_id = int(input("Enter participant's unique entry ID number: ").strip())
            if any(participant[3] == entry_id for participant in participants):
                print("This ID is already taken. Please choose another.")
                continue
            break
        except ValueError:
            print("Entry ID must be a whole number.")

    while True:
        try:
            age = int(input("Enter participant's age: ").strip())
            break
        except ValueError:
            print("Age must be a whole number.")

    participants.append([first_name, last_name, address, entry_id, age])

def draw_winner(participants):
    """
    Determines the raffle winner.
    """
    # Apply raffle formula and store raffle draw number
    for participant in participants:
        raffle_draw_number = participant[3] + participant[4]
        participant.insert(0, raffle_draw_number)

    # Find the participant with the highest raffle draw number
    winner = max(participants, key=lambda x: x[0])

    print(f"The winner is {winner[1]} {winner[2]} with Entry ID {winner[3]}.")

if __name__ == "__main__":
    main_menu()
