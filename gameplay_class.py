import pandas
import os
from random import choice
from score_class import ScoreClass
from button_class import WordButton

s = ScoreClass()

noun_word_button = WordButton("Noun")
adverb_word_button = WordButton("Adverb")
verb_word_button = WordButton("Verb")
adjective_word_button = WordButton("Adjective")

YELLOW = "#e9bc4b"
GREEN = "#65c941"
ORANGE = "#ee8231"
PURPLE = "#b35ed8"


class GamePlay:
    def __init__(self):
        self.to_learn = {}
        self.sentence_word = {}
        self.guess = 5
        self.answer = ""
        self.back = False
        
    def click_button(self, s, button):

        """This function checks if the word within the sentence is a verb."""

        # When the player clicks on the 'verb' button, a description of what a verb is, is displayed. 
        # If the player chose correctly, the correct phrase is removed from the 'to_learn dictionary', 
        # and the player is told their score.

        from interface import canvas, verb_merits, noun_merits, adjective_merits, adverb_merits

        self.answer = button.answer
        print(self.answer)
        self.answer_reveal()
        if self.sentence_word["Grammar"] == self.answer:
            self.remove_phrase()
            if not s.stop_score:
                subscore = s.word_type_score[self.answer]
                if not subscore.is_complete:
                    subscore.current_score += 1
                    if self.answer == "Verb":
                        canvas.itemconfig(verb_merits,
                                          text=f"{self.answer} "
                                               f"score = {subscore.current_score} / {subscore.target_score}")
                        s.verb_score_1 = subscore.current_score
                    elif self.answer == "Noun":
                        canvas.itemconfig(noun_merits,
                                          text=f"{self.answer} "
                                               f"score = {subscore.current_score} / {subscore.target_score}")
                        s.noun_score_1 = subscore.current_score
                    elif self.answer == "Adverb":
                        canvas.itemconfig(adverb_merits,
                                          text=f"{self.answer} "
                                               f"score = {subscore.current_score} / {subscore.target_score}")
                        s.adverb_score_1 = subscore.current_score
                    elif self.answer == "Adjective":
                        canvas.itemconfig(adjective_merits,
                                          text=f"{self.answer} "
                                               f"score = {subscore.current_score} / {subscore.target_score}")
                        s.adjective_score_1 = subscore.current_score

                    s.stop_score = True
                    if subscore.current_score == subscore.target_score:
                        subscore.is_complete = True
                    self.score_check()

    def start_game(self):

        from interface import verb_button, adverb_button, adjective_button, noun_button, verb_img, adverb_img, \
            adjective_img, noun_img, card_text_grammar_des, card_text_sentence, canvas, card_text_word

        """This function generates a random word/sentence from the to_learn dictionary. 
        It also resets the answer and stop_score variables, to allow for the game to
        be replayed."""

        try:
            data = pandas.read_csv("grammar_type_to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("grammar_project.csv")
            self.to_learn = original_data.to_dict(orient="records")
        else:
            self.to_learn = data.to_dict(orient="records")

        self.answer = ""
        s.stop_score = False
        verb_button.configure(image=verb_img,
                              command=lambda: self.click_button(s, verb_word_button), fg="Black"),
        adverb_button.configure(image=adverb_img,
                                command=lambda: self.click_button(s, adverb_word_button),
                                fg="Black"),
        adjective_button.configure(image=adjective_img,
                                   command=lambda: self.click_button(s, adjective_word_button),
                                   fg="Black"),
        noun_button.configure(
            image=noun_img,
            command=lambda: self.click_button(s, noun_word_button),
            fg="Black")

        canvas.itemconfig(card_text_grammar_des, text="")
        self.sentence_word = choice(self.to_learn)
        canvas.itemconfig(card_text_sentence, text=self.sentence_word["Sentence"], fill="black")
        canvas.itemconfig(card_text_word, text=self.sentence_word["Word"], fill="black")

        self.score_check()

    def answer_reveal(self):

        from interface import verb_button, adverb_button, adjective_button, noun_button, card_text_grammar_des, \
            canvas, \
            card_text_word, clear_button

        """This function checks if the player's choice is correct, and presents the answer to the player. 
        This function also changes the grammar type button's command function, to run the do_nothing function."""

        if self.sentence_word["Grammar"] == "Noun":
            canvas.itemconfig(card_text_word,
                              text=self.sentence_word['Word'],
                              fill=GREEN)
            if self.answer == "Noun":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {self.sentence_word['Word']} is a noun.\nA noun is a word "
                                       f"used to identify people, places or things.",
                                  fill=GREEN)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{self.sentence_word['Word']} is a noun. \nA noun is a word used to identify "
                                       f"people, places or things.",
                                  fill=GREEN)
                self.if_wrong_answer()
            verb_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adjective_button.configure(
                image=clear_button,
                command=self.do_nothing,
                fg="White"),
            adverb_button.configure(image=clear_button,
                                    command=self.do_nothing,
                                    fg="White"),
            noun_button.configure(command=self.do_nothing)
        elif self.sentence_word["Grammar"] == "Verb":
            canvas.itemconfig(card_text_word,
                              text=self.sentence_word['Word'],
                              fill=PURPLE)
            if self.answer == "Verb":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {self.sentence_word['Word']} is a verb.\nA verb is a "
                                       f"word that describes what the subject is doing.",
                                  fill=PURPLE)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{self.sentence_word['Word']} is a verb. \nA verb is a word that describes "
                                       f"what the subject is doing.",
                                  fill=PURPLE)
                self.if_wrong_answer()
            noun_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adjective_button.configure(image=clear_button,
                                       command=self.do_nothing,
                                       fg="White"),
            adverb_button.configure(image=clear_button,
                                    command=self.do_nothing,
                                    fg="White"),
            verb_button.configure(command=self.do_nothing)
        elif self.sentence_word["Grammar"] == "Adverb":
            canvas.itemconfig(card_text_word,
                              text=self.sentence_word['Word'],
                              fill=ORANGE)
            if self.answer == "Adverb":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {self.sentence_word['Word']} is an adverb.\nAn adverb "
                                       f"is a word that describes how an action is carried out.",
                                  fill=ORANGE)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{self.sentence_word['Word']} is an adverb. \nAn adverb is a word that "
                                       f"describes how an action is carried out.",
                                  fill=ORANGE)
                self.if_wrong_answer()
            verb_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adjective_button.configure(image=clear_button,
                                       command=self.do_nothing,
                                       fg="White"),
            noun_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adverb_button.configure(command=self.do_nothing)
        else:
            canvas.itemconfig(card_text_word,
                              text=self.sentence_word['Word'],
                              fill=YELLOW)
            if self.answer == "Adjective":
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"Correct! Well done. {self.sentence_word['Word']} is an adjective. "
                                       f"\nAn adjective is a word that describes a person, place or thing.",
                                  fill=YELLOW)
            else:
                canvas.itemconfig(card_text_grammar_des,
                                  text=f"{self.sentence_word['Word']} is an adjective. \nAn adjective is a word "
                                       f"that describes a person, place or thing.",
                                  fill=YELLOW)
                self.if_wrong_answer()
            verb_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adverb_button.configure(image=clear_button,
                                    command=self.do_nothing,
                                    fg="White"),
            noun_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adjective_button.configure(command=self.do_nothing)

    def score_check(self):

        """This function checks if the player has completed 20 correct answers. If so, this function runs the 
        end_game function. This function also checks the length of the 'to_learn' dictionary. If the dictionary 
        has less than one entry, this function removes the "grammar_type_to_learn.csv", so that it can be recreated 
        with a full amount of entries."""

        try:
            data = pandas.read_csv("grammar_type_to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("grammar_project.csv")
            self.to_learn = original_data.to_dict(orient="records")
        else:
            self.to_learn = data.to_dict(orient="records")

        if s.verb_score_complete and s.noun_score_complete and s.adjective_score_complete and \
                s.adverb_score_complete == True:
            self.end_game()
        else:
            pass
        if len(self.to_learn) < 1:
            os.remove("grammar_type_to_learn.csv")

    def remove_phrase(self):

        """This function removes the current sentence/word from the to_learn dictionary."""

        self.to_learn.remove(self.sentence_word)
        print(len(self.to_learn))
        data = pandas.DataFrame(self.to_learn)
        data.to_csv("grammar_type_to_learn.csv", index=False)

    def if_wrong_answer(self):

        """This function reduces the player's lives by 1 point. The player has 5 lives. This function also checks if 
        the player has 0 lives, if so, then this function runs another function which ends the game."""

        # If the player chooses the wrong answer, their tries are reduced by 1 point. 5 wrong tries and the game ends.
        # The player can restart the game to try and beat their old score.

        self.guess -= 1
        if self.guess == 0:
            self.end_game()

    def do_nothing(self):
        """This function does nothing."""
        # This function temporarily disables the grammar type button's command function, so that the player cannot
        # reuse the button during the result reveal moment.
        pass

    def end_game(self):

        from interface import verb_button, adverb_button, adjective_button, noun_button, card_text_grammar_des, \
            card_text_sentence, canvas, card_text_word, clear_button, end_button, continue_button, new_score_text, \
            old_score_text, top_score_text

        """This function stops the game and tells the player how many merits they achieved."""

        total_merits = s.adverb_score_1 + s.verb_score_1 + s.adjective_score_1 + s.noun_score_1
        max_score = total_merits + 20
        end_button.configure(text="End",
                             command=self.do_nothing,
                             fg="White")
        continue_button.configure(text="Reset",
                                  command=self.reset_game,
                                  fg="White")
        if s.verb_score_complete and s.noun_score_complete and s.adjective_score_complete and s.adverb_score_complete \
                == True:
            s.new_score = max_score
            s.top_score = max_score
            canvas.itemconfig(card_text_sentence,
                              text=f"Well done! You scored {total_merits} "
                                   f"merits!\nPlus an extra 20 merits for completing "
                                   f"the game!\nYour final score is {max_score}!")
            canvas.itemconfig(card_text_word,
                              text="End Game",
                              fill="black")
            canvas.itemconfig(card_text_grammar_des,
                              text="")
            verb_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adverb_button.configure(image=clear_button,
                                    command=self.do_nothing,
                                    fg="White"),
            noun_button.configure(image=clear_button,
                                  command=self.do_nothing,
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
                                  command=self.do_nothing,
                                  fg="White"),
            adverb_button.configure(image=clear_button,
                                    command=self.do_nothing,
                                    fg="White"),
            noun_button.configure(image=clear_button,
                                  command=self.do_nothing,
                                  fg="White"),
            adjective_button.configure(image=clear_button,
                                       command=self.do_nothing,
                                       fg="White")
        canvas.itemconfig(new_score_text, text=f"New score = {s.new_score}")
        canvas.itemconfig(old_score_text, text=f"Old score = {s.old_score}")
        canvas.itemconfig(top_score_text, text=f"Top score = {s.top_score}")

    def reset_game(self):

        """This function resets all game values to their starting position."""

        from interface import canvas, end_button, continue_button, new_score_text, old_score_text

        self.guess = 5
        s.adverb_score_1 = 0
        s.verb_score_1 = 0
        s.adjective_score_1 = 0
        s.noun_score_1 = 0
        s.adverb_score_complete = False
        s.verb_score_complete = False
        s.noun_score_complete = False
        s.adjective_score_complete = False

        os.remove("grammar_type_to_learn.csv")

        end_button.configure(text="End", command=self.end_game, fg="White")
        continue_button.configure(text="Continue", command=self.start_game, fg="White")
        if s.new_score > s.old_score:
            s.top_score = s.new_score
        else:
            s.top_score = s.old_score
        s.old_score = s.new_score
        s.new_score = 0

        canvas.itemconfig(new_score_text, text=f"New score = {s.new_score}")
        canvas.itemconfig(old_score_text, text=f"Old score = {s.old_score}")

        self.start_game()
