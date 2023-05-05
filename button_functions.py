from gameplay_functions import answer_reveal, remove_phrase, score_check


def verb_click():

    """When the player clicks on the verb button, this function checks if the word within the sentence is a verb.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    ButtonClass.verb_score = ButtonClass.verb_score_1
    GamePlay.answer = "Verb"
    answer_reveal()
    if GamePlay.sentence_word["Grammar"] == "Verb":
        remove_phrase()
        if ScoreClass.stop_score == False:
            if ButtonClass.verb_score < 5:
                ButtonClass.verb_score += 1
                ButtonClass.verb_score_1 = ButtonClass.verb_score
                canvas.itemconfig(ButtonClass.verb_merits, text=f"Verb score = {ButtonClass.verb_score_1} / 5")
                ScoreClass.stop_score = True
                if ButtonClass.verb_score == 5:
                    ButtonClass.verb_score_complete = True
                score_check()
            elif ButtonClass.verb_score == 5:
                ButtonClass.verb_score_complete = True
                score_check()


def noun_click():

    """When the player clicks on the noun button, this function checks if the word within the sentence is a noun.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    ButtonClass.noun_score = ButtonClass.noun_score_1
    GamePlay.answer = "Noun"
    answer_reveal()
    if GamePlay.sentence_word["Grammar"] == "Noun":
        remove_phrase()
        if ScoreClass.stop_score == False:
            if ButtonClass.noun_score < 5:
                ButtonClass.noun_score += 1
                ButtonClass.noun_score_1 = ButtonClass.noun_score
                canvas.itemconfig(ButtonClass.noun_merits, text=f"Noun score = {ButtonClass.noun_score_1} / 5")
                ScoreClass.stop_score = True
                if ButtonClass.noun_score == 5:
                    ButtonClass.noun_score_complete = True
                score_check()
            elif ButtonClass.noun_score == 5:
                ButtonClass.noun_score_complete = True
                score_check()


def adverb_click():

    """When the player clicks on the verb button, this function checks if the word within the sentence is an adverb.
    The player is informed and a description of what an adverb is, is displayed. The correct phrase is removed from
    the to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    ButtonClass.adverb_score = ButtonClass.adverb_score_1
    GamePlay.answer = "Adverb"
    answer_reveal()
    if GamePlay.sentence_word["Grammar"] == "Adverb":
        remove_phrase()
        if ScoreClass.stop_score == False:
            if ButtonClass.adverb_score < 5:
                ButtonClass.adverb_score += 1
                ButtonClass.adverb_score_1 = ButtonClass.adverb_score
                canvas.itemconfig(ButtonClass.adverb_merits, text=f"Adverb score = {ButtonClass.adverb_score_1} / 5")
                ScoreClass.stop_score = True
                if ButtonClass.adverb_score == 5:
                    ButtonClass.adverb_score_complete = True
                score_check()
            elif ButtonClass.adverb_score == 5:
                ButtonClass.adverb_score_complete = True
                score_check()


def adjective_click():

    """When the player clicks on the adjective button, this function checks if the word within the sentence is an
    adjective.The player is informed and a description of what a verb is, is displayed. The correct phrase is removed
    from the to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    ButtonClass.adjective_score = ButtonClass.adjective_score_1
    GamePlay.answer = "Adjective"
    answer_reveal()
    if GamePlay.sentence_word["Grammar"] == "Adjective":
        remove_phrase()
        if ScoreClass.stop_score == False:
            if ButtonClass.adjective_score < 5:
                ButtonClass.adjective_score += 1
                ButtonClass.adjective_score_1 = ButtonClass.adjective_score
                canvas.itemconfig(ButtonClass.adjective_merits, text=f"Adjective score = {ButtonClass.adjective_score_1} / 5")
                ScoreClass.stop_score = True
                if ButtonClass.adjective_score == 5:
                    ButtonClass.adjective_score_complete = True
                score_check()
            elif ButtonClass.adjective_score == 5:
                ButtonClass.adjective_score_complete = True
                score_check()
