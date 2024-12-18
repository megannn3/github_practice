import sys
import time

scenes = {
1: "Welcome to the game! You are a wanderer, with many magical abilities, including world-skipping. That means you can travel between worlds through portals! I'm Leao, a portalspren, and I accompany new world skippers like you on adventures. Are you ready for your first adventure? \n (Type the number to select your choice)",    
2: "So you've reached a portal stone. Which world do you decide to go to?", 
3: "Unfortunately, that part doesn't exist yet...so I guess you have no choice", 
4:"Uhhh...okay.Hope you have a good life!",
5:"Now that's some scenery! But this seems to be a developing world...not much for us here",
6:"Wow, this world sure is cool...but a bit empty for now",
7:"Alright then...I told you it was empty",
8:"Now this is a bustling town! Finally a well-developed world. Ah, looks like there's some locals in need of a world-skipper!",
9: "Where do you want to world-skip to today?",
10:"Golspince is a cool name. Not sure the world is quite living up to the expectations though...is that kilia steak I smell?",
11: "'Hello there! I'm Jeph, a botanist here in Elvwilows. I've been hearing stories of a plant, called Sangsettia, that has some magical properties I'd like to study. Issue is, it only grows on a world named Twiltrie. Have you been there? Well anyways, I'd appreciate if you could get me a couple healthy sprigs of that. I'll give you 200 elids for this quest.' ",
12: "That was good. I see why people actually visit this world now.",
13: "'Ah, well that's alright then. Have a good day!'",
14: "Nice job, you've died. What did you think would happen?",
15: "Hmm, pretty smoky here...wonder what that could be about. Oh dear, is that a dragon? I think it's time to go!",
16: "'Wonderful! From what I've heard, this plant should be easy to find in the forests. This Twiltrie is said to be quite beautiful too, and very peaceful. Once you've gotten it, meet me back atmy shop here. Best of luck!'",
17:"You've arrived in Twiltrie! Jeph was right, it is quite beautiful here. Time to get that plant.",
18: "This forest has the most magic I've ever encountered! Even the forest critters glow with lumen. Must be something in the water. Speaking of water, that old well seems to have some sort of plant growing around it.",
19: "Look at all these shops! Everyone seems so happy here, and these goods look really high quality too...but you don't have much elid, maybe you should finish that quest",
20:"'Ah, greetings traveler! Sangsettia is not at all difficult to find, but you're in luck, because I know all the best spots. I've found that the old well in the forest has the healthiest, most powerful sprigs. Don't take too much!'",
21: "There it is! That's some good-looking Sangsettia. Well, that was surprisingly easy, I guess it's time to go back and get your elid.",
22: "Uhh...something's wrong. This is really weird, but it looks like all the magic is gone from the stone! And what in the worlds is that tendril of black mist reaching towards the stone?",
23:"These people don't seem to be aware of any dangers or evils. Maybe we'll hear something in the tavern. Ah see, I'm sure that mysterious looking gentleman over there has some information.",
24: "The deeper into the forest we go, the darker it gets. Is that normal? Can you feel that shift, too? The magic is changing...it feels evil now. You can see it in the trees, the lumen doesn't glow so bright here. Wait, is that a wood wisp? That certainly isn't how they normally linger.",
25: "\x1B[3m It's here...it will never leave. Nothing in this world can escape. Warn them, they don't see it. They won't see it until it's too late...\x1B[0m \n That...doesn't sound good. I don't think this wood wisp is going to make it. I didn't even know that was possible, the death of a guardian. Maybe the townspeople should be informed. Or...what's that by the tree there? It looks like a wisp, but far stronger in magic?",
26: "'Yes, I know what you speak of. I spend much of my time in the deep woods, but lately the evil has been so strong I haven't. I've seen it, but I do not know what causes it. I fear it may consume our world, and I sit here helpless. But you, traveler, may be able to help. There is a wisp in the forest, the elder wisp. No one but those who can use the magic can hear it's words, but it may be able to tell you how to stop this evil. I know of some who have tried, but none have returned. Your inquiriy brings me hope, for the evil is advancing, and few have attempted to stop it in many weeks. I wish for your success, as I dread our world's fate if you fail'",
27:"\x1B[3m I see you, wanderer \n I know you wish to help, and that you must. Our time is running out. I grow weaker by the moment. This evil, you have seen it, yes? \x1B[0m \nAh, so this wisp knows us...even though it doesn't have eyes. But I suppose the evil it is referring to was at the portal stone, so yes. \n \x1B[3m It spreads, and soon it will not threaten only this world, but many others. Few dare to stop it, and few are able. But I see your heart. I know you seek adventure, and your skill in magic is greater than I've seen in many years. You may be our last hope. Follow my light, it will lead you where you need to go. I do not doubt that your powers will succeed, but my heart goes with you. Farewell. \x1B[0m ",
28: "Coward much? Great choice to abandon the call of the wisp and take a world's only hope. It's been two days, and the evil just destroyed Twiltrie's lumen source. \n A world physically can't survive without a lumen source. Many other worlds meet this same fate in the coming weeks, but you wouldn't know. \n Because you're dead.",
29: "Feeling brave, are we? Hmm, that's strange. Looks like the light path branches out here. One way goes down into the misty valley, and the other goes up that tree. ",
30: "Alright, that's pretty ominous. Whoa, what are those...misty...dead...deer? They don't come closer, but they do look like they want to kill you. Look at that cave up ahead, does it seem to be burning to you? I don't know if we're up for this challenge.",
31:"We made it up...Oh! Here's another wisp, this one looks...different. It burns with a different magic, we've never felt this before. I think it know what you're doing, and it's offering you a vial of some sort of light. I think it's to help your magic! ",
32: "Well, we made it to the lava ca- \n \x1B[3m Why have you come here? Surely you know there is no hope. You think yourself so strong, but your weak magic stands no chance against the evil. \x1B[0m \n Where is that voice coming from?? \n \x1B[3m That wisp was a fool to send you here . Leave now, tell all of this world, and all the universe's inevitable fate. Or stay, and suffer. \x1B[0m \n I-it's cho-choking us with the e-evil! Our magic isn't stro-ong eno...ugh...",
33: "Aaand it-or whatever that voice was- was right. Your magic was certainly not strong enough, and you did suffer a pretty horrible fate. I won't get into the details.\n Nice try, but you're dead again. ",
34: "Woah...by some miracle, the vial seems to be strengthening your magic, more than the evil expects! You can actually defeat it! \n Look, the mists are dispersing, but there still seem to be some remants of the evil...",
35: "Well, we're back at the botanist's shop! Make sure you thank Jeph for the elid, and have fun on your world-skipping adventures!",
36:"Wonderful choice! The people and wisps of Twiltrie are thankful for your help defeating the evil, and rebuilding the deep forests that were dominated by it. They are even offering you a home in Twilitre, where you can stay in between world-skipping adventures!",
37: "\n \x1B[3m Why have you come here? Surely you know there is no hope. You think yourself so strong, but your weak magic stands no chance against the evil. \x1B[0m \n Where is that voice coming from?? \n \x1B[3m That wisp was a fool to send you here . Leave now, tell all of this world, and all the universe's inevitable fate. Or stay, and suffer. \x1B[0m \n I-it's cho-choking us with the e-evil! Our magic isn't stro-ong eno...ugh...",

}

answers = {
1: ["Alright, let's go!","I'd like to customize my character"], 
2:["Elduniory","Elvwilows", "Phovilnds"],
3:["Oh, well, start the adventure", "No, I quit!"],
4:["Start over?"],
5:["Back to the portal stone"],
6:["I'd like to stay here","Go back to the portal stone"],
7: ["Okay I'm ready to go now"],
8: ["Go ask what quests they have", "I'm not interested, back to the portal stone"],
9: ["Elduniory","Elvwilows", "Phovilnds"],
10:["Go eat the inter-world famous kilia steak","Back to the portal stone again"],
11:["Ok, I'll take the job", "I'm not interested in this quest"],
12:["Alright, time to go"],
13:["Stay in Elvwilows", "Back to the portal stone"],
14:["Restart the game"],
15:["I'm getting out of here", "I want to stay with the dragon"],
16:["Go to portal stone to Twiltrie","That doesn't sound like my thing...go somewhere else"],
17:["Go to village","Explore forest"],
18:["Go see what's growing by the well"],
19:["Ask where the plant can be found","Explore forest"],
20:["Go to old well"],
21:["Go back to portal stone", "Stay here for now"],
22: ["Run back to village to ask what's going on","Keep exploring, and try to figure out what's wrong"],
23: ["Ask if the mysterious looking gentleman knows anything", "Nevermind, no one here could know anything, I'll figure it out myself."],
24:["Investigate the wood wisp", "Run back to village to ask what's going on"],
25:["Run back to village to ask what's going on","Go to the strange wisp" ],
26: ["Find the elder wisp"],
27:["Follow the light path", "Escape responsibility and hide in the village"],
28: ["Restart game"],
29:["Follow the straight path down into the valley", "Climb up the tree on the branching path"],
30: ["Go into the burning lava cave", "Run away from the dead deer and lava cave"],
31: ["Accept the vial and continue on the straight path", "Take vial and leave path, going back to village"],
32: ["Drink the vial, and try to use your lumen magic to burn away the choking mist", "Run out of the cave, back to the village"],
33: ["Restart game"],
34: ["Leave through now working portal stone to deliver plant", "Stay on Twiltrie to help wood wisps get rid of remnants of evil"],
35: ["Restart game"],
36: ["Restart game"],
37:["Use your lumen magic to burn away the choking mist","Run out of the cave, back to the village"],




}

paths = {
"Alright, let's go!": 2,
"I'd like to customize my character": 3,
"Elduniory":5,
"Elvwilows":8,
"Phovilnds":6,
"Oh, well, start the adventure":2,
"No, I quit!":4,
"Start over?":1,
"Back to the portal stone":9,
"I'd like to stay here":7,
"Go back to the portal stone":9,
"Okay I'm ready to go now": 9,
"Go ask what quests they have":11,
"I'm not interested, back to the portal stone":9,
"Go eat the inter-world famous kilia steak":12,
"Back to the portal stone again":9,
"Ok, I'll take the job":16,
"I'm not interested in this quest":13,
"Alright, time to go": 9,
"Stay in Elvwilows":8,
"Back to the portal stone":9,
"Restart the game":1,
"I'm getting out of here":9,
"I want to stay with the dragon":14,
"Go to portal stone to Twiltrie": 17,
"That doesn't sound like my thing...go somewhere else":9,
"Go to village":19,
"Explore forest":18,
"Go see what's growing by the well":21,
"Ask where the plant can be found":20,
"Go to old well":21,
"Go back to portal stone":22,
"Stay here for now":17,
"Run back to village to ask what's going on":23,
"Keep exploring, and try to figure out what's wrong":24,
"Ask if the mysterious looking gentleman knows anything":26,
"Nevermind, no one here could know anything, I'll figure it out myself.":24,
"Investigate the wood wisp":25,
"Go to the strange wisp":27,
"Find the elder wisp":27,
"Follow the light path":29,
"Escape responsibility and hide in the village":28,
"Restart game":1,
"Follow the straight path down into the valley":30,
"Climb up the tree on the branching path":31,
"Go into the burning lava cave":37,
"Run away from the dead deer and lava cave":28,
"Accept the vial and continue on the straight path":32,
"Take vial and leave path, going back to village":28,
"Use your lumen magic to burn away the choking mist":33,
"Run out of the cave, back to the village":28,
"Leave through now working portal stone to deliver plant":35,
"Stay on Twiltrie to help wood wisps get rid of remnants of evil":36,
"Drink the vial, and try to use your lumen magic to burn away the choking mist":34

}

def type(text):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    


def show(scene):
    type(scenes[scene])
    value = answers[scene]
    
    for i in range(len(value)):
        print("\n")
        type((str(i+1) + ":    "+value[i])) 
        print("\n")
    choose = input()
    
    if not choose.isdigit():
        type("Uhh... try again")
        choice = value[int(input())-1]
    else:
        choice = value[int(choose)-1]
    show(paths[choice])
show(1)
def p (text):
    for i in range(len(text)): 
        c = text[i+1]
        for i in range(len(c)):
            print('"'+c[i]+'":')
#p(answers)





