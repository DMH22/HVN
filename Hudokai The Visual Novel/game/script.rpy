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

#Background List
#Nexus


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
#remove cyrill.
"Prisoner 30895 and LIONE RUN from a large robotic spider that gives
chase."
"Several reinforcement officers get in the way"
"You can hear a strange sound coming from inside the ship as the large robotic spider tank begins to move forward"
#place arachnivolt image/animation.
"You turn ,lifting you hand up to push through the officers"
"suddenly a ball of fire apperes in your hand"
menu:
    nn"What the hell !"
    "Panic":
        "As you begin to panic the fireball springs from you hand forcing the officers to dodge and you both run through"
    "Throw it Confidently":
        "Before the officers have a chance to advance you throw the ball of fire and it explodes just in front of them and creates a path for the two of you to escape through"
    #

l"I don’t need you fighting my battles... especially not with that whacked out ability you have."
nn"..."
l"Tsk... my life in the hands of a mute, typical. Here’s a hint: Only rubber can absorb the electrical energy of our Arachnivolt tank bot. If its energy is taken, it will stop, otherwise it will perpetually repair itself."

"You continue to hear the sound of a large machine but so far you have only encounterd guards"

l"Look theres water over there by the tree"

"As you both clean your hands and drink the fresh cold water you hear a crashing from the direction you came"
"Coming towards you is a machine spider tank"

l"Oh crud"

"Lione steps back and hits the tree"

l"Prisoner 30985 quick use that power to combust the tree sap it might slow it down!"

menu:
    nn"What should i do?"
    "Combust the sap":
        l"Smells like burning rubber..."
    "Collect the sap":
        l"You want to keep that? Fool! Throw it away on the Arachnivolt. There’s nowhere else to run... we have to fight it to stay alive..."

"Lione springs forward quickly charging the tank ,just as its raises itself up to swipe at her she drops to the floor skidding under it , you hear the sound of metal on metal"
"As it continues towards you the see through sphere begins to vibrate , you take it out and a light shines out bathing the tank , you notice its slowed down enough for you to roll under its legs and out the way"
"Lione grabs your jumpsuit and pulls you aside as the spiders head turns to face you and opens its mouth"
"Its blast explodes the cliff face behind you and your flung high into the air above it"
"you feel the the sphere in you pocket heating up and feel the fireball gathering in your hands"
"you fire one off allowing you to gain your balance and aim"
#show concept art 1
"and unleash the other fireball directy into the airvents on the top as lione unleashes a flurry of sword attacks taking its legs off"

l"You can thank me for my quick thinking, later... But don’t get me wrong,
criminal, I am grateful for your help... but you’ve got me into some deep dung."















    # This ends the game.

return
