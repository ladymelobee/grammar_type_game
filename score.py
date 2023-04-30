import os
import pandas
from button_objects import verb, adverb, gameplay, adjective, noun
from interface import canvas


class ScoreClass:
    def __init__(self):
        self.old_score = 0
        self.top_score = 0
        self.new_score = 0
        self.click_score = ""
        self.click_score_complete = False
        self.stop_score = False

        self.score_text = canvas.create_text(200, 450,
                                             fill="",
                                             text=f" score = ",
                                             font=("Ariel", 16, "bold"))
        canvas.grid(column=0, row=0)

    def score_check(self):
        if verb.verb_score_complete and noun.noun_score_complete and adjective.adjective_score_complete and \
                adverb.adverb_score_complete == True:
            gameplay.end()
        if len(gameplay.to_learn) < 1:
            os.remove("grammar_type_to_learn.csv")
            try:
                data = pandas.read_csv("grammar_type_to_learn.csv")
            except FileNotFoundError:
                original_data = pandas.read_csv("grammar_project.csv")
                gameplay.to_learn = original_data.to_dict(orient="records")
            else:
                gameplay.to_learn = data.to_dict(orient="records")


class Merits:
    def __init__(self):
        self.merits = canvas.create_text(711, 30,
                                         fill="",
                                         text=f" score =  / 5",
                                         font=("Ariel", 13, "bold"))
        self.canvas.grid(column=0, row=0)




