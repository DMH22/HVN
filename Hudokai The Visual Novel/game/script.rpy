# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Cast List

define nn = Character("Prisoner 30895")#, image="novanum_left")
define no = Character("Nova")#, image="novanum_left")
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

#Area List
#Nexus - Nexus Cliffside - Crash site - Achevment House - Cafe-Doctors - Item Shop - Inn - Church - Roke's House - Max's House - Train Station - Town Watch Tower

#Journal Variables
default journal001 = False
default seen_nexus_scene_1 = False
default seen_nexus_scene_2 = False

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

    "As you look around the carnage of the ship you notice two large spheres laying on the ground and put them in your pocket"
    "you move forward and hear a noise coming from near the entrance to the ship"
    "Among the rubble and bodys you encounter a restless female whos alive"
    "As you move a box aside to help you see Long red hair, black uniform with shiny cyan, vertical strips down her arms and legs. Piercing eyes."

    show lione_right at right

    l "(Groggy) Prisoner 30895... This is your fault."

    nn "..."

    l"Not much of a talker... fine. Your actions speak louder than words, anyway..."

    nn"..."

    " You watch as she stuggles to her feet"

    l"For the attempted murder of law enforcement, as well as damage of a prison ship..."

    hide lione_right
    show lione_left
    show cyrillwar_right at right
    cw"I, Warden Cyrril War, place you, Lione Burgess, under arrest."

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
    hide cyrillwar_right
    "Prisoner 30895 and LIONE RUN from a large robotic spider that gives
    chase."
    "Several reinforcement officers get in the way"
    "You can hear a strange sound coming from inside the ship as the large robotic spider tank begins to move forward"
    #show gp_battler
    "You turn ,lifting you hand up to push through the officers"
    "suddenly a ball of fire apperes in your hand"
    menu:
        nn"What the hell !"
        "Panic":
            "As you begin to panic the fireball springs from you hand forcing the officers to dodge and you both run through"
        "Throw it Confidently":
            "Before the officers have a chance to advance you throw the ball of fire and it explodes just in front of them and creates a path for the two of you to escape through"
        #

    #hide gp_battler
    l"I don’t need you fighting my battles... especially not with that whacked out ability you have."
    nn"..."
    l"Tsk... my life in the hands of a mute, typical. Here’s a hint: Only rubber can absorb the electrical energy of our Arachnivolt tank bot. If its energy is taken, it will stop, otherwise it will perpetually repair itself."

    "You continue to hear the sound of a large machine but so far you have only encounterd guards"

    l"Look theres water over there by the tree"

    "As you both clean your hands and drink the fresh cold water you hear a crashing from the direction you came"
    "Coming towards you is a machine spider tank"
    #show arachnivolt

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
    # hide arachnivolt

    l"You can thank me for my quick thinking, later... But don’t get me wrong,
    criminal, I am grateful for your help... but you’ve got me into some deep dung."


    menu:
        nn"What should i do?"
        "Why are you such a bitch?":
            l"Excuse me?"
            nn"Well, I mean you’re judging me for something you don’t even know is true and ignoring the things you do know, like saving your life."
            l"So! Your mouth does blab! And what garbage it spouts, too."
            nn"You comparing me to a bin? ‘Cause I can recycle your sad state of a body into something less of a hindrance right now."
            l"The nerve of it! Criminals will always be criminals... and I don’t feel any safer with you anymore, 30895."
        "We’re in the eye of the storm.":
            l"Excuse me?"
            nn"That warden will realise we’ve escaped, eventually... not to mention we don’t know where we are."
            l"Aha! So you do talk! And quite the thinker, too... *cough*"
            nn"We need to find you a doctor."
            l"Since when did a criminal care about a vice-warden? Don’t give me that fake kindness."
            nn"Criminals can reform. Anyone can change."
            l"..."
            nn"I don’t even remember what I did that imprisoned me... I wish I knew."
            l"Shut up. Just... shut up, 30895."


    nn"You have to stop calling me by a prison number."
    l"(Preoccupied)If it wasn’t us, then who crashed the ship? I hope the Warden’s okay."
    nn"The name’s... "
    no"Nova"
    l"I know who you are. Your report said more than enough to make me want to part ways with you."

    menu:
        nn"What should i do?"
        "We must stick together!":
            l"I want to go on my own."
            no"The only thing I remember is how to use my fists - that scares me. You know more about me than I do. You know who I am."
            l"I know who you was. Tough. You don’t want to know, trust me."
            no"Nor will I let you wander off in your condition. We’re staying together."
            l"...Your heart is kinder than your report makes you out to have been. Okay... fine. Support me until we find a doctor. Then, maybe you can tell me what’s up with your weird ability."
            no"The one that freezes enemies? I honestly don’t know."
            l"You don’t?"
            no"It’s like I can feel the energy near my body and then absorb it into me before releasing it at the enemy, again. "
            no"I think it’s something to do with this sphere I have..."
            l"*Hack* Hudokai?! That’s... the prison ship’s... stasis Hudokai... *cough*"
            no"We’ll talk more when we find you some aid."
        "Fine. Wander off. It’s your funeral.":
            l"Like you care."
        "I need to stick with you.":
            l"Stick to the prison... it’s where you ultimately belong for the crime you committed."
            no"You know more about me than I do."
            l"You seem to remember how to cause violence just fine."
            no"And that scares me."
            l"I... need to find a doctor... before the warden returns."
            no"Doesn’t it worry you that he targeted you for a crime I apparently committed?"
            l"...Yes. I... need time to think. I... *cough* I need to know why the Hudokai stasis cells disengaged... and why you are even here."
            no"I wonder if there’s any connection between that and the energy sphere I’ve been using in combat?"
            l"That... was the... *cough* Hudokai? *hack* No... gotta go."

    no"Looks like there’s a town ahead..."
    #show nexus title screen with a fade.
$ journal001 = True

#Area List
#Nexus - Nexus Cliffside - Crash site - Achevment House -
#Cafe-Doctors - Item Shop - Inn - Church - Roke's House - Max's House - Train Station - Town Watch Tower


label nexus:
    # scene bg_town
    while True:
        scene yellow
        "You are in the Nexus. Go where?"
        menu:
            "Nexus Cliffside":
                call nexus_Cliffside
            "Crash site":
                call crash_site
            "Achevment House":
                call achevment_house
            "Item Shop":
                call item_shop
            "Inn":
                call inn
            "Roke's House":
                call roke_house
            "Max's House":
                call max_house
            "Train Station":
                call train_station
            "Town Watch Tower":
                call town_watch_tower

label nexus_Cliffside:
    scene red
    "You are at Nexus Cliffside."
    if journal001:
        no"The wardens back that way we better stay away"
    else:
        no"i can see the town from here"
    menu:
        "return to nexus":
            jump nexus
    return

label crash_site:
    scene red
    "You are at the crash site."
    if journal001:
        no"The wardens back that way we better stay away"
    else:
        no"i can see the town from here"
    menu:
        "return to nexus":
            jump nexus
    return

label achevment_house:
    scene red
    "You are at the Achevment House."
    if journal001:
        "worker""Sorry we arent open until the next cycle, come back later"
        no"Any suggestions?"
        "worker""Maybe try some shops around town"
    else:
        "worker""Welcome"
    menu:
        "return to nexus":
            jump nexus
    return

label item_shop:
    scene red
    "You are at the Item Shop."
    if journal001:
        "worker""Sorry we arent open until the next cycle, come back later"
        no"Any suggestions?"
        "worker""Maybe try some shops around town"
    else:
        "worker""Welcome"
    if seen_nexus_scene_1:
        jump nexus_scene_2
    else:
        "worker""Welcome"
    menu:
        "return to nexus":
            jump nexus
    return

label inn:
    scene red
    "You are at the Inn."
    if journal001:
        "worker""Sorry we arent open until the next cycle, one second is that women hurt?"
        no"Maybe...?"
        l"Yes im hurt"
        "worker""We have a doctor who works here part time, come this way"
        $ journal001 = False
        jump nexus_scene_1

    else:
        "worker""Welcome here take a bed and sleep"

    if seen_nexus_scene_4:
        jump nexus_scene_5
    menu:
        "return to nexus":
            jump nexus
    return

label roke_house:
    scene red
    "You are at the Roke's House."
    if journal001:
        r"GET THE HELL OUTTA HERE BRAT"
    else:
        r"Welcome kid"
    menu:
        "return to nexus":
            jump nexus
    return

label max_house:
    scene red
    "You are at Max's House."
    if journal001:
        no"This house has been set alight but theres no damage to the surrounding buildings?"
    else:
        no"What a dump!"
    if seen_nexus_scene_2:
        jump nexus_scene_3

    menu:
        "return to nexus":
            jump nexus
    return

label train_station:
    scene red
    "You are at the Train Station."
    if journal001:
        no" It looks like theres no train here right now"
    else:
        no"The trains here"
    if seen_nexus_scene_3:
        jump nexus_scene_4
    menu:
        "return to nexus":
            jump nexus
    return

label town_watch_tower:
    scene red
    "You are at the Town Watch Tower."
    if journal001:
        no"Because large dark towers dont scream OMINOUS!"
    else:
        no"Nope"
    menu:
        "return to nexus":
            jump nexus
    return

label nexus_scene_1:
    scene red
    "Nova leaves Lione in the care of the doctor and leaves the inn"
    "Nova shakily TRAVELS down an alley towards the town. As he does so, a crimson armoured solider turns to him in the alley."
    f"Yo, we’ve found the Hudokai, so there’s no need to worry. See ya back at the station."
    "He walks off, leaving the Nova confused."
    no"Who.."
    "Nova turns the corner only to see another Nova walking down the path towrds him."
    "He hides and watches as this strange other version of himself walks by."
    no"I have to find out what’s going on."
    $ seen_nexus_scene_1 = True
    menu:
        no"Im so confused ,what should i do?"
        "Follow Him":
            no"I need answers now"
            jump item_shop

        "Explore":
            no"ill look for answers later"
            jump nexus

label nexus_scene_2:
    " Nova turns and looks through the window. But the other him isn’t in there. Tense. Suddenly, regreting his chooses, hes punched in the face and floored by a stranger."
    "The stranger quickly pats Nova's body down and then runs off."
    no"Worse things have happened today."
    no"Oi!"
    $ seen_nexus_scene_2 = True
    jump nexus

label nexus_scene_3:
    "Nova catches up with the stranger and tackles him to the floor"
    "Both of them raise there hands ready to fight"
    menu:
        "What’s going on?":
            "Why the hell did you punch me?"
            "The pair begin to cycle each other"
        "I’m gonna punch you.":
            "Nova's fist flashs out catching the strager in the face"
            no"TELL ME!"
    m"I punch whoever I feel like."
    no"I knockout whoever I feel like."
    m"I especially punch mouthy bastards like you, looking lost in this world of survival."
    m"There’s no point if we’re already prisoners of the Nexus..."
    no"So what if I am lost?"
    m"Then you’re new in town."
    "They relax a bit more."
    no"Yeah. Tell me the way out and we’ll call it quits."
    m"I’ll call it quits when I finally get a phone to do so."
    no"You... That’s why you floored me and searched my pockets. Why do you want a phone so bad?"
    m"You’re new. You might have had a phone or a memory of outside of town... I’ve been here so long that the only thing I remember is setting fire to my house... I never forget it. I try to remember more by sitting on what remains of the roof, every midnight."
    "Max looks pained."
    m"Fluffing crap, bollocks, scock!"
    menu:
        "You won’t have a scock if you don’t tell me what I want to know.":
            m"Did you ever call your dad?"
            no"What?"
            m"Did you ever call him to ask how he was?"
            no"I... honestly don’t remember. I... I don’t remember anything before coming here."
            m"They say those who remember, those who are the strongest, are the first to go."
            "Max leaves."
        "Look, forget I said anything. I just wanna know how to leave.":
            m"Why?"
            no"Didn’t you hear me? I’m lost. I need to get home."
            m"But home’s here. Those who don’t understand that are arseholes. Arseholes who turn their back on their home... their family... their world."
            no"Forget it. I’ll survive on my own, thanks."
            "Nova walks away, shaking his head. Max leaves. As Nova walks away from him he spots someone walking by and heads towards him."
            no"‘Scuse me. Can you tell me the way out of this town?"
            "The person looks horrified."
            "Crazy-Man""You’ll be the next one taken!"
            no"What the hell’s wrong with this town?!"
            no"I wonder if there’s any transport to get me out of here? I’ll try up north of the town."
            $ seen_nexus_scene_3 = True
    menu:
        "return to nexus":
            jump nexus

label nexus_scene_4:
    no"I wonder what’s beyond this town..."
    "Nova boards the train, but after a few mnuests of the trains shaking mvement he finds himself back to the same train station. All town exits take them back to the town."
    no"That’s strange. So I can’t leave the town? It’s like that messy haired mugger said. I have to find him, otherwise we’re stuck here."
    "A man walks out of the shadows."
    "MATT""I’ve been watching you."
    no"So I’ve noticed."
    "MATT""I’m Matt. I watch all newcomers to the Nexus."
    no"What’s the Nexus?"
    "MATT""You feel weak from all that’s happened, today. It’s best you find somewhere to rest, first. Ask me again, tomorrow. Don’t look for me. I’ll find you."
    "MATT disappears, quite literally."
    no"I hate people telling me what to do."
    $ seen_nexus_scene_4 = True
    menu:
        "return to nexus":
            jump nexus

label nexus_scene_5:
        "Nova manages to doze off"
        "A SHORT WHILE LATER"
        "BANG"
        f"He’s here, somewhere..."
        "person""Aaaaaaargh!"
        f"No, the one we want has silver hair. What’s in this room?"
        no"I have to hide!"
        menu:
            "better hide but where"
            "Floorboards":
                    "FOLTIX and GEIST enter the room, killing several people as they wake up."
                    f"This is the last room. Search!"
                    "GEIST""..."
                    f"I don’t care. It’s my head on the line if the boss finds out. How was I supposed to know it wasn’t you?"
                    f"I mentioned Hudokai, that’s what I did, Geist! He mustn’t know. He needs eliminating."
                    f"He isn’t here. Fluff! He must’ve escaped. All right, Geist, think. Where would you go if you were him?"
            "Under the bed":
                    f"This is the last room. Search the beds!"
                    "GEIST""..."
                    f"All right. How about we flush him out? Destroy the beds and wardrobe. Make sure they’re no hiding places!"
                    "Nova quickly rolls from under the bed and under the nearest curtain"
                    f"I dread to think if that boy already has some Hudokai, thanks to me. Geist, he must be eliminated!"
                    "Nova holds his breath tryig not to breath"
                    f"He isn’t here. The boss is gonna go mad! Keep searching the town!"
            "Haystack":
                    f"The haystack! Set fire to it. Kill all witnesses"
                    "GEIST""..."
                    "Geist moves forward setting the haystack alight and nova leaps out"
                    f"There he is! No silver haired clone will get away with the Hudokai info! Exterminate him."
                    #GAME OVER
            "Behind Curtains":
                    "FOLTIX and GEIST enter the room, killing several people as they wake up."
                    f"This is the last room. Search!"
                    "GEIST""..."
                    f"I don’t care. It’s my head on the line if the boss finds out. How was I supposed to know it wasn’t you?"
                    f"I mentioned Hudokai, that’s what I did, Geist! He mustn’t know. He needs eliminating."
                    f"He isn’t here. Fluff! He must’ve escaped. All right, Geist, think. Where would you go if you were him?"
        $ seen_nexus_scene_5 = True
        menu:
            "return to nexus":
                jump nexus




# This ends the game.
return
