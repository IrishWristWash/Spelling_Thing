# Imports
import pyttsx3
import random

# Declaring variables etc.
engine = pyttsx3.init()
engine.setProperty('rate', 180)
x = 0
word_list = ['hikoi', 'denouement', 'kaiako', 'doggerel', 'poroporoaki', 'anaphora', 'rangatiratanga', 'genre',
             'manuhiri', 'neologism', 'pu', '̄ra', '̄kau', 'parody', 'dystopian', 'cathartic', 'nuance', 'etymology',
             'peregrination', 'epithet', 'colloquial', 'phenomenon', 'talisman', 'oviparous', 'schematic', 'malachite',
             'semiotic', 'oleiferous', 'anachronistic', 'arboreal', 'labyrinth', 'hygroscopic', 'celadon', 'haustellum',
             'oscillate', 'belligerent', 'cerebellum', 'cataclysm', 'pelagic', 'caveat', 'photosynthesis', 'sequence',
             'inert', 'constituency', 'quadrilateral', 'referendum', 'igneous', 'suffragette', 'edacious', 'apartheid',
             'aqueous', 'feminism', 'ubiquitous', 'anarchy', 'incumbency', 'orison', 'boycott', 'welkin', 'sovereignty',
             'menorah', 'remembrance', 'monotheistic', 'deification', 'inoi', 'ecumenical', 'whakapohane', 'thurible',
             'ra', '̄', 'hui', 'exegesis', 'wananei', 'sacristy', 'Ramadan', 'euphony', 'embouchure', 'plangent',
             'clarion', 'arpeggio', 'appoggiatura', 'medley', 'scherzo', 'cadenza', 'ensemble', 'exemplar', 'turquoise',
             'dynamism', 'avarice', 'enfilade', 'balalaika', 'philippic', 'gallimaufry', 'vapidity', 'nostalgia',
             'pugnacious', 'virtuosic', 'lithe', 'charismatic', 'boisterous', 'palpable', 'tumescent', 'taciturn',
             'refulgent', 'niveous']
points = 0
systemrun = 0


def repeat():
    system_run = 0
    engine.say("How do you spell " + (random_word))
    engine.runAndWait()
    player_reply = input("Answer: ")

    if player_reply == "repeat":
        system_run = 1
        repeat()

    if player_reply == random_word:
        engine.say("Congratulations!")

    if player_reply != random_word and system_run == 0:
        engine.say("Sorry you spelt that wrong.")
        engine.say("Here is the correct spelling.")
        letterlist = list(random_word)
        print(random_word)


while len(word_list) > 0:

    system_run = 0
    random_word = random.choice(word_list)
    engine.say("How do you spell " + str(random_word))
    engine.runAndWait()
    player_reply = input("Answer: ")

    if player_reply == "skip":
        system_run = 1
        engine.say("The correct spelling was.")
        print(random_word)

    if player_reply == "repeat":
        system_run = 1
        repeat()

    if player_reply == random_word:
        engine.say("Congratulations!")
        points += 1
        print("You have " + (str(points)) + " points.")

    if player_reply != random_word and system_run == 0:
        engine.say("Sorry you spelt that wrong.")
        engine.say("Here is the correct spelling.")
        letterlist = list(random_word)
        print(random_word)
        word_list.remove(random_word)
