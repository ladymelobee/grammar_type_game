from gameplay_functions import answer_reveal, remove_phrase, score_check
from gameplay_class import GamePlay
from score_class import ScoreClass
from interface import canvas

g = GamePlay()
s = ScoreClass()


def verb_click():

    """This function checks if the word within the sentence is a verb."""
    
    #When the player clicks on the 'verb' button, a description of what a verb is, is displayed. 
    #If the player chose correctly, the correct phrase is removed from the 'to_learn dictionary', 
    #and the player is told their score.

    s.verb_score = s.verb_score_1
    g.answer = "Verb"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Verb":
        remove_phrase()
        if not s.stop_score:
            if s.verb_score < 5:
                s.verb_score += 1
                s.verb_score_1 = s.verb_score
                canvas.itemconfig(s.verb_merits, text=f"Verb score = {s.verb_score_1} / 5")
                s.stop_score = True
                if s.verb_score == 5:
                    s.verb_score_complete = True
                score_check()
            elif s.verb_score == 5:
                s.verb_score_complete = True
                score_check()


def noun_click():

    """This function checks if the word within the sentence is a noun."""
    
    #When the player clicks on the 'noun' button, a description of what a noun is, is displayed. 
    #If the player chose correctly, the correct phrase is removed from the 'to_learn dictionary', 
    #and the player is told their score.

    s.noun_score = s.noun_score_1
    g.answer = "Noun"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Noun":
        remove_phrase()
        if not s.stop_score:
            if s.noun_score < 5:
                s.noun_score += 1
                s.noun_score_1 = s.noun_score
                canvas.itemconfig(s.noun_merits, text=f"Noun score = {s.noun_score_1} / 5")
                s.stop_score = True
                if s.noun_score == 5:
                    s.noun_score_complete = True
                score_check()
            elif s.noun_score == 5:
                s.noun_score_complete = True
                score_check()


def adverb_click():

    """This function checks if the word within the sentence is a adverb."""
    
    #When the player clicks on the 'adverb' button, a description of what a adverb is, is displayed. 
    #If the player chose correctly, the correct phrase is removed from the 'to_learn dictionary', 
    #and the player is told their score.

    s.adverb_score = s.adverb_score_1
    g.answer = "Adverb"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Adverb":
        remove_phrase()
        if not s.stop_score:
            if s.adverb_score < 5:
                s.adverb_score += 1
                s.adverb_score_1 = s.adverb_score
                canvas.itemconfig(s.adverb_merits, text=f"Adverb score = {s.adverb_score_1} / 5")
                s.stop_score = True
                if s.adverb_score == 5:
                    s.adverb_score_complete = True
                score_check()
            elif s.adverb_score == 5:
                s.adverb_score_complete = True
                score_check()


def adjective_click():

    """This function checks if the word within the sentence is a adjective."""
    
    #When the player clicks on the 'adjective' button, a description of what a adjective is, is displayed. 
    #If the player chose correctly, the correct phrase is removed from the 'to_learn dictionary', 
    #and the player is told their score.

    s.adjective_score = s.adjective_score_1
    g.answer = "Adjective"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Adjective":
        remove_phrase()
        if not s.stop_score:
            if s.adjective_score < 5:
                s.adjective_score += 1
                s.adjective_score_1 = s.adjective_score
                canvas.itemconfig(s.adjective_merits, text=f"Adjective score = {s.adjective_score_1} / 5")
                s.stop_score = True
                if s.adjective_score == 5:
                    s.adjective_score_complete = True
                score_check()
            elif s.adjective_score == 5:
                s.adjective_score_complete = True
                score_check()
