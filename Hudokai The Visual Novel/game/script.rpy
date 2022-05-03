# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Cast List

define nn = Character("Prisoner 30895")#, image="novanum_left")
define n = Character("Nova")
define l = Character("Lione")#, image="lione_left")
define a = Character("Aliza")
define k = Character("Kim")
define m = Character("Max")
define p = Character("Phoenix")

# Cult Of Kai Members

define v = Character("V.Len")
define cw = Character("Cyrril War")#, image="cyrillwar_right")
define bw = Character("Ben War")
define g = Character("Guy")
define pg = Character("Penny Greyback")
define gg = Character("Greg Gory")
define f = Character("Foltix")
define gn = Character("Geist")

#Other Notable Characters

define v = Character("Varsh")
define r = Character("Roke")
define t = Character("Tom")
define j = Character("Jalfuzzy")
define ko = Character("Koel")
define s = Character("Smaz")
define ph = Character("Phyllis")
define ss = Character("Sloppy Scock")


# The game starts here.

label start:

    scene bg nexus 1

    "A crash site. Dead bodies scatter a rocky landscape. Pieces
of futuristic metal embed the area. A silver haired young
adult moans, gets up slowly, then falls back down."


    show novanum_left at left
    nn "arr..."

    menu:
        nn"My head is fuzzy , what should i do?"
        "Look at the crashed ship":
            nn"Wow ... was i on that thing when it crashed?"

        "Check around for survivors":
            nn"There seems to be a lot of dead people around , looks like i got lucky"

        "Check around the surrounding area":
            nn"Hmm there are a lot of smashed boxes around"
#
    "As you look around the carnage of the ship you notice two large spheres laying on the ground and put them in your pocket"
    "you move forward and hear a noise coming from near the entrance to the ship"
    "Among the rubble and bodys you encounter a restless female whos alive"
    "As you move a box aside to help you see Long red hair, black uniform with shiny cyan, vertical strips down her arms and legs. Piercing eyes."

    show lione_right at right

    l "(Groggy)
Prisoner 30895... This is your
fault."

    nn "..."

    l"Not much of a talker... fine. Your
actions speak louder than words,
anyway..."

    nn"..."

    " You watch as she stuggles to her feet"

    l"For the attempted murder of law
enforcement, as well as damage of a
prison ship..."

    hide lione_right
    show lione_left
    show cyrillwar_right at right
    cw"I, Warden Cyrril War, place you,
Lione Burgess, under arrest."

"CYRRIL WAR walks into view, cybernetic pistol in hand. Prisoner 30895
and LIONE turn to the blue suited warden. With a military
coat and disposition, CYRRIL produces an electrolysed ring."

menu:
    nn"What should i do?"
    "Grab vice-warden and run":
        l"Let go of me, you filthy criminal!"
        cw"Criminals always run. I’m sure you’re aware that none escape the Arachnivolt."
        l"I... am no... criminal!"
    "Grab the vice-warden’s blade":
        l"How dare you... grab... my weapon!"
        cw"And against a warden of the law, too. So you really are an accomplice, standing up for the vice-warden-turned-traitor."
        l"He is none of my concern!"
        cw"Save your testimony for the Arachnivolt. None escape its jaws of justice."
        l"Tsk..."
        cw"Run. Run! I dare you, run!"
    "Attack the warden":
        cw"You think striking me will stop your sentences?"
        l"No! He does not represent me!"
        cw"It matters not! Your fates lie with the Arachnivolt, now."


label after_menu:

"Prisoner 30895 and LIONE RUN from a large robotic spider that gives
chase."
"Several reinforcement officers get in the way"
"You can hear a strange sound comng from inside the ship and turn lifting you hand up to push through the officers and suddenly a ball of fire apperes in your hand"
menu:
    nn"What the hell !"
    "Panic":
        "As you begin to panic the fireball springs from you hand forcing the officers to dodge and you both run through"
    "Throw it Confidently":
        "Before the officers have a chance to advance you throw the ball of fire and it explodes just in front of them and creates a path for the two of you to escape through"

#












    # This ends the game.

return
