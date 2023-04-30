from buttons import ButtonClass
from interface import canvas
from score import ScoreClass
from gameplay import GamePlay

verb = ButtonClass()
noun = ButtonClass()
adjective = ButtonClass()
adverb = ButtonClass()
gameplay = GamePlay()
score = ScoreClass()

#PLAYER CHOOSES GRAMMAR TYPE BUTTON
def verb_button():
    verb_button.answer = "Verb"
    verb.button_reveal()
    if gameplay.sentence_word["Grammar"] == "Verb":
        gameplay.remove_phrase()
        if verb.stop_score == False:
            if verb.verb_score < 5:
                verb.verb_score += 1
                verb.verb_score_1 = verb.verb_score
                canvas.itemconfig(verb.verb_merits, text=f"Verb score = {verb.verb_score_1} / 5")
                verb.stop_score = True
                if verb.verb_score == 5:
                    verb.verb_score_complete = True
                ScoreClass.score_check()
            elif verb.verb_score == 5:
                verb.verb_score_complete = True
                ScoreClass.score_check()


def noun_button():
    noun.answer = "Noun"
    noun.button_reveal()
    if gameplay.sentence_word["Grammar"] == "Noun":
        gameplay.remove_phrase()
        if noun.stop_score == False:
            if noun.noun_score < 5:
                noun.noun_score += 1
                noun.noun_score_1 = noun.noun_score
                canvas.itemconfig(noun.noun_merits, text=f"Noun score = {noun.noun_score_1} / 5")
                noun.stop_score = True
                if noun.noun_score == 5:
                    noun.noun_score_complete = True
                ScoreClass.score_check()
            elif noun.noun_score == 5:
                noun.noun_score_complete = True
                ScoreClass.score_check()


def adverb_button():
    adverb.answer = "Adverb"
    adverb.button_reveal()
    if gameplay.sentence_word["Grammar"] == "Adverb":
        gameplay.remove_phrase()
        if adverb.stop_score == False:
            if adverb.adverb_score < 5:
                adverb.adverb_score += 1
                adverb.adverb_score_1 = adverb.adverb_score
                canvas.itemconfig(adverb.adverb_merits, text=f"Adverb score = {adverb.adverb_score_1} / 5")
                adverb.stop_score = True
                if adverb.adverb_score == 5:
                    adverb.adverb_score_complete = True
                ScoreClass.score_check()
            elif adverb.adverb_score == 5:
                adverb.adverb_score_complete = True
                ScoreClass.score_check()


def adjective_button():
    adjective.answer = "Adjective"
    adjective.button_reveal()
    if gameplay.sentence_word["Grammar"] == "Adjective":
        gameplay.remove_phrase()
        if adjective.stop_score == False:
            if adjective.adjective_score < 5:
                adjective.adjective_score += 1
                adjective.adjective_score_1 = adjective.adjective_score
                canvas.itemconfig(adjective.adjective_merits, text=f"Adjective score = {adjective.adjective_score_1} / 5")
                adjective.stop_score = True
                if adjective.adjective_score == 5:
                    adjective.adjective_score_complete = True
                ScoreClass.score_check()
            elif adjective.adjective_score == 5:
                adjective.adjective_score_complete = True
                ScoreClass.score_check()