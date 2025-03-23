#Joshua Monfort
rooms = {
    'Audience Hall': {'directions': {'South': 'Bedroom', 'East': 'Kitchen', 'North': 'Coop', 'West': 'Study'},
                      'item': None},
    'Bedroom': {'directions': {'North': 'Audience Hall', 'East': 'Crypt'}, 'item': 'Guardian Armor'},
    'Crypt': {'directions': {'West': 'Bedroom'}, 'item': "Apollo's Helmet"},
    'Coop': {'directions': {'South': 'Audience Hall', 'East': 'Exhibit'}, 'item': 'The Ethereal Axe'},
    'Exhibit': {'directions': {'West': 'Coop'}, 'item': 'The Aegis Shield'},
    'Kitchen': {'directions': {'West': 'Audience Hall', 'North': 'Main Chamber'}, 'item': 'Gapple'},
    'Main Chamber': {'directions': {'South': 'Kitchen'}, 'item': 'Shalltear Blood-Fallen'},
    'Study': {'directions': {'East': 'Audience Hall'}, 'item': 'The Book of Dead'}
}

def show_instructions():
    print("\nWelcome to Vampire Slayer Text Adventure Game!")
    print("Objective: Collect all 6 legendary items to defeat Shalltear Blood-Fallen.")
    print("Commands:")
    print("  - Move: go North, go South, go East, go West")
    print("  - Pick up items: get [item name]")
    print("  - Quit the game: Quit")

def show_status(inside_room, inventory):
    print(f"\nYou are in the {inside_room}.")
    item = rooms[inside_room]['item']
    if item:
        print(f"You see a {item} here.")
        print(f"To pick it up, type: get {item}")
    else:
        print("There are no items in this room.")

    print("Your current inventory:", inventory if inventory else "Empty")
    print("Available directions:", ', '.join(rooms[inside_room]['directions'].keys()))

def define_direction_and_move(direction_from_user, current_room):
    direction_from_user = direction_from_user.capitalize()  # Ensure direction is capitalized
    if direction_from_user in rooms[current_room]['directions']:
        new_room = rooms[current_room]['directions'][direction_from_user]
        print(f"Moving to {new_room}...")
        return new_room
    else:
        print("Invalid direction. You can't go that way.")
        print("Available directions:", ', '.join(rooms[current_room]['directions'].keys()))
        return current_room

def pick_up_item(user_input, current_room, inventory):
    item = rooms[current_room]['item']
    if item and user_input.lower() == f"get {item.lower()}":
        inventory.append(item)
        rooms[current_room]['item'] = None  # Remove item from the room
        print(f"You have obtained: {item}")
    elif item:
        print("You must type the correct command to pick up the item.")
    else:
        print("There is no item to pick up here.")

def encounter_shalltear(inventory):
    # If player has all items, they can face Shalltear
    if len(inventory) == 6:
        print("\nWith all 6 legendary items, you face Shalltear Blood-Fallen!")
        print("In an epic battle, you defeat her and become the Vampire Slayer! Victory!")
    else:
        print("\nYou are ambushed by Shalltear. Unprepared as you are, she sucks all your blood GAME OVER.")

def main():
    inside_room = 'Audience Hall'
    inventory = []
    all_items = ['Guardian Armor', "Apollo's Helmet", 'The Ethereal Axe', 'The Aegis Shield',
                 'Gapple', 'The Book of Dead']

    show_instructions()

    while True:
        show_status(inside_room, inventory)

        # Victory check (but don't break, keep playing)
        if len(inventory) == len(all_items):
            print("\nCongratulations! You have collected all 6 legendary items!")
            print("You are now ready to face Shalltear Blood-Fallen.")

        # Player will automatically face Shalltear when they reach Main Chamber with all items
        if inside_room == 'Main Chamber':
            encounter_shalltear(inventory)
            break  # Game ends after facing Shalltear

        user_input = input("\nWhat do you want to do? (type 'Quit' to exit): ").strip().lower()

        if user_input == "quit":
            print("Thank you for playing!")
            break
        elif user_input.startswith("get "):
            pick_up_item(user_input, inside_room, inventory)
        elif user_input.startswith("go "):
            direction = user_input[3:].strip()  # Get direction after "go"
            inside_room = define_direction_and_move(direction, inside_room)
        else:
            print("Invalid input. Please try again.")

# Call main function to start game
main()
