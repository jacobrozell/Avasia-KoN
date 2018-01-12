# NEWEST VERSION 4/3/17 (11:46)

# Fastest run ever recorded : 1 minutes, 59.2 seconds
# Try and beat it!

# *** Walkthrough ***:
# https://docs.google.com/document/d/1Z66YHWr4cZ_A_3xnZOEdGZGcvAwPsENSKryyxVO7kIU/edit?usp=sharing


# ------Recent Fixes------
# Gave name to druid scout with lantern (Dentros)
# Changed name of Silvarum to Silvarium
# Western Path's direction was changed to be parallel to Splitpath.
# Fixed several, several typos
# Made Neutrals reside in the city of Ofelos


from time import sleep
import random
from random import randint


# Initializing

def wait(time_multiplier=1):
    global time
    seconds = -1
    if time == "OFF":
        seconds = 0
    if time == "ON":
        seconds = 8
    if seconds == -1:
        return False
    sleep(seconds * time_multiplier)
    return True


def userinput(message):
    ans = input(message)
    if ans == "":
        return ""
    ans = ans.upper().replace("USE", "").replace("CAST", "").replace(" ", "")
    return ans


def containsAny(string, options):
    for option in options:
        if option.upper() in string.upper():
            return True

    return False


def textspeed():
    global time
    while True:
        print()
        print()
        print("\033[2;36;48mAvasia: King of Nacastrum!")
        print("\033[0;26;48m")
        print()
        print()
        print("Do you want delay between sentences? (On or off) ")
        ans = input("On is strongly recommended for first time players.")
        print()
        time = ans.upper()
        if wait(0):
            intro()
            break
        else:
            print()


def intro():
    print()
    print()
    print("You hear waves and the sound of the ocean around you.")
    print("But... Where are you?")
    print("You pull yourself to your feet.")
    print("It appears that you are alongside a beach.")
    wait()
    print()
    print("The whisper of the ocean and the scream of the fierce wind penetrate your ears.")
    print("You see the remains of a gate to your north.")
    print("As you draw closer you see what appears to be an older gentleman, who seems out of place.")
    print("This can't be the guard, you think to yourself.")
    print("The guard is dressed in common-wear and has nothing to defend himself, other than a short broken spear.")
    print()
    wait()
    print(""" "Welcome to Oceandale." """)
    print(""" "Or what's left of it..." """)
    print(""" "Last week Oceandale was attacked by the faction of Agroman." """)
    print()
    wait()
    print(""" "Once all of Avasia was united under the Kaefden family." """)
    print(""" "But the youngest son of the king thirsted for power." """)
    print(""" "He began a protest in Kaefden's capital, Aylova, which quickly became violent." """)
    print(""" "The youngest son urged his father for the crown and spited him for his lack of leadership." """)
    print(""" "Together, the older brother and the king, banished him from all of Kaefden." """)
    print(""" "The king couldn't allow for this behavior to fall upon his citizens, or certain chaos would follow." """)
    print()
    wait(2)
    print(""" "The younger brother built the Agromanian faction from the ground up." """)
    print(""" "Of course, many Kaefden people followed of all races. Mages, Humans, and Druids alike." """)
    print(""" "Although the brothers, and the king are long gone, the rivalry and the hatred still exist." """)
    print(""" "The Agroman faction today believes in brotherhood and loyalty." """)
    print(""" "The Kaefden faction believes in order and integrity." """)
    print(""" "There's a city who remains neutral in the matter; the city of Ofelos." """)
    print(""" "They believe that a united Avasia would benefit the people more than petty fighting." """)
    print(""" "After Oceandale nearly fell to the Barbarians, I'm starting to see their point. """)
    print()
    wait(2.5)
    print(""" "Go into the city. There isn't much left to see." """)
    print(
        "------------------------------------------------------------------------------------------------------------")
    print()
    print("You venture forth until you begin to see the debris of crumbling and post-burnt houses.")
    print()
    wait(.5)
    global lev
    lev = 0
    global sword
    sword = 0
    global lant
    lant = 0
    global druid
    druid = 0
    global fireball
    fireball = 0
    global slipp
    slipp = 0
    global ndoor
    ndoor = 0
    global grass
    grass = 0
    global forestlore
    forestlore = 0
    global dagger
    dagger = 0
    global armory
    armory = 0
    global blood
    blood = 0
    global geo
    geo = 0
    global guesses
    guesses = 3
    global tunnel
    tunnel = 0
    global roadfir
    roadfir = 0
    global roadgeo
    roadgeo = 0
    global roadlev
    roadlev = 0
    global rod
    rod = 0
    global deathcount
    deathcount = 0
    global lady
    lady = 0
    global escort
    escort = 0
    global orange
    orange = 0
    global lock
    lock = 0
    global cgates
    cgates = 0
    global tran
    tran = 0
    global symbols
    symbols = ["^'", "~'", ">'", ";'"]
    random.shuffle(symbols)

    oceandale()


# oceandale functions


def oceandale():
    if escort == 0:
        print("To the NORTH, a blood-stained road continues through the city.")
        print("To the EAST, there is debris barely distinguishable as a trading post.")
        print("To the WEST, you see a house that appears untouched, unmarked by the Agroman faction.")
        print("To the SOUTH, the southern gate leads to the shore-front.")
        print()
        north = ["NORTH"]
        east = ["EAST"]
        west = ["WEST"]
        south = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        ans = userinput("Which way would you like to investigate?")
        print()
        if containsAny(ans, east):
            print()
            print(
                "As you near the broken remnants of a trading post, the stench of fish and burnt wood fills the air.")
            print("A few people are attempting to make the place a bit more organized.")
            print("You could try and talk to them.")
            print()
            while True:
                ans = input("What would you like to do?")
                ans = ans.upper()
                talk = ["TALK"]
                leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
                if containsAny(ans, talk):
                    print()
                    print("You approach one of the men cleaning up the debris and announce yourself.")
                    print("He takes a moment to look at you before speaking.")
                    print()
                    print(""" "Trading post is closed, mage, if you couldn't tell already." """)
                    print(""" "The damn Agromanians burned my beloved store to the ground!" """)
                    print(""" "They showed up in the middle of the night, the cowards!" """)
                    print(""" "My wife, they took my wife!" """)
                    print(""" "I swear those bastards will get what's coming to them." """)
                    print(""" "I.. I need to be alone now." """)
                    print()
                    print("There's no other reason for you to continue loitering around here.")
                    print()
                    print("You leave the trading post.")
                    print()
                    print()
                    wait()
                    oceandale()
                    break
                if containsAny(ans, leave):
                    print()
                    print("You leave the trading post.")
                    print()
                    wait()
                    oceandale()
                    break
        if containsAny(ans, west):
            magehouse()
        if containsAny(ans, north):
            print("You venture NORTH into the outskirts of the city.")
            print()
            graveyard()
        if containsAny(ans, south):
            print("You venture SOUTH to the beach.")
            print()
            beach()
        else:
            oceandale()

    if escort == 1:
        print("To the NORTH, the road continues into the city.")
        print("To the SOUTH, the southern gate leads to the shore-front.")
        print()
        print("Your quest is finally coming to an end. Head NORTH towards Nacastrum.")
        print("On the other hand, maybe the Old Mage would like to see the beach before venturing on.")
        print()
        ans = userinput("Which way would you like to investigate?")
        print()
        north = ["NORTH"]
        south = ["SOUTH"]
        if containsAny(ans, north):
            print("You venture NORTH into the outskirts of the city.")
            print()
            graveyard()
        if containsAny(ans, south):
            print("You venture SOUTH to the beach.")
            print()
            beach()


def magehouse():
    global lev
    global escort
    global lock
    if lev == 0:
        print()
        print("You draw nearer to the house, when the door bursts open, pages")
        print("of books fly in every direction. The sudden gust of wind startles you.")
        print()
        wait()
        print("However, no one is there.")
        print("You enter the house to see stacks of books piled to the ceiling.")
        print("The heavy door behind you slams shut in an instant.")
        print("You quickly jump and look to the door to see what caused it.")
        print()
        wait()
        print("However, you can't find the cause of the paranormal occurrence.")
        print("You turn back around to be face to face with an elderly brunette woman,")
        print("whose appearance alone sparks recognition.")
        print("You decide that she was the one controlling the door.")
        print()
        wait(2)
        print("The woman spoke with intellect and fluency, despite her age.")
        print(""" "You recognize one of your own don't you?" """)
        print(""" "Mage to mage; Kaefden to Kaefden." """)
        print(""" "But... YOU are lost, terribly lost." """)
        print()
        wait()
        print(""" "All mages have been exiled from Nacastrum, not just you." """)
        print(""" "But YOU... " """)
        print(""" "You might have what it takes." """)

        while True:
            ans = input(""" "Answer me: what faction do the mages represent?" """)
            ans = ans.upper()
            k = ["KAEFDEN"]
            if containsAny(ans, k):
                break
            else:
                print("Try again.")
        print()
        print(""" "Glad you know the simplest of things about our people." """)
        print(""" "Do you know why Nacastrum banished its people?" """)
        print()
        print(""" "Vashirr, the king of the mages, used his power to teleport Nacastrum's citizens." """)
        print(""" "After the fall of Oceandale, Vashirr heard of rumors from the druids." """)
        print(""" "Nacastrum was to be attacked by the full force of the barbarians of the north." """)
        print(""" "I never trusted Vashirr. Soon after he became King, I left" """)
        wait()
        print()
        print(""" "What is the last thing you truly remember? """)
        print(""" "Many mages have thought to have been teleported out of the city." """)
        print(""" "Most have ventured east to Kaefden's capital, Aylova." """)
        wait()
        print(""" "Vashirr didn't save you." """)
        print(""" "His true intentions are certainly clouded." """)
        print(""" "He scattered his people for a reason." """)
        print(""" "All this seems to me, that he has sided with the Agromanians." """)
        print(""" "The mages lived in a floating city... What real threat did the barbarians pose?" """)
        print()
        wait(2)
        print(""" "I'm too old to venture on this quest." """)
        print(""" "But you... You can reunite our people." """)
        print(""" "Before I die, I want to see the Nacastrum I remember from my childhood." """)
        print()
        wait()
        print(""" "This is your quest! You must unlock the gates to Nacastrum and unite our people!" """)
        print()
        wait()
        print("She walks over to her enormous stack of books and yanks one in the middle.")
        print("The other books fall to the ground with a loud crash.")
        print("She satisfyingly dusts off the cover of a very large, old book.")
        print()
        print(""" "This spell will certainly prove useful in your quest!" """)
        print()
        print(""" "It's called Levitate." """)
        print()
        print("\033[1;32;48mYou obtained the spell Levitate!")
        print("\033[0;26;48m")
        wait(2)
        print(""" "Use it to simply float or hover." """)
        print()
        print(""" "Sadly, that is all I have to offer." """)
        print(""" "Many things have changed since I lived in Nacastrum." """)
        print(""" "None-the-less, this spell will guide you in your quest to reestablish our home." """)
        print()
        print("You thank the Old Mage and continue back into Oceandale, with a new sense of purpose.")
        print()
        wait()
        lev = 1
        lock = 1
        oceandale()
    if lock == 1:
        print()
        print("The door is locked.")
        print("It seems the Old Mage is no longer home.")
        print()
        oceandale()
    if lady == 1:
        print()
        print("You approach the Mage's house and open the door.")
        print("As you head inside, the room is eerily quiet.")
        print("You look around and notice the Old Mage from before sitting at a desk.")
        print("Before you can utter a word she calls out to you without turning around.")
        print()
        print(""" "I've been waiting for you." """)
        print()
        wait(1)
        print("You stop in your tracks and listen to what she has to say.")
        print()
        print(""" "So it is done then?" """)
        print()
        print("You're unsure what she is talking about.")
        print("You stay silent.")
        print()
        print(""" "I knew there was something special about you from the moment you stepped through my door." """)
        print(""" "I felt your energy before you even entered my home." """)
        print()
        wait(2)
        print("She gets up from her desk and approaches you.")
        print()
        print(""" "Ah, I can see it in your eyes." """)
        print(""" "You've seen many things in your travels." """)
        print(""" "Come, I have something to show you." """)
        print()
        print("She gestures you to follow her as she walks into a back room and down a staircase into the basement of "
              "her home.")
        wait(1.5)
        print("The room is pitch black and you can't see a thing.")
        print("The mage snaps her fingers and candles around the room light up.")
        print()
        print("In the center of the room is a silver table.")
        print()
        print(""" "Come on, don't be shy." """)
        print()
        wait(1)
        print("You walk over to the table and on it is a long staff, nearly 6 feet long.")
        print("The staff is made of silver with gold etchings wrapping around it.")
        print("At the end is a blue gemstone about the size of your hand.")
        print()
        print(""" "I bet you're wondering what this is." """)
        print(""" "You already know, you just don't realize it." """)
        print(""" "The only reason you are here is because you need this staff to get to Nacastrum." """)
        print(""" "I've kept it safe while I waited on you to return." """)
        print(""" "I know you've seen it, the Ring of Malkos." """)
        print(""" "The monument under our home." """)
        print()
        wait(2)
        print("You remember the platform with the silver circle under Nacastrum.")
        print()
        print(""" "The Rings of Malkos are teleporters, named after our first king." """)
        print(""" "The only way to Nacastrum is through that gate." """)
        print(""" "This staff acts as a key to the Rings of Malkos." """)
        print()
        print(""" "You know what we must do next." """)
        print(""" "Let us not waste any time. Our home awaits." """)
        print()
        while True:
            ans = input(""" "But before we go, are you sure you're ready?" """)
            ans = ans.upper()
            y = ["YES", "Y"]
            n = ["NO", "N"]
            if containsAny(ans, y):
                print()
                print("You and the Old Mage leave the house on the final journey to Nacastrum.")
                print()
                escort = 1
                oceandale()
                escort = 1
                break
            if containsAny(ans, n):
                print()
                print(""" "Come back when you are truly ready." """)
                print()
                oceandale()
                break
    if escort == 1:
        print()
        print(""" "We need to go to Nacastrum." """)
        print()
        oceandale()


def graveyard():
    global sword
    if escort == 0:
        print()
        print("To the NORTH is a broken arch that appears to be the gate out of the city. ")
        print("To the EAST, comes a stench, more vile than you ever could have imagined.")
        print("To the WEST, there is a fallen building that seems to have significance.")
        print("To the SOUTH, the path goes back to the main part of Oceandale.")
        print()
        ans = userinput("Which way would you like to investigate?")
        print()
        north = ["NORTH"]
        east = ["EAST"]
        west = ["WEST"]
        south = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        if containsAny(ans, west):
            print()
            print("There is what appears to be the remnants of a rustic church.")
            print("Ashes of burned holy books and wooden benches lay burned and battered.")
            print("Nothing remains except an alter, dedicated to the matron God of the Ocean.")
            print("Survivors gather wood and try to salvage whatever they can.")
            wait()
            print()
            print("You gain a new sense of hatred for the brutality of the barbarians.")
            print()
            wait()
            print("You go back to the upper part of town.")
            graveyard()
        elif containsAny(ans, east):
            print()
            print("The smell of the burnt and decaying bodies stung your nostrils and left you gasping for breath.")
            print("Piles of bodies, tell you that the population of Oceandale must have decreased dramatically. ")
            print(
                "The sun falls on the 6-feet tall endless stack of bodies, which doesn't help the protruding stench. ")
            print("However, a glimmer of light is flickering in the middle.")
            print()
            if sword == 0:
                while True:
                    ans = userinput("What do you do?")
                    verbs = ["TAKE", "GRAB", "STEAL", "GET"]
                    look = ["LOOK", "INVESTIGATE", "SEARCH"]
                    leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
                    if containsAny(ans, look):
                        print()
                        print("You discover the flicker of light comes from a soldier's sheath.")
                        print("A long sword lays half unsheathed, suspended on the decayed back of the man. ")
                        print()
                    elif containsAny(ans, verbs):
                        print()
                        print("Although death is honorable in fighting for a just cause, ")
                        print("he won't be needing that anymore. You decide to take the long sword.")
                        print()
                        print()
                        print("\033[1;32;48mYou received the Long Sword!")
                        print("\033[0;26;48m")
                        wait(.5)
                        sword = 1
                        graveyard()
                        break
                    elif containsAny(ans, leave):
                        print("You leave the graveyard and head back into town.")
                        graveyard()
                        break
                    else:
                        print("Bad input. Try using a different verb.")
                        print()
            if sword == 1:
                y = ["YES", "Y"]
                leave = ["LEAVE", "BACK", "EXIT", "NO", "N"]
                print("The bodies lay, piled and rotting.")
                print()
                ans = input("Would you like to pay your respect?")
                ans = ans.upper()
                if containsAny(ans, leave):
                    print("You leave the graveyard and head back into town.")
                    graveyard()
                elif containsAny(ans, y):
                    print()
                    print("How could one do this?")
                    print("Is the Faction War that intense to justify the slaughter of a village? ")
                    print("You pay respects for the lost citizens and then venture back into town.")
                    wait(.5)
                    graveyard()
                else:
                    print()

        elif containsAny(ans, south):
            print("You travel back to the main area of town.")
            print()
            oceandale()
        elif containsAny(ans, north):
            print("You venture to and through the rustic gates of northern Oceandale.")
            print()
            splitpath()
        else:
            graveyard()

    if escort == 1:
        print()
        print("To the NORTH is a broken arch that appears to be the gate out of the city. ")
        print("To the SOUTH, the path goes back to the main part of Oceandale.")
        print()
        print("You really should make your way to Nacastrum.")
        print()
        ans = userinput("Which way would you like to investigate?")
        print()
        north = ["NORTH"]
        south = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        if containsAny(ans, south):
            print("You travel back to the main area of town.")
            print()
            oceandale()
        elif containsAny(ans, north):
            print("You venture to and through the rustic gates of northern Oceandale.")
            print()
            splitpath()
        else:
            print()


def beach():
    global rod
    if escort == 0:
        print("You stand along the beach, gazing outward.")
        print("Distant ships sit along the horizon, fishing.")
        print("The sea breeze is very calming.")
        print()
        wait()
        while True:
            verbs = ["STRETCH", "RELAX", "EXERCISE", "YOGA"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
            fish = ["FISH", "FISHING"]
            ans = userinput("What would you like to do?")
            if containsAny(ans, fish):
                if rod == 0:
                    print()
                    print("You don't have a fishing rod.")
                    print()
                if rod == 1:
                    fishingbeach()
                    break
            elif containsAny(ans, verbs):
                print()
                print("You take a deep breath and do some yoga moves.")
                print()
                print("A couple of back bends.")
                print("A few Eagles.")
                print("Even a Crow Pose.")
                print()
                print("Both your body and mind feel revitalized.")
                print()
            elif containsAny(ans, leave):
                print()
                print("You leave and return to Oceandale.")
                print()
                oceandale()
                break
            else:
                print()
                print("This would be a great place to do some stretching.")
                print()

    if escort == 1:
        print("You take the Old Mage to the shore.")
        print("She gazes outwards and begins to talk to you.")
        print()
        print(""" "Many, many nights I come out here and ponder how it would be if I didn't leave Nacastrum." """)
        print(""" "I think I've been waiting... Well." """)
        print(""" "I've been waiting for someone like you to come along." """)
        print(""" "Who thought when I did finally go back, I would be assisting such an important cause." """)
        print(""" "We'd best get to it." """)
        print()
        wait(2)
        print("You and the Old Mage go back into Oceandale.")
        print()
        oceandale()


def fishingbeach():
    global orange
    global deathcount
    print()
    print("You cast a line into the ocean.")
    print()
    cast = (randint(2, 12))
    while True:
        if cast == 2:
            print()
            print("Moments after casting a line, you feel a pull on the fishing rod!")
            print()
            print("You pull back the line and discover a huge fish made of pure gold hanging on the hook!")
            print("It must be worth a fortune!")
            print()
            orange = 0
            break
        if cast == 3:
            print()
            print("Minutes pass and you finally feel a tug on the line!")
            print()
            print("You fight with the line until eventually you manage to reel it in.")
            print()
            print("Out of the water appears a large crab like monster!")
            print()
            orange = 0
            if sword == 1:
                print()
                print("Fortunately, you draw your sword and slay the beast before it can attack.")
                print("Looks like you'll be eating crab for dinner!")
                print()
                break
            if fireball == 1:
                print()
                print("Just before the beast attacks, you blast it with Inflame.")
                print("The smell of cooked crab fills the air.")
                print("Delicious.")
                print()
                break
            else:
                print()
                print("The beast lunges forward and snaps at you!")
                print("Its mighty claws clutch tightly around your waist!")
                print()
                print("You're snapped completely in half and the crab-monster drags your body into the ocean.")
                print()
                print("\033[1;31;48mYou have died.")
                print("\033[0;26;48m")
                deathcount += 1
                print()
                textspeed()
                break
        if cast == 4 or cast == 5 or cast == 6:
            print()
            print("After minutes of silence you reel in your line.")
            print()
            orange = 0
            break
        if cast == 7 or cast == 8 or cast == 9:
            print()
            print("Minutes after casting your line into the ocean you feel the weight of the fishing rod become "
                  "slightly heavier.")
            print()
            print("You assume that you've got a bite so you reel in the line only to discover an old shoe.")
            print("How disappointing.")
            print()
            orange = 0
            break
        if cast == 10 or cast == 11:
            print()
            print("A few minutes pass and you feel a bite on the line!")
            print()
            print("You fight with the fishing rod and eventually reel in a large fish!")
            print("Looks like you've caught dinner!")
            print()
            orange = 0
            break
        if cast == 12:
            if orange < 4:
                print()
                print("After a few minutes of waiting, you feel a tug on the line!")
                print("You reel in the fishing rod and find a floppy orange colored fish.")
                print()
                print("It looks absolutely useless, just splashing about.")
                print()
                print("You toss it back into the ocean.")
                print()
                orange = orange + 1
                break
            if orange >= 3:
                print()
                print("You wait just a few moments before your fishing line is taken right out of your hands!")
                print()
                print("The water begins to ripple and you watch as an enormous blue sea-serpent plunges out of "
                      "the water!")
                print("You have no time at to react before it dives down and gobbles you up.")
                print()
                print("\033[1;31;48mYou have died.")
                print("\033[0;26;48m")
                deathcount += 1
                print()
                textspeed()
                break
    print()
    while True:
        ans = input("Would you like to cast your line again?")
        ans = ans.upper()
        if ans == "YES":
            fishingbeach()
            break
        if ans == "NO":
            beach()
            break


def splitpath():
    if escort == 0:
        print()
        print("To the NORTH is a forest.")
        print("To the EAST appears to lead to the mountains.")
        print("To the WEST is a familiar pathway, but you can't quite place its significance in your memory.")
        print("To the SOUTH, the path leads you back into the upper part of Oceandale.")
        print()
        ans = userinput("Which way would you like to investigate?")
        print()
        north = ["NORTH"]
        east = ["EAST"]
        west = ["WEST"]
        south = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        if containsAny(ans, south):
            print()
            print("You travel back to the upper part of Oceandale.")
            graveyard()
        if containsAny(ans, north):
            print()
            forestenterance()
        if containsAny(ans, west):
            print()
            print("The road seems to be well maintained, but not a soul is in sight.")
            print("Abandoned carriages dot the road, some of which are ablaze and destroyed.")
            print("It seems the Agromanians have been stalking this road.")
            print()
            westernroad()
        if containsAny(ans, east):
            print("You walk along the path.")
            print("Trees become mountains, and each step is higher than the past.")
            print("Finally, it levels off.")
            print()
            wait()
            print("You begin to hear the roar of water close-by.")
            print("Ahead you notice the beginnings of a bridge.")
            print("As you draw in closer you see that the bridge disappears deep into the chasm.")
            print("The end of the bridge is hidden by the rapid water.")
            bridge()
        else:
            splitpath()
            print()

    if escort == 1:
        print()
        print("You need to take the Old Mage West, to Nacastrum.")
        print()
        ans = userinput("Which way would you like to investigate?")
        print()
        west = ["WEST"]
        east = ["EAST"]
        south = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        if containsAny(ans, west):
            print()
            print("You're intrigued by the road to the WEST and decide to head in that direction.")
            westernroad()
        elif containsAny(ans, south):
            print()
            oceandale()
        elif containsAny(ans, east):
            print()
            print("You need to take the Old Mage West, to Nacastrum.")
            print()
        else:
            print()
            print("You need to take the Old Mage West, to Nacastrum.")
            print()


# mountain functions


def mountain():
    print()
    print("To the NORTH, there is a small divot between the rocks you can easily fit through.")
    print("To the EAST, the ground follows parallel around the mountain.")
    print("To the WEST, the path extends straight, but narrow, parallel to the roaring chasm.")
    print("Going SOUTH takes you back to the split path.")
    print()
    while True:
        ans = userinput("Which way would you like to investigate?")
        print()
        north = ["NORTH"]
        east = ["EAST"]
        west = ["WEST"]
        south = ["SOUTH"]
        if containsAny(ans, south):
            print()
            print("You levitate back across the bridge to the split-path.")
            splitpath()
            break
        elif containsAny(ans, north):
            print()
            caveentrance()
            break
        elif containsAny(ans, east):
            druidtalk()
            break
        elif containsAny(ans, west):
            print()
            print("You go WEST, along the mountain wall, being very careful to avoid the chasm.")
            print("Finally, the path you're on opens up to allow you to walk more freely.")
            westmountain()
            break
        elif mountain():
            print()


def bridge():
    print()
    print("The bridge is impassable.")
    print()
    while True:
        global lev
        global sword
        global deathcount
        global tran
        s = ["SWORD", "CUT"]
        float = ["LEVITATE", "LEV", "LEVITATE", "LEV"]
        v = ["SWIM", "DIVE", "WATER"]
        j = ["JUMP"]
        leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
        ans = input("What do you do?")
        ans = ans.upper()
        print()
        if containsAny(ans, s):
            if sword == 0:
                print("You don't have a sword.")
                print()
            if sword == 1:
                print(
                    "No nearby trees are long enough to span across the chasm, even if your sword could cut down one.")
                print()
        elif containsAny(ans, float):
            if lev == 0:
                print("You don't know the spell.")
                print("You can try and jump across the chasm though.")
                print("Good luck.")
                print()
                bridge()
            elif lev == 1:
                print("Due to a strong tone in your voice, Levitate echos across the mountains.")
                print("You hover across the chasm, surprisingly easy for your first time.")
                print("Almost, as if it wasn't your first time at all.")
                print("Never-the-less, you cross the roaring chasm safe and sound.")
                wait()
                mountain()
                tran = 1
                break
            elif geo == 1 and lev == 0:
                print("You don't know the spell.")
                print("You can try and jump across the chasm though.")
                print("Good luck.")
                print()
                bridge()
            elif geo == 1 and lev == 1:
                print("Due to a strong tone in your voice, Levitate echos across the mountains.")
                print("You hover across the chasm, surprisingly easy for your first time.")
                print("Almost, as if it wasn't your first time at all.")
                print("Never-the-less, you cross the roaring chasm safe and sound.")
                wait()
                mountain()
                brid = 1
                break
        elif containsAny(ans, j):
            print("You jump in the water and then realize, halfway into the jump, that the chasm is VERY deep.")
            print()
            print()
            print("\033[1;31;48mYou have died.")
            print("\033[0;26;48m")
            deathcount += 1
            print()
            textspeed()
            break
        elif containsAny(ans, v):
            print("You jump in the water and then realize, halfway into the jump, that the chasm is VERY deep.")
            print()
            print()
            print("\033[1;31;48mYou have died.")
            print("\033[0;26;48m")
            deathcount += 1
            print()
            textspeed()
            break
        elif containsAny(ans, leave):
            print("I'll find another way, you think to yourself.")
            print("You travel back the way you came.")
            splitpath()
            break
        else:
            print("I don't understand that.")
            bridge()
            print()


def druidtalk():
    global druid
    global lant
    if druid == 0:
        print()
        print("You follow the path to the EAST.")
        print("As you travel further, you notice tracks on the ground.")
        print("The tracks are fairly small and are in the shape of a paw-print.")
        print()
        wait()
        print("You decide to follow the tracks and eventually find yourself behind a red fox.")
        print("The fox quickly discovers your presence and turns around in a threatening pose.")
        print("After a stare-down between you and the fox, the fox relaxes and begins to walk towards you.")
        print()
        wait(.5)
        print("As it walks closer, its size begins to increase.")
        print("The fox then begins to stand on its hind legs, much like a human.")
        print("To your surprise, what was a fox transforms into a man with long, cherry-red hair.")
        print()
        wait(.5)
        print(""" "Ah, greetings mage. My apologies for the reaction. You never know what could be out here." """)
        print()
        wait()
        print(""" "My name is Dentros." """)
        print(""" "I am a scout from Cataracta." """)
        print(""" "If you can't tell, I am a Druid." """)
        print(""" "I hope I am not being too presumptuous, but I must ask." """)
        print(""" "What are you doing here?" """)
        print()
        wait()
        print("You explain your quest to the druid.")
        print("He waits for you to finish before speaking.")
        print()
        print(""" "You seek to reopen Nacastrum?" """)
        print(""" "Yes, a difficult task indeed." """)
        print(""" "Since Vashirr exiled his people, I must admit, my people have been worried." """)
        print(
            """ "If the king of the Mage feared the Agromanians, then surely they are a real force to be reckoned with." """)
        wait()
        print()
        print(""" "But I recognize your quest." """)
        print(""" "If Cataracta was to be taken, I would do anything to protect my home." """)
        print()
        print(""" "Deep within the mountains is a secret of the Old Mages." """)
        print(""" "The druid of Cataracta have known of it for ages, but do not posses the means to reach it." """)
        print(""" "I suggest you look for this hidden knowledge. It may be of use to you." """)
        print()
        wait(2)
        print(""" "Oh, before you leave." """)
        print(""" "Take this lantern. The caves are dark and you will need to be able to see." """)
        print()
        print("\033[1;32;48mYou received a lantern!")
        print("\033[0;26;48m")
        print(""" "Good luck, my friend." """)
        print()
        print("Dentros returns to his fox form and leaps away.")
        wait()
        print("You return back to the place you came from.")
        print()
        druid = 1
        lant = 1
        mountain()
    else:
        print("There is nothing of significance here.")
        mountain()


def westmountain():
    print()
    print("To the NORTH, the path you're on converts to stone.")
    print("To the EAST, the mountains serve as an impenetrable wall.")
    print("To the WEST, you see the forest with a massive tree protruding over the tree line.")
    print("SOUTH takes you back to where you crossed the chasm.")
    print()
    while True:
        ans = userinput("Which way would you like to investigate?")
        print()
        n = ["NORTH"]
        e = ["EAST"]
        w = ["WEST"]
        leave = ["SOUTH", "BACK", "LEAVE", "RETURN", "EXIT"]
        if containsAny(ans, n):
            if cgates == 0:
                druidpath()
                break
            if cgates == 1:
                print("You don't want to make another scene in front of the druids.")
                print()
        elif containsAny(ans, w):
            print("The great forest trees block a clear landing across the chasm.")
            print()
        elif containsAny(ans, e):
            print("The stone is thick and impenetrable.")
            print()
        elif containsAny(ans, leave):
            print()
            mountain()
            break
        else:
            print("I don't understand that.")
            print()


def druidpath():
    global cgates
    print("You continue until the dirt path becomes stone and the chasm's roar becomes the chirps of birds.")
    print("Ahead you see a huge stone gate, enriched with blue crystal shards.")
    print("You see a group of six men talking under the blue gleaming gate.")
    print()
    while True:
        ans = userinput("What do you do?")
        print()
        talk = ["TALK", "APPROACH"]
        if containsAny(ans, talk):
            print("These men seem friendly enough.")
            print("You approach them to start a converation.")
            print("One of the men facing you sees you and shouts.")
            print()
            wait(.75)
            print(""" "Who are you!? Stay back!" """)
            print()
            print("Suddenly, one of the men lets out an unhuman roar!")
            print("Before anything else is said the man is on all fours.")
            print("He thrashes as hairs protrude from his ever-growing body.")
            print("The man is now a big, black, terrifying wolf!")
            print()
            wait(.75)
            print("You know that the druids are allies with the mages.")
            print("You need to show them who you are.")
            print()
            ans = userinput("What do you do?")
            print()
            lev = ["LEVITATE", "LEV"]
            ear = ["EAR", "EARS"]
            scorch = ["INFLAME", "IN-FLAME"]
            bendy = ["STONEBEND", "STONE-BEND"]
            if containsAny(ans, lev):
                print()
                print("You desperately mumble levitate under your breath.")
                print("Suddenly, the druid men are like little stone pebbles as you ascend towards the heavens.")
                print("Once you see the wolf transform back into human form, you deicde it is safe to come back down.")
                print()
                wait(.75)
                print("The man that shouted, obviously the leader, begins to apologize.")
                print()
                print(""" "Dreadfully sorry about that, Mage." """)
                print(""" "You can't be too careful around here, not with those cursed Agromanians lurking around." """)
                print()
                wait(.5)
                print("He gestures to his group.")
                print(""" "We are a group of hunters. Our duty is to provide food for the people of Cataracta." """)
                print(""" "We are just one of the several class groups." """)
                print(""" "Some of us hunt and some of us are scouts." """)
                print(""" "This is just the druid way." """)
                wait(.75)
                print()
                print("He looks to his group.")
                print(""" "You all did well today. Go from here and get some rest." """)
                print()
                print("The hunters of Cataracta follow the stone path into the city.")
                wait(.5)
                print()
                print("The leader stays and begins talking to you.")
                print()
                print(""" "My name is Cellious. I'm the chief of that hunting pack." """)
                print(""" "I heard what happened to Nacastrum. We all did." """)
                print(""" "Most mages went towards Aylova, the capital." """)
                print(""" "But not you. You're still here." """)
                print()
                wait(.5)
                print(""" "I'm afriad I can't let you into the city." """)
                print(""" "Our king is extremely paranoid of spies now that Oceandale has been attacked." """)
                print(""" "I wish you safe travels, Mage." """)
                print(""" "Good luck. And most of all, if you see any Agromanians..." """)
                print("Cellious roars ferociously showing his hatred.")
                print()
                wait()
                print("You make your way all the way back to where you crossed the bridge.")
                print()
                cgates = 1
                mountain()
                break
            elif containsAny(ans, ear):
                print()
                print("You quickly pull back your hair and flash your ears!")
                print("Almost immediately, the group seems to understand that you mean no harm.")
                print()
                print("The man that shouted, obviously the leader, begins to apologize.")
                print()
                print(""" "Dreadfully sorry about that, Mage." """)
                print(""" "You can't be too careful around here, not with those cursed Agromanians lurking around." """)
                print()
                wait(.5)
                print("He gestures to his group.")
                print(""" "We are a group of hunters. Our duty is to provide food for the people of Cataracta." """)
                print(""" "We are just one of the several class groups." """)
                print(""" "Some of us hunt; some of us heal; some of us are scouts." """)
                print(""" "This is just the druid way." """)
                wait(.75)
                print()
                print("He looks to his group.")
                print(""" "You all did well today. Go from here and get some rest." """)
                print()
                print("The hunters of Cataracta follow the stone path into the city.")
                wait(.5)
                print()
                print("The leader stays and begins talking to you.")
                print()
                print(""" "My name is Cellious. I'm the chief of that hunting pack." """)
                print(""" "I heard what happened to Nacastrum. We all did." """)
                print(""" "Most mages went towards Aylova, the capital." """)
                print(""" "But not you. You're still here." """)
                print()
                wait(.5)
                print(""" "I'm afriad I can't let into the city." """)
                print(""" "Our king is extremely paranoid of spies now that Oceandale has been attacked." """)
                print(""" "I wish you safe travels, Mage." """)
                print(""" "Good luck. And most of all, if you see any Agromanians..." """)
                print("Cellious roars ferociously showing his hatred.")
                print()
                wait()
                print("You make your way all the way back to where you crossed the bridge.")
                print()
                cgates = 1
                mountain()
                break
            elif containsAny(ans, scorch):
                if fireball == 0:
                    print()
                    print("You don't know that spell.")
                    print()
                if fireball == 1:
                    print()
                    print("That would certainly start a wildfire, or kill your allies.")
                    print("Find another way! Quick!")
                    print()
            elif containsAny(ans, bendy):
                if geo == 0:
                    print()
                    print("You don't know that spell.")
                    print()
                if geo == 1:
                    print()
                    print("You cast Stonebend!")
                    print("Right in front of you, the stone pathway lurches upwards to hide the pack of men.")
                    print("You wait a few seconds and cast Stonebend again to put the path back the way it was. ")
                    print("The men seem surprised but immediately understand you mean no harm.")
                    print("The man that shouted, obviously the leader, begins to apologize.")
                    print()
                    print(""" "Dreadfully sorry about that, Mage." """)
                    print(
                        """ "You can't be too careful around here, not with those cursed Agromanians lurking around." """)
                    print()
                    wait(.5)
                    print("He gestures to his group.")
                    print(""" "We are a group of hunters. Our duty is to provide food for the people of Cataracta." """)
                    print(""" "We are just one of the several class groups." """)
                    print(""" "Some of us hunt; some of us heal; some of us are scouts." """)
                    print(""" "This is just the druid way." """)
                    wait(.75)
                    print()
                    print("He looks to his group.")
                    print(""" "You all did well today. Go from here and get some rest." """)
                    print()
                    print("The hunters of Cataracta follow the stone path into the city.")
                    wait(.5)
                    print()
                    print("The leader stays and begins talking to you.")
                    print()
                    print(""" "My name is Cellious. I'm the chief of that hunting pack." """)
                    print(""" "I heard what happened to Nacastrum. We all did." """)
                    print(""" "Most mages went towards Aylova, the capital." """)
                    print(""" "But not you. You're still here." """)
                    print()
                    wait(.5)
                    print(""" "I'm afriad I can't let into the city." """)
                    print(""" "Our king is extremely paranoid of spies now that Oceandale has been attacked." """)
                    print(""" "I wish you safe travels, Mage." """)
                    print(""" "Good luck. And most of all, if you see any Agromanians..." """)
                    print("Cellious roars ferociously showing his hatred.")
                    print()
                    wait()
                    print("You make your way all the way back to where you crossed the bridge.")
                    print()
                    cgates = 1
                    mountain()
                    break
            else:
                print("You need to show them you're a mage.")
                print()
        else:
            print("You can try talking to them.")
            print()


# cave functions


def caveentrance():
    print("You slide past through the divot and venture a few steps before you realize you can't see anything.")
    print("You wait for your eyes to adjust but they never do.")
    print("Complete darkness overwhelms you.")
    print()

    while True:
        global lant
        global lev
        l = ["LEVITATE", "LEV"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
        light = ["LIGHT", "LANTERN"]
        ans = userinput("What do you do?")
        print()
        if containsAny(ans, leave):
            print("Maybe there's another way?")
            mountain()
        elif containsAny(ans, l):
            if lev == 0:
                print("You don't know that spell.")
                print()
            if lev == 1:
                print("There's a time and place for everything, but not now.")
                print()
        elif ans == "TORCH":
            print("Items don't just appear in this game.")
            print()
        elif lant == 0:
            if containsAny(ans, light):
                print("What lantern?")
                print("I must've missed when you obtained that.")
                print("Items don't just appear out of thin air ya'know?")
                wait()
                print()
        elif lant == 1:
            if containsAny(ans, light):
                print("You fire up the lantern!")
                print()
                wait()
                print("The lantern illuminates the narrow walls in front of you with a quick flare!")
                print("The narrow path makes you shimmy your way through.")
                print("As you progress forward, your body is slowly consumed by water.")
                print()
                wait()
                print("The water is up to your breast now and you come to a dead end.")
                print("Even with the lantern, you can't see a clear way forward.")
                print()
                wait()
                break
        else:
            print()
            print("I don't understand that.")
            print()
    while True:
        global deathcount
        verbs = ["CRAWL", "SWIM", "DIVE"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "TURN"]
        l = ["LEVITATE", "LEV"]
        ans = userinput("What do you do?")
        print()
        if containsAny(ans, l):
            if lev == 0:
                print("You don't know that spell.")
                print()
            if lev == 1:
                print()
                print("...")
                while True:
                    y = ["YES", "Y"]
                    no = ["LEAVE", "BACK", "EXIT", "NO", "N"]
                    ans = input("Are you sure you want to use levitate in here?")
                    if containsAny(ans, y):
                        print()
                        print("Your voice echos through the dark cave as you fling upwards out of the water.")
                        print(
                            "You overcompensate for the weight of the water and spring upwards; faster than intended.")
                        print("The roof of the cave is home to several stalactites.")
                        print()
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    elif containsAny(ans, no):
                        print()
                        print("Good answer.")
                        break
                    else:
                        print()
                        print("Yes or no?")
        elif containsAny(ans, verbs):
            print("You take a deep breath and go underwater.")
            print("You see that there is a hole in the cave wall to your east.")
            print("You swim and wiggle your way through the small hole.")
            print()
            wait()
            print("You resurface, gasping for breath.")
            print("You are now in a extremely large room, with every movement sending echos running in all directions.")
            print()
            mcave()
            break
        elif containsAny(ans, leave):
            mountain()

        else:
            print()
            print("I don't understand that.")
            print()


def ncave():
    global ndoor
    if ndoor == 0:
        print("You slide in-between the rocks to see it opens up quite distinctly.")
        print("You walk under a massive archway that is inscribed with ancient writing.")
        print("Ahead and you see a massive crumbling stone-gate.")
        print("The walls are inscribed with ancient writings, foreign to you.")
        print("The writings penetrate from the wall at about a quarter inch.")
        print("Symbols include:" + " %' " + "  )* " "  <~ ")
        print()
        while True:
            l = ["LEVITATE", "LEV"]
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
            light = ["LIGHT", "LANTERN"]
            look = ["LOOK", "INVESTIGATE", "SEARCH"]
            push = ["TOUCH", "PUSH", "PRESS", "TAP"]
            ans = userinput("What do you do?")
            print()
            if containsAny(ans, l):
                print("Seriously?")
                print()
            elif containsAny(ans, light):
                print("Your lantern is already on...")
                print()
            elif containsAny(ans, look):
                print("The symbols penetrate from the wall...")
                print("It appears it is some kind of button.")
                print()
            elif containsAny(ans, push):
                while True:
                    leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
                    print("(1, 2, or 3?)")
                    ans = userinput("Which symbol?" + " %' " + "  )* " "  <~ ")
                    print()
                    if ans == ")*" or ans == "3":
                        print("You reach out and touch the cold inscription.")
                        print("Absolutely nothing happens.")
                        wait()
                        print()
                    elif ans == "<~" or ans == "2":
                        print("You reach out and touch the cold inscription.")
                        print("Absolutely nothing happens.")
                        wait()
                        print()
                    elif ans == "%'" or ans == "1":
                        print()
                        print("A low rumbling turns to a loud thunderous roar, the northern gate is rolling open!")
                        print("After the dust settles, and you clear your eyes...")
                        wait()
                        print("The stone-gate has rolled away, leaving a new entrance to the north!")
                        print()
                        ndoor = 1
                        print("You venture north, knowing beyond the stone-gate hides what you came for.")
                        fireballroom()
                        break
                    elif containsAny(ans, leave):
                        mcave()
                    else:
                        print("(You can also use 1, 2, or 3)")
                        print()

            elif containsAny(ans, leave):
                print("You decide you will come back later.")
                print()
                mcave()
                break
            else:
                print()
                print("Not an option.")
                print()

    if ndoor == 1:
        while True:
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
            forward = ["NORTH", "FORWARD", "N"]
            g = ["gate"]
            print("The stone door to the north is open.")
            print("South takes you back to the main part of the cave.")
            print()
            ans = userinput("Which way do you want to go?")
            print()
            if containsAny(ans, g):
                print("You venture through where the stone gate once was.")
                fireballroom()
                break
            elif containsAny(ans, forward):
                print("You venture through where the stone gate once was.")
                fireballroom()
                break
            elif containsAny(ans, leave):
                print("You decide you will come back later.")
                print()
                mcave()
                break
            else:
                print()
                print("Not an option.")
                print()


def mcave():
    global symbols
    print()
    print("Enormous pink crystals illuminate the room around you.")
    print("There are several paths branching off in nearly every direction.")
    print("There are paths to the NORTH, NORTHEAST, NORTHWEST, EAST, and WEST.")
    print("Going to the SOUTH returns you to the entrance of the cave.")
    print()
    ans = input("Which way would you like to investigate?")
    ans = ans.upper()
    print()
    if ans == "SOUTH" or ans == "GO SOUTH" or ans == "S":
        print("You crawl your way back out of the cave.")
        mountain()
    elif ans == "NORTH" or ans == "GO NORTH" or ans == "N":
        print()
        ncave()
    elif ans == "EAST" or ans == "GO EAST" or ans == "E":
        print()
        ecave()
    elif ans == "WEST" or ans == "GO WEST" or ans == "W":
        print()
        wcave()
    elif ans == "NORTHWEST" or ans == "GO NORTHWEST" or ans == "NW":
        print()
        nwcave()
    elif ans == "NORTHEAST" or ans == "GO NORTHEAST" or ans == "NE":
        print()
        necave()
    else:
        print()
        mcave()
        print()


def ecave():
    global symbols
    print()
    print("You head eastward, ever further into the cave.")
    print("You're surrounded by the same pink crystal spires that encompass the previous rooms.")
    print("The clear reflections of the crystals make the area in front of you seem infinite.")
    print("The farthest wall, however, lacks the pink crystal stalagmites.")
    print()
    wait()
    print("Even though you're drawn to the crystals' shine, your determination drives you onward.")
    print("You approach the farthest wall and discover that it is made of stone.")
    print("Four strange markings cover the wall, but the first three seem to be illegible.")
    print()
    wait()
    print("Unlike the first three, you can make out the final symbol.")
    print("\033[1;33;48mThe symbol is " + symbols[3])
    print("\033[0;26;48m")
    print()
    wait(2)
    print("After further inspection of the room, you decide that there is nothing else in the room worth your time.")
    print("You head back through the passage that lead to this room.")
    print()
    mcave()


def wcave():
    print()
    print("You delve into the western passage and find yourself in a cold, dark, and damp room.")
    print("You can hear droplets of what you assume to be water hit the hard ground.")
    print("While your lantern burns bright, you can only see less than a few feet in front of you.")
    print("The drips of water echo deep into the cave and sound as if they came from a league away.")
    print()
    wait()
    print("You press on deeper into the cave as the droplets become more prominent.")
    print("You feel some sort of liquid fall onto your arm.")
    print("Curious, you move the lantern to your arm to see what it was.")
    print("You hoped that it was water, but soon discover that it was not.")
    print("The liquid is red.")
    print()
    wait(2)
    print("Fear quickly rushes over you and you are tempted to turn back.")
    print("But the thought of discovering the true purpose of your quest drives you deeper in to the dark.")
    print()
    wait(.5)
    wcavefork()


def wcavefork():
    while True:
        global symbols
        print()
        ans = userinput("Which direction do you go? LEFT or RIGHT?")
        left = ["LEFT", "L"]
        right = ["RIGHT", "R"]
        back = ["BACK", "RETURN", "LEAVE"]
        if containsAny(ans, left):
            print()
            print("You waste no time heading to the left.")
            print("You are still consumed by fear as you run down the path.")
            print("Thoughts of regret fill your mind.")
            print()
            wait()
            print(""" "Why am I doing this?" """ + "you think to yourself." + """ "What is the point of all this?" """)
            print("The thought of returning your memory and uniting the mages drives you forward with vigor.")
            wait()
            print("You finally meet a dead end.")
            print("The stone wall in front of you is etched in the same strange markings you've seen previously.")
            print("There is a marking that you notice repeats at the start in all of the groups of markings.")
            print("\033[1;33;48mThe symbol is " + symbols[0])
            print("\033[0;26;48m")
            print()
            wait()
            print("Not wanting to waste anymore time in this god forsaken place, you rush back to where you came from.")
            mcave()
            break
        elif containsAny(ans, right):
            print()
            print("You run down the right path.")
            print("As you sprint down the corridor something catches your leg and you fall face first into the ground.")
            print("You drop your lantern and watch as it rolls forward.")
            print("You watch it come to a stop as it continues to emit its light.")
            print()
            wait()
            print("The lantern illuminates a large amount of corpses that litter the cave.")
            print("The bodies have huge gashes and bite marks covering each one.")
            print("You can only hope that you don't meet the same fate as these poor souls.")
            print("You grab your lantern and head back to the fork in the cave.")
            print()
            wait()
        elif containsAny(ans, back):
            print("You return to the main part of the cave.")
            print()
            mcave()
        else:
            print()
            print("I don't understand that.")
            print()


def decodesymbols(Array):
    symbolsstring = str.join("", Array).replace("'", "")
    return symbolsstring.translate(str.maketrans("^~>;", "1234"))


def fireballroom():
    global fireball
    global geo
    global guesses
    global deathcount
    global symbols
    if fireball == 0:
        print("There is a cracked stone pedestal, centered in the room.")
        print("The smell of charred ash stings your nostrils.")
        print("A dead mage lies in the corner of the room.")
        print("His body is now just black ash in the shape of what he once was.")
        print()
        print("It seems you are not alone on your quest.")
        print()
        print("On the pedestal are four symbols, horizontal to each other.")
        print("Just like before, the symbols are a quarter inch indented out.")
        print()
        print("The symbols include:" + "(^' ~' >' ;')")
        print()
        while True:
            l = ["LEVITATE", "LEV"]
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
            light = ["LIGHT", "LANTERN"]
            push = ["TOUCH", "PUSH", "PRESS", "TAP"]
            ans = userinput("What do you do?")
            print()
            if containsAny(ans, l):
                print("You seriously have got to stop.")
                print()
            elif containsAny(ans, light):
                print("It's already lit fam.")
                print()
            elif containsAny(ans, push):
                print()
                break
            elif containsAny(ans, leave):
                print()
                ncave()
            else:
                print()
                print("Not an option.")
                print()
    while True:
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
        print("(^' is 1) (~' is 2) (>' is 3) (;' is 4)")
        print("i.e. 1234")
        print()
        print("Which order do you want to touch the symbols?")
        ans = input("(^' ~' >' ;')")
        print()
        if ans != decodesymbols(symbols):
            guesses -= 1
            print()
        if guesses == 0:
            print("Suddenly the room goes completely black.")
            print("The entrance behind you rolls shut once again.")
            print("The ground under you becomes immensely hot.")
            print()
            wait()
            print("The heat crawls its way up your body, breaking you into a sweat.")
            print("You feel around the walls, desperately trying to find some escape.")
            print("The darkness of the room suddenly illuminates.")
            print()
            wait()
            print("The cause of the heat is now apparent.")
            print("A massive ball of fire hurls towards you.")
            print()
            print()
            wait(.5)
            print("\033[1;31;48mYou have died.")
            print("\033[0;26;48m")
            deathcount += 1
            print()
            textspeed()
        if ans == decodesymbols(symbols):
            if geo == 0:
                print("Fire erupts from the pedestal.")
                print("You quickly back up to avoid being burned.")
                print("The flames soon recede and a tome is left.")
                print()
                wait()
                print("You cautiously approach the tome and place your hand on it.")
                print("The book radiates heat and burns when you touch it.")
                print("Without hesitation, you pry the tome open.")
                print()
                wait()
                print("Visions of flame fill your mind and you're soon shown a place that looks strangely familiar.")
                print("Memories of your kind in a courtyard spew fire from their palms with no effort.")
                print("Your body begins to warm and your very veins are filled with heat.")
                print()
                wait()
                print("Your vision returns to the cave's chamber.")
                print("Almost immediately, you fire a blast of flame from your hand leaving the vines on the "
                      "walls crisp and burned.")
                print("It seemed almost natural.")
                print()
                wait()
                print()
                print("\033[1;32;48mYou received Inflame!")
                print("\033[0;26;48m")
                print()
                wait(2)
                print("You leave the cave with new found strength and a sense of victory.")
                fireball = 1
                mountain()
            if geo == 1:
                print("Fire erupts from the pedestal.")
                print("You quickly back up to avoid being burned.")
                print("The flames soon recede and a tome is left.")
                print()
                wait()
                print("You cautiously approach the tome and place your hand on it.")
                print("The book radiates heat and burns when you touch it.")
                print("Without hesitation, you pry the tome open.")
                print()
                wait()
                print("Visions of flame fill your mind and you're soon shown the courtyard you saw previously when you "
                      "learned Stone-bend.")
                print("Memories of mages spew fire from their palms with no effort.")
                print("Your body begins to warm and your very veins are filled with heat.")
                print()
                wait()
                print("Your vision returns to the cave's chamber.")
                print("Almost immediately, you fire a blast of flame from your hand leaving the vines on the walls "
                      "crips and burned.")
                print("It seemed almost natural.")
                print()
                wait()
                print("\033[1;32;48mYou received Inflame!")
                print("\033[0;26;48m")
                wait()
                print("You leave the cave with new found strength and a sense of victory.")
                fireball = 1
                mountain()
        if ans == "NO IDEA":
            print("Thanks for your honesty.")
            print("I'm not going to give you the answer, however.")
            print()
        if containsAny(ans, leave):
            print("You leave and go all the way back to the main cave.")
            mcave()
            break

    if fireball == 1:
        print()
        print("An empty pedestal and ashes of old vines lie in front of you.")
        print("You decide to go back.")
        print()
        mcave()


def nwcave():
    print()
    print("You head into the north-western entrance.")
    print("As you continue onward, the large pink crystals begin to decrease in size.")
    print("Some of them are even cracked or broken all together.")
    wait()
    print("While you march forward, you hear a crisp, crunching sound come from under your boot.")
    print("You look down to see that the ground is littered in broken shards.")
    print("All of them seem to be colorless, despite the fact they could only have come from the pink crystal spires.")
    print("You discover a body laying cold on the floor.")
    wait(2)
    print("His satchel is busted open and full of the pink shards that are now almost translucent.")
    print("He appears to have been attempting to mine the shards.")
    print()
    wait()
    nwcavebody()


def nwcavebody():
    global deathcount
    while True:
        ans = userinput("What do you want to do?")
        print()
        look = ["SEARCH", "INVESTIGATE", "LOOK", "INSPECT", "BODY", "HELP"]
        con = ["CONTINUE", "KEEP GOING", "FORWARD", "STRAIGHT"]
        s = ["SHARDS", "SHARD"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
        if containsAny(ans, s):
            print("It seems unnecessary to take any of the shards.")
            print()
        elif containsAny(ans, con):
            print()
            print("You decide that this man's fate is not of your concern and continue on.")
            print()
            nwcavecontinue()
            break
        elif containsAny(ans, look):
            print()
            print("You turn over the body and find that he has a wound in his chest.")
            print("The front of his clothes are covered in blood that clearly came from where he was injured.")
            print("You look further and determine that he had been stabbed with some kind of weapon.")
            print("You find his pickaxe laying on the floor next to him.")
            print()
            while True:
                ans = userinput("Do you want to take the pickaxe?")
                print()
                y = ["YES", "Y"]
                n = ["NO", "N"]
                if containsAny(ans, y):
                    print("You grab the pickaxe.")
                    print()
                    ans = userinput("Do you want to attempt to mine the crystals using the pickaxe?")
                    if containsAny(ans, y):
                        print()
                        print("You walk towards one of the remaining crystals and set down your lantern.")
                        print("You grasp the pickaxe with both of your hands and hold it above your head.")
                        wait()
                        print("Just as you're about to slam down the pick into the crystals... ")
                        print("You feel a sharp pain in the center of your back.")
                        wait()
                        print(
                            "You drop the pickaxe and look down to see the tip of a spear extruding from your chest.")
                        print("The world around you darkens and you fall to the ground..")
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    if containsAny(ans, n):
                        print()
                        print("It probably isn't a good idea to mine the pink crystals considering the miner's fate.")
                        print("You don't think a pickaxe is worth carrying around. ")
                        print("You continue on through the cave.")
                        wait()
                        print()
                        nwcavecontinue()
                        break
                    else:
                        print()
                        print("Yes or No?")
                        print()
                if containsAny(ans, n):
                    print()
                    print("You leave the mystery of the miner alone and continue along the path.")
                    print()
                    nwcavecontinue()
        elif containsAny(ans, leave):
            print()
            print("You leave the mystery of the miner alone and go back to the main part of the cave.")
            mcave()
            break
        else:
            print("I don't understand that.")
            print()
            print("The body of the miner lays lifeless on the ground.")
            print()


def nwcavecontinue():
    global solution
    print()
    print("Without the pink crystals reflecting the light of your lantern, you find it difficult to see.")
    print("After walking for a few minutes, you see a pink light in the distance.")
    print("You close the distance between yourself and the pink light.")
    wait(2)
    print("You find that the light was coming from a crystal much larger than the ones you've previously seen.")
    print("Upon further inspection, you notice that four symbols are etched into the side of it.")
    print("Much of the crystal has been cracked and broken, probably by the dead man you saw earlier.")
    wait(2)
    print("Three of the four symbols are illegible, but you can decipher one of them.")
    print("\033[1;33;48mThe second of the four is " + symbols[1])
    print("\033[0;26;48m")
    print()
    wait()
    print("You return back from whence you came.")
    print()
    mcave()


def necave():
    print("You decide to head into the north-eastern cave.")
    print("Much of what you see before you doesn't seem out of the ordinary according to the previous area.")
    print("The cave is eerily quiet and it makes you feel on edge.")
    print("You grip tighter to your lantern and continue on.")
    print()
    wait(2)
    print("You eventually come to a dead end.")
    print("There is nothing you can see in the immediate area in-front of you, but you're finding it difficult to see.")
    print("You hold your lantern up higher and discover cages hanging from the ceiling.")
    print("The cages are fairly high up and completely out of your reach.")
    print("You can make out what looks like a leg hanging out of one of the cages.")
    print()
    wait(2)
    necavecage()


def necavecage():
    global solution
    while True:
        l = ["LEVITATE", "LEV"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
        jump = ["REACH", "JUMP", "TIP", "TOES"]
        climb = ["CLIMB", "SCALE", "WALL"]
        ans = userinput("What do you want to do?")
        ans = ans.upper()
        print()
        if containsAny(ans, l):
            print()
            print("You shout the cast for LEVITATE and slowly drift upwards to one of the cages.")
            print("Inside the cage is an old skeleton that could have been here for hundreds of years.")
            print("The skeleton is still clothed and has a piece of parchment tucked under his arm.")
            wait()
            print("Driven by curiosity, you instinctively grab the parchment and drift down back to the ground.")
            print("You read the parchment and find writings in your native tongue...")
            print("But most of the text seems to have faded.")
            print()
            wait()
            print("At the very bottom of the parchment are four markings.")
            print("The first two and the last are impossible to read due to the faded writing.")
            print("With some effort and cross referencing with the markings you've seen...")
            print()
            wait()
            print("You manage to decipher the third symbol.")
            print("\033[1;33;48mThe symbol is " + symbols[2])
            print("\033[0;26;48m")
            print()
            wait()
            print("You think you have what you came for and return back to where you came from.")
            print()
            print()
            mcave()
        elif containsAny(ans, jump):
            print()
            print(
                "You try your hardest to jump up to the cages, but quickly realize that they are way to high to reach.")
            print("You will have to try something else.")
            print()
            necavecage()
        elif containsAny(ans, leave):
            print()
            print("You give up trying to reach the cage and return back from where you came.")
            print()
            mcave()
        elif containsAny(ans, climb):
            print()
            print("You look to the nearest wall and attempt to scale it to reach the cages.")
            print("You climb a few feet off the ground before quickly losing your grip and plummeting to the ground.")
            print("You're uninjured besides a few scrapes and bruises.")
            print("It seems that the wall doesn't have enough for you to grab onto.")
            print("You will have to try something else.")
            print()
            necavecage()
        else:
            print()
            print("I don't understand that.")
            print()


# forest functions


def forestgrass():
    while True:
        global fireball
        global sword
        global grass
        global lev
        print()
        ans = input("What do you want to do?")
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN"]
        swor = ["SWORD", "CUT"]
        fire = ["INFLAME", "IN-FLAME"]
        l = ["LEVITATE", "LEV"]
        if containsAny(ans, l):
            print()
            print("You can't simply use levitate to escape all your problems.")
            print()
            print("Try something else.")
            print()
        elif containsAny(ans, fire):
            if fireball == 1:
                print()
                print("Considering that there is a lot of flammable material around,")
                print("You decide that it isn't a good idea to cast Inflame.")
                print()
            if fireball == 0:
                print()
                print("You don't know that spell.")
                print()
        elif containsAny(ans, swor):
            if sword == 0:
                print()
                print("You have nothing to cut the grass with.")
                print()
            if sword == 1 and lev == 1:
                print()
                print("You unsheathe the sword you took from the body in Oceandale.")
                print("You're not a master swordsman, but you easily manage to cut your way into the forest.")
                grass = 1
                print()
                print("You continue into the forest.")
                print()
                ftrap()
                break
            if sword == 1 and lev == 0:
                print()
                print("You unsheathe the sword you took from the body in Oceandale.")
                print("You're not a master swordsman, but you easily manage to cut your way into the forest.")
                grass = 1
                print()
                print("You continue into the forest.")
                print()
                ftrapnolev()
                break
        elif containsAny(ans, leave):
            print()
            print("You return back to the split-path.")
            print()
            splitpath()
            break
        else:
            print()
            print("Perhaps you can cut the grass.")
            print()


def ftrap():
    print()
    print("The forest is full of lush flora and fauna.")
    print("Many of the trees ascend deep into the heavens and you lose sight of the tree-tops.")
    print("As you venture deeper into the forest, the grass and foliage make it difficult to see where you're walking.")
    print()
    print("Despite your difficulties, you continue on.")
    print("Unfortunately, you manage to accidentally spring some sort of trap!")
    print()
    wait()
    print("The sword you were using to cut your way through the forest falls out of your hand.")
    print("You are now caught in a net that is suspended about seven feet from the ground.")
    print("You could use levitate and try and undo the knot from the top.")
    print("But as soon as the thought comes to mind, you see a man approaching.")
    print("Something in the man's face shows no hostility.")
    print("However his longbow on his back and his knife in his hand says otherwise.")
    print("None-the-less, you decide to play victim.")
    print()
    wait(2)
    print("The marksman cuts the rope that is suspending you in the air.")
    print("Although he didn't hesitate to set you free, he seems impartial to your safety.")
    print("Mid-fall you silently cast levitate and glide down to your feet.")
    print("The marksman looks impressed.")
    print()
    wait()
    print(""" "Look what we have here." """)
    print(""" "I recognize a mage when I see one. You sure have your work cut out for you." """)
    print(""" "Kaefden to Kaefden, you must reestablish Nacastrum as the great city it once was." """)
    print(""" "And with it, unite the mages of Avasia." """)
    print()
    wait()
    print(""" "My former brethren decided staying aligned as Kaefden, wasn't worth the fight." """)
    print(""" "The elders decided to move North, way beyond the conflict between the Agromanians and the Kaefden." """)
    print(""" "A few of us decided to stay." """)
    print(""" "This is our homeland, and if war is coming, we will stand and fight or we will die." """)
    print(""" "But our blood will fall in OUR homeland." """)
    print()
    wait()
    print(""" "Without the mages to the west, morale of our people is low." """)
    print(""" "Reuniting Nacastrum will give us a fighting chance against the Agromanians." """)
    print(""" "It's in my people's best interest to help you." """)
    print(""" "Follow me." """)
    print()
    print("You follow steadfast, feeling a bond between your fellow Kaefden.")
    wait(2)
    mforest()


def ftrapnolev():
    print()
    print("The forest is full of lush flora and fauna.")
    print("Many of the trees ascend deep into the heavens and you lose sight of the tree-tops.")
    print("As you venture deeper into the forest, the grass and foliage make it difficult to see where you're walking.")
    print()
    wait()
    print("Despite your difficulties, you continue on.")
    print("Unfortunately, you manage to accidentally spring some sort of trap!")
    print("The sword you were using to cut your way through the forest falls out of your hand.")
    print("You are now caught in a net that is suspended about seven feet from the ground.")
    print("Regrettably, you are trapped with no way out.")
    print()
    wait(2)
    print("You only spend a few minutes attempting to free yourself until a young man appears.")
    print("The man is armed with a bow with arrows as well as a small hunting knife.")
    print("He is dressed in animal pelts and leather hides. He has a bear pelt over his head that acts as a hood.")
    print()
    wait()
    print("The man cautiously approaches you with his knife drawn,")
    print("but the look on his face shows that he means no harm.")
    print("Just as you begin to explain yourself, he cuts the rope that keeps the net suspended in the air...")
    print("Sending you plummeting to the ground.")
    print()
    wait(2)
    print("Surprisingly, you seem to have sustained no injuries.")
    print("The man stares at you for a moment and then helps you up from the ground.")
    print()
    print(""" "Look what we have here." """)
    print(""" "I recognize a mage when I see one. You sure have your work cut out for you." """)
    print(""" "Kaefden to Kaefden, you must reestablish Nacastrum as the great city it once was." """)
    print(""" "And with it, unite the mages of Avasia." """)
    print()
    wait()
    print(""" "My former brethren decided staying aligned as Kaefden, wasn't worth the fight." """)
    print(
        """ "The elders decided to move North to the city of Ofelos, way beyond the conflict between the Agromanians and the Kaefden." """)
    print(""" "A few of us, decided to stay." """)
    print(""" "This is our homeland, and if war is coming. We will stand and fight or we will die." """)
    print(""" "But our blood will fall in OUR homeland." """)
    print()
    wait(2)
    print(""" "Without the mages to the west, morale of our people is low." """)
    print(""" "Reuniting Nacastrum will give us a fighting chance against the Agromanians." """)
    print(""" "It's in my people's best interest to help you." """)
    print(""" "Follow me." """)
    print()
    wait(2)
    print("You follow steadfast, feeling a bond between your fellow Kaefden.")
    mforest()


def mforest():
    global forestlore
    if forestlore == 0:
        print()
        print("You follow your new friend until you reach a clearing in the forest.")
        print("Before you lies something you have never seen before.")
        print("At the center of the clearing is an enormous tree,")
        print("much larger than all the others in the forest.")
        print("The leaves glisten in the sun and the huge limbs reach out in all directions.")
        print()
        wait(2)
        print("Around the trunk of the tree are numerous houses, all suspended above the ground.")
        print("Makeshift bridges connect the massive tree to the other surrounding trees that house smaller huts.")
        print("Most of the bridges lead into the tree at multiple locations.")
        print("At the base of the tree is a large gate.")
        print()
        wait()
        print("As you admire the magnificence of the city, your friend begins to speak.")
        print()
        print(""" "This is my home, Silvarium." """)
        print(""" "My people have lived here for centuries." """)
        print(""" "This tree has supplied us with life, leaving it to those savages would be an atrocity." """)
        print(""" "When my ancestors joined the Kaefden faction, your people, the mages, gave us a gift." """)
        print(""" "The Elders kept this spell in secretism, wanting to keep all marksmen equal." """)
        print()
        wait(2)
        print(""" "The spell is kept at the very top of the tree, where the Elders resided." """)
        print(""" "When my people went north to escape the barbarians, they sealed the upper chamber." """)
        print(""" "The few of us that have remained, have busied ourselves with hunting." """)
        print()
        wait()
        print(""" "This gate leads to the center chamber of the tree which spirals to the top." """)
        print()
        print(""" "Venture on, brother, and reunite our people before it is too late." """)
        print()
        wait()
        print("You enter into the massive tree.")
        forestlore = 1
        treeenterance()

    if forestlore == 1:
        print()
        print("North holds Silvarium's giant tree.")
        print("South will take you back to the split-path.")
        print()
        while True:
            ans = input("Which way do you want to investigate?")
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
            n = ["NORTH", "FORWARD", "CONTINUE"]
            if containsAny(ans, n):
                print("You enter through the rustic gate.")
                treeenterance()
                break
            if containsAny(ans, leave):
                splitpath()
                break


def forestenterance():
    print("You decide to head NORTH towards what looks like a forest.")
    print()
    global grass
    if grass == 0:
        print("As you head deeper into the trees, vines and grass begin to get longer.")
        print("The vines and long grass make it impossible to continue on.")
        print()
        forestgrass()
    else:
        print()
        print("You continue into the forest.")
        print()
        mforest()


def treeenterance():
    global geo
    if geo == 0:
        print()
        print("Around the room you see numerous tables set up.")
        print("Residents of the city are bringing game in and dropping them off here before returning to hunt.")
        print("A few of the residents give you curious looks, but continue about their business.")
        print("A staircase leads UP to the second floor of the tree.")
        print("The rustic gate leads outside back to Silvarium's main forest clearing.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            talk = ["TALK", "INVESTIGATE", "APPROACH", "ASK"]
            up = ["UP", "STAIRS", "UPSTAIRS"]
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
            if containsAny(ans, talk):
                print()
                print("You approach the nearest resident, a young boy who appears frightened by you.")
                print("Although frightened, he strikes up a conversation when you get near enough to talk. ")
                print()
                print(""" "My name is Marlux. My dad is apart of the hunting squad. I stay here to learn." """)
                print(""" "I've never seen you here before." """)
                print(""" "Well I need to get back to my class." """)
                print()
                print("The boy runs shyly into a room on the eastern side of the room.")
                print()
            elif containsAny(ans, up):
                print()
                print("With no reason to stay on the bottom floor, you follow a staircase up to the second floor.")
                print()
                treefloor2()
                break
            elif containsAny(ans, leave):
                print()
                print("You leave through the main gate and head out to the forest clearing.")
                print()
                mforest()
                break
            else:
                print()
                print("You could try and talk to a nearby resident.")
                print()
    if geo == 1:
        print()
        print("You've got everything you need from here.")
        print()
        mforest()


def treefloor2():
    print()
    print("You are on the second floor of the large tree.")
    print()
    print("To the LEFT is a room that is devoted to skinning animals and harvesting meat.")
    print("To the RIGHT is what looks like an armory.")
    print("Going UP the stairs leads you to the third floor.")
    print("Heading DOWN the stairs takes you to the first floor.")
    print()
    while True:
        d = ["DOWN", "DOWNSTAIRS"]
        up = ["UP", "UPSTAIRS"]
        left = ["LEFT", "BUTCHER"]
        right = ["RIGHT", "ARMORY"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
        ans = userinput("Which way do you want to investigate?")
        if containsAny(ans, up):
            print()
            print("You head up the stairs to the third floor of the tree.")
            treefloor3()
            break
        if containsAny(ans, d):
            print()
            print("You head down the staircase to the first floor.")
            print()
            treeenterance()
            break
        if containsAny(ans, left):
            print()
            treebutcher()
            break
        if containsAny(ans, right):
            print()
            treearmory()
            break


def treebutcher():
    global dagger
    if dagger == 0:
        print()
        print("You walk into the room and immediately you're hit with the smell of raw animal meat.")
        print("A few men are stationed at tables skinning animals.")
        print("Others are harvesting meat from previously skinned creatures.")
        print()
        wait(.5)
        print("Most of the men are too busy to be bothered by your presence.")
        print("Another, however, notices you enter and gives you a curious look.")
        print("He is very large, almost double your size.")
        print("He has a long, bushy beard that extends far beyond his chest.")
        print("His clothing is made of what looks like bear skin.")
        print("It appears that he is the head of this area.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            talk = ["TALK", "APPROACH", "ASK", "LEADER"]
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
            if containsAny(ans, leave):
                print()
                print("You leave the room and go back to the main atrium.")
                print()
                treefloor2()
                break
            elif containsAny(ans, talk):
                print()
                print("You approach the man who is currently overseeing the others.")
                print()
                print(""" "You there!" """)
                print(""" "What is a mage doing in my butchery?" """)
                print(""" "Can't you see that I am busy feeding my people?" """)
                print()
                print("The man seems slightly annoyed by your presence.")
                print("You could simply leave and return to the atrium or perhaps you could try to explain yourself.")
                print()
                break
        while True:
            ans = userinput("What would you like to do?")
            talk = ["TALK", "EXPLAIN"]
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
            if containsAny(ans, leave):
                print()
                print("You leave the room and go back to the main atrium.")
                print()
                treefloor2()
                break
            elif containsAny(ans, talk):
                print()
                print("You explain to the man that you were simply exploring.")
                print("You tell him that you're trying to unlock Nacastrum and you need something that is "
                      "kept here to do it.")
                print()
                wait(.5)
                print("After you mention Nacastrum, the man's face goes from annoyed to facetious.")
                print(""" "You need a spell?" """)
                print(""" "You mean the one those damned Elders traded our pride for?" """)
                print(""" "The Sylvians were fine before we made that deal with those mage!" """)
                print(""" "Now look what those Elders did. They ran off, the cowards!" """)
                print(""" "For all I care, I'll be glad that tome is gone." """)
                print(""" "Unfortunately, I have no way to give it to you." """)
                print(""" "Us common folk weren't allowed near it and when the Elders left, they locked it up." """)
                print(""" "But since you're here to get rid of it, I may have something to help you." """)
                print(""" "Wait here." """)
                print()
                wait(4)
                print("The large man heads into a back room and comes back moments later with a small, dusty chest.")
                print()
                print(""" "When the elders fled, they left some of their possessions here." """)
                print(""" "I was told to keep this safe, but as far as I'm concerned, my butchery is my land." """)
                print(""" "I don't want anything those damned elders had." """)
                print()
                print("He hands the chest over to you and goes back to his business.")
                print()
                wait(2)
                print("You open the chest and there doesn't seem to be much of interest.")
                print("You dig into the chest and find a few pieces of clothing made of leather and animal pelts.")
                print("Just as you are about to close the chest, something at the very bottom catches your eye.")
                print()
                wait(.5)
                print("You dig up a dagger that looks like nothing you've ever seen.")
                print("The hilt of the dagger is wrapped in dark leather.")
                print("At the base and top of the hilt are cross-guards that form what looks like mandibles.")
                print("The blade of the dagger is razor sharp and made of a metal unknown to you.")
                print("The metal is a clear \033[1;36;48mblue.")
                print("\033[0;26;48m")
                print()
                wait(.5)
                print("\033[1;32;48mYou received Dagger!")
                print("\033[0;26;48m")
                print()
                wait(.25)
                print("You put the dagger away and head back to the atrium.")
                print()
                wait()
                dagger = 1
                treefloor2()
                break
    if dagger == 1:
        print()
        print("You walk into the room and immediately you're hit with the smell animal insides.")
        print("A few men are stationed at tables skinning animals.")
        print("Others are harvesting meat from previously skinned creatures.")
        print()
        print("The men are far too busy to be bothered by your presence.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
            if containsAny(ans, leave):
                print()
                print("You leave the room and go back to the atrium.")
                print()
                treefloor2()
                break
            else:
                print()
                print("There isn't anything here left for you to do.")
                print()


def treearmory():
    global armory
    if armory == 0:
        print()
        print("You enter a room that is full of assorted weaponry.")
        print("Along the walls are weapon racks housing bows, swords, daggers, and other weapons.")
        print("All of them look custom made for the Sylvian people.")
        print("You don't get very far before you are stopped by a guard.")
        print()
        print(""" "Stop right there! This area is restricted to Sylvian hunters only." """)
        print(""" "By those pointed ears and the robes you're wearing I can see that you are Kaefden." """)
        print()
        print("You can either turn back or explain yourself to the guard.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            att = ["KILL", "ATTACK", "FIGHT"]
            ex = ["EXPLAIN", "TALK"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
            fire = ["INFLAME", "IN-FLAME"]
            if containsAny(ans, att):
                print()
                print("Attacking an ally makes you no better than the Barbarians.")
                print()
            elif containsAny(ans, fire):
                if fireball == 0:
                    print("You don't know that spell.")
                    print()
                if fireball == 1:
                    print()
                    print("Attacking an ally makes you no better than the Barbarians.")
                    print("Besides, you're inside a giant tree.")
                    print("Not the best idea.")
                    print()
            elif containsAny(ans, leave):
                print()
                print("Not wanting to cause any trouble, you return to the atrium.")
                print()
                treefloor2()
                break
            elif containsAny(ans, ex):
                print()
                print("You explain to the guard that you were simply exploring.")
                print(
                    "You tell her that you're trying to get to Nacastrum and that you need something that is kept "
                    "here to do it.")
                print()
                print("The guard seems puzzled by your story.")
                print("She processes what you've told her for a moment and then responds.")
                print()
                wait(2)
                print(""" "All that we keep here are bows and blades reserved for Sylvians." """)
                print(""" "Whatever you're looking for, you'll have to look elsewhere." """)
                print(""" "Now off with you!" """)
                print()
                print("You return to the second floor's atrium.")
                print()
                armory = 1
                treefloor2()
                break
    if armory == 1:
        print()
        print("You enter a room that is full of assorted weaponry.")
        print("Along the walls are weapon racks housing bows, swords, daggers, and other weapons.")
        print("All of them look custom made for the Sylvians.")
        print("You don't get very far before you are stopped by a guard.")
        print()
        wait()
        print(""" "Kaefden! Didn't I tell you that you're not allowed here?" """)
        print(""" "Off with you!" """)
        print()
        print("You return to the second floor's atrium.")
        print()
        treefloor2()


def treefloor3():
    print()
    print("To the LEFT of you is what looks like some kind of church.")
    print("To the RIGHT is a library.")
    print("If you continue UP the stairs you will be on the fourth and final floor of the tree.")
    print("Going DOWN the stairs leads you to the second floor of the tree.")
    print()
    while True:
        d = ["DOWN", "DOWNSTAIRS"]
        up = ["UP", "UPSTAIRS"]
        left = ["LEFT", "CHURCH"]
        right = ["RIGHT", "LIBRARY"]
        ans = userinput("Where would you like to go?")
        if containsAny(ans, left):
            print()
            treechurch()
            break
        if containsAny(ans, right):
            print()
            treelibrary()
            break
        if containsAny(ans, up):
            print()
            print()
            print("You head up the stairs another time and find yourself in a large open room.")
            print("This area is unlike the atria of the previous floors.")
            print("There are no other rooms besides the one you are in.")
            print("There are no people to cause commotion.")
            print("Not even a guard is in sight.")
            print("After a few moments of looking around, you notice a large symbol on the ground.")
            wait(2)
            treefloor4()
            break
        if containsAny(ans, d):
            print()
            treefloor2()
            break


def treechurch():
    print("You head in to what appears to be a place of worship.")
    print("At the front of the room is a statue.")
    print()
    print("You notice a few of the civilians are approaching and praying to the statue.")
    print("It seems that it is some kind of shrine.")
    print()
    print("As you look around the room, you spot a woman in clothing different to the rest.")
    print("She is wearing an elk's head as a sort of hat and is draped in strange animal skins.")
    print("It looks like she is attending to the people praying to the shrine.")
    print()
    while True:
        talk = ["TALK", "APPROACH", "ASK", "SPEAK"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
        shrine = ["SHRINE", "STATUE"]
        ans = userinput("What would you like to do?")
        if containsAny(ans, leave):
            print()
            print("You return to the third floor atrium.")
            print()
            treefloor3()
            break
        elif containsAny(ans, shrine):
            print()
            print("You decide to take a look at the shrine.")
            print()
            treechurchshrine()
            break
        elif containsAny(ans, talk):
            print()
            print(
                "You approach the strangely dressed woman and wait for her to finish attending to a civilian "
                "before speaking to her.")
            print()
            print(
                """ "Greetings, mage. All are welcome in the Church of Suformin, God of the Hunt. What can I do
                for you?" """)
            treechurchwoman()
            break
        else:
            print()
            print()
            print()


def treechurchwoman():
    while True:
        global dagger
        print()
        dag = ["DAGGER", "KNIFE"]
        god = ["SUFORMIN", "GOD"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
        mean = ["MEANING OF LIFE"]
        ans = userinput("You can ask about Suformin or ask about the dagger.")
        if containsAny(ans, god):
            print()
            print(""" "Ah! Suformin is the God of the Hunt, our mistress of the kill." """)
            print(""" "We owe our lives to her." """)
            print(""" "When we first left Aylova in search of a new home, it was Suformin who showed us
            this place." """)
            print(""" "She is an example of not only strength of the body, but strength of the mind." """)
            print(""" "All of us who live in Silvarium believe that she first lead us here for a reason." """)
            print(""" "Those who left turned their backs on her and will face her wrath in due time." """)
            print()
            print(""" "Are there any other questions you have?" """)
            print()
        elif containsAny(ans, dag):
            if dagger == 0:
                print()
                print(""" "If by 'dagger' you mean the one Suformin is holding," """)
                print(""" "That blade was a knife she used to hunt and slay her enemies." """)
                print(""" "It is said that after she left our mortal plain, she would send her dagger to those she
                            deemed fit to wield it." """)
                print(""" "No one knows where the dagger is kept or where it was last seen, but that is not
                         of our concern." """)
                print(""" "Only the one who is supposed to find it will find it." """)
                print()
                print(""" "Is there anything else I can answer for you?" """)
                print()
            if dagger == 1:
                print()
                print(""" "What is this?" """)
                print(""" "Where did you find this?" """)
                print(""" "This is Suformin's dagger!" """)
                print(""" "Suformin would not entrust a mortal with her dagger lightly, especially a mage." """)
                print(""" "If you weren't meant to have her dagger, you would not have it now." """)
                print(""" "Take great care of it. I suspect great things to come from you." """)
                print()
                print(""" "Before you leave, is there anything else I can answer for you?" """)
                print()
        elif containsAny(ans, mean):
            print()
            print(""" "42." """)
            print()
        elif containsAny(ans, leave):
            print()
            treefloor3()
            break
        else:
            print()
            print(""" "I don't understand the question." """)
            print()


def treechurchshrine():
    print()
    print("The statue is of a woman.")
    print("She's wearing hide clothing and is holding a dagger.")
    print("She also has a bow on her back.")
    print()
    print()
    global dagger
    if dagger == 0:
        print()
        print("With nothing else of interest, you return to the entrance of the church.")
        print()
        treechurch()
    if dagger == 1:
        print("Upon closer inspection, you notice that the dagger the statue has resembles the one you have.")
        print("Perhaps someone can provide more information.")
        print()
        print("You return to the entrance of the church.")
        print()
        treechurch()


def treelibrary():
    print()
    print("The library walls are absolutely covered in bookcases containing stacks and stacks of old texts.")
    print("In the center of the room are a few tables with civilians sat at them reading.")
    print("Before you are able to get lost in the knowledge stored here, you are greeted by a man.")
    print("He is donned in an exquisite fox coat.")
    print("It appears that he is the head of the library.")
    print()
    wait(2)
    print(""" "Welcome, Mage. I heard that we had a visitor here." """)
    print(""" "I pride myself as the number one hoarder of knowledge in this city." """)
    print(""" "I expect you to treat all of the texts here with your utmost respect." """)
    print(""" "Should I find you mistreating any of the books here, I will have you fed to angry, starving wolves." """)
    print(""" "Now that you know how things work here, what can I do for you?" """)
    print()
    treelibrarian()


def treelibrarian():
    while True:
        print()
        ex = ["EXPLAIN", "TASK"]
        mag = ["MAGE", "ASK"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
        ans = userinput("You can explain your task, ask about the mages, or leave.")
        if containsAny(ans, leave):
            print()
            print("You turn around and head back to the third floor atrium.")
            print()
            treefloor3()
            break
        elif containsAny(ans, ex):
            print()
            print("You take a moment to explain your task to the keeper of the library.")
            print("At first he seems skeptical, but indulges you.")
            print()
            print(""" "So you seek the knowledge those Elders sealed away." """)
            print(""" "I never liked that they would keep a secret from the baron of knowledge." """)
            print(""" "Unfortunately for you, I have no idea how to get what ever lies behind the seal." """)
            print(
                """ "The only thing I can tell you is that the seal is the same one used by the mages of old, but surely you know that." """)
            print()
            print(""" "Now, if you have no further questions, I need to return to my duties." """)
            print()
        elif containsAny(ans, mag):
            print()
            print(""" "Ah, the mage. A proud and knowledgeable people." """)
            print(""" "As you already know, the Mage live up in their floating city of Nacastrum." """)
            print(""" "Or at least they used to." """)
            print()
            wait()
            print(
                """ "They lived there up until your king, Vashirr, saved them from the barbarians by banishing them from the city." """)
            print(""" "I've always been jealous of the Mage, keepers of the most advanced magic ever known." """)
            print(""" "I was excited to hear that they were going to give us a spell as a sort of peace offering." """)
            print(""" "And then those damned Elders sealed it up and saved it for themselves." """)
            print()
            wait(2)
            print(
                """ "They say it was to keep everyone equal, but I think it was just to keep them above all of us." """)
            print(
                """ "Over the years, I've heard rumors that the Elders themselves have been unable to open the seal." """)
            print(""" "It seems that their blood isn't worthy!" """)
            print()
            print(""" "But you've heard me ramble on for far too long." """)
            print(""" "If you need nothing else, I will return to my duties." """)
            print()
            wait(2)
        else:
            print()


def treefloor4():
    print()
    print(
        "A large circle covers the ground with another, slightly smaller circle inside, forming what looks like a target.")
    print("Two strange daggers cross blades in the center.")
    print("Blood drips from the daggers with a distinct redness.")
    print("The symbol seems familiar, but you can't quite place its significance.")
    print()
    if blood == 0:
        treeseal()
    if blood == 1:
        bloodseal()


def treeseal():
    global deathcount
    global lev
    global fireball
    while True:
        ans = userinput("What would you like to do?")
        leave = ["LEAVE", "BACK", "EXIT", "DOWN", "NOTHING"]
        flame = ["INFLAME", "IN-FLAME"]
        float = ["LEVITATE"]
        cut = ["CUT", "BLOOD"]
        dag = ["DAGGER", "SUFORMIN"]
        sword = ["SWORD"]
        if containsAny(ans, leave):
            print()
            print("You return back to the third floor.")
            print()
            treefloor3()
        elif containsAny(ans, float):
            if lev == 0:
                print()
                print("You don't know that spell.")
            if lev == 1:
                print()
                print("There is no reason to use that here.")
                print()
        elif containsAny(ans, flame):
            if fireball == 0:
                print()
                print("You don't know that spell.")
                print()
            if fireball == 1:
                print()
                print("It probably isn't a good idea to cast a fire spell in a flammable room.")
                print()
        elif containsAny(ans, sword) and containsAny(ans, cut):
            while True:
                print()
                ans = userinput("Where do you want to cut yourself with the sword?")
                hand = ["HAND"]
                leg = ["LEG"]
                neck = ["NECK"]
                back = ["BACK", "LEAVE", "EXIT", "RETURN"]
                if containsAny(ans, back):
                    treefloor4()
                    break
                elif containsAny(ans, hand):
                    print()
                    print("You carefully cut the palm of your hand with the longsword.")
                    print("Blood slowly drips down onto the ground below you.")
                    print()
                    print("Nothing happens.")
                    print()
                    treefloor4()
                    break
                elif containsAny(ans, leg):
                    print()
                    print("You cut your leg and watch as blood drips down onto the floor.")
                    print()
                    print("Nothing happens.")
                    print()
                    treefloor4()
                    break
                elif containsAny(ans, neck):
                    print()
                    ans = userinput("Are you sure you want to do that?")
                    print()
                    yes = ["YES", "Y"]
                    no = ["NO", "N"]
                    if containsAny(ans, yes):
                        print()
                        print("You cut your neck open and watch your blood spew onto the ground.")
                        print("It's too late before you realize that was a horrible idea.")
                        print("Your vision fades to black and darkness consumes you....")
                        print()
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    elif containsAny(ans, no):
                        print()
                        treefloor4()
                        break
                    else:
                        print("Yes or no?")
                        print()
                else:
                    print()
                    print("Hand, neck, or leg?")
                    print()
        elif containsAny(ans, dag) and containsAny(ans, cut):
            while True:
                print()
                ans = userinput("Where do you want to cut yourself with the dagger?")
                hand = ["HAND"]
                leg = ["LEG"]
                neck = ["NECK"]
                back = ["BACK", "LEAVE", "EXIT", "RETURN"]
                if containsAny(ans, back):
                    treefloor4()
                    break
                elif containsAny(ans, hand):
                    print()
                    print("You carefully cut the palm of your hand and watch as blood drips onto the floor.")
                    print()
                    bloodseal()
                    break
                elif containsAny(ans, leg):
                    print()
                    print("You cut your leg and watch as blood drips down onto the floor.")
                    print()
                    bloodseal()
                    break
                elif containsAny(ans, neck):
                    print()
                    ans = userinput("Are you sure you want to do that?")
                    yes = ["YES", "Y"]
                    no = ["NO", "N"]
                    if containsAny(ans, yes):
                        print()
                        print("You cut your neck open and watch your blood spew onto the ground.")
                        print("It's too late before you realize that was a horrible idea.")
                        print("Your vision fades to black and darkness consumes you....")
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    elif containsAny(ans, no):
                        print()
                        print("Good choice.")
                        treefloor4()
                        break
                    else:
                        print("Yes or no?")
                        print()

        elif containsAny(ans, cut):
            print()
            ans = userinput("Cut yourself with what?")
            sword = ["SWORD"]
            dagger = ["DAGGER", "SUFORMIN"]
            if containsAny(ans, sword):
                print()
                ans = userinput("Where do you want to cut yourself?")
                hand = ["HAND"]
                leg = ["LEG"]
                neck = ["NECK"]
                back = ["BACK", "LEAVE", "EXIT", "RETURN"]
                if containsAny(ans, back):
                    treefloor4()
                    break
                elif containsAny(ans, hand):
                    print()
                    print("You carefully cut the palm of your hand with the longsword.")
                    print("Blood slowly drips down onto the ground below you.")
                    print()
                    print("Nothing happens.")
                    print()
                    treefloor4()
                    break
                elif containsAny(ans, leg):
                    print()
                    print("You cut your leg and watch as blood drips down onto the floor.")
                    print()
                    print("Nothing happens.")
                    print()
                    treefloor4()
                    break
                elif containsAny(ans, neck):
                    print()
                    ans = userinput("Are you sure you want to do that?")
                    print()
                    yes = ["YES", "Y"]
                    no = ["NO", "N"]
                    if containsAny(ans, yes):
                        print()
                        print("You cut your neck open and watch your blood spew onto the ground.")
                        print("It's too late before you realize that was a horrible idea.")
                        print("Your vision fades to black and darkness consumes you....")
                        print()
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    elif containsAny(ans, no):
                        print()
                        treefloor4()
                        break
                    else:
                        print("Yes or no?")
                        print()
                else:
                    print()
                    print("Hand, neck, or leg?")
                    print()
            elif containsAny(ans, dagger):
                print()
                ans = userinput("Where do you want to cut yourself?")
                hand = ["HAND"]
                leg = ["LEG"]
                neck = ["NECK"]
                back = ["BACK", "LEAVE", "EXIT", "RETURN"]
                if containsAny(ans, back):
                    treefloor4()
                    break
                elif containsAny(ans, hand):
                    print()
                    print("You carefully cut the palm of your hand and watch as blood drips onto the floor.")
                    print()
                    bloodseal()
                    break
                elif containsAny(ans, leg):
                    print()
                    print("You cut your leg and watch as blood drips down onto the floor.")
                    print()
                    bloodseal()
                    break
                elif containsAny(ans, neck):
                    print()
                    ans = userinput("Are you sure you want to do that?")
                    yes = ["YES", "Y"]
                    no = ["NO", "N"]
                    if containsAny(ans, yes):
                        print()
                        print("You cut your neck open and watch your blood spew onto the ground.")
                        print("It's too late before you realize that was a horrible idea.")
                        print("Your vision fades to black and darkness consumes you....")
                        print()
                        print("\033[1;31;48mYou have died.")
                        print("\033[0;26;48m")
                        deathcount += 1
                        print()
                        textspeed()
                        break
                    elif containsAny(ans, no):
                        print()
                    else:
                        print()
                        print("You have died.")
                        print()
                else:
                    print()
                    print("Hand, neck, or leg?")
                    print()
        else:
            print()


def bloodseal():
    global blood
    if blood == 0:
        print()
        print("As your blood falls to the floor, a low rumbling escalates into a loud roar.")
        print("The dagger you were holding begins to glow and your blood seeps into the blade.")
        print("The blood that fell to the ground runs into the circles that surround the crossed blades.")
        print("It begins to flow towards the farthest wall.")
        print()
        wait()
        print("As your blood approaches the wall, you notice etchings on it create an arch.")
        print("Your blood continues to travel up the arch and begins to emit the same blue glow as the dagger.")
        print()
        print("The arch that is etched into the wall begins to slide back, pulling the tree wall with it.")
        print("Moments later a hidden entrance reveals itself!")
        print()
        wait()
        bloodsealspell()
    if blood == 1:
        print()
        bloodsealspell()


def bloodsealspell():
    global geo
    print()
    print("You head into the newly discovered room.")
    print("It is extremely dark besides a faint blue glow.")
    print()
    print("At the center of the room is a pedestal.")
    if fireball == 1:
        print("The walls of the room are etched in the same runes you saw in the caves.")
        print("The runes are the source of the glow within the room.")
        print()
        wait(.5)
        print("You approach the pedestal and find a tome made completely of stone.")
        print("The stone tome is etched in the runes that paint the walls of this chamber.")
        print(
            "You draw closer and closer to the book and just as you're within arms length the book throws itself open.")
        print()
        wait()
        print("Your vision fades to the same courtyard you saw when you learned the spell Inflame.")
        print("You see mages moving the very bones of the earth with nothing but their mind.")
        print("You feel an incredible pressure in your mind and body.")
        print("The force of gravity tugs at your very soul and you feel as though your weight has increased ten-fold "
              "for a moment.")
        print("Everything in your body feels as hard as rock.")
        print("This soon passes and you look to the stone book.")
        print()
        print("Without thinking, you extend your arm to it and watch as the book crumbles into pebbles and "
              "flies to the back wall.")
        print()
        wait(2)
        print("\033[1;32;48mYou received Stonebend!")
        print("\033[0;26;48m")
        print()
        wait(2)
        print("You exit the spell's chamber and leave the Tree.")
        print()
        geo = 1
        mforest()
    if fireball == 0:
        print("The walls of the room are etched in strange runes that you don't recognize.")
        print("The runes are the source of the glow within the room.")
        print()
        wait(.5)
        print("You approach the pedestal and find a tome made completely of stone.")
        print("The stone tome is etched in the runes that paint the walls of this chamber.")
        print(
            "You draw closer and closer to the book and just as you're within arms length the book throws itself open.")
        print()
        wait()
        print("Your vision fades to a strange, yet familiar, courtyard.")
        print("You see mages moving the very bones of the earth with nothing but their mind.")
        print("You feel an incredible pressure in your mind and body.")
        print("The force of gravity tugs at your very soul and you feel as though your weight has increased ten-fold "
              "for a moment.")
        print("Everything in your body feels as hard as rock.")
        print("This soon passes and you look to the stone book.")
        print("Without thinking, you extend your arm to it and watch as the book crumbles into pebbles and "
              "flies to the back wall.")
        print()
        wait(2)
        print("\033[1;32;48mYou received Stonebend!")
        print("\033[0;26;48m")
        print()
        wait(2)
        print("You exit the spell's chamber and leave Sylvarum.")
        geo = 1
        mforest()


# To Nacastrum!


def westernroad():
    if escort == 0:
        print("To the NORTH, the dirt road turns to pavement. Something inside you tells you NORTH is extremely "
              "dangerous.")
        print("EAST takes you back the way you came.")
        print("To your WEST, the dirt path continues.")
        print()
        while True:
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "EAST"]
            north = ["NORTH"]
            west = ["WEST"]
            ans = userinput("Which way would you like to investigate?")
            if containsAny(ans, west):
                print()
                shoreside()
                break
            if containsAny(ans, north):
                print()
                print("You decide to travel north.")
                print("Going this way leads to inevitable danger.")
                print("You can't quite remember where it leads.")
                print("But you know one thing for sure.")
                print("You will never be the same again.")
                print()
                wait()
                roadtonecasturm()
                break
            if containsAny(ans, leave):
                print()
                print("You venture back to the split-path.")
                print()
                splitpath()
                break
    if escort == 1:
        print()
        print("You take the Old Mage west.")
        print()
        print("To the NORTH is the path to Nacastrum.")
        print("EAST takes you back the way you came.")
        print()
        while True:
            ans = userinput("Which way would you like to investigate?")
            north = ["NORTH"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "EAST"]
            if containsAny(ans, north):
                print()
                print("You guide the Old Mage on the path to Nacastrum.")
                print()
                teleporter()
                break
            elif containsAny(ans, leave):
                print()
                splitpath()
                break


def roadtonecasturm():
    global roadfir
    global roadlev
    global roadgeo
    if roadfir == 0 or roadfir == 1:
        roadblockfireball()
    if roadfir == 2:
        if roadgeo == 0:
            roadblockstone()
        if roadgeo == 1:
            if roadlev == 0:
                roadblocklev()
            if roadlev == 1:
                teleporter()


def roadblockfireball():
    global roadfir
    if roadfir == 0:
        print()
        print("Everything seems strangely quiet.")
        print()
        print("You pause for a moment and get a strange feeling that you're being watched.")
        print("You look to your surroundings and only see trees and shrubbery.")
        print()
        print("Suddenly, a large mob of Agromanian erupt from the tree line!")
        print("It appears that they have been robbing those who travel down this road!")
        print("Luckily, you aren't caught off-guard and have a moment to react.")
        print()
        wait(1.5)
        roadattack()
    if roadfir == 1:
        print("You recall that last time you were here you got attacked by Agromanian.")
        print("This time you'll have to be prepared or die.")
        print()
        print("You continue on a little further and, sure enough, the Agromanian rush at you from the tree line.")
        print()
        roadattack()
    if roadfir == 2:
        roadblocklev()


def roadblockstone():
    global geo
    global sword
    global fireball
    global lev
    global roadgeo
    print()
    print("As you continue on, the grass along the path comes to an abrupt end.")
    print("Monolithic stone spires block your path and reach far into the sky.")
    print("You can tell the spires are unnatural because of the surrounding trees and foliage.")
    print()
    while True:
        ans = userinput("What would you like to do?")
        float = ["LEVITATE", "LEV"]
        fire = ["INFLAME", "IN-FLAME"]
        swor = ["SWORD", "STAB"]
        stone = ["STONEBEND", "STONE-BEND"]
        leave = ["LEAVE", "BACK", "EXIT", "SOUTH", "RETURN", "OUTSIDE"]
        if containsAny(ans, float):
            if lev == 1:
                print()
                print("The stone spires are far too tall for you to Levitate safely over.")
                print()
            if lev == 0:
                print()
                print("You don't know that spell.")
                print()
        elif containsAny(ans, fire):
            if fireball == 1:
                print()
                print("You take a deep breath and prepare to cast Inflame.")
                print(
                    "You sling your arm forward with all the force you have and watch as fire spews out of your hand.")
                print()
                print("It appears as though the fire has had no affect on the stone spires.")
                print()
            if fireball == 0:
                print()
                print("You don't know that spell.")
                print()
        elif containsAny(ans, swor):
            if sword == 1:
                print()
                print("Surely you can think of something better.")
                print("You can't just stab your problems away.")
                print()
            if sword == 0:
                print()
                print("You don't have a sword.")
                print()
        elif containsAny(ans, stone):
            if geo == 1:
                print()
                print("You close your eyes and envision the stone spires shattered.")
                print("You take a deep breath and extend your arms out in front of you.")
                print()
                print("Moments later you hear a rumbling coming in the direction of the spire.")
                print("You open your eyes and watch as a hole is punched straight through the stone.")
                print("Bits of rock fly in all directions and you're left with a clear path to continue through!")
                print()
                ans = userinput("Would you like to continue on?")
                yes = ["YES", "Y"]
                no = ["NO", "N"]
                if containsAny(ans, yes):
                    print()
                    print("You decide to continue on through the tunnel you've created.")
                    print()
                    roadblocklev()
                    break
                if containsAny(ans, no):
                    print()
                    print("You head back to where you came from.")
                    print()
                    westernroad()
                    break
        elif containsAny(ans, leave):
            print()
            print("You head back to where you came from.")
            print()
            westernroad()
            break
        else:
            print()
            print("I don't understand that.")
            print()


def roadattack():
    global roadfir
    global lev
    global sword
    global geo
    global fireball
    global dagger
    global deathcount
    if roadfir == 0:
        while True:
            ans = userinput("What do you do?")
            float = ["LEVITATE", "LEV"]
            fire = ["INFLAME", "IN-FLAME"]
            swor = ["SWORD", "STAB"]
            stone = ["STONEBEND", "STONE-BEND"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "RUN", "ESCAPE"]
            dag = ["DAGGER", "SUFORMIN"]
            if containsAny(ans, float):
                if lev == 1:
                    print()
                    print("You quickly cast Levitate and slowly drift into the air.")
                    print("Unfortunately, one of the Agromanian grabs a hold of your leg.")
                    print()
                    print("You're pulled to the ground before you can get far enough away from them to escape.")
                    print("You're quickly being surrounded, but you're managing to keep them at bay.")
                    print()
                    print("You need to think quickly before you are killed.")
                    print()
                    roadfir = 1
                    roadattack()
                    break
                if lev == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, swor):
                if sword == 1:
                    print()
                    print("You draw your sword and prepare to fight.")
                    print("The Agromanian draw closer and closer.")
                    print("You take a few of them out, but more of them keep coming.")
                    print("You're no master swordsman, so you won't be able to hold them much longer.")
                    print()
                    print("You need to think quickly before you are killed.")
                    print()
                    roadfir = 1
                    roadattack()
                    break
                if sword == 0:
                    print()
                    print("You don't have a sword.")
                    print()
            elif containsAny(ans, fire):
                if fireball == 1:
                    print()
                    print("You quickly direct your palm towards the Agromanians while casting Inflame.")
                    print("Heat rages from your veins and fire spews forth.")
                    print("A majority of the Agromanian are burned to a crisp and the survivors run in terror.")
                    print()
                    print("Teaches them to prey on a Mage.")
                    print()
                    wait()
                    roadfir = 2
                    ans = userinput("Would you like to continue down the path?")
                    yes = ["YES", "Y", "NORTH"]
                    no = ["NO", "N", "SOUTH"]
                    if containsAny(ans, yes):
                        print()
                        print("You decide to continue on.")
                        print()
                        roadblockstone()
                        break
                    if containsAny(ans, no):
                        print()
                        print("You decide you will come back later and return back from where you came from.")
                        print()
                        westernroad()
                        break
                if fireball == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, stone):
                if geo == 1:
                    print()
                    print("You look around and cannot find any rock or stone to pull from with Stonebend.")
                    print("The only rock available is the pavement and it won't be enough to stop the Agromanian.")
                    print()
                    print("You need to think quickly before you are killed.")
                    print()
                    roadfir = 1
                    roadattack()
                    break
                if geo == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, dag):
                if dagger == 1:
                    print()
                    print("You draw Suformin's Dagger and prepare to fight for your life.")
                    print()
                    print("With all your might, and maybe even a little help from Suformin herself, you slay a "
                          "few of the Agromanian.")
                    print("Unfortunately, you're unable to kill the rest of them.")
                    print("The Agromanian are quickly over taking you.")
                    print()
                    print("You need to think quickly before you are killed.")
                    print()
                    roadfir = 1
                    roadattack()
                    break
                if dagger == 0:
                    print()
                    print("You don't have a dagger.")
                    print()
            elif containsAny(ans, leave):
                print()
                print("You turn and run away from the Agromanian.")
                print("A few chase after you, but their armor makes them too slow to keep up with you.")
                print("You narrowly manage to escape and head back to where you came from.")
                print()
                print("While you escaped this time, you know that your luck won't be the same next time around.")
                roadfir = 1
                westernroad()
                break
    if roadfir == 1:
        while True:
            ans = userinput("What do you do?")
            print()
            l = ["LEVITATE", "LEV"]
            fire = ["INFLAME", "IN-FLAME"]
            swor = ["SWORD", "STAB"]
            stone = ["STONEBEND", "STONE-BEND"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "RUN", "ESCAPE"]
            dag = ["DAGGER", "SUFORMIN"]
            if containsAny(ans, l):
                if lev == 1:
                    print()
                    print("You cast Levitate, but the Agromanian are far too close for you to escape.")
                    print("They drag you back down to the ground.")
                    print("You are beaten and stabbed to death.")
                    print()
                    print("\033[1;31;48mYou have died.")
                    print("\033[0;26;48m")
                    deathcount += 1
                    print()
                    textspeed()
                    break
                if lev == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, swor):
                if sword == 1:
                    print()
                    print("You draw your sword and prepare to fight.")
                    print("Unfortunately, no matter how hard you try, you're overwhelmed by the sheer number of "
                          "Agromanian.")
                    print()
                    print("Your sword arm is chopped off, leaving you defenseless.")
                    print("You're at the mercy of these scum.")
                    print("Sadly, they don't have a reputation for keeping their captives alive.")
                    print()
                    print("Moments later, you are slain.")
                    print()
                    print()
                    print("\033[1;31;48mYou have died.")
                    print("\033[0;26;48m")
                    deathcount += 1
                    print()
                    textspeed()
                    break
                if sword == 0:
                    print()
                    print("You don't have a sword.")
                    print()
            elif containsAny(ans, fire):
                if fireball == 1:
                    print()
                    print("You quickly direct your palm towards the Agromanians while casting Inflame.")
                    print("Heat rages from your veins and fire spews forth.")
                    print("A majority of the Agromanian are burned to a crisp and the survivors run in terror.")
                    print()
                    print("Teaches them to prey on a Mage.")
                    print()
                    roadfir = 2
                    while True:
                        ans = userinput("Would you like to continue down the path?")
                        yes = ["YES", "Y"]
                        no = ["NO", "N"]
                        if containsAny(ans, yes):
                            print()
                            print("You decide to continue on.")
                            print()
                            roadblockstone()
                            break
                        if containsAny(ans, no):
                            print()
                            print("You decide you will come back later and return back from where you came from.")
                            print()
                            westernroad()
                            break
                if fireball == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, stone):
                if geo == 1:
                    print()
                    print("You look around and cannot find any rock or stone to pull from with Stonebend.")
                    print("The only rock available is the pavement and it won't be enough to stop the Agromanian.")
                    print()
                    print(
                        "Unfortunately, you don't have time to think of another option before you are surrounded.")
                    print()
                    print("Moments later, you are beaten and stabbed to death.")
                    print()
                    print()
                    print("\033[1;31;48mYou have died.")
                    print("\033[0;26;48m")
                    deathcount += 1
                    print()
                    textspeed()
                    break
                if geo == 0:
                    print()
                    print("You don't know that spell.")
                    print()
            elif containsAny(ans, dag):
                if dagger == 1:
                    print()
                    print("You draw Suformin's Dagger and prepare to fight for your life.")
                    print()
                    print("With all your might, and maybe even a little help from Suformin herself, "
                          "you slay a few of the Agromanian.")
                    print("Unfortunately, you're unable to kill the rest of them.")
                    print("The Agromanian quickly over run you and you killed.")
                    print()
                    print()
                    print("\033[1;31;48mYou have died.")
                    print("\033[0;26;48m")
                    deathcount += 1
                    print()
                    textspeed()
                    break
                if dagger == 0:
                    print()
                    print("You don't have a dagger.")
                    print()
            elif containsAny(ans, leave):
                print()
                print("The Agromanian are far too close for you to escape.")
                print("You must react before you are killed.")
                print()


def roadblocklev():
    print()
    print("As you continue on, trees appear on both sides of you.")
    print("Things begin to look awfully familiar.")
    print("You begin to hear the distant roar of water.")
    print("Something tells you that you've been here before.")
    print()
    wait(2)
    print("Ahead you notice the beginnings of a bridge.")
    print("As you draw in closer, you see that the bridge disappears deep into the chasm.")
    print("The end of the bridge is hidden by the rapid water.")
    print()
    wait()
    print("This is the very same bridge that held the entrance to the mountain...")
    print(""" "What is it doing here?" + " you think to yourself." """)
    print("You gaze around at the scenery in awe at how familiar all is.")
    print()
    print("You gaze far into the chasm and notice something is off.")
    print("The water, although roaring, is still.")
    print("No wind appears to be present either.")
    print()
    wait(2)
    print("In fact, the trees are also completely motionless.")
    print("Wait... The trees!")
    print("Some are coming out of the motionless water further down the stream.")
    print("As you lock in to your surroundings, things begin to become blurry and not well defined.")
    print()
    wait()
    print("Much like a memory.")
    print()
    while True:
        ans = input("What do you do?")
        ans = ans.upper()
        look = ["LOOK", "INVESTIGATE", "SEARCH"]
        l = ["LEVITATE", "LEV"]
        fire = ["INFLAME", "IN-FLAME"]
        swor = ["SWORD", "STAB"]
        stone = ["STONEBEND", "STONE-BEND"]
        leave = ["LEAVE", "BACK", "EXIT", "RETURN", "SOUTH"]
        dag = ["DAGGER", "SUFORMIN"]
        swim = ["SWIM", "JUMP", "DIVE"]
        if containsAny(ans, look):
            print()
            print("As you continue to look around, parts become blurrier and even more undefined.")
            print(""" "Am I dreaming?" + " you think to yourself. " """)
            print("Something draws you towards the water.")
            print()
        elif containsAny(ans, l):
            print()
            print("Just like before, from your memories, you Levitate safely across the broken bridge.")
            print("You feel... unfinished.")
            print("However, you can continue on the blurry path.")
            print()
            while True:
                ans = input("Do you wish to continue or Levitate back across the path?")
                ans = ans.upper()
                con = ["CONTINUE", "FORWARD"]
                leave = ["LEAVE", "BACK", "EXIT", "RETURN", "LEVITATE"]
                if containsAny(ans, con):
                    print()
                    print("You continue on.")
                    print("The path before you begins to become indistinguishable.")
                    print("Around you all color disappears.")
                    print("Ahead of you, is pure, absolute blackness.")
                    print()
                    print("You turn to back to see even more blackness.")
                    print("In the distance is a faint glow of light.")
                    print("You hear a static that you can make out as the roar of the chasm, coming from the glow.")
                    print()
                    print("You decide going back towards it is the best solution.")
                    print("The glow grows bigger and bigger until you are back inside.")
                    print("You Levitate back across the chasm.")
                    print()
                    print("You will have to find another way.")
                    print()
                    break
                if containsAny(ans, leave):
                    print("You can't shake the feeling that something is very wrong.")
                    print("You decide to Levitate back across the chasm.")
                    print()
                    print()
                    break
        elif containsAny(ans, fire):
            print()
            print("Care will prevent 9 out of 10 forest fires.")
            print("In other words... No. Stop. Try something else.")
            print()
        elif containsAny(ans, swim):
            print()
            print("You take a deep breath and jump into the water.")
            print("To your surprise, you stop and find yourself standing on what feels like solid ground.")
            print("Quickly your vision changes from what was a chasm to the stone pathway you were following before.")
            print()
            wait()
            print("In front of you lies an enormous shadow.")
            print("You can't believe your eyes.")
            print("You slowly look to the skies and see it.")
            print()
            print("Nacastrum, Floating city of the Mage.")
            print()
            wait(2)
            print("Vague memories return to you of Nacastrum.")
            print("Without a second to waste, you rush onward to what lies ahead.")
            print()
            teleporter()
            break
        elif containsAny(ans, leave):
            print()
            westernroad()


def teleporter():
    global lady
    global lock
    if lady == 0:
        print()
        print("You follow the path to its end and find a stone staircase of but a few steps that extend meters long.")
        print("At the top of the staircase is a huge round platform.")
        print("In the center is a large, hollow circle made of silver that is perpendicular to the ground.")
        print()
        wait()
        print("The runes you've encountered numerous times cover the edge of the circle as well as the ground.")
        print("You walk to the base of the circle and notice a hole in the stone platform.")
        print("The hole is a few inches in diameter, but you can't tell how deep it is.")
        print()
        wait(1.5)
        print("You feel a familiar energy eminating from the platform.")
        print("You're completely stumped on what to do from here.")
        print("You know that this monument has some significance, but you can't quite recall what it is.")
        print()
        wait()
        print("Suddenly, you remember the Old Mage in Oceandale.")
        print("Perhaps she can give some insight.")
        print()
        print("You head back to the western path.")
        print()
        wait(.5)
        lady = 1
        lock = 0
        westernroad()
    if lady == 1:
        print()
        print("You arrive with the Old Mage at the Ring of Malkos under Nacastrum.")
        print("She walks to the center of the monument and raises the staff into the air.")
        print("With one quick movement, she slams the staff into the port in the platform.")
        print()
        wait()
        print(
            "Immediately a loud rumbling that could have been heard from all of Avasia erupts from the Ring of Malkos.")
        print("You're nearly blinded by a light that blasts from the ring.")
        print("The blinding light slowly shifts to a visage of a huge city.")
        print("Without a moment to spare, she pulls the staff from its port and rushes into the portal.")
        print()
        wait(2)
        print("You take a deep breath before charging into the portal yourself.")
        print()
        print("Instantly, hundreds of memories fill your mind.")
        print("Memories of the great city of Nacastrum.")
        print("Memories of practicing spells in the courtyards.")
        print("All of the thoughts you never knew existed all flood into your head at once.")
        print()
        wait(2)
        print("Everything that you didn't understand before suddenly makes sense.")
        print("A memory long forgotten is presented to you.")
        print()
        wait(.5)
        print("You remember getting a knock at your door at the age of eight.")
        print("When your parents opened the door, they were met by two men in blue robes.")
        print("They talked with your parents while you skulked in the background.")
        print("After a few minutes of talking, your mother came to you with tears in her eyes.")
        print("She kneeled down and stared at you.")
        print("She begins to talk to you in a wavering voice.")
        print()
        wait(2)
        print(""" "It's time for you to go." """)
        print(""" "You're going to join the Acadamey." """)
        print(""" "These men are here to take you there. You're going to learn all there is to know about magic." """)
        print(""" "Please, son, don't forget us." """)
        print()
        wait(1.5)
        print("The vision fades and you're presented with more memories.")
        print()
        print(
            "You remember when Vashirr became king when you were thirteen and how all of "
            "Nacastrum loved him and praised him.")
        print("You remember all the spells you were taught in school.")
        print("You remember your gradation from the Academy.")
        print("You remember your work as a teacher to the new young Mages.")
        print()
        wait(2)
        print("Suddenly, another vision presents itself.")
        print()
        wait(.125)
        print("You were the age of thirty-three at home in bed asleep.")
        print("You wake up startled by a loud humming and a blinding light piercing your window.")
        print("As you head down the stairs of your home, you put on a robe. The same robe you're wearing now.")
        print(
            "Immediately when you step outside, you spot guards rallying up citizens and bringing them towards Vashirr's castle.")
        print("You run to the guards to see what is going on and as you approach one catches you in his eyes.")
        print("He looks to another guard and points to you.")
        print("A few guards rush over and grab you.")
        print()
        wait(3)
        print("You try to explain that this must be a mistake as you've done nothing wrong, but the guards "
              "won't have any of it.")
        print()
        print("You and your fellow captives are brought to the main courtyard of Vashirr's castle.")
        print("There are hundreds of other mages in the courtyard.")
        print("At the front of the courtyard stands Vashirr, your king.")
        print()
        print("Next to him stands a man in barbaric armor. He is an Agromanian.")
        print("Behind Vashirr is a portal that seems to be transporting women and children along with Agromanian.")
        print()
        wait(.5)
        print("You recognize many of the faces being taken in to the portal.")
        print("Friends, students, and other citizens are being forcefully dragged in.")
        print()
        print("One of the faces sticks out more than the rest.")
        print("It's your mother.")
        print()
        wait(2)
        print("She's trying to resist and above all the commotion is a voice shouting to her.")
        print("The voice is your father.")
        print()
        print("Your father is being held back by the guards of Nacastrum, but manages to break free and "
              "run to your mother.")
        print("He makes only a few feet before he is blasted with magic by Vashirr.")
        print("His body lies lifeless on the ground and your mother screams in horror.")
        print()
        wait(2)
        print("You're unable to utter a single word as your father is murdered before your eyes and your "
              "mother is dragged in the portal.")
        print()
        print("Vashirr turns from your dead father and looks to the crowd.")
        print("He raises his hand and light pierces from his palm to the stars.")
        print(
            "You and the others can't help but look to the sky and watch as the light falls back to Nacastrum at you.")
        print()
        print("This is the last thing you remember before you woke up on the beach.")
        print("Your vision fades and you appear at the base of a Ring of Malkos in Nacastrum.")
        print()
        print("You fall to your knees and scream out in anger and pain.")
        wait(3)
        print()
        print("The old mage looks to you in confusion.")
        print()
        print(""" "What did you see?" She asks. """)
        print()
        print("You explain your visions and how your father was murdered and you mother kidnapped.")
        print("Her face is filled with grief and she kneels down to comfort you.")
        print()
        print(""" "Take as long as you need. We will move on when you are ready." """)
        print()
        wait(1.5)
        while True:
            ans = input("Are you ready to continue?")
            ans = ans.upper()
            yes = ["YES", "Y", "CONTINUE"]
            if containsAny(ans, yes):
                nacastrum()
                break
            else:
                print()
                print("Take as much time as you need.")
                print()


def nacastrum():
    print()
    print("After you take a few moments to contemplate what all has happened,")
    print("You feel a rush of determination and resentment towards Vashirr, your 'king'.")
    print("You know now that, even though Vashirr says he banished the mages to save them, there is "
          "something nefarious afoot.")
    print()
    wait()
    print("You and the Old Mage venture deeper into Nacastrum towards the King's Castle.")
    print("The huge mage towers of stone cast shadows over the streets of silver that you walk.")
    print("Many of the civilian houses are intact, but some seem to have been ransacked by the Agroman.")
    print()
    print("The Old Mage looks at the wreckage with confusion at first, but then gradually she begins to "
          "understand what happened.")
    print()
    wait(2)
    print(""" "This isn't the Nacastrum I remember." """)
    print(""" "Nacastrum was a proud city where those who wished to learn about magic had a safe place to do so." """)
    print()
    print("The Old Mage stops in her tracks and looks to you.")
    print()
    wait(.5)
    print(""" "I'm afraid I haven't been completely honest with you." """)
    print()
    print(""" "Let me start with introducing my self, once and for all." """)
    print(""" "I am Thekia. I once was part of the High Mage's Council." """)
    print()
    while True:
        ans = userinput(""" "Do know about the High Mage's Council?" """)
        ans = ans.upper()
        yes = ["YES", "Y"]
        no = ["NO", "N"]
        if containsAny(ans, yes):
            print(""" "Then you know of our importance." """)
            print(""" "When Vashirr became King, our power and influence waned." """)
            print(""" "Over the years, Vashirr ignored our advice and did what he wanted for his personal benefit." """)
            print()
            wait(2)
            print(""" "He eventually exposed the High Mage's Council to the public and painted us as a corrupt group
            of petty politicians." """)
            print(
                """ "When the public spoke up against us, Vashirr eliminated the council and banished its members." """)
            print(""" "His act of 'appeasing the people' solidified his role as King." """)
            print()
            wait(2)
            print(""" "Years passed and, well, you know what happened then." """)
            print(""" "Without the High Mage's Council to stop Vashirr, the people of Nacastrum were left
            to his mercy." """)
            print(""" "Vashirr is a powerful mage and a formidable foe, but I know we can stop him." """)
            print()
            print(""" "But first, we must return Nacastrum to its former glory." """)
            print(""" "Come on, we don't have any time to waste." """)
            wait(2)
            ending()
            break
        if containsAny(ans, no):
            print()
            print(""" "I am not surprised. The High Mage's Council was kept hidden from most of the public." """)
            print(""" "We advised the King and dealt with foreign affairs from the shadows." """)
            print(""" "The High Mage's Council has been around since Nacastrum had been founded." """)
            print()
            wait(2)
            print(""" "However, when Vashirr became King, our power and influence waned." """)
            print(""" "Over the years, Vashirr ignored our advice and do what he wanted for his personal benefit." """)
            print()
            wait(2)
            print(
                """ "He eventually exposed the High Mage's Council to the public and painted us as a corrupt group of petty politicians." """)
            print(
                """ "When the public spoke up against us, Vashirr eliminated the council and banished its members." """)
            print(""" "His act of 'appeasing the people' solidified his role as King." """)
            print()
            wait(2)
            print(""" "Years past and, well, you know what happened then." """)
            print(
                """ "Without the High Mage's Council to stop Vashirr, the people of Nacastrum were left to his mercy." """)
            print(""" "Vashirr is a powerful mage and a formidable foe, but I know we can stop him." """)
            print()
            wait(2)
            print(""" "But first, we must return Nacastrum to its former glory." """)
            print(""" "Come on, we don't have any time to waste." """)
            wait()
            ending()
            break


def ending():
    print()
    print("You and Thekia finally arrive at the King's Castle of Nacastrum.")
    print("The stone and silver castle shoots so far in to the atmosphere that you almost lose sight "
          "of the tower's peaks.")
    print("At the front of the castle are walls with crenellations lining the tops.")
    print()
    wait()
    print("You and Tekia enter the King's Castle and find it in ruins.")
    print(
        "Kaefden and Nacastrum banners that previously hung from the walls are ripped apart and lie on the floor.")
    print("The silver floors are scratched and ruined along with the carpets that lead to the throne room.")
    print()
    wait()
    print("Thekia looks around, disgusted, but then averts her eyes to you.")
    print()
    print(""" "This place is an absolute mess. We have a lot of work cut out for us." """)
    print(""" "Luckily, I know where we can get some friends." """)
    print()
    wait()
    print(
        "Thekia heads into the courtyard of the King's Castle and places the staff used to open the Rings of Malkos into its designated slot.")
    print(
        "Before she can activate the ring, you look out into the courtyard and spot a body lying on the floor.")
    print()
    print("The body looks familiar.")
    print("Your heart sinks as you realise that the body is your father.")
    print()
    wait(1.5)
    print("You rush over the rotting corpse. The smell and look of the body is horrid, but you don't care.")
    print("Memories of your father trying to stop the Agromanians from taking your mother return.")
    print()
    print("More thoughts of anger and hatred fill your mind as tears swell up in your eyes.")
    print("You vow to your father's lifeless body to, if not save her, avenge your mother as well as him.")
    print()
    print("Light shines on a pendant around your fathers neck.")
    print("One made of silver with a blue gemstone in the middle.")
    print()
    print(
        "You take a moment to recollect yourself before taking your father's pendant and placing it around your neck.")
    print()
    wait(2)
    print("Thekia activates the Ring of Malkos and a visage of another city appears.")
    print(
        "She waits for you to return to her, puts her hand on your shoulder, and walks with you into the portal.")
    print()
    print("Moments later, you are transported to a huge city. One even bigger than Nacastrum.")
    print()
    wait()
    print("You ask Thekia where you are and she explains.")
    print()
    print(""" "We are in the capital of Kaefden, Aylova." """)
    print(""" "Many of the mages that were banished came here for safety." """)
    print()
    print(
        "Hundreds of people witness you and Thekia travel from the portal because of its central location in the city.")
    print("Thekia walks past you and looks to the crowd.")
    wait(2)
    print()
    print(""" "People of Kaefden!" """)
    print(""" "We have come with terrible news." """)
    print(""" "Vashirr of Nacastrum has banished the Mage from our home to weaken the bond between our people
    and the people of Aylova." """)
    print(""" "Vashirr, the old king of Nacastrum, has joined the Agroman and wishes to destroy both of our
    people for his own gain." """)
    print()
    wait(2)
    print("The citizens of Aylova appear confused and afraid.")
    print()
    print(""" "Mages of Aylova! Come with me and rebuild the home that was unrightfully
    stolen from you!" """)
    print(""" "We promise you, that we will not rest until Vashirr and the Agroman are defeated and the people
    of Avasia live in peace!" """)
    print(""" "We cannot force you to join us, but if you wish to help, come with us through the portal." """)
    print()
    wait(2)
    print("Thekia turns and nods to you and walks back into the portal.")
    print("You wait a moment and look to the people of Aylova and then follow her back to Nacastrum.")
    print()
    print("You wait outside the Ring of Malkos in Nacastrum for a few moments.")
    print()
    wait(2)
    print("All that is left is the humming of the portal and the abandoned city.")
    print("You wait in anticipation for at least someone to come through.")
    print()
    print("Moments later, A lone mage comes through the portal and looks around.")
    print(
        "He runs out in to the city with tears in his eyes. It seems his memory has returned to him much like yours.")
    print()
    print("Almost immediately, more mage come through the Ring of Malkos to return to their home.")
    print("A sense of pride and joy fills your spirit.")
    print()
    wait(2.5)
    print(
        "Even people who aren't mage enter the portal to join you in your efforts to stop Vashirr and the Agromanian.")
    print()
    print("Thekia, with a sigh of relief, speaks to you.")
    print()
    wait()
    print(""" "Thank you, for all you have done." """)
    print(""" "None of this would have been possible without you." """)
    print(""" "But there is work to be done. We have just started." """)
    print()
    print(""" "Let us go, my king." """)
    print()
    wait()
    print()
    print()
    print("\033[2;36;48mAvasia: King of Nacastrum!")
    print("\033[0;26;48m")
    print()
    print("Congratulations on completing the game!")
    print()
    wait()
    print()
    credits()


def credits():
    print()
    print()
    print("~-CREDITS-~")
    print()
    print()
    print("-DEVELOPERS-")
    print("----------------")
    print("CO-LEAD DEV: Jacob Rozell")
    print("CO-LEAD DEV: Chase Pernatozzi")
    print()
    print("DEV: Devan Deloach")
    print("DEV: Joshua Rogers")
    print()
    wait(.75)
    print("-BETA TESTERS-")
    print("----------------")
    print("Megan Haskins")
    print("Jeremiah Rhodes")
    print("Anna Ferguson")
    print("Derek Powell")
    print("Jack Powell")
    print("Nathan Brooks")
    print()
    print("-SPECIAL THANKS TO OUR FRIENDS AND FAMILY FOR THEIR LOVE & SUPPORT-")
    print()
    print()
    print()
    textspeed()


# BeachFront

def shoreside():
    global rod
    print()
    print("The smell of a sea breeze reminds you of the bustling trade city, Oceandale, except quietier.")
    print("You look around and notice a small hut sitting on the edge of the sea.")
    print("The beach front lies WEST of you.")
    print()
    while True:
        ans = userinput("What would you like to do?")
        leave = ["LEAVE", "BACK", "RETURN"]
        hut = ["HUT", "ENTER"]
        o = ["OCEAN", "SEA", "WEST"]
        if containsAny(ans, leave):
            print()
            print("You return back to where you came from.")
            print()
            westernroad()
            break
        if containsAny(ans, hut):
            print()
            print("You head towards the hut on the beach.")
            beachhut()
            break
        if containsAny(ans, o):
            print()
            print("You decide to walk to the water.")
            print()
            shore()


def beachhut():
    global rod
    if rod == 0:
        print()
        print("The hut appears very poorly maintained.")
        print("You come to the conclusion that is abandoned.")
        print("The previous owner must have left years ago.")
        print()
        print("Next to the front door is an old fishing rod.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            frod = ["ROD", "TAKE"]
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "OUTSIDE"]
            enter = ["ENTER"]
            if containsAny(ans, enter):
                print()
                print("The inside of the hut is nearly barren.")
                print("Nothing of interest is inside the hut.")
                print()
                beachhut()
                break
            if containsAny(ans, leave):
                print()
                print("You leave and return to the beach.")
                print()
                shoreside()
                break
            if containsAny(ans, frod):
                print()
                print("\033[1;32;48mYou received the FISHING ROD!")
                print("\033[0;26;48m")
                print()
                print("You leave the hut.")
                rod = 1
                shoreside()
                break
    if rod == 1:
        print()
        print("The hut appears very run down and poorly maintained.")
        print("You come to the conclusion that is abandoned.")
        print("The previous owner must have left years ago.")
        print()
        while True:
            ans = userinput("What would you like to do?")
            leave = ["LEAVE", "BACK", "EXIT", "RETURN", "OUTSIDE"]
            enter = ["ENTER"]
            if containsAny(ans, enter):
                print()
                print("The inside of the hut is nearly barren.")
                print("Nothing of interest is inside the hut.")
                print()
                beachhut()
                break
            if containsAny(ans, leave):
                print()
                print("You leave and return to the beach.")
                print()
                shoreside()
                break


def shore():
    global rod
    print()
    print("You look out to sea and see nothing but water.")
    print("It's actually quite calming.")
    print()
    while True:
        ans = userinput("What would you like to do?")
        verbs = ["STRETCH", "RELAX", "EXERCISE", "YOGA"]
        leave = ["LEAVE", "BACK", "EXIT", "RETURN"]
        fish = ["FISH", "FISHING"]
        if containsAny(ans, fish):
            if rod == 0:
                print()
                print("You don't have a fishing rod.")
                print()
            if rod == 1:
                fishing()
                break
        elif containsAny(ans, verbs):
            print()
            print("You take a deep breath and do some yoga moves.")
            print()
            print("A couple of back bends.")
            print("A few Eagles.")
            print("Even a Crow Pose.")
            print()
            print("Both your body and mind feel revitalized.")
            print()
        elif containsAny(ans, leave):
            print()
            print("You leave and return to the beach.")
            print()
            shoreside()
            break
        else:
            print()
            print("This would be a good place to do some stretching.")
            print()


def fishing():
    global orange
    global deathcount
    print()
    print("You cast a line into the ocean.")
    print()
    cast = (randint(2, 12))
    while True:
        if cast == 2:
            print()
            print("Moments after casting a line, you feel a pull on the fishing rod!")
            print()
            print("You pull back the line and discover a huge fish made of pure gold hanging on the hook!")
            print("It must be worth a fortune!")
            print()
            orange = 0
            break
        if cast == 3:
            print()
            print("Minutes pass and you finally feel a tug on the line!")
            print()
            print("You fight with the line until eventually you manage to reel it in.")
            print()
            print("Out of the water appears a large crab like monster!")
            print()
            orange = 0
            if sword == 1:
                print()
                print("Fortunately, you draw your sword and slay the beast before it can attack.")
                print("Looks like you'll be eating crab for dinner!")
                print()
                break
            if fireball == 1:
                print()
                print("Just before the beast attacks, you blast it with Inflame.")
                print("The smell of cooked crab fills the air.")
                print("Delicious.")
                print()
                break
            else:
                print()
                print("The beast lunges forward and snaps at you!")
                print("Its mighty claws clutch tightly around your waist!")
                print()
                print("You're snapped completely in half and the crab-monster drags your body into the ocean.")
                print()
                print("\033[1;31;48mYou have died.")
                print("\033[0;26;48m")
                deathcount += 1
                print()
                textspeed()
                break
        if cast == 4 or cast == 5 or cast == 6:
            print()
            print("After minutes of silence you reel in your line.")
            print()
            orange = 0
            break
        if cast == 7 or cast == 8 or cast == 9:
            print()
            print("Minutes after casting your line into the ocean you feel the weight of the fishing rod "
                  "become slightly heavier.")
            print()
            print("You assume that you've got a bite so you reel in the line only to discover an old shoe.")
            print("How disappointing.")
            print()
            orange = 0
            break
        if cast == 10 or cast == 11:
            print()
            print("A few minutes pass and you feel a bite on the line!")
            print()
            print("You fight with the fishing rod and eventually reel in a large fish!")
            print("Looks like you've caught dinner!")
            print()
            orange = 0
            break
        if cast == 12:
            if orange < 4:
                print()
                print("After a few minutes of waiting, you feel a tug on the line!")
                print("You reel in the fishing rod and find a floppy orange colored fish.")
                print()
                print("It looks absolutely useless, just splashing about.")
                print()
                print("You toss it back into the ocean.")
                print()
                orange += 1
                break
            if orange >= 3:
                print()
                print("You wait just a few moments before your fishing line is taken right out of your hands!")
                print()
                print("The water begins to ripple and you watch as an enormous blue sea-serpent "
                      "plunges out of the water!")
                print("You have no time at to react before it dives down and gobbles you up.")
                print()
                print("\033[1;31;48mYou have died.")
                print("\033[0;26;48m")
                deathcount += 1
                print()
                textspeed()
                break
    print()
    while True:
        ans = input("Would you like to cast your line again?")
        ans = ans.upper()
        yes = ["YES", "Y", "FISH"]
        no = ["NO", "N"]
        if containsAny(ans, yes):
            fishing()
            break
        if containsAny(ans, no):
            shore()
            break


textspeed()










