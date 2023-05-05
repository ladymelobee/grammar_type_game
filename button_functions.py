from gameplay_functions import answer_reveal, remove_phrase, score_check


def verb_click():

    """When the player clicks on the verb button, this function checks if the word within the sentence is a verb.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    g = GamePlay()
    b = ButtonClass()
    s = ScoreClass()

    b.verb_score = b.verb_score_1
    g.answer = "Verb"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Verb":
        remove_phrase()
        if s.stop_score == False:
            if b.verb_score < 5:
                b.verb_score += 1
                b.verb_score_1 = b.verb_score
                canvas.itemconfig(b.verb_merits, text=f"Verb score = {b.verb_score_1} / 5")
                s.stop_score = True
                if b.verb_score == 5:
                    b.verb_score_complete = True
                score_check()
            elif b.verb_score == 5:
                b.verb_score_complete = True
                score_check()


def noun_click():

    """When the player clicks on the noun button, this function checks if the word within the sentence is a noun.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    g = GamePlay()
    b = ButtonClass()
    s = ScoreClass()

    b.noun_score = b.noun_score_1
    g.answer = "Noun"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Noun":
        remove_phrase()
        if s.stop_score == False:
            if b.noun_score < 5:
                b.noun_score += 1
                b.noun_score_1 = b.noun_score
                canvas.itemconfig(b.noun_merits, text=f"Noun score = {b.noun_score_1} / 5")
                s.stop_score = True
                if b.noun_score == 5:
                    b.noun_score_complete = True
                score_check()
            elif b.noun_score == 5:
                b.noun_score_complete = True
                score_check()


def adverb_click():

    """When the player clicks on the verb button, this function checks if the word within the sentence is an adverb.
    The player is informed and a description of what an adverb is, is displayed. The correct phrase is removed from
    the to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    g = GamePlay()
    b = ButtonClass()
    s = ScoreClass()

    b.adverb_score = b.adverb_score_1
    g.answer = "Adverb"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Adverb":
        remove_phrase()
        if s.stop_score == False:
            if b.adverb_score < 5:
                b.adverb_score += 1
                b.adverb_score_1 = b.adverb_score
                canvas.itemconfig(b.adverb_merits, text=f"Adverb score = {b.adverb_score_1} / 5")
                s.stop_score = True
                if b.adverb_score == 5:
                    b.adverb_score_complete = True
                score_check()
            elif b.adverb_score == 5:
                b.adverb_score_complete = True
                score_check()


def adjective_click():

    """When the player clicks on the adjective button, this function checks if the word within the sentence is an
    adjective.The player is informed and a description of what a verb is, is displayed. The correct phrase is removed
    from the to_learn dictionary, and the player is told their score."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay
    from score_class import ScoreClass
    from interface import canvas

    g = GamePlay()
    s = ScoreClass()
    b = ButtonClass()

    b.adjective_score = b.adjective_score_1
    g.answer = "Adjective"
    answer_reveal()
    if g.sentence_word["Grammar"] == "Adjective":
        remove_phrase()
        if s.stop_score == False:
            if b.adjective_score < 5:
                b.adjective_score += 1
                b.adjective_score_1 = b.adjective_score
                canvas.itemconfig(b.adjective_merits, text=f"Adjective score = {b.adjective_score_1} / 5")
                s.stop_score = True
                if b.adjective_score == 5:
                    b.adjective_score_complete = True
                score_check()
            elif b.adjective_score == 5:
                b.adjective_score_complete = True
                score_check()
