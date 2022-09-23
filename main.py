import random

insults = ["your ears have worms","you have beard lice","your face makes the mirror hurt","your singing makes me want to listen to a vaccum cleaner"]
insulters = ["Coraline","Harry Potter","Percy Jackson","Katniss Everdeen"]
insultees = ["your mom", "a catipiller", "you", "a boat", "the former president" "Vladamir Putin"]
sentence = random.choice(insulters)+" says "+random.choice(insults)+" to "+random.choice(insultees)

print(sentence)