def start_game():
    print("Welcome to the Enchanted Forest Adventure!")
    print("You find yourself at the edge of a dark, enchanted forest.")
    print("Legends say that a treasure is hidden deep within, but many dangers lurk as well.")
    print("The air is thick with mystery, and you can hear distant howls and rustling leaves.")
    print("Do you dare to enter the forest?")
    choice = input("Type 'yes' to enter or 'no' to stay: ").lower()
    if choice == 'yes':
        enter_forest()
    elif choice == 'no':
        stay_outside()
    else:
        invalid_choice(start_game)

def invalid_choice(callback):
    print("Invalid choice, please try again.")
    callback()

def enter_forest():
    print("\nYou step into the forest, the trees closing in around you.")
    print("The forest is alive with the sounds of chirping birds and scurrying animals.")
    print("After walking for a while, you come to a fork in the path.")
    print("Do you go left, where the path is overgrown and shadowy, or right, where it seems more open and inviting?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        invalid_choice(enter_forest)

def stay_outside():
    print("\nYou decide it's safer to stay outside the forest.")
    print("You set up a camp and enjoy a peaceful night under the stars, the warmth of your campfire keeping the darkness at bay.")
    print("In the morning, you feel refreshed and ready for a new adventure.")
    end_game("stay")

def left_path():
    print("\nYou take the left path, pushing through thick underbrush and dodging low-hanging branches.")
    print("The forest grows darker and more mysterious. Suddenly, a wise old owl swoops down and lands on a branch above you.")
    print("The owl offers you a choice: a golden key that promises great fortune or a silver key that holds ancient secrets.")
    choice = input("Type 'golden' or 'silver': ").lower()
    if choice == 'golden':
        golden_key()
    elif choice == 'silver':
        silver_key()
    else:
        invalid_choice(left_path)

def right_path():
    print("\nYou take the right path, walking along a sun-dappled trail with flowers blooming on either side.")
    print("Soon, you find yourself at a river, its waters sparkling in the sunlight.")
    print("There is a boat tied to the shore, and a bridge further down the path.")
    print("Do you take the boat across the river or cross the bridge to continue on the path?")
    choice = input("Type 'boat' or 'bridge': ").lower()
    if choice == 'boat':
        boat()
    elif choice == 'bridge':
        bridge()
    else:
        invalid_choice(right_path)

def golden_key():
    print("\nYou take the golden key from the owl.")
    print("It glows with a warm light, and you feel a sense of courage and determination fill your heart.")
    print("You continue down the path and find a massive, ornate treasure chest, covered in intricate carvings.")
    print("Do you use the golden key to open it?")
    choice = input("Type 'yes' to open or 'no' to leave it: ").lower()
    if choice == 'yes':
        open_treasure()
    elif choice == 'no':
        leave_treasure()
    else:
        invalid_choice(golden_key)

def silver_key():
    print("\nYou take the silver key from the owl.")
    print("It feels cold in your hand, and a shiver runs down your spine as if you can feel the weight of ancient mysteries.")
    print("You continue down the path and come across a twisted, old tree with a small, locked door at its base.")
    print("Do you use the silver key to open the door?")
    choice = input("Type 'yes' to open or 'no' to leave it: ").lower()
    if choice == 'yes':
        open_door()
    elif choice == 'no':
        leave_door()
    else:
        invalid_choice(silver_key)

def boat():
    print("\nYou untie the boat and carefully row across the river, the sound of water lapping against the sides filling your ears.")
    print("On the other side, you find a cave entrance hidden behind a waterfall, the mist creating rainbows in the sunlight.")
    print("Do you enter the cave to explore or head back to the riverbank?")
    choice = input("Type 'enter' to go into the cave or 'back' to return to the river: ").lower()
    if choice == 'enter':
        enter_cave()
    elif choice == 'back':
        back_to_river()
    else:
        invalid_choice(boat)

def bridge():
    print("\nYou cross the bridge, the wood creaking under your weight as you look down at the rushing water below.")
    print("On the other side, you encounter a friendly deer with soft, brown eyes.")
    print("The deer nudges you gently and leads you to a hidden grove filled with beautiful, glowing flowers.")
    print("You feel at peace here, the tranquility washing over you. Do you rest here or continue your journey?")
    choice = input("Type 'rest' to stay or 'continue' to keep going: ").lower()
    if choice == 'rest':
        rest_in_grove()
    elif choice == 'continue':
        continue_journey()
    else:
        invalid_choice(bridge)

def rest_in_grove():
    print("\nYou decide to rest in the hidden grove, lying down on the soft grass and breathing in the sweet fragrance of the flowers.")
    print("As you drift off to sleep, you feel a sense of calm and contentment, dreaming of adventures yet to come.")
    end_game("grove")

def continue_journey():
    print("\nYou thank the deer and continue on your journey, feeling refreshed and hopeful.")
    print("As you walk, the path winds deeper into the forest, promising more adventures ahead.")
    enter_forest()

def open_treasure():
    print("\nYou use the golden key to open the treasure chest.")
    print("Inside, you find a trove of gold and jewels, enough to make you rich for life. However, there is also a mysterious map.")
    print("Do you take the treasure and leave or follow the map to uncover even greater secrets?")
    choice = input("Type 'take' to take the treasure or 'follow' to follow the map: ").lower()
    if choice == 'take':
        take_treasure()
    elif choice == 'follow':
        follow_map()
    else:
        invalid_choice(open_treasure)

def leave_treasure():
    print("\nYou decide to leave the treasure chest untouched, feeling a sense of accomplishment for resisting greed.")
    print("As you walk away, you feel lighter and more confident, ready to face whatever comes next.")
    end_game("no_treasure")

def open_door():
    print("\nYou use the silver key to open the door in the tree.")
    print("Inside, you find a magical portal that swirls with vibrant colors and promises new adventures.")
    print("Do you step through the portal or leave it be?")
    choice = input("Type 'step' to enter the portal or 'leave' to close the door: ").lower()
    if choice == 'step':
        step_through_portal()
    elif choice == 'leave':
        leave_portal()
    else:
        invalid_choice(open_door)

def leave_door():
    print("\nYou decide to leave the door unopened, feeling the weight of potential dangers behind it.")
    print("As you walk away, you hear strange noises behind you but choose not to look back, continuing your adventure with caution.")
    end_game("no_portal")

def enter_cave():
    print("\nYou enter the cave, your footsteps echoing on the stone floor.")
    print("The cave is filled with glittering crystals that cast a magical light.")
    print("At the far end, you see a dragon with scales that shimmer in the dim light, guarding a pile of treasure.")
    print("Do you approach the dragon bravely or quietly leave the cave?")
    choice = input("Type 'approach' to go to the dragon or 'leave' to exit the cave: ").lower()
    if choice == 'approach':
        approach_dragon()
    elif choice == 'leave':
        leave_cave()
    else:
        invalid_choice(enter_cave)

def back_to_river():
    print("\nYou decide to head back to the river.")
    print("As you reach the shore, you see a group of friendly forest creatures gathered around a bonfire.")
    print("They invite you to join their feast and share stories of the forest.")
    end_game("feast")

def approach_dragon():
    print("\nYou bravely approach the dragon, your heart pounding in your chest.")
    print("The dragon eyes you carefully, then speaks in a deep, rumbling voice: 'You are the first to approach me without fear.'")
    print("Impressed by your courage, the dragon offers you a choice: a share of its treasure or a powerful, magical artifact.")
    choice = input("Type 'treasure' to take the treasure or 'artifact' to choose the artifact: ").lower()
    if choice == 'treasure':
        take_dragon_treasure()
    elif choice == 'artifact':
        take_artifact()
    else:
        invalid_choice(approach_dragon)

def leave_cave():
    print("\nYou quietly leave the cave, not wanting to disturb the dragon.")
    print("As you step outside, you feel a sense of relief and continue your journey, wiser for the experience.")
    end_game("safe_exit")

def take_treasure():
    print("\nYou take the treasure from the chest, feeling the weight of gold and jewels in your hands.")
    print("You leave the forest, now rich beyond your wildest dreams, but always wondering what secrets the map held.")
    end_game("treasure")

def follow_map():
    print("\nYou decide to follow the map, intrigued by the promise of even greater adventures.")
    print("The map leads you through hidden paths and ancient ruins, revealing secrets long forgotten.")
    print("Your journey continues as you uncover the true magic of the enchanted forest.")
    end_game("map")

def step_through_portal():
    print("\nYou step through the portal, feeling a rush of energy as the world around you changes.")
    print("You find yourself in a beautiful meadow, filled with vibrant flowers and singing birds.")
    print("In this secret haven, you feel at peace, away from the dangers of the forest.")
    end_game("portal")

def leave_portal():
    print("\nYou decide to leave the portal untouched, closing the door behind you.")
    print("You walk away with a sense of curiosity about what lies beyond, but content to continue your adventure in the forest.")
    end_game("no_portal")

def take_dragon_treasure():
    print("\nYou accept a share of the dragon's treasure, the gold and jewels sparkling in the dim light.")
    print("The dragon smiles, a rare and fearsome sight, and tells you that you have earned its respect.")
    end_game("dragon_treasure")

def take_artifact():
    print("\nThe dragon gives you a magical artifact, a beautifully crafted amulet that pulses with power.")
    print("You feel its magic coursing through you, granting you abilities beyond your imagination.")
    end_game("artifact")

def end_game(outcome):
    if outcome == "stay":
        print("\nYou decided to stay out of the forest. Perhaps another adventure awaits you.")
    elif outcome == "grove":
        print("\nYou rest in the hidden grove, enjoying the peace and beauty of the place.")
    elif outcome == "treasure":
        print("\nYou have found the treasure and completed your adventure successfully.")
    elif outcome == "no_treasure":
        print("\nYou chose to leave the treasure. Your adventure continues with newfound wisdom.")
    elif outcome == "portal":
        print("\nYou discovered a magical portal to a secret haven. A perfect ending to your adventure.")
    elif outcome == "no_portal":
        print("\nYou chose to leave the door unopened. Your adventure continues with caution.")
    elif outcome == "feast":
        print("\nYou join the forest creatures in their feast and make new friends.")
    elif outcome == "dragon_treasure":
        print("\nYou befriended the dragon and gained treasure. A heroic end to your adventure!")
    elif outcome == "artifact":
        print("\nYou received a powerful magical artifact from the dragon. Your journey has just begun!")
    elif outcome == "safe_exit":
        print("\nYou safely exited the cave, continuing your journey with a sense of relief.")
    elif outcome == "map":
        print("\nYou followed the map, uncovering the deeper secrets of the enchanted forest. The adventure continues!")
    print("\nThank you for playing the Enchanted Forest Adventure!")

if __name__ == "__main__":
    start_game()
