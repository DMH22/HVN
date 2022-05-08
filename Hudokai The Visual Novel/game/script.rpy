﻿# The script of the game goes in this file.

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
default seen_nexus_scene_3 = False
default seen_nexus_scene_4 = False
default seen_nexus_scene_5 = False
default seen_nexus_scene_6 = False
default seen_nexus_scene_7 = False
default see_nexus_scene_8 = False

# The game starts here.

label start:

    scene

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
    $ journal001 = True
    #show nexus title screen with a fade.


#Nexus Area List
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
    if seen_nexus_scene_6:
        jump nexus_scene_7
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
    if seen_nexus_scene_7:
        jump nexus_scene_8
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
    else:
        no"What a dump!"
        if seen_nexus_scene_5:
            jump nexus_scene_6
        else:
            no"What a dump!"

    menu:
        "return to nexus":
            jump nexus
    return

label train_station:
    scene red
    "You are at the Train Station."
    if journal001:
        no"It looks like theres no train here right now"
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
        no"No, I can’t wait for Matt. I’m not safe. I need to find that messy haired mugger punk right now for answers. He said he liked to stay up at night on a rooftop..."
        "PERSON""Will he heal us of our wounds? Let’s hurry!"
        no"Um... no. I was talking to myself."
        "PERSON""And you do that often when people are dying around you?"
        no"..."
        "Nova leaves"

        $ seen_nexus_scene_5 = True
        menu:
            "return to nexus":
                jump nexus

label nexus_scene_6:
    "Night falls across the nexus"
    "Nova explores the Nexus in his search for MAX."
    "He finds him on the rooftop, alone. He joins him on top of the burnt house."
    m"I burnt this place. I burnt it down."
    no"You can’t burn the past... only forget it."
    m"How can I forget how he looked at me as he left? My dad, I mean. He just left me and mum alone. I hated him. I hated the house he bought us."
    no"If it helps, I don’t remember my dad. Not yet, anyway. I think I have amnesia."
    m"So you’ve come to me for answers? I should ask you some questions, myself, with that prison garb and stuff. Fine, what do you want to know?"
    menu:
        "What’s Hudokai?":
            m"Budokai?"
            no"Hudokai."
            m"I honestly don’t know."
        "Why can’t I escape this town?":
            m"You’re prisoner to the Nexus. It’s what everyone calls this town. I don’t know why, but there’s no fluffing way of leaving. Everyone’s trapped in this limbo."
            no"And how did you end up here?"
            m"I bombed my house. I didn’t just set it alight. But when I set off the charge, a large black hole appeared in the centre of the house. About the size of a small building. It fluffing pulled me and the house through into this place. I’ve never been able to escape."
        "Why’d you attack me earlier?":
            m"You have no phone, no food, no anything. I have to mug to survive. I thought I made that clear. All I have is my burnt house."
        "I’m being hunted by an armoured killer!":
            m"Foltix?"
            no"A friend of yours?"
            m"You’d best get out of here, idiot! Everyone knows Foltix. He’s part of the Town Watch."
            no"Sounds friendly for a maliciously murderous group!"
            m"He’s right-hand to the Town Watch leader, Greg. No one knows what he looks like. He always keeps hidden and yet... he always knows what’s going on."
            no"And you all let him lead you?"
            m"Well, he watches over us. Sometimes horrible monsters get sucked into this town. The Town Watch exterminates them. They are the law, here. No one knows Greg’s true motives, though. He has nothing to gain from this all."
            " FOLTIX appears out of nowhere and charges at the building at warp speed."
            "He jumps across the gap and tackles Nova but catches Max."
            "The world spirals away. Darkness. Flashes of light reveal FOULTIX violently attacking Nova."
            "The darkness fades away."
            "Nova, beaten and bruised. He can barely stand."
            "FOLTIX is in front of him."
            f"Welcome to my world of pain - the Dark Dimension."
            no"Another dimension?!"
            "FOLTIX attacks Nova once more, forcing him back."
            f"Hudokai. You know too much. I am deeply sorry for the slip of my tongue, though. Really, I am. If I hadn’t confused you with my good pal, Geist, I wouldn’t have to do this."
            no"I don’t even know what Hudokai is!"
            f"Liar. Prepare to duel to the death."
            "No matter what nova trys his attacks will not hit foltix who toys with him until he bacomes bored"
            "Nova manages to fake to the left and shoot foltix with a fireball"
            no"How d’you like that?"
            f"Hudokai! You already have some Hudokai! Fiend! Let me show you what Hudokai can really do... and why we at the Watch are the true owners!"
            "Foltix unleashes a bolt of lighting trapping nova"
            "Suddenly, FOLTIX is attacked from behind by Max."
            f"Looks like I kidnapped another cockroach. My bad."
            "FOLTIX turns to face Max."
            m"Take me back! I’ve done nothing to the Town Watch!"
            f"Hmm. I... won’t touch you."
            m"Huh?"
            f"This complicates things. Of all the people to bump into... please forgive me, Max."
            m"You can’t be..."
            no"You heard him! Take... *hack* us back!"
            f"Still ticking? It can’t be helped. I must leave. Sorry about this Dark Dimension business. It’s the furthest I could take you. I must check on the Hudokai store!"
            "FOLTIX disappears from existence, seemingly. Max looks around, then goes to Nova."
            m"Yo, you all right?"
            menu:
                "(I’m fine)":
                    no"I’m fine"

                "(I’ve seen better days)":
                    no"I’ve seen better days"

                "(I’m really fluffing hurt, you bitch)":
                    no"I’m really fluffing hurt, you bitch"
            "MATT appears out of nowhere."
            "MATT""He’ll be fine, now that I’m here."
            m"Fluffing hell, who the fluff are you?"
            "MATT""There’s no need for such language."
            no"Matt..."
            "MATT""We’re at the edge of the void. Foltix lied. We’re not in any dimension."
            no"...You came early."
            "MATT""Nope. It’s gone midnight. I kept my word and here I am. Let’s go."
            "MATT spins around and the world fades back to Max’s house."
            m"How did you take us back?"
            "MATT""It’s time. Take Mr. Nova inside your burnt tent of a place and rest up. He’s bruised, but will heal with some curative Hudokai."
            m"Curative Hudokai? What the fluff?"
            no"Do it..."
            "Max takes Nova inside, leaving MATT outside alone."
            "MATT""It’s a new day."
            "The remander of the night passes without insident"
            "Max standing outside of the house and MATT walking back and forth. Nova walks out of the house, slowly."
            no"I feel incredible."
            "MATT""That’s the curative Hudokai."
            m"What the fluff is Hudokai, anyway?"
            "MATT""Today I won’t be answering your questions, but handing you over to a more experienced fighter of the Nexus."
            no"I can fight just fine, it seems."
            "MATT""You’re as flimsy as a hotdog."
            m"Do you like hotdogs or something?"
            "MATT""How did you guess?"
            m"Intuition."
            "MATT""We call him Roke Zephyr. He’s a veteran fighter from a country cooked by war in a far off dimension. Say that all in one breath."
            no"Who are you, really?"
            "MATT""I like to see myself as a guardian of the Nexus. I was the very first to be transported here. My task, for now, is to bring you to Roke."
            no"I’m not following you."
            "MATT""You don’t have to, dude. But you do have to see Roke, today. If you’d prefer to make your own way there, then I’ll see you there."
            no"I want answers! I don’t want to fight, anymore."
            "MATT""You fought the highest power and killed millions."
            no"!"
            "MATT""I met Lione. She told me your prisoner report. She fears you, dude, but doesn’t want to admit it. You’re a wanted criminal. You have to fight if you want to survive."
            no"I’ll... find my own way."
            $ seen_nexus_scene_6 = True


    menu:
        "return to nexus":
            jump nexus

label nexus_scene_7:
    "Nova travels across the Nexus."
    "Everywhere is blocked off beyond the main path leading to the inn."
    "Nova eventually finds a middle aged man with one arm and a red scarf - ROKE."
    "MATT is with him, as is Max and LIONE."
    "Roke""Better late than never."
    no"I was blatantly guided here."
    "MATT""I knew you’d see sense!"
    l"Ah. Nova. Nice of you to show your face after leaving me."
    no"Huh. I thought you left me."
    l"I was injured!"
    m"So, why the fluff am I here?"
    "Roke""Good point. Matt, why are these squirts in my sight?"
    "MATT""They are targets of the Cult of Kai. They have Hudokai."
    "Roke""I have one piece of advice for you weaklings: Get out, now."
    l"Like I’m going to listen to that when you judged us on appearance."
    no"So says the vice-warden."
    "Roke""You don’t have what it takes, simple as. Battle isn’t beautiful, nor is it glorious. It isn’t child’s play and the playground is a bloodbath. It’s death."
    no"So maybe I died and was reborn?"
    "Roke""An epiphany? You blow chunks. Hudokai ain’t a laughing matter."
    m"So what exactly is Hudokai?"
    l"An energy source in the form of condensed matter. They’re rare, but we of the prison ship had a stasis Hudokai implanted to keep prisoners locked in place, frozen in time."
    "Roke""Bitch don’t know nothing. Hudokai is hell. Condensed Dark Matter from the void - a place between dimensions."
    "Matt""You might know that place as the Nexus."
    no"So we’re locked between all dimensions, in the void."
    "Roke""And in here lies a bounty of different Hudokai, which those idiots, like Foltix, of the cult want."
    m"The cult? You mean the Town Watch."
    "Roke""I mean what I said, dumbass! They only call themselves the “Town Watch” as a guise. Bastards. They really want the Hudokai, but like us, Greg’s groupies are trapped in here."
    l"So you’re going to teach us how to use the Hudokai against this “Cult of Kai”?"
    "Roke""No, ‘cause you suckas don’t got it. And even if I did, it won’t solve anything. No one can escape the Nexus void without a ship. The sky’s the only escape, but since no one has a ship, it ain’t a worry."
    no"I came here by ship."
    "Roke""You what?"
    l"Our prison ship crashed here."
    "Roke""..."
    "Matt""Best get cracking, Roke. If the cult escape the void and out into the infinite dimensions with the Hudokai, they will start to abuse it."
    no"This “cult”. I take it there are others on the outside?"
    "Matt""No one knows what’s beyond the void. The strong are taken out by the Town Watch and many have lived here too long to remember their past before entering the Nexus."
    "Roke""All right, fine. Since no one don’t know how to use Hudokai in battle but me, and since I don’t wanna see the universes ravaged like my home... I’ll teach you freaks how to use the latent power of Hudokai."
    "Matt""Oh, Rokey, I knew you’d see sense"
    "Roke""It’s Roke. Roke Zephyr. Don’t none o’ you forget that! Matt, you owe me. "
    "MATT leaves the area."
    "Roke""Twerp. All right, kids, follow me to my mansion."
    $ seen_nexus_scene_7 = True

    menu:
        "return to nexus":
            jump nexus

label nexus_scene_8:
    "Once they reach the mansion, ROKE charges Nova and begis to attack"
    "Roke""Defend yourself if you want to live!"
    menu:
        "I don’t even have a weapon!":
            "Roke""Who says you need a weapon to fight?"
            no"But you have one."
            "Roke""Fighting ain’t ever fair, kid. It’s all about your defence... if you want to live."
        "If we attack as a team, we might survive!":
            l"I don’t much like the idea of working with a criminal again."
            "Roke""But maybe Nova has a point?"
            no"There’ll be more targets for him to aim at. You can be my meat sheild, Lione."
            l"How dare you! I’ll show you who will be the dead weight if we team up. Hmph!"
            m"We should defend, at any rate. Otherwise we might not make it - he’s serious."
            no"All right, weapon or not, here we come!"
        "I thought this was “training”!":
            l"Quit whining. There is no training in the real world."
            "Roke""Saggy face is right."
            l"What did you call me?"
            "Roke""And she’s the only one with a bit of combat training... but nothing will prepare you for me. Best learn how to defend before I squash you!"
    n"His attacks do some serious damage. I’d best use the defend option to take less damage and survive his onslaught."
    "Roke""Defending also heals your health, or ‘HP’, by a small percentage. Your Hudokai is also a powerful weapon, so powerful that it will drain its own energy after every use. I call this ‘MP’. It can be restored when given an ionic charge or after resting for the night."
    n"I think you’d better concentrate on the battle."
    "Roke""Infernal kid ain’t gonna tell me how to fight!"
    "The fight ends with a draw both Novas Group and Roke are catching there breath when Foltix arrives"
    f"Ahh, Roke. I should’ve known it was you. I followed the flashes of Hudokai in the sky."
    "Roke""Oh, goody. It’s the Town Watch."
    l"I thought the strong were removed from the Nexus?"
    f"If it were up to me, I’d leave them around. They’d be helpful, but Greg doesn’t want that and I respect his decision. Besides, Roke is actually too strong for me to handle. As far as Greg’s concerned, Roke doesn’t exist."
    no"Sounds like you do all of his handywork."
    f"Greg’s a good friend. My best friend, in fact. He does other things for our group."
    m"You don’t seem like such a bad guy..."
    f"I like to think I’m not, but... well, I am. I can’t deny the things I’ve done, or am going to do. I can’t allow you guys to know what you know."
    "Roke""He won’t let ya go with your trained strength, either. Not now."
    f"Oh? So it was this lot using the Hudokai to light up the sky. I see. Then I definitely have to take you guys down. Sorry about that."
    m"I... won’t let you!"
    f"Look, I’ll leave you be if you just stand aside, Max."
    l"What’s so special about him?"
    m"He’s my dad! I know it!"
    "Roke""Family means nothing on the battlefield. Trust me."
    m"And I’ve been saving these two daggers just for your return, dad... how dare you turn your back on us all! I didn’t think you could be in here with me... but I won’t forgive you!"
    f"Is that what you think?"
    "Roke""Hey, kid. Best back him up. After all, I reckon you’ll be pleasantly surprised after what I taught you... here"
    "Roke toss's Nova a pistol"
    "Nova turns to see both Max and Lione egin to rush foltix , Nova lets loose a couple shots that hurmlessly bounce of foltix's armour"
    "As Max approuches Foltix moves away and into lione's swords range"
    "Nova notices a circullar slot in the handle of the pistol and slots the Combust Hudokai in"
    "Nova feels the heat through the pistols handle and lets loose a round of bullets that errupt from the pistol as fireballs slamming into foltix"
    f"Such... strength! But how?"
    no"We were much stronger in that fight. In such a short amount of time, too..."
    f"I... must tell Greg!"
    m"Don’t you dare, dad. This is between you and me."
    f"Time out, time out! I’m not your father, but I do know how you feel."
    m"You’re... not my dad? No. It’s me - Max Judge! I’m your son. R-right?"
    "FOLTIX removes his helmet. He has the same head as Max."
    no"Another Max?"
    f"I’m you from a different dimension. That’s why I didn’t want to fight you."
    m"W-what? Another me? I almost... killed myself!"
    f"Stop being so melodramatic. Damn. That assault really stung."
    "Roke""I think it’s about time you were done away with, don’t you, Foltix?"
    f"Ugh... You still on... about what I did to your friend?"
    "Roke""You didn’t have to fight that battle, but you did. I ain’t never gonna forgive you."
    no"People change."
    "Roke""Tell that to my dead partner."
    f"I’m certainly not... the man I was..."
    menu:
        "(Let Foltix go)":
            no"I’m not going to chase you."
            "Roke""What?!"
            f"..."
            l"From what I understand, Foltix’s hands are stained in the blood of Roke’s entire homeland. Never let a criminal escape."
            no"I don’t think Foltix is as bad as you’re all making him out to be. I think he’s a changed man."
            f"I only want... to do what is right. It isn’t... always the easiest decision, though..."
            l"Screw you! A criminal is a criminal! I’ll arrest you and prove to the Warden I can be trusted!"
            f"...The Warden?"
            l"As vice-warden, it is my duty!"
            f"...Poor girl. It isn’t always fun following orders..."
            no"Let him go. All we need to do is concentrate on repairing that prison ship to get out of here."
        "(Kill Foltix)":
            no"But you still follow orders to kill, otherwise you wouldn’t have attacked us. Maybe you haven’t changed that much, after all."
            f"I beg you... Just let me go... I will leave you be like I leave Roke!"
            "Roke""Too much blood has been spilt. Now that there’s this little team and a ship to shape up and get outta here on, I think it’s time to do you in."
            f"No, wait!"
            no"Goodbye, Foltix. Let me kill you in the name of justice."
            "Nova kills FOLTIX with his weapon. Silence."
            l"Justice can be brutal."
            "Roke""He killed my partner in battle. He devastated thousands of homelands. He deserved it."
    m"It felt like a part of me died inside after that... I wonder what Greg will do next?"
    "Roke""Now don’t get me wrong, ‘cause I trained you to take on the Cult of Kai members, but Greg’s not your concern at the minute."
    menu:
        "You can’t tell me what to do.":
            "Roke""I damn well can. Your concern is fixing up that prison ship and getting out of here. You can leave Greg behind!"
        "You’re right.":
            l"Agreeing with someone? You?"
            no"It’s the prison ship. If we can fix that up, we can get out of here and leave Greg trapped here, still. He won’t ever be a problem."
    l"I don’t know if your tiny brain even noticed, but the prison ship was left in no condition to fly."
    no"We’ll make it work."
    "Roke""And I’m guessing you know how it works, little lady?"
    "Roke""Tell me and I’ll make sure you get off this forsaken rock ‘cause I’m coming with you."
    m"But you have a mansion here and none of you know what’s outside. Why do you want to leave?"
    l"I know what’s out there. There may be very little Hudokai, but it’s a lot more interesting than this place."
    "Roke""People come to the Nexus after a piece of rare Hudokai is ripped open from an explosion, or mass amount of energy. Loads of us have slipped here and haven’t been able to get out. Now you take it from me, when a ship finally appears to get someone out, they’ll want to get out!"
    l"I haven’t got a choice. I have to co-operate with a criminal, a brute and someone who has daddy issues."
    m"Actually, I don’t want to leave."
    "Roke""You’re insane, kid."
    m"This place has become my home. I don’t know why anyone would want to leave their home."
    "Roke""Whatever. My partner thought like you did and he was a Death Bringer - one o’ those people who are trained to watch over others and sentence them to their deaths when their time has come. He was a Death Bringer and he still died, protecting our home."
    m"Then maybe I’ll wander out there at some point and find my home planet? I’ll protect my home from the cult. Right now, my home is here."
    "Roke""Bloody kid... You remind me way too much of him... Now, don’t you go thinking I’ve gone all soft, but... I’d like you to have this."
    m"What’s this? A scythe? You Death or something?"
    "Roke""That’s what the Death Bringers wield. Only those trained in their death arts can slice the soul out of a living being, but... I reckon you can have it. It’s a weapon. It will help you protect your home."
    m"This was your partner’s, wasn’t it? You gay?"
    "Roke""Shut up and use it, before I change my mind! Lione, where the hell to next?"
    l"The first thing we’re going to do is rendezvous with the Reality Council, once we’re out of here."
    no"The what?"
    l"They are an alliance of world leaders. They council the innermost solar system of the galaxy, in three dimensions. Their word is law. We should tell them about the cult."
    no"Wait, what about your precious Warden? He’s your superior."
    l"He’ll still be in the Nexus. I want to prove myself to him before I next see him. If we capture a member of the cult as proof that they exist, as well as clear my name... that should do it."
    no"Yeah, he blamed you for the takedown of the prison ship."
    "Roke""Sounds like a load of manure to me. I just wanna get this ship running."
    l"The engines are critically damaged, numbskull. We don’t even know what parts we’ll need for it to get running again, let alone the metal plating for the exterior."
    "Roke""Then I’ll go and examine the piece o’ junk whilst you do your thing, twerp. It ain’t rocket science."
    l"Actually, it kind of is."
    "Roke""Whatever. My old man used to be a mechanic and I used to watch him when he worked. I know what I’m looking for. Here, take this old radio. I used it in the war. Good for keeping contact across wide distances. I’ll let you know what we’re looking for whilst you do your waste of time thing."
    l"It’s not a waste of time if it helps the believability of our claim."
    no"If I help you get this Greg guy, will you tell me more about, you know, me and my life before the crash? I’m sick of being in the dark."
    l"On your head, be it."
    no"Let’s ask around and see where this Greg is situated, then."
    "Roke""Yeah, and I’ll give you this talkie radio so we can keep each other updated on stuff."
    $seen_nexus_scene_8 = True
    menu:
        "return to nexus":
            jump nexus




# This ends the game.
return
