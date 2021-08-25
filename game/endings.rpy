define d = Character("Developer")

label finalIncorrect:
    stop music
    d "Hold on Lawyer Berd."
    d "I'm in your head btw."
    d "That's not right."
    d "THINK."
    d "It's obvious that selection would lead to nowhere."
    d "But there's still a {i}mystery{/i} in the evidence..."
    d "... One that can finally close this case forever!"
    l "Ok then, I'll rethink this."
    #Villan Suite; Phoenix Wright Special Courtroom 2008 Concert Orchestra
    play music("audio/finalpush.mp3")
    jump final


label end:
    #Pursuit ~ Keep Pressing On; Phoenix Wright Dual Destinies OST
    play music("audio/pursuit.mp3")
    l "Your Berd and the members of this court. The answer is obvious. And it was a mystery that we had never solved... until now!"
    l "Remember what Crown Berd said when he presented this lighter..."
    call crown from _call_crown_15
    c "We also have a lighter"
    show lighter:
        zoom 0.5
        xalign 1.0
        yalign .0
    c "It has the accused fingerprints."
    c "And someone's unknown fingerprints."
    c "We got no record of the known berds."
    c "Such as pink berd!!!, blue berd, bean berd, boomer berd, and pog berd >:D"
    c "{b}If we can compare the fingerprints to its owner, we can identify the person.{/b}"
    call defense from _call_defense_24
    l "If my theory holds true, then this berd here is in fact the terrorist!"
    l "Your Berd! The defense calls for an analysis of the fingerprints on the witness and the fingerprints on the lighter!"
    call witness from _call_witness_7
    t "Uh no! This is a violation of my berd rights!"
    call judge from _call_judge_18
    j "Kewl Berd, if you refuse the scan, you are effectively telling the court that you are the terrorist!"
    call witness from _call_witness_8
    t "Fine, conduct the scan."
    call courtcalm from _call_courtcalm_3
    "TWO HOURS LATER"
    call judge from _call_judge_19
    "Analysis Berd" "Your Berd! The fingerprints match!"
    j "Hm.. This doesn't look good for you Kewl Berd."
    call defense from _call_defense_25
    l "Your Berd! The defense rests its case."
    call crown from _call_crown_16
    show crownberd:
        linear .1 rotate 360
        linear .1 rotate 0
        repeat
    c "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    #Investigation: Mystery Suite; Ace Attorney Meets Orchestra
    play music("audio/final.mp3") fadein 1.0
    call judge from _call_judge_20
    j "Oh wow. This has taken a complete 180."
    j "Kewl Berd... or should I say Terrorist Berd."
    j "Do you object to any of these accusations made against you."
    call terroristB from _call_terroristB_1
    define a = Character("Terrorist Berd")
    a "No your berd."
    a "The defense has made a one for one recreation of what I was doing."
    a "I accept my fate."
    a "But I have one request your berd."
    call judge from _call_judge_21
    j "Yes?"
    call terroristB from _call_terroristB_2
    a "If I am about to be executed... please let my remains be a Costco Rotisserie Chicken."
    call judge from _call_judge_22
    j "Very well. I will ensure that happens if the higher courts give you the death sentence."
    call terroristB from _call_terroristB_3
    a "Thank you."
    hide terroristberd with fade
    pause 1.0
    call judge from _call_judge_23
    j "Anyways, Defense Berd! That was amazing! I can't believed you found this again!"
    call defense from _call_defense_26
    l "Thank you Your Berd. And today is an amazing record, I had 100-1 against Crown Berd!"
    call crown from _call_crown_17
    show crownberd:
        linear .1 rotate 360
        linear .1 rotate 0
        repeat
    c "JIOJDIFNI8OIOHFUIGBIEHSUDOFisjdofijdifoAJFODSIJFOISWFOIJOAJEWF"
    c "IJDOISFJIOEWHRFI OIJFIOSEF AWOEIDHRFIOAE FHIOAEJDFIOA"
    call judge from _call_judge_24
    j "Ok I think Crown Berd is having a stroke. While the paramedics come, I would like to render my verdict now."
    stop music
    j "The court finds the defendant..."
    j "NOT GUILTY"

    scene bg court
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
        yzoom -1.0
    show lawyerberd:
        xalign 0.7 yalign 0.55
        zoom 0.5
    show lawyerberd:
        linear .1 yzoom -1.0
        linear .1 yzoom 1.0
        repeat
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25
    show judgeberd:
        linear 0.1 xzoom -1.0
        linear .1 xzoom 1.0
        repeat
    pause 1.0
    scene bg jbench
    show judgeberd:
        yalign 0.35 xalign 0.5
        zoom 1.6
    j "Court is adjourned!"


    show bg court with fade
    hide judgeberd
    show lawyerberd:
        xalign 0.7 yalign 0.55
        zoom 0.5
    #Ace Attorney 3 Epilogue; Ace Attorney Meets Orchestra
    play music "audio/endcourt.mp3"
    "2 Hours Later"

    scene bg defense
    show lawyerberd:
        xzoom -1.0
        yalign .9 xalign 0.5
        zoom 2.0
    l "That was an epic party."
    l "I never saw a drunk judge before."
    l "And Crown Berd! Even after that surgery, he drank like a full bottle of Spirytus!"
    l "What a berd."
    l "Now that I think of it, who was my client?"
    "That would be me."
    scene bg witness with fade
    show daberd:
        yalign 1.2 xalign .5
        zoom 1.6
    e "Good job lawyer berd, thanks for defending me today."
    scene bg defense
    show lawyerberd:
        xzoom -1.0
        yalign .9 xalign 0.5
        zoom 2.0
    l "Wait, you were my client?"
    l "Wow. Now that I think of it, the picture does contain you."
    call witnessF from _call_witnessF
    e "Haha yeah. This was very interesting."
    call defense from _call_defense_27
    l "Now that I think of it, how did your fingerprints get on everything?"
    call witnessF from _call_witnessF_1
    e "I found a perfect chocolate cigarette on the ground."
    e "And then I saw a lighter."
    e "This must have been Terrorist Berd running away and dropping the lighter."
    e "And then I thought:"
    e "What would it be like to smoke chocolate?"
    e "But when I picked the lighter up, the po po came."
    e "So yeah. And here we are now."
    e "My community service was supposed to tell this lovely person playing this game"
    e "About the history of Berds."
    e "But now that you have disovered the truth... I guess I don't need to do that anymore."
    e "But they can always start a new game... and discover the history of berds."
    call defense from _call_defense_28
    l "Who are you talking to?"
    call witnessF from _call_witnessF_2
    e "Heh heh. You won't know Lawyer Berd... the time will come..."
    e "When you realize what I can really do."
    call defense from _call_defense_29
    l "Ok then..."
    l "Anyways, wanna go smoke a chocolate cigarette?"
    call witnessF from _call_witnessF_3
    e "OH BOY! LET'S GO!"


    scene bg court with fade
    "And the two berds walked out into the distance... and smoked a chocolate cigarette."
    "From their stories... it felt sweet."
    "Of course, they had to go to the hospital later and pump the chocolate out of their lungs"
    "But they lived happily ever after."
    "THE END."

    window hide
    pause 1.0
    window show
    d "thanks for playing this!"
    d "This had took a surprising turn."
    d "But I hope you had just as much fun playing this as I did coding this!"
    d "As always, if you want to get more intricate story"
    d "Play the Phoenix Wright games or Aviary Attorney."
    d "Also, if you are curious about the music used, I used the following(not in order):"
    "Ace Attorney 3 Epilogue, Investigation- Mystery Suite, Phoenix Wright- Objection, The Steel Samurai, Kurain Genealogy all from Ace Attorney Meets Orchestra;"
    "Villain Suite from Phoenix Wright Special Courtroom 2008 Orchestra Concert ~Phoenix Meets Orchestra~, Pursuit~Keep Pressing On from the Phoenix Wright Dual Destinies OST."
    "And the Court theme from Phoenix Wright Ace Attorney OST."
    #Add music here
    d "Anyways, I hope you had fun!"
    d "I'll see you next time!"
    jump done

label incorrect:
    stop music fadeout 1.0
    j "WRONG"
    l "what?"
    scene bg jbench
    show judgeberd:
        yalign 0.35 xalign 0.5
        zoom 1.6
    j "WRONG. YOU CHOSE THE WRONG OPTION."
    l "oh noes."
    j "Unforutantely, we don't have time for this. This case is extremely clear. I see no room for misinterpretation of the facts. I am ready to render a verdict."
    l "The court finds the defendant..."
    l "GUILTY"

    scene bg court
    show crownberd:
        xzoom -1.0
        zoom 0.5
        xalign 0.3 yalign 0.55
    show crownberd:
        linear .1 yzoom -1.0
        linear .1 yzoom 1.0
        repeat
    show lawyerberd:
        xalign 0.7 yalign 0.55
        yzoom -1.0
        zoom 0.5
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25
    pause 2.0
    show judgeberd:
        zoom 0.5
        xalign 0.5 yalign 0.25

    scene bg jbench
    show judgeberd:
        yalign 0.35 xalign 0.5
        zoom 1.6
    j "The accused will surrender to the court immediately, to be held pending trial at a higher court within a month from today's date."
    j "That is all. The court is adjourned!"
    jump done
