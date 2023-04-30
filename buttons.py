from tkinter import PhotoImage, Button, CENTER
from button_objects import gameplay, verb, adverb, adjective, noun, score
from interface import canvas, card_text_word, card_text_grammar_des, GREEN, clear_button, PURPLE, ORANGE, YELLOW, \
    adjective_merits
import pandas


class ButtonClass:
    def __init__(self):
        self.adverb_score = 0
        self.verb_score = 0
        self.adjective_score = 0
        self.noun_score = 0

        self.adverb_score_1 = 0
        self.verb_score_1 = 0
        self.adjective_score_1 = 0
        self.noun_score_1 = 0

        self.adverb_score_complete = False
        self.verb_score_complete = False
        self.noun_score_complete = False
        self.adjective_score_complete = False

        self.noun_merits = 0
        self.verb_merits = 0
        self.adjective_merits = 0
        self.adverb_merits = 0

    button_img = PhotoImage(file="")
    button = Button(image='',
                    highlightthickness=0,
                    text='',
                    compound=CENTER,
                    font=("Ariel", 20, "bold"),
                    command='')
    button.grid(column=0, row=0)

    def button_reveal(self):
        if gameplay.sentence_word["Grammar"] == "Noun":
            canvas.itemconfig(card_text_word,
                              text=gameplay.sentence_word['Word'],
                              fill=GREEN)
            if gameplay.answer == "Noun":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {gameplay.sentence_word['Word']} is a noun. "
                                  f"\nA noun is a word used to "f"identify people, places or "
                                  f"things.", fill=GREEN)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{gameplay.sentence_word['Word']} is a noun. \nA noun is a word "
                                  f"used to "f"identify people, places or things.",
                                  fill=GREEN)
                gameplay.if_wrong_answer()
            verb.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(image=clear_button,
                                command=gameplay.button_do_nothing,
                                fg="White"),
            adverb.configure(image=clear_button,
                             command=gameplay.button_do_nothing,
                             fg="White"),
            noun.configure(command=gameplay.button_do_nothing)
        elif gameplay.sentence_word["Grammar"] == "Verb":
            canvas.itemconfig(card_text_word,
                              text=gameplay.sentence_word['Word'],
                              fill=PURPLE)
            if gameplay.answer == "Verb":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {gameplay.sentence_word['Word']} is a verb. "
                                  f"\nA verb is a word that describes what the subject is "
                                  f"doing.", fill=PURPLE)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{gameplay.sentence_word['Word']} is a verb. \nA verb is a word that "
                                  f"describes what the subject is doing.", fill=PURPLE)
                gameplay.if_wrong_answer()
            noun.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(image=clear_button,
                                command=gameplay.button_do_nothing,
                                fg="White"),
            adverb.configure(image=clear_button,
                             command=gameplay.button_do_nothing,
                             fg="White"),
            verb.configure(command=gameplay.button_do_nothing)
        elif gameplay.sentence_word["Grammar"] == "Adverb":
            canvas.itemconfig(card_text_word,
                              text=gameplay.sentence_word['Word'],
                              fill=ORANGE)
            if gameplay.answer == "Adverb":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {gameplay.sentence_word['Word']} is an adverb. "
                                  f"\nAn adverb is a word that describes how an action is "
                                  f"carried out.", fill=ORANGE)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{gameplay.sentence_word['Word']} is an adverb. \nAn adverb is a "
                                  f"word that describes how an action is carried out.",
                                  fill=ORANGE)
                gameplay.if_wrong_answer()
            verb.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(image=clear_button,
                                command=gameplay.button_do_nothing,
                                fg="White"),
            noun.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adverb.configure(
                command=gameplay.button_do_nothing)
        else:
            canvas.itemconfig(card_text_word,
                              text=gameplay.sentence_word['Word'],
                              fill=YELLOW)
            if gameplay.answer == "Adjective":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {gameplay.sentence_word['Word']} is an "
                                  f"adjective. \nAn adjective is a word that describes a "
                                  f"person, place or thing.", fill=YELLOW)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{gameplay.sentence_word['Word']} is an adjective. \nAn adjective "
                                       f"is a word that describes a person, place or thing.",
                                  fill=YELLOW)
                gameplay.if_wrong_answer()
            verb.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adverb.configure(image=clear_button,
                             command=gameplay.button_do_nothing,
                             fg="White"),
            noun.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(command=gameplay.button_do_nothing)

    def button_action(self):
        if gameplay.sentence_word["Grammar"] == "":
            gameplay.to_learn.remove(gameplay.sentence_word)
            print(len(gameplay.to_learn))
            data = pandas.DataFrame(gameplay.to_learn)
            data.to_csv("grammar_type_to_learn.csv", index=False)
        if score.stop_score == False:
            if score.click_score < 5:
                score.click_score += 1
                adjective_score_1 = score.click_score
                canvas.itemconfig(adjective_merits,
                                  text=f"Adjective score = {adjective_score_1} / 5")
                score.stop_score = True
                if score.click_score == 5:
                    score.click_score_complete = True
                score.score_check()
            elif score.click_score == 5:
                score.click_score_complete = True
                score.score_check()

    def if_wrong_answer(self):
        gameplay.guess -= 1
        if gameplay.guess == 0:
            gameplay.end()

    def button_do_nothing(self):
        pass







