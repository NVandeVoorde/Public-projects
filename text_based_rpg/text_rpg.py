
# text based rpg

from datetime import datetime
from math import floor
import time
import winsound
import sys
import os

#to do: 

#   check that it doesnt break = check every corner
#   counter hallway
#   executable with sound 


absolute_path = os.path.dirname(__file__)

def interval(start, end): 
    interval = end - start
    interval_sec = round(interval.total_seconds())
    interval_min = floor(interval_sec / 60)
    interval_hours = floor(interval_min / 60)
    
    return interval_sec, interval_min, interval_hours

def input_clean(): 
    global counter_turns
    counter_turns += 1
    print_clean("\nYou consider your options and choose: \n") 
    x = input()
    print("\n--------------------------------------------")
    return x

def print_clean(sentence): 
    winsound.PlaySound(absolute_path + "./sounds/typewriter.wav",  winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC)
    for word in sentence: 
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound(absolute_path + "./sounds/start.wav",  winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC)

# intro scene
def own_cell(): 
    instruction = ''
    print("\n{CELL}")
    print_clean("You're in the middle of your cell, picking your nose instead of your brain.\n")
    while instruction not in directions: 
        instruction = input_clean()
        if instruction == 'L': 
            own_cell_bed()
        elif instruction == 'R': 
            own_cell_shelf()
        elif instruction == 'F': 
            own_cell_door()
        elif instruction == 'B': 
            own_cell_wall()
        elif instruction == 'H': 
            hallway() #remove after
        else: 
            print_clean("That is not a valid option.\n")
        
def own_cell_wall(): 
    print("\n{CELL WALL}")
    instruction = ''
    print_clean((
        "You're looking at the backside of you're wall.\n"
        "Apart from your own name, " + user_name + ", and the number of days you've been here there is not much to see.\n"
        ))
    while instruction not in directions: 
        print_clean("You seem to have limited options.\n")
        instruction = input_clean() 
        if instruction == 'B': 
            own_cell()
        else: 
            print_clean("Nothing to see here\n")
            own_cell_wall()

def own_cell_bed(x = 0): 
    print("\n{CELL BED}")
    instruction = ''
    global counter_cellbed
    inner_counter = x
    if counter_cellbed == 0: 
        print_clean((
            "You gaze down at something that is supposed to go down for a bed.\n"
            "In reality, it is little more than a few wooden planks and a blanket that smells just like it looks.\n"
            "Maybe a quick nap would clear your mind and easen your escape? [yes/no]\n"
            ))
        inner_counter += 1
    elif counter_cellbed > 0 and inner_counter == 0:  
        print_clean("Although your bed does not seem particularly enticing, you could still take a nap if you want. [yes/no]\n"
              "Or, i mean, you can just walk away.\n")
    elif counter_cellbed > 0 and inner_counter > 0:
        print_clean('You just keep staring at the bed, and reflect on your possibilities [move: L/R/F/B or sleep: yes/no], i guess...?\n')
    while instruction not in directions or instruction not in choice_yes_no:
        counter_cellbed += 1
        instruction = input_clean()
        if instruction == 'yes': 
            print_clean("\nYou lay down.\n" 
                  "Some time later you wake up, without knowing how much minutes, hours or even days you've been asleep.\n"
                  "Sadly, you don't feel any clearer.\n")
            own_cell_bed(1)
        elif instruction == 'no': 
            own_cell_bed(1)
        elif instruction == 'B': 
            own_cell()
        elif instruction in ['L', 'R', 'F']: 
            print_clean("\nNothing to see here\n")
            own_cell_bed(1)
        else: 
            print_clean('Select a valid instruction\n')


def own_cell_door(): 
    print("\n{CELL DOOR}")
    global counter_celldoor
    if counter_hallway > 0: 
        print_clean("You squeeze past the half open door from your cell towards the hallway.\n")
        hallway()
    elif counter_celldoor == 0 and 'shelf' not in inventory: 
        print_clean("When you put you're ear on the cell door you can hear somebody snore.\n") 
        winsound.PlaySound(absolute_path + "./sounds/snore.wav",  winsound.SND_FILENAME|winsound.SND_ASYNC)
        time.sleep(5)
        winsound.PlaySound(None, winsound.SND_PURGE)
        print_clean("Doing so, you see that there is a gap between the wall and the door.\n"
            "With your bare hands, you try to open the door, unfortunately without succes.\n"
            "You take a step back into your cell to come up with something more clever.\n"
            )
        own_cell()
        counter_celldoor += 1
    elif counter_celldoor > 0 and 'shelf' not in inventory: 
        print_clean("You try to pull the door again, but the only thing you break are your nails.\n"
              "You sigh while you mockingly take a step back")
        own_cell()
        counter_celldoor += 1
    elif counter_celldoor == 0 and 'shelf' in inventory: 
        winsound.PlaySound(absolute_path + "./sounds/snore.wav",  winsound.SND_FILENAME|winsound.SND_ASYNC)
        print_clean("\nWhen you put you're ear on the cell door you can hear somebody snore.\n") 
        winsound.PlaySound(absolute_path + "./sounds/snore.wav",  winsound.SND_FILENAME|winsound.SND_ASYNC)
        time.sleep(5)
        winsound.PlaySound(None, winsound.SND_PURGE)
        print_clean("Doing so, you see that there is a gap between the wall and the door.\n"
            "With your bare hands, you try to open the door, unfortunately without succes.\n\n"
            "You remember the shelf you broke and have the brilliant idea to use it as a lever.\n"
            "With all you're force, you pry the door open.\n"
            "Big brain moment!\n"
            )
        enter_hallway()
        counter_celldoor += 1
    else:
        print_clean("While you stand in front of your cell door, you remember the broken shelf that you could use as a lever.\n"
                "With all you're force, you pry the door open.\n"
                "Big brain moment!\n")
        counter_celldoor += 1
        enter_hallway()

def own_cell_shelf(): 
    print("\n{CELL RIGHT WALL}")
    instruction = ''
    if not all(x in shelf_options for x in ['1', '2', '3']):
        print_clean(
            "Connected to the wall of your cell is a small wooden shelf.\n"
            "From your perspective, it is just another torture mechanism, seeing that nothing is on it.\n"
            "Your mind is filled with hatefull thoughts, what do you do? [1 / 2 / 3].\n\n"
            )
    else: 
        print_clean("The wall looks even sader without a shelf.\n")
    if '1' not in shelf_options: 
        print_clean("\t1. You smash the shelf out of rage!\n")
    if '2' not in shelf_options: 
        print_clean("\t2. Stay cool calm and collective, brain power will get you out.\n")
    if '3' not in shelf_options: 
        print_clean("\t3. Maybe you can finally use the shelf and put the bed sheets on top. A clean cell is a clean mind. \n") 

    while instruction not in directions: 
        instruction = input_clean()
        if instruction == '1': 
            print_clean("\nA close up meet and greet with your fist is poorly handled by the shelf.\n"
                  "It breaks down and falls on the ground.\n"
                  "You take a step back to cool your nerves.\n")
            inventory.append('shelf')
            shelf_options.append('1')
            own_cell()
        if instruction == '2': 
            print_clean("\nYou remember a quote from a chinese fellow.\n"
                  "'The noble-minded are calm and steady.'\n"
                  "Confused you oblige and take a step back.\n")
            shelf_options.append('2')
            own_cell()
        if instruction == '3': 
            print_clean("\nWhile putting the sheets on the shelf, you make a huge tear in the sheets.\n"
                  "You yell 'SHHEEET', and throw the damned sheets back onto the bed.\n"
                  "You need to get out, because the nights will become even colder.\n")
            shelf_options.append('3')
            own_cell_bed() 
        elif instruction == 'B': 
            own_cell()
        elif instruction in directions: 
            print_clean("Nothing else to see here\n")
            own_cell_shelf() 
        else: 
            print_clean('Select a valid instruction.\n')

def enter_hallway(): 
    global counter_hallway
    counter_hallway += 1
    winsound.PlaySound(absolute_path + "./sounds/doorcrack.wav",  winsound.SND_FILENAME)
    print_clean("\nWith a big crack, the wooden shelf breaks.\n"
          "Luckely, it created an opening large enough for you to grab the door itself and rip it out.\n"
          "While you stand there, thinking you are some kind of superman, you see the origin of the snoring.\n"
          "You stand in a small hallway with an iron gate at the end. Behind it sits a seemingly lazy guard.\n"
          "Mildly annoyed, he says 'congratulations, you managed to change one cell for another'\n"
          "'Make yourself at home kiddo and feel free to look in the other empty cells, because you ain't getting through this gate'\n"
          "With a big smug face, the guards closes his eyes and sinks deeper into his chair, ready for another pleasant dream.\n"
          "You take one step forward and rattle the gate. Dang...this seems too strong to open with brute force. You will have to find another way. \n")
    hallway()           

def hallway():
    print("\n{HALLWAY}") 
    instruction = ''
    print_clean("You stand in the empty small hallway, your previous cell behind you and your next obstacle before you.\n"
          "Left and right seem to be open cells from previous inhabitants.\n")
    while instruction not in directions: 
        instruction = input_clean()  
        if instruction == 'B': 
            own_cell()
        elif instruction == 'F': 
            iron_gate()
        elif instruction == 'R': 
            empty_cell()
        elif instruction == 'L': 
            haunted_cell()

def iron_gate(): 
    print("\n{IRON GATE}") 
    print_clean("Iron gate")
    succes()

def haunted_cell(): 
    print("\n{LEFT CELL}") 
    instruction = ''
    global counter_haunted
    winsound.PlaySound(absolute_path + "./sounds/skeleton.wav",  winsound.SND_FILENAME)
    if counter_haunted == 0: 
        print_clean("You grasp your heart, that scared the bejeezus out of you.\n"
            "In front of you stands a haunting ghost, skeleton thingie.\n"
            "I mean, how do you call something like this when you haven't seen anything like this in your life.\n"
            "'Howdy', the ghost says very calmly, 'My name is Rudy, sorry to startle you.'\n"
            "'I am just simply looking here for a way to enter heaven. I know I had something useful in my old cell, but i can't seem to find it.'\n"
            "'Care to help me?'\n\n"
            )
        print_clean("\t1. This little skeleton might seem like a smooth talker, but you ain't taking any of it.\n"
              "\t   You decide to take him out in bare knuckle fight.\n")
        print_clean("\t2. Run! That's a fucking ghost, you don't mess with ghosts!\n")
        if 'book' not in inventory: 
            print_clean("\t3. Sure, whatever, I'll take any help I can get.\n") 
        else: 
            print_clean("\t3. I think I already know just how!\n")

    elif counter_haunted > 0:
        print_clean("OOOW... That sound gets me everytime, stop that Rudy!\n"
              "You gather your thoughts and consider your options: \n\n")
        print_clean("\t1. You still don't like his smug skull, CHAAARGGEE!\n")
        print_clean("\t2. I need to get the fuck out of here, but without showing fear, OBVIOUSLY.\n")
        if 'book' not in inventory: 
            print_clean("\t3. Helping this guy, sure sure, but how?\n") 
        else: 
            print_clean("\t3. I think I already know just how!\n")
   
    while instruction not in ['1', '2', '3']: 
        instruction = input_clean()
        if instruction == '1': 
            die()
        elif instruction == '2':
            print_clean("Without saying a word, you run back to the hallway.\n") 
            counter_haunted += 1
            hallway()
        elif instruction == '3' and counter_haunted == 0 and 'book' not in inventory: 
            print_clean("Rudy-boy, old chap, you must an old prisoner here!\n"
                  "Let's make a deal, I get you your way into heaven and u get me a way out of here!\n"
                  "Rudy laughs and responds 'That seems like a very fair arrangement, deal!' \n"
                  "You shake hands with a rather boney hand and leave to find the answer.\n")
            counter_haunted += 1
            hallway()
        elif instruction == '3' and counter_haunted > 0 and 'book' not in inventory:  
            print_clean("If the answer is not in the Rudy's cell, where else could it be?\n")
            counter_haunted += 1
            hallway()
        elif instruction == '3' and 'book' in inventory: 
            help_rudy()

def help_rudy(): 
    print_clean("\nWith some proud, you hold the uncovered book in the air yelling: 'Is this your stairway to heaven?'\n"
                "Clearly annoyed, Rudy opens the book and extracts a little golden spoon.\n"
                "'THIS is my stairway to heaven', he winks. 'Those simpletons would not let me freaking enter without a spoon. Yikes.'\n\n")
    print_clean("Although you feel relieved that Rudy can enjoy perpetual freedom in heaven, you remind him of the deal.\n"
                "He smiles, walks closer, shakes your hand again, and then dissappears in thin air.\n"
                "Your first instinct is to scream, but than you realize that Rudy's hand is still in yours!\n"
                "In spite of your disgust, you understand that those barebone fingers and knuckles represent a lock-picking tool and return to the hallway.\n")
    inventory.append('hand')
    hallway()

def empty_cell():
    print("\n{RIGHT CELL}") 
    instruction = ''
    print_clean("You stand in the middle of an almost identical cell as yours.\n")
    while instruction not in directions: 
        instruction = input_clean()
        if instruction == 'F': 
            empty_cell_wall()
        elif instruction == 'B': 
            hallway()
        elif instruction == 'R': 
            empty_cell_bed()
        elif instruction == 'L': 
            empty_cell_shelf()
        else: 
            print_clean("\nEnter valid option:\n")

def empty_cell_wall():
    print("\n{CELL BACK WALL}")  
    instruction = ''
    print_clean("The back walls looks as eary as yours, with the name of the previous inhabitant instead of yours.\n"
          "But wait a minute, it says 'Rudy'! This was Rudy's cell!\n"
          "How can a man haunt the wrong cell in a hallway with 3 rooms... Sigh\n"
          "But apart from that discovery, there is nothing on the wall to help you.\n")
    while instruction not in directions: 
        instruction = input_clean()
        if instruction == 'B': 
            empty_cell()
        elif instruction in ['L', 'R', 'F']: 
            print_clean('\nNothing to see here.\n')
            empty_cell_wall()
        else: 
            print_clean('\nEnter a valid option.\n')

def empty_cell_bed(): 
    print("\n{CELL BED}")  
    instruction = ''
    print_clean("You look at a bed that could have been yours. No sheets though, sad.\n")
    while instruction not in directions: 
        instruction = input_clean()
        if instruction == 'B': 
            empty_cell()
        elif instruction in ['L', 'R', 'F']: 
            print_clean('\nNothing to see here.\n')
            empty_cell_bed()
        else: 
            print_clean('\nEnter a valid option.\n')

def empty_cell_shelf(): 
    print("\n{CELL LEFT WALL}")  
    instruction = ''
    print_clean("On the left wall of the cell, you would expect a shelf, as in your own cell.\n"
          "Instead, you see some poorly stacked bricks.\n"
          "What do you do? [verb]\n")
    instruction = input_clean()
    while instruction not in verbs:  
        if instruction != 'quit': 
            print_clean("You " + instruction + " the wall. Unfortunatly, to no avail. What else could work? [enter quit to leave] \n")
            instruction = input_clean()
        elif instruction == 'quit': 
            print_clean("\nYou give up, although u probably shouldn't.\n")
            empty_cell()
    
    print_clean("\n\nYou " + instruction + " the wall... and a few bricks fall to the ground.\n"
                "Just enough to reveal a small cavety. You reach out with your hand and recover and old book.\n"
                "It reads: 'A stairway to heaven'.\n"
                "This is probably what Rudy has been looking for! Which is weird, but anyhow.\n"
                ) 
    inventory.append('book')
    empty_cell()

def iron_gate(): 
    print("\n{IRON GATE}")  
    if 'hand' not in inventory: 
        #Sounds? 
        print_clean("You rattle the gate, but it doesn't give in. Not even a bit.\n")
        winsound.PlaySound(absolute_path + "./sounds/rattle_gate.wav",  winsound.SND_FILENAME)
        print_clean("The guard opens one eye at the sound, but quickly closes it again after seeing your pityful attempt to break out.\n"
                    "You might need something more sturdy, or more clever.\n")
    else: 
        print_clean("With his hand in your hand, you tiptoe towards the gate. \n"
                    "You break Rudy's index finger and push it into the lock.\n"
                    "As silently as skeletonly possible, you twist the bone left and right to unlock the gate.\n")
        winsound.PlaySound(absolute_path + "./sounds/lock.wav",  winsound.SND_FILENAME) 
        winsound.PlaySound(absolute_path + "./sounds/open_gate.wav",  winsound.SND_FILENAME)
        print_clean("\nCLICK! The gate finally opens!\n"
                    "You hold your breath, pass the sleeping guard and a few seconds later you run towards your freedom!\n")
        succes()

def die(): 
    instruction = ''
    print_clean("You charge at Rudy, but quickly come to the conclusion that it's quite impossible to hurt a skeleton.\n"
          "At first Rudy looks a bit confused at your pityful attempt to murder a dead person.\n"
          "Then he chuckles and with one punch to the nose, he fucks you up and brings you to his world.\n")
    winsound.PlaySound(absolute_path + "./sounds/dying.wav",  winsound.SND_FILENAME)
    print_clean(
          "\nYou died u idiot! Although, death might also be considered as some kind of escape. I guess...\n"
          "Want to try and make it out again, preferably alive? [yes/no] \n")
    global inventory
    global shelf_options
    global counter_celldoor
    global counter_haunted
    inventory = []
    shelf_options = []
    counter_celldoor = 0
    counter_haunted = 0

    while instruction not in choice_yes_no: 
        instruction = input_clean()
        if instruction == 'yes': 
            print_clean("\nRise again, my friend!\n")
            own_cell()
        elif instruction == 'no': 
            print_clean("\nNo problem, i figured you were a quitter anyway...\n"
                  "Thanks for playing!")
        else: 
            print_clean("Enter valid option")

def succes(): 
    print_clean("\nYou did it!\n"
                "You escaped the slightly dark dungeon!\n"
                "Thanks for playing!\n\n")
    end = datetime.now()
    total_interval = interval(start, end)
    spent_sec, spent_min, spent_hours = total_interval
    print("\n########################################\n")
    print_clean("END REPORT: \n")
    print_clean("\nYou spend "+ str(spent_min) + " minutes and " + str( spent_sec-(spent_min*60) ) + " seconds!\n")
    print_clean("You took " + str(counter_turns) + " turns to figure it out, congratulations " + user_name + "!\n")
    print("\n########################################\n")


# Start of game
inventory = []
counter_turns = 0 
directions = ['L', 'R', 'F', 'B']
choice_yes_no = ['yes', 'no']
instruction = ''
shelf_options = []
counter_celldoor = 0
counter_haunted = 0
counter_cellbed = 0
counter_hallway = 0
verbs = ['push', 'break', 'kick', 'charge', 'punch', 'headbump']

print("\n\n########################################\n")
print("SLIGHTLY DARK DUNGEON - Beginner project\n")
print("########################################\n\n")

winsound.PlaySound(absolute_path + "./sounds/start.wav",  winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC)
user_name = input("Provide me with a suitable alter-ego for the epic text-based RPG that awaits: \n")

start = datetime.now()

print_clean(
    "\n" + user_name + ", you wake up in a dirty and smelly cell.\n"
    "You can see your cell door in front of you, it does not seems be that sturdy.\n"
    "However, you might find something in your cell, your brilliant mind presumes.\n"
    "To look and move around enter the command L (left), R (right), F (forward) or B (backward) and ENTER. \n\n"
    )
    
own_cell() 
    
if __name__ == '__main__':
    main()    