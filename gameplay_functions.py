import pandas
import os
from random import choice


def start_game():

    from button_functions import verb_click, adverb_click, adjective_click, noun_click
    from interface import verb_button, adverb_button, adjective_button, noun_button, verb_img, adverb_img, \
        adjective_img, noun_img, card_text_grammar_des, card_text_sentence, canvas, card_text_word

    """The random word function is the opening program, and starts the game by generating a random word/sentence from
    the to_learn dictionary. It also resets the answer and stop_score variables, to allow for the game to
    be replayed."""

    from gameplay_class import GamePlay
    from score_class import ScoreClass

    g = GamePlay()
    s = ScoreClass()

    try:
        data = pandas.read_csv("grammar_type_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("grammar_project.csv")
        g.to_learn = original_data.to_dict(orient="records")
    else:
        g.to_learn = data.to_dict(orient="records")

    g.answer = ""
    s.stop_score = False
    verb_button.configure(image=verb_img,
                          command=verb_click, fg="Black"),
    adverb_button.configure(image=adverb_img,
                            command=adverb_click,
                            fg="Black"),
    adjective_button.configure(image=adjective_img,
                               command=adjective_click,
                               fg="Black"),
    noun_button.configure(
        image=noun_img,
        command=noun_click,
        fg="Black")

    canvas.itemconfig(card_text_grammar_des, text="")
    g.sentence_word = choice(g.to_learn)
    canvas.itemconfig(card_text_sentence, text=g.sentence_word["Sentence"], fill="black")
    canvas.itemconfig(card_text_word, text=g.sentence_word["Word"], fill="black")

    score_check()


def answer_reveal():

    from interface import verb_button, adverb_button, adjective_button, noun_button, card_text_grammar_des, canvas, \
        card_text_word, clear_button

    YELLOW = "#e9bc4b"
    GREEN = "#65c941"
    ORANGE = "#ee8231"
    PURPLE = "#b35ed8"

    """After the player has made their choice, the answer_reveal function checks if the player's choice is correct, and
    presents the answer to the player. This function also temporarily disables the grammar buttons, until the player
    uses the continue button."""

    from gameplay_class import GamePlay

    g = GamePlay()

    if g.sentence_word["Grammar"] == "Noun":
        canvas.itemconfig(card_text_word,
                          text=g.sentence_word['Word'],
                          fill=GREEN)
        if g.answer == "Noun":
            canvas.itemconfig(card_text_grammar_des,
                              text=f"Correct! Well done. {g.sentence_word['Word']} is a noun.\nA noun is a word "
                                   f"used to identify people, places or things.",
                              fill=GREEN)
        else:
            canvas.itemconfig(card_text_grammar_des,
                              text=f"{g.sentence_word['Word']} is a noun. \nA noun is a word used to identify "
                                   f"people, places or things.",
                              fill=GREEN)
            if_wrong_answer()
        verb_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(
            image=clear_button,
            command=do_nothing,
            fg="White"),
        adverb_button.configure(image=clear_button,
                                command=do_nothing,
                                fg="White"),
        noun_button.configure(command=do_nothing)
    elif g.sentence_word["Grammar"] == "Verb":
        canvas.itemconfig(card_text_word,
                          text=g.sentence_word['Word'],
                          fill=PURPLE)
        if g.answer == "Verb":
            canvas.itemconfig(card_text_grammar_des,
                              text=f"Correct! Well done. {g.sentence_word['Word']} is a verb.\nA verb is a "
                                   f"word that describes what the subject is doing.",
                              fill=PURPLE)
        else:
            canvas.itemconfig(card_text_grammar_des,
                              text=f"{g.sentence_word['Word']} is a verb. \nA verb is a word that describes "
                                   f"what the subject is doing.",
                              fill=PURPLE)
            if_wrong_answer()
        noun_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(image=clear_button,
                                   command=do_nothing,
                                   fg="White"),
        adverb_button.configure(image=clear_button,
                                command=do_nothing,
                                fg="White"),
        verb_button.configure(command=do_nothing)
    elif g.sentence_word["Grammar"] == "Adverb":
        canvas.itemconfig(card_text_word,
                          text=g.sentence_word['Word'],
                          fill=ORANGE)
        if g.answer == "Adverb":
            canvas.itemconfig(card_text_grammar_des,
                              text=f"Correct! Well done. {g.sentence_word['Word']} is an adverb.\nAn adverb "
                                   f"is a word that describes how an action is carried out.",
                              fill=ORANGE)
        else:
            canvas.itemconfig(card_text_grammar_des,
                              text=f"{g.sentence_word['Word']} is an adverb. \nAn adverb is a word that "
                                   f"describes how an action is carried out.",
                              fill=ORANGE)
            if_wrong_answer()
        verb_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(image=clear_button,
                                   command=do_nothing,
                                   fg="White"),
        noun_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adverb_button.configure(command=do_nothing)
    else:
        canvas.itemconfig(card_text_word,
                          text=g.sentence_word['Word'],
                          fill=YELLOW)
        if g.answer == "Adjective":
            canvas.itemconfig(card_text_grammar_des,
                              text=f"Correct! Well done. {g.sentence_word['Word']} is an adjective. "
                                   f"\nAn adjective is a word that describes a person, place or thing.",
                              fill=YELLOW)
        else:
            canvas.itemconfig(card_text_grammar_des,
                              text=f"{g.sentence_word['Word']} is an adjective. \nAn adjective is a word "
                                   f"that describes a person, place or thing.",
                              fill=YELLOW)
            if_wrong_answer()
        verb_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adverb_button.configure(image=clear_button,
                                command=do_nothing,
                                fg="White"),
        noun_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(command=do_nothing)


def score_check():

    """score_check ends the game if the player has completed 20 correct answers."""

    from buttons_class import ButtonClass
    from gameplay_class import GamePlay

    g = GamePlay()
    b = ButtonClass()

    try:
        data = pandas.read_csv("grammar_type_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("grammar_project.csv")
        g.to_learn = original_data.to_dict(orient="records")
    else:
        g.to_learn = data.to_dict(orient="records")

    if b.verb_score_complete and b.noun_score_complete and b.adjective_score_complete and \
            b.adverb_score_complete == True:
        end_game()
    else:
        pass
    if len(g.to_learn) < 1:
        os.remove("grammar_type_to_learn.csv")


def remove_phrase():

    """If the player guesses the correct grammar type for the sentence, the sentence/word is removed from the
    to_learn dictionary."""

    from gameplay_class import GamePlay

    g = GamePlay()

    g.to_learn.remove(g.sentence_word)
    print(len(g.to_learn))
    data = pandas.DataFrame(g.to_learn)
    data.to_csv("grammar_type_to_learn.csv", index=False)


def if_wrong_answer():

    """If the player chooses the wrong answer,  their tries are reduced by 1 point. 5 wrong tries and the game ends.
    The player can restart the game to try and beat their old score."""

    from gameplay_class import GamePlay

    g = GamePlay()

    g.guess -= 1
    if g.guess == 0:
        end_game()


def do_nothing():
    """After the player has used a grammar type button, the button's command function is temporarily disabled using this
    function (do_nothing), to prevent the function running again, whilst the proceeding functions complete."""
    pass


def end_game():

    from interface import verb_button, adverb_button, adjective_button, noun_button, card_text_grammar_des, \
        card_text_sentence, canvas, card_text_word, clear_button, end_button, continue_button, new_score_text, \
        old_score_text, top_score_text

    """The end function is activated when the player uses the 'end' button. The function tells the player how many
    merits they achieved. If they completed the game, by choosing 20 correct answers, then they achieve an extra 20
    merits, earning 40 merits in total."""

    from score_class import ScoreClass
    from buttons_class import ButtonClass

    b = ButtonClass()
    s = ScoreClass()

    total_merits = b.adverb_score_1 + b.verb_score_1 + b.adjective_score_1 + b.noun_score_1
    max_score = total_merits + 20
    end_button.configure(text="End",
                         command=do_nothing,
                         fg="White")
    continue_button.configure(text="Reset",
                              command=reset_game,
                              fg="White")
    if b.verb_score_complete and b.noun_score_complete and b.adjective_score_complete and \
            b.adverb_score_complete == True:
        s.new_score = max_score
        s.top_score = max_score
        canvas.itemconfig(card_text_sentence,
                          text=f"Well done! You scored {total_merits} merits!\nPlus an extra 20 merits for completing "
                               f"the game!\nYour final score is {max_score}!")
        canvas.itemconfig(card_text_word,
                          text="End Game",
                          fill="black")
        canvas.itemconfig(card_text_grammar_des,
                          text="")
        verb_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adverb_button.configure(image=clear_button,
                                command=do_nothing,
                                fg="White"),
        noun_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(image=clear_button, fg="White")
    else:
        s.new_score = total_merits
        if s.new_score > s.old_score:
            s.top_score = total_merits
        else:
            pass
        canvas.itemconfig(card_text_sentence, text=f"You scored {total_merits} merits!")
        canvas.itemconfig(card_text_word,
                          text="End Game",
                          fill="black")
        canvas.itemconfig(card_text_grammar_des,
                          text="")
        verb_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adverb_button.configure(image=clear_button,
                                command=do_nothing,
                                fg="White"),
        noun_button.configure(image=clear_button,
                              command=do_nothing,
                              fg="White"),
        adjective_button.configure(image=clear_button,
                                   command=do_nothing,
                                   fg="White")
    canvas.itemconfig(new_score_text, text=f"New score = {s.new_score}")
    canvas.itemconfig(old_score_text, text=f"Old score = {s.old_score}")
    canvas.itemconfig(top_score_text, text=f"Top score = {s.top_score}")


def reset_game():

    from interface import canvas, end_button, continue_button, new_score_text, old_score_text
    from score_class import ScoreClass
    from buttons_class import ButtonClass
    from gameplay_class import GamePlay

    b = ButtonClass()
    g = GamePlay()
    s = ScoreClass()

    g.guess = 5
    b.adverb_score_1 = 0
    b.verb_score_1 = 0
    b.adjective_score_1 = 0
    b.noun_score_1 = 0
    b.adverb_score_complete = False
    b.verb_score_complete = False
    b.noun_score_complete = False
    b.adjective_score_complete = False

    os.remove("grammar_type_to_learn.csv")

    end_button.configure(text="End", command=end_game, fg="White")
    continue_button.configure(text="Continue", command=start_game, fg="White")
    if s.new_score > s.old_score:
        s.top_score = s.new_score
    else:
        s.top_score = s.old_score
    s.old_score = s.new_score
    s.new_score = 0

    canvas.itemconfig(new_score_text, text=f"New score = {s.new_score}")
    canvas.itemconfig(old_score_text, text=f"Old score = {s.old_score}")

    start_game()
