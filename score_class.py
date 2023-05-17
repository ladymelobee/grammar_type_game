class ScoreClass:
    def __init__(self):
        self.old_score = 0
        self.top_score = 0
        self.new_score = 0
        self.click_score = ""
        self.click_score_complete = False
        self.stop_score = False

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

        self.word_type_score = {
            "Noun": SubScore(5),
            "Verb": SubScore(5),
            "Adverb": SubScore(5),
            "Adjective": SubScore(5)
        }

        self.word_type_merit = {
            "Noun": SubScore(5),
            "Verb": SubScore(5),
            "Adverb": SubScore(5),
            "Adjective": SubScore(5)
        }


class SubScore:
    def __init__(self, target_score):

        self.current_score = 0
        self.target_score = target_score
        self.is_complete = False

