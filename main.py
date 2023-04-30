from tkinter import *
from random import choice
import pandas
import os

"""Grammar Practice game
I adapted what I learnt from Angela Yu's 100 days of code Tkinter lesson, on building a language learning flash card
memory game, into a grammar type practice game for my son. The lesson taught us how to create a csv file with
different categories, and bring this into pycharm. We then used pandas to convert the csv file into a data frame,
and then into a dictionary. The game uses the random function to pull a random word (key), and sentence (value) from
the dictionary, and present this to the player. Looking at the word in context to the sentence, the player has to
decide whether the word is a verb, noun, adjective or adverb. After the player has made their choice,
by clicking on one of the 4 grammar type buttons, the answer is presented back to them, along with a description of
the corresponding grammar type. The player earns merits if they choose correctly. A new csv file is created which
copies all the original data from the dictionary. When the player guesses correctly, the word/sentence is removed
from the new csv file, to avoid repetition. The player can end the game at any point, but if they complete 20 correct
answers, the game ends automatically, and they earn an extra 20 points. The game has been designed for little and
often game-play, and with light gamification, and little punishment. My son loves the Tom Gates books, and playing
football, so I used these as references to build the words and sentences within the csv file. In the Tom Gates books
they earn merits, so I used merits as the scoring system. If others were to use this program, they could adapt the csv
file to use their own references. After playing this through with my son, I noticed that after several answers, he
started to guess, rather than think through the correct answer. To help resolve this, I limited the player's
ability for incorrect answers by having 5 wrong answers end the game. This helped motivate the player to beat their 
previous score, and aim to achieve 20 correct questions to earn maximum merits."""


BACKGROUND_COLOR = "#C5f2f6"
YELLOW = "#e9bc4b"
GREEN = "#65c941"
ORANGE = "#ee8231"
PURPLE = "#b35ed8"
to_learn = {}
sentence_word = {}
guess = 5
back = False
answer = ""
adverb_score_1 = 0
verb_score_1 = 0
adjective_score_1 = 0
noun_score_1 = 0
stop_score = False
adverb_score_complete = False
verb_score_complete = False
noun_score_complete = False
adjective_score_complete = False
old_score = 0
top_score = 0
new_score = 0


"""The below try code catches an exception error, which is caused when the program tries to open a csv file which has
not yet been created."""
try:
    data = pandas.read_csv("grammar_type_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("grammar_project.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def remove_phrase():
    """If the player guesses the correct grammar type for the sentence, the sentence/word is removed from the
    to_learn dictionary."""
    global data
    to_learn.remove(sentence_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("grammar_type_to_learn.csv", index=False)


def if_wrong_answer():
    """If the player chooses the wrong answer,  their tries are reduced by 1 point. 5 wrong tries and the game ends.
    The player can restart the game to try and beat their old score."""
    global guess
    guess -= 1
    if guess == 0:
        end()


def reset_game():
    global guess, adverb_score_1, adjective_score_1, verb_score_1, noun_score_1, adverb_score_complete, \
        verb_score_complete, noun_score_complete, adjective_score_complete, new_score, old_score, top_score
    guess = 5
    adverb_score_1 = 0
    verb_score_1 = 0
    adjective_score_1 = 0
    noun_score_1 = 0
    adverb_score_complete = False
    verb_score_complete = False
    noun_score_complete = False
    adjective_score_complete = False
    os.remove("grammar_type_to_learn.csv")
    end_button.configure(text="End", command=end, fg="White")
    continue_button.configure(text="Continue", command=random_word, fg="White")
    if new_score > old_score:
        top_score = new_score
    else:
        top_score = old_score
    old_score = new_score
    new_score = 0
    canvas.itemconfig(new_score_text, text=f"New score = {new_score}")
    canvas.itemconfig(old_score_text, text=f"Old score = {old_score}")
    random_word()


def do_nothing():
    """After the player has used a grammar type button, the button's command function is temporarily disabled using this
    function (do_nothing), to prevent the function running again, whilst the proceeding functions complete."""
    pass


def end():
    """The end function is activated when the player uses the 'end' button. The function tells the player how many
    merits they achieved. If they completed the game, by choosing 20 correct answers, then they achieve an extra 20
    merits, earning 40 merits in total."""
    global adverb_score_1, verb_score_1, adjective_score_1, noun_score_1, old_score, new_score, top_score
    global noun_score_complete, adverb_score_complete, adjective_score_complete, verb_score_complete
    total_merits = adverb_score_1 + verb_score_1 + adjective_score_1 + noun_score_1
    max_score = total_merits + 20
    end_button.configure(text="End", command=do_nothing, fg="White")
    continue_button.configure(text="Reset", command=reset_game, fg="White")
    if verb_score_complete and noun_score_complete and adjective_score_complete and adverb_score_complete == True:
        new_score = max_score
        top_score = max_score
        canvas.itemconfig(card_text_sentence, text=f"Well done! You scored {total_merits} merits!\nPlus an extra "
                                                   f"20 merits for completing the game!"
                                                   f"\nYour final score is {max_score}!")
        canvas.itemconfig(card_text_word, text="End Game", fill="black")
        canvas.itemconfig(card_text_grammar_des, text="")
        verb_button.configure(image=clear_button, command=do_nothing, fg="White"), adverb_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        noun_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            image=clear_button, fg="White")
    else:
        new_score = total_merits
        if new_score > old_score:
            top_score = total_merits
        else:
            pass
        canvas.itemconfig(card_text_sentence, text=f"You scored {total_merits} merits!")
        canvas.itemconfig(card_text_word, text="End Game", fill="black")
        canvas.itemconfig(card_text_grammar_des, text="")
        verb_button.configure(image=clear_button, command=do_nothing, fg="White"), adverb_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        noun_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            image=clear_button, command=do_nothing, fg="White")
    canvas.itemconfig(new_score_text, text=f"New score = {new_score}")
    canvas.itemconfig(old_score_text, text=f"Old score = {old_score}")
    canvas.itemconfig(top_score_text, text=f"Top score = {top_score}")


def score_check():
    """score_check ends the game if the player has completed 20 correct answers."""
    global noun_score_complete, adverb_score_complete, adjective_score_complete, verb_score_complete, to_learn, \
        original_data, data
    if verb_score_complete and noun_score_complete and adjective_score_complete and adverb_score_complete == True:
        end()
    else:
        pass
    if len(to_learn) < 1:
        os.remove("grammar_type_to_learn.csv")
        try:
            data = pandas.read_csv("grammar_type_to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("grammar_project.csv")
            to_learn = original_data.to_dict(orient="records")
        else:
            to_learn = data.to_dict(orient="records")
    else:
        pass


def random_word():
    """The random word function is the opening program, and starts the game by generating a random word/sentence from
    the to_learn dictionary. It also resets the answer and stop_score variables, to allow for the game to
    be replayed."""
    global answer, sentence_word, stop_score, back, old_score, new_score
    answer = ""
    stop_score = False
#    old_score = new_score
#    new_score = 0
#    canvas.itemconfig(new_score_text, text=f"New score = {new_score}")
#    canvas.itemconfig(old_score_text, text=f"Old score = {old_score}")
    verb_button.configure(image=verb_img, command=verb_click, fg="Black"), adverb_button.configure(image=adverb_img,
                                                                                                   command=adverb_click,
                                                                                                   fg="Black"),
    adjective_button.configure(image=adjective_img, command=adjective_click, fg="Black"), noun_button.configure(
        image=noun_img, command=noun_click, fg="Black")
    canvas.itemconfig(card_text_grammar_des, text="")
    sentence_word = choice(to_learn)
    canvas.itemconfig(card_text_sentence, text=sentence_word["Sentence"], fill="black")
    canvas.itemconfig(card_text_word, text=sentence_word["Word"], fill="black")
    score_check()


def verb_click():
    """When the player clicks on the verb button, this function checks if the word within the sentence is a verb.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""
    global answer, verb_score_1, verb_score_complete, stop_score
    verb_score = verb_score_1
    answer = "Verb"
    answer_reveal()
    if sentence_word["Grammar"] == "Verb":
        remove_phrase()
        if stop_score == False:
            if verb_score < 5:
                verb_score += 1
                verb_score_1 = verb_score
                canvas.itemconfig(verb_merits, text=f"Verb score = {verb_score_1} / 5")
                stop_score = True
                if verb_score == 5:
                    verb_score_complete = True
                else:
                    pass
                score_check()
            elif verb_score == 5:
                verb_score_complete = True
                score_check()
            else:
                pass
        else:
            pass
    else:
        pass


def noun_click():
    """When the player clicks on the noun button, this function checks if the word within the sentence is a noun.
    The player is informed and a description of what a verb is, is displayed. The correct phrase is removed from the
    to_learn dictionary, and the player is told their score."""
    global answer, noun_score_1, noun_score_complete, stop_score
    noun_score = noun_score_1
    answer = "Noun"
    answer_reveal()
    if sentence_word["Grammar"] == "Noun":
        remove_phrase()
        if stop_score == False:
            if noun_score < 5:
                noun_score += 1
                noun_score_1 = noun_score
                canvas.itemconfig(noun_merits, text=f"Noun score = {noun_score_1} / 5")
                stop_score = True
                if noun_score == 5:
                    noun_score_complete = True
                else:
                    pass
                score_check()
            elif noun_score == 5:
                noun_score_complete = True
                score_check()
            else:
                pass
        else:
            pass
    else:
        pass


def adverb_click():
    """When the player clicks on the verb button, this function checks if the word within the sentence is an adverb.
    The player is informed and a description of what an adverb is, is displayed. The correct phrase is removed from
    the to_learn dictionary, and the player is told their score."""
    global answer, adverb_score_1, adverb_score_complete, stop_score
    adverb_score = adverb_score_1
    answer = "Adverb"
    answer_reveal()
    if sentence_word["Grammar"] == "Adverb":
        remove_phrase()
        if stop_score == False:
            if adverb_score < 5:
                adverb_score += 1
                adverb_score_1 = adverb_score
                canvas.itemconfig(adverb_merits, text=f"Adverb score = {adverb_score_1} / 5")
                stop_score = True
                if adverb_score == 5:
                    adverb_score_complete = True
                else:
                    pass
                score_check()
            elif adverb_score == 5:
                adverb_score_complete = True
                score_check()
            else:
                pass
        else:
            pass
    else:
        pass


def adjective_click():
    """When the player clicks on the adjective button, this function checks if the word within the sentence is an
    adjective.The player is informed and a description of what a verb is, is displayed. The correct phrase is removed
    from the to_learn dictionary, and the player is told their score."""
    global answer, adjective_score_1, adjective_score_complete, stop_score
    adjective_score = adjective_score_1
    answer = "Adjective"
    answer_reveal()
    if sentence_word["Grammar"] == "Adjective":
        remove_phrase()
        if stop_score == False:
            if adjective_score < 5:
                adjective_score += 1
                adjective_score_1 = adjective_score
                canvas.itemconfig(adjective_merits, text=f"Adjective score = {adjective_score_1} / 5")
                stop_score = True
                if adjective_score == 5:
                    adjective_score_complete = True
                else:
                    pass
                score_check()
            elif adjective_score == 5:
                adjective_score_complete = True
                score_check()
            else:
                pass
        else:
            pass
    else:
        pass


def answer_reveal():
    """After the player has made their choice, the answer_reveal function checks if the player's choice is correct, and
    presents the answer to the player. This function also temporarily disables the grammar buttons, until the player
    uses the continue button."""
    global answer, sentence_word
    if sentence_word["Grammar"] == "Noun":
        canvas.itemconfig(card_text_word, text=sentence_word['Word'], fill=GREEN)
        if answer == "Noun":
            canvas.itemconfig(card_text_grammar_des, text=f"Correct! Well done. {sentence_word['Word']} is a noun. "
                                                          f"\nA noun is a word used to "f"identify people, places or "
                                                          f"things.", fill=GREEN)
        else:
            canvas.itemconfig(card_text_grammar_des, text=f"{sentence_word['Word']} is a noun. \nA noun is a word "
                                                          f"used to "f"identify people, places or things.", fill=GREEN)
            if_wrong_answer()
        verb_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        adverb_button.configure(image=clear_button, command=do_nothing, fg="White"), noun_button.configure(
            command=do_nothing)
    elif sentence_word["Grammar"] == "Verb":
        canvas.itemconfig(card_text_word, text=sentence_word['Word'], fill=PURPLE)
        if answer == "Verb":
            canvas.itemconfig(card_text_grammar_des, text=f"Correct! Well done. {sentence_word['Word']} is a verb. "
                                                          f"\nA verb is a word that describes what the subject is "
                                                          f"doing.", fill=PURPLE)
        else:
            canvas.itemconfig(card_text_grammar_des, text=f"{sentence_word['Word']} is a verb. \nA verb is a word that "
                                                          f"describes what the subject is doing.", fill=PURPLE)
            if_wrong_answer()
        noun_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        adverb_button.configure(image=clear_button, command=do_nothing, fg="White"), verb_button.configure(
            command=do_nothing)
    elif sentence_word["Grammar"] == "Adverb":
        canvas.itemconfig(card_text_word, text=sentence_word['Word'], fill=ORANGE)
        if answer == "Adverb":
            canvas.itemconfig(card_text_grammar_des, text=f"Correct! Well done. {sentence_word['Word']} is an adverb. "
                                                          f"\nAn adverb is a word that describes how an action is "
                                                          f"carried out.", fill=ORANGE)
        else:
            canvas.itemconfig(card_text_grammar_des, text=f"{sentence_word['Word']} is an adverb. \nAn adverb is a "
                                                          f"word that describes how an action is carried out.",
                              fill=ORANGE)
            if_wrong_answer()
        verb_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        noun_button.configure(image=clear_button, command=do_nothing, fg="White"), adverb_button.configure(
            command=do_nothing)
    else:
        canvas.itemconfig(card_text_word, text=sentence_word['Word'], fill=YELLOW)
        if answer == "Adjective":
            canvas.itemconfig(card_text_grammar_des, text=f"Correct! Well done. {sentence_word['Word']} is an "
                                                          f"adjective. \nAn adjective is a word that describes a "
                                                          f"person, place or thing.", fill=YELLOW)
        else:
            canvas.itemconfig(card_text_grammar_des, text=f"{sentence_word['Word']} is an adjective. \nAn adjective "
                                                          f"is a word that describes a person, place or thing.",
                              fill=YELLOW)
            if_wrong_answer()
        verb_button.configure(image=clear_button, command=do_nothing, fg="White"), adverb_button.configure(
            image=clear_button, command=do_nothing, fg="White"),
        noun_button.configure(image=clear_button, command=do_nothing, fg="White"), adjective_button.configure(
            command=do_nothing)


window = Tk()
window.title("Grammar Practice")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
clear_button = PhotoImage(file="images/clear1.png")
card_background = canvas.create_image(411, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=4)

"""Card_Text_Sentence"""
card_text_sentence = canvas.create_text(400, 263, text="", fill="Black", font=("Ariel", 20, "italic"))
canvas.grid(column=0, row=0)

"""Card_Text_Word"""
card_text_word = canvas.create_text(397, 150, text="", fill="Black", font=("Ariel", 56, "bold"))
canvas.grid(column=0, row=0)

"""Card_Text_Grammar"""
card_text_grammar_des = canvas.create_text(397, 360, text="", justify=CENTER, fill="Black", font=("Ariel", 14, "bold"))
canvas.grid(column=0, row=0)

"""verb_button"""
verb_img = PhotoImage(file="images/verb.png")
verb_button = Button(image=verb_img, highlightthickness=0, text='Verb', compound=CENTER,
                     font=("Ariel", 20, "bold"), command=verb_click)
verb_button.grid(column=3, row=1)

"""noun_button"""
noun_img = PhotoImage(file="images/noun.png")
noun_button = Button(image=noun_img, highlightthickness=0, text='Noun', compound=CENTER,
                     font=("Ariel", 20, "bold"), command=noun_click)
noun_button.grid(column=1, row=1)

"""adjective_button"""
adjective_img = PhotoImage(file="images/adjective.png")
adjective_button = Button(image=adjective_img, highlightthickness=0, text='Adjective', compound=CENTER,
                          font=("Ariel", 20, "bold"), command=adjective_click)
adjective_button.grid(column=0, row=1)

"""adverb_button"""
adverb_img = PhotoImage(file="images/adverb.png")
adverb_button = Button(image=adverb_img, highlightthickness=0, text='Adverb', compound=CENTER,
                       font=("Ariel", 20, "bold"), command=adverb_click)
adverb_button.grid(column=2, row=1)

"""adjective_merits"""
adjective_merits = canvas.create_text(104, 30, fill=YELLOW, text=f"Adjective score = {adjective_score_1} / 5",
                                      font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""noun_merits"""
noun_merits = canvas.create_text(312, 30, fill=GREEN, text=f"Noun score = {noun_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""adverb_merits"""
adverb_merits = canvas.create_text(512, 30, fill=ORANGE, text=f"Adverb score = {adverb_score_1} / 5",
                                   font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""verb_merits"""
verb_merits = canvas.create_text(711, 30, fill=PURPLE, text=f"Verb score = {verb_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""continue_button"""
continue_img = PhotoImage(file="images/clear.png")
continue_button = Button(image=continue_img, fg="White", highlightthickness=0, text='Continue', compound=CENTER,
                         font=("Ariel", 15), command=random_word)
continue_button.grid(column=0, row=2)

"""end_button"""
end_img = PhotoImage(file="images/clear.png")
end_button = Button(image=end_img, fg="White", highlightthickness=0, text='End', compound=CENTER, font=("Ariel", 15),
                    command=end)
end_button.grid(column=3, row=2)

"""Top Score"""
top_score_text = canvas.create_text(200, 450, fill="pink", text=f"Top score = {top_score}", font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

"""Old Score"""
old_score_text = canvas.create_text(400, 450, fill="pink", text=f"Old score = {old_score}", font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

"""New Score"""
new_score_text = canvas.create_text(600, 450, fill="pink", text=f"New score = {new_score}", font=("Ariel", 16, "bold"))

random_word()

window.mainloop()
