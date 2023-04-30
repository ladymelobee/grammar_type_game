from random import choice
import pandas
from button_objects import gameplay, verb, adverb, adjective, noun, score, verb_button
from interface import verb_img, adjective_img, adverb_img, noun_img, canvas, card_text_grammar_des, card_text_sentence, \
    card_text_word, end_button, continue_button, clear_button


class GamePlay:
    def __init__(self):
        self.to_learn = {}
        self.sentence_word = {}
        self.guess = 5
        self.answer = ""
        self.back = False

    def start_game(self):
        verb.configure(image=verb_img,
                       command=verb_button,
                       fg="Black")
        adverb.configure(image=adverb_img,
                         command=adverb,
                         fg="Black"),
        adjective.configure(image=adjective_img,
                            command=adjective,
                            fg="Black")
        noun.configure(image=noun_img,
                       command=noun,
                       fg="Black")
        canvas.itemconfig(card_text_grammar_des, text="")
        sentence_word = choice(gameplay.to_learn)
        canvas.itemconfig(card_text_sentence,
                          text=sentence_word["Sentence"],
                          fill="black")
        canvas.itemconfig(card_text_word,
                          text=sentence_word["Word"],
                          fill="black")
        score.score_check()

    def end(self):
        total_merits = adverb.adverb_score_1 + verb.verb_score_1 + adjective.adjective_score_1 + noun.noun_score_1
        max_score = total_merits + 20
        end_button.configure(text="End",
                             command=gameplay.button_do_nothing,
                             fg="White")
        continue_button.configure(text="Reset",
                                  command=gameplay.reset_game,
                                  fg="White")
        if verb.verb_score_complete and noun.noun_score_complete and adjective.adjective_score_complete and \
                adverb.adverb_score_complete == True:
            score.new_score = max_score
            score.top_score = max_score
            canvas.itemconfig(card_text_sentence,
                              text=f"Well done! You scored {total_merits} merits!\nPlus an extra "
                              f"20 merits for completing the game!"
                              f"\nYour final score is {max_score}!")
            canvas.itemconfig(card_text_word,
                              text="End Game",
                              fill="black")
            canvas.itemconfig(card_text_grammar_des,
                              text="")
            verb_button.configure(image=clear_button,
                                  command=gameplay.button_do_nothing,
                                  fg="White"),
            adverb.configure(image=clear_button,
                             command=gameplay.button_do_nothing,
                             fg="White"),
            noun.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(image=clear_button,
                                fg="White")
        else:
            new_score = total_merits
            if new_score > score.old_score:
                score.top_score = total_merits
            canvas.itemconfig(card_text_sentence,
                              text=f"You scored {total_merits} merits!")
            canvas.itemconfig(card_text_word,
                              text="End Game",
                              fill="black")
            canvas.itemconfig(card_text_grammar_des,
                              text="")
            verb_button.configure(image=clear_button,
                                  command=gameplay.button_do_nothing,
                                  fg="White"),
            adverb.configure(image=clear_button,
                             command=gameplay.button_do_nothing,
                             fg="White"),
            noun.configure(image=clear_button,
                           command=gameplay.button_do_nothing,
                           fg="White"),
            adjective.configure(image=clear_button,
                                command=gameplay.button_do_nothing,
                                fg="White")
        canvas.itemconfig(new_score_text,
                          text=f"New score = {score.new_score}")
        canvas.itemconfig(old_score_text,
                          text=f"Old score = {score.old_score}")
        canvas.itemconfig(top_score_text,
                          text=f"Top score = {score.top_score}")

    def reset_game(self):
        score.guess = 5
        adverb.adverb_score_1 = 0
        verb.verb_score_1 = 0
        adjective.adjective_score_1 = 0
        noun.noun_score_1 = 0
        adverb.adverb_score_complete = False
        verb.verb_score_complete = False
        noun.noun_score_complete = False
        adjective.adjective_score_complete = False
        os.remove("grammar_type_to_learn.csv")
        end_button.configure(text="End",
                             command=gameplay.end,
                             fg="White")
        continue_button.configure(text="Continue",
                                  command=gameplay.start_game,
                                  fg="White")
        if score.new_score > score.old_score:
            score.top_score = score.new_score
        else:
            score.top_score = score.old_score
        old_score = score.new_score
        new_score = 0
        canvas.itemconfig(new_score_text,
                          text=f"New score = {new_score}")
        canvas.itemconfig(old_score_text,
                          text=f"Old score = {old_score}")
        gameplay.start_game()

    def remove_phrase(self):
        gameplay.to_learn.remove(gameplay.sentence_word)
        print(len(gameplay.to_learn))
        data = pandas.DataFrame(gameplay.to_learn)
        data.to_csv("grammar_type_to_learn.csv", index=False)