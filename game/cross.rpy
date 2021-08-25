label cross:
    default correctStatement = 0
    default correctItem = 0
    default finalCounter = 0
    call defense from _call_defense_2
    "Select an option:"
    menu:
        "Present":
            jump present
        "Court Record":
            jump record
        "Rewatch Testimony":
            jump testimony

label present:
    "What statement has a contradiction?"
    menu:
        "{b}1.{/b}So this guy right, he's walking on the road.":
            $ correctStatement +=0
            jump itemPresent
        "{b}2.{/b}And he had a bomb!!!!!!!!":
            $ correctStatement +=1
            jump itemPresent
        "{b}3.{/b}I called the po po immediatitely":
            $ correctStatement +=0
            jump itemPresent
        "{b}4.{/b}And then they arrested him.":
            $ correctStatement +=0
            jump itemPresent
        "{b}5.{/b}Which is very poggers.":
            $ correctStatement +=0
            jump itemPresent

label itemPresent:
    "What item contradicts that statement?"
    menu:
        "Bomb":
            $ correctItem +=1
            jump check
        "Lighter":
            $ correctItem +=0
            jump check
        "Cigarette":
            $ correctItem +=0
            jump check


label check:
    l "OBJECTION!"
    if correctStatement == 1 and correctItem == 1:
        jump correctone

    else:
        jump incorrect


label correctone:
    #Phoenix Wright- Objection; Ace Attorney Meet Orchestra
    play music "audio/objection.mp3"
    l "Your berd! I have a ground breaking contradiction!"
    call judge from _call_judge_5
    j "Oh, what is it???"
    call defense from _call_defense_3
    l "This so called 'bomb' is not a bomb!"
    l "In fact, it is a pepper shaker!"
    call courtcrazy from _call_courtcrazy_1
    "The court goes wild at this fact."
    scene bg prosecution
    show crownberd:
        yalign 1.1 xalign 0.5
        zoom 2.0
    c "Impossible, then this witness is lying!"
    c "And what were those lab technicians doing when I asked them 'does this blow up?'"
    call judge from _call_judge_6
    j "oh my, he's right. this is a pepper shaker!"
    j "this would go well with fish!"

    call defense from _call_defense_4
    l "Therefore, my client is not guilty."

    call crown from _call_crown_4
    c "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"

    call judge from _call_judge_7
    j "Well anyways, I am ready to render a verdict."

    call courtcalm from _call_courtcalm
    "..."
    show crownberd:
        linear 1.0 yalign 0.3
        pause 0.5
        linear 1.0 yalign .55
    stop music
    c "HOLD IT"
    call crown from _call_crown_5
    #The Steel Samurai; Ace Attorney Meets Orchestra
    play music("audio/rebut.mp3")
    c "The defense has failed to prove one thing!"
    c "If the defendant isn't guilty, then who is?"
    c "We had a guaranteed witness statement that this man in fact saw a bomb carried by him."
    c "In fact, we have a photo of this!"
    call defense from _call_defense_5
    l "What? I was never informed of this?!?!?!"
    l "Objection! This cannot be accepted this late in the trial!"
    call judge from _call_judge_8
    j "Objection overruled. Lawyer Berd, stop trying to hide the truth. I cannot state that your client is innocent until we have {i}someone{/i} in custody."
    call defense from _call_defense_6
    show lawyerberd:
        linear 0.5 xzoom -1.0
        linear 0.5 xzoom 1.0
        repeat
    l "(Damn it, I have to figure out who the accused is. Maybe this picture does help.)"
    call defense from _call_defense_7
    l "Fine then. Crown Berd, please show the picture."
    call crown from _call_crown_6
    c "Haha Lawyer Berd. Looks like you're in a pickle now."
    c "Mmmmmmm. Pickle."
    call courtcalm from _call_courtcalm_1
    show crownberd:
        linear 20 xalign 0.9
    "..."
    call judge from _call_judge_9
    j "Uh, Crown Berd? Are you there?"
    call crown from _call_crown_7
    c "Ah yes your berd!"
    c "I was thinking of pickles!"
    c "Pickles are delicious don't you think?"
    call courtcalm from _call_courtcalm_2
    show crownberd:
        linear 20 xalign 0.9
    show judgeberd:
        linear 20 yalign 1.0
    "Crown Berd and Judge Berd" "Mmmmmmmmm. Pickles."
    call defense from _call_defense_8
    l "Anyways... Crown Berd, can you show me the picture?"
    call crown from _call_crown_8
    c "Ah of course, here it is:"

    scene picture
    window hide
    pause 2.0
    c "Note how the defendant is carrying the bomb."
    l "Huh, I can't see them?"
    c "You can see the picture more clearly by clicking 'H'."
    c "Try it out now."
    j "Wow, thank you Crown Berd! I was having that question as well!"
    c "Anyways... we had news that a berd terrorist is there."
    l "But could there have not been a berd terrorist there??"
    c "Impossible. Our BerdTerrorist 2000 Detector had detected a berd terrorist there at that specific time and location."
    c "The image had been taken via a CCTV camera."
    call judge from _call_judge_10
    show picture:
        zoom 0.2
        xalign 1.0
        yalign .0
    j "Very well, the court accepts this photo into the court record."
    show picture:
        linear 3.0 xalign 0.7 yalign 0.4 zoom 0.7
    "Added picture to the court record."
    call crown from _call_crown_9
    c "Ha lawyer berd! How can you refute this evidence now?"
    call defense from _call_defense_9
    l "Hm... I would like the witness to describe the terrorist."
    call judge from _call_judge_11
    j "Very well, the witness will describe the terrorist and his actions."
    call witness from _call_witness_3
    show terroristberd:
        pause 1.0 xzoom -1.0
        pause 1.0 xzoom 1.0
    t "Ok then..."
    call defense from _call_defense_10
    $ counter = 0
    $ correctStatement = 0
    $ correctItem = 0
    $ pictureCount = 1
    l "(Huh? He's looking more scared than usual...)"
    #Kurain Genealogy; Ace Attorney Meets Orchestra
    play music "audio/testify.mp3"
    jump testimonytwo

label crossTwo:
    call defense from _call_defense_11
    "Select an option:"
    menu:
        "Present":
            jump presentTwo
        "Court Record":
            jump recordTwo
        "Rewatch Testimony":
            jump testimonytwo

    label presentTwo:
        "What statement has a contradiction?"
        menu:
            "{b}1.{/b} Ok, so if I recall, the berd was walking on the road.":
                $ correctStatement +=0
                jump itemPresentTwo
            "{b}2.{/b} There was a cigarette on the ground.":
                $ correctStatement +=0
                jump itemPresentTwo
            "{b}3.{/b} And he was holding a pepper shaker.":
                $ correctStatement +=0
                jump itemPresentTwo
            "{b}4.{/b} As for his characteristics, uh, he was a white berd.":
                $ correctStatement +=0
                jump itemPresentTwo
            "{b}5.{/b} And, he looked pretty normal, nothing was on his face.":
                $ correctStatement +=1
                jump itemPresentTwo

    label itemPresentTwo:
        "What item contradicts that statement?"
        menu:
            "Bomb":
                $ correctItem +=0
                jump checkTwo
            "Lighter":
                $ correctItem +=0
                jump checkTwo
            "Cigarette":
                $ correctItem +=0
                jump checkTwo
            "Picture":
                $correctItem += 1
                jump checkTwo


    label checkTwo:
        l "OBJECTION!"
        if correctStatement == 1 and correctItem == 1:
            jump correctTwo

        else:
            jump incorrect
label correctTwo:
    #Phoenix Wright- Objection; Ace Attorney Meet Orchestra
    play music "audio/objection.mp3"
    l "Your berd! Something doesn't line up here!"
    call judge from _call_judge_12
    j "What is it?"
    call defense from _call_defense_12
    l "The witness has stated that nothing is on the terrorist's face."
    l "However, it's very evident that my client is not the terrorist."
    l "And since we have found out that the 'bomb' is a pepper shaker, it is reasonable to assume that berd on the road is not the terrorist"
    l "In fact, that's just my client walking on the road looking at a chocolate cigarette!"
    l "Therefore, we can assume the berd that is wearing a scar is the terrorist!"
    call crown from _call_crown_10
    c "Wait, wait, wait. But that scar berd there does not have a bomb! We must still assume that the bomb is this pepper shaker here."
    c "Probably the contents inside here are explosive!"
    c "Your berd! The prosecution requests for another day of investigation!"
    l "OBJECTION!"
    call defense from _call_defense_13
    l "The defense disagrees, it has been stated that the evidence is just pepper."
    call judge from _call_judge_13
    j "Objection overruled. Lawyer Berd, please continue on with your explanation."
    call defense from _call_defense_14
    l "Thank you your berd. As I was stating, this scar berd here needs investigation, as there is no evidence of a bomb."
    l "However, the court has not thought of something."
    scene picture
    l "Note in this picture the buildings are very close together."
    l "Any person would think if a {i}fire{/i} has gotten out, it would raze the whole city down!"
    l "And there would be no evidence because the lighter can be disposed in the fire!"
    l "So this terrorist did not want to bomb the city, they wanted to RAZE it!"
    call crown from _call_crown_11
    c "NO."
    call defense from _call_defense_15
    l "But yes my dear crown berd and the members of this court."
    l "The defense holds its theory that the planned terrorist act was ARSON not a BOMBING!"
    call courtcrazy from _call_courtcrazy_2
    pause 1.0
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
    c "OBJECTION!"
    call crown from _call_crown_12
    c "But there's no direct evidence related to an arson!"
    l "OBJECTION!"
    call defense from _call_defense_16
    l "Oh, but there is... note that the only plausible weapon here is a lighter."
    l "In the {i}court record{/i} it has been stated that the lighter still works!"
    call judge from _call_judge_14
    j "Objection sustained."
    j "But Lawyer Berd, who is this mysterious berd? We had never seen a berd with a scar before?"
    call defense from _call_defense_17
    l "Yes, and it puzzled me for a while too."
    l "But then I realized, only two berds were here."
    l "And it was suprising that our witness knew so much information..."
    l "... considering even the general public and the defense has never seen the picture before it was presented by the prosecution."
    l "And as my final trick, witness!"
    call witness from _call_witness_4
    show terroristberd:
        pause .1 xzoom -1.0
        pause .1 xzoom 1.0
        repeat
    t "Uh... Uh what"
    call defense from _call_defense_18
    l "Please take off your kewl glasses."
    call witness from _call_witness_5
    t "Uh, no. This will ruin my kewlness."
    call judge from _call_judge_15
    j "KEWL BERD! The court demands you take off your glasses or face the charges of being the terrorist."
    call witness from _call_witness_6
    t "Crap."
    scene bg witness with fade
    show terroristberd off:
        yalign 1.2 xalign.5
        zoom 1.6
    t "..."
    call defense from _call_defense_19
    l "See! He has the scar! This confirms my theory!"
    call courtcrazy from _call_courtcrazy_3
    pause 1.0
    call crown from _call_crown_13
    c "No. This can't be true. Why did my witness became the accused??"
    call defense from _call_defense_20
    l "Therefore your berd, I have fully proved that in fact, my client is not the terrorist!"
    l "But instead, it's the witness, standing right here!!!"
    call courtcrazy from _call_courtcrazy_4
    show crownberd:
        linear 1.0 yalign 0.3
        pause 0.5
        linear 1.0 yalign .55
    stop music
    c "HOLD IT"
    #Villan Suite; Phoenix Wright Special Courtroom 2008 Concert Orchestra
    play music("audio/finalpush.mp3")
    c "Uh... The defense has failed to prove one thing..."
    c "There could be dozens of other berds who have that exact same scar!"
    c "The defense has failed to prove that it's just this witness!"
    call terroristB from _call_terroristB
    t "Uh, yeah! There could be dozens of other berds that have the exact same scar as me!"
    t "There is no concrete evidence that it's me!"
    call judge from _call_judge_16
    j "Yes, the witness and the prosecution has a point. Defense Berd, do you have any evidence that proves that its this berd?"
    call defense from _call_defense_21
    l "(Crap, I never thought they would go this far. But I have gotten this far... no backing out now!)"
    l "Yes your berd, I do have evidence that it's Kewl Berd."
    call crown from _call_crown_14
    c "IMPOSSIBLE! HOW PREPOSTROUS! YOU MUST SURELY BE BLUFFING NOW!"
    call judge from _call_judge_17
    j "Hold on Crown Berd, let this berd speak."
    j "Lawyer Berd, what evidence would you like to present to the court that finally accuses this witness of being a terrorist?"
    jump final

    label final:
        $ finalCounter += 1
        call defense from _call_defense_22
        l "Very well, I present this!"
        menu:
            "Present":
                menu:
                    "Select an item"
                    "Bomb":
                        jump finalIncorrect
                    "Lighter":
                        jump end
                    "Cigarette":
                        jump finalIncorrect
                    "Picture":
                        jump finalIncorrect
            "Court Record":
                jump recordTwo

label record:
    "Select an item:"
    hide lawyerberd
    hide bomb
    hide lighter
    hide cigarette
    menu:
        "Bomb":
            show bomb:
                xalign 0.5 yalign 0.4 zoom 1.2
            "A pepper shaker that is shaped like a bomb. It's not a bomb. It would taste pretty nice with some fish."
            jump record
        "Lighter":
            show lighter:
                xalign 0.7 yalign 0.4 zoom 1.2
            "A lighter that has your client's fingerprints."
            "It also has someone's unknown fingerprints on it"
            "It can produce fire."
            "Was this really used to light a bomb???"
            jump record
        "Cigarette":
            show cigarette:
                xalign 0.7 yalign 0.4 zoom 1.2
            "A chocolate cigarette."
            "It has your client's fingerprints on it."
            "You would take a bite but it's vital evidence."
            jump record
        "Back":
            jump cross
    label recordTwo:
        call defense from _call_defense_23
        "Select an item:"
        hide lawyerberd
        hide bomb
        hide lighter
        hide cigarette
        hide picture
        menu:
            "Bomb":
                show bomb:
                    xalign 0.5 yalign 0.4 zoom 1.2
                "A pepper shaker that is shaped like a bomb. It's not a bomb. It would taste pretty nice with some fish."
                jump recordTwo
            "Lighter":
                show lighter:
                    xalign 0.7 yalign 0.4 zoom 1.2
                "A lighter that has your client's fingerprints."
                "It also has someone's unknown fingerprints on it"
                "It can produce fire."
                "Was this really used to light a bomb???"
                jump recordTwo
            "Cigarette":
                show cigarette:
                    xalign 0.7 yalign 0.4 zoom 1.2
                "A chocolate cigarette."
                "It has your client's fingerprints on it."
                "You would take a bite but it's vital evidence."
                jump recordTwo

            "Picture":
                scene picture
                "The picture of the moment."
                "Shows all the evidence and two berds in the picture."
                "Was there really a berd terrorist here?"
                jump recordTwo
            "Back":
                if(finalCounter > 0):
                    jump final
                else:
                    jump crossTwo
