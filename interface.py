from tkinter import PhotoImage, Canvas, CENTER, Tk, Button
from buttons_class import ButtonClass
from button_functions import verb_click, noun_click, adjective_click, adverb_click
from gameplay_functions import start_game, end_game
from score_class import ScoreClass

s = ScoreClass()
b = ButtonClass()

BACKGROUND_COLOR = "#C5f2f6"
YELLOW = "#e9bc4b"
GREEN = "#65c941"
ORANGE = "#ee8231"
PURPLE = "#b35ed8"

window = Tk()
window.title("Grammar Practice")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,
                height=526,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
clear_button = PhotoImage(file="images/clear1.png")
card_background = canvas.create_image(411, 263,
                                      image=card_front_img)
canvas.grid(column=0, row=0, columnspan=4)

"""Card_Text_Sentence"""
card_text_sentence = canvas.create_text(400, 263,
                                        text="",
                                        fill="Black",
                                        font=("Ariel", 20, "italic"))
canvas.grid(column=0, row=0)

"""Card_Text_Word"""
card_text_word = canvas.create_text(397, 150,
                                    text="",
                                    fill="Black",
                                    font=("Ariel", 56, "bold"))
canvas.grid(column=0, row=0)

"""Card_Text_Grammar"""
card_text_grammar_des = canvas.create_text(397, 360,
                                           text="",
                                           justify=CENTER,
                                           fill="Black",
                                           font=("Ariel", 14, "bold"))
canvas.grid(column=0, row=0)

"""verb_button"""
verb_img = PhotoImage(file="images/verb.png")
verb_button = Button(image=verb_img,
                     highlightthickness=0,
                     text='Verb',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=verb_click)
verb_button.grid(column=3, row=1)

"""noun_button"""
noun_img = PhotoImage(file="images/noun.png")
noun_button = Button(image=noun_img,
                     highlightthickness=0,
                     text='Noun',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=noun_click)
noun_button.grid(column=1, row=1)

"""adjective_button"""
adjective_img = PhotoImage(file="images/adjective.png")
adjective_button = Button(image=adjective_img,
                          highlightthickness=0,
                          text='Adjective',
                          compound=CENTER,
                          font=("Ariel", 20, "bold"),
                          command=adjective_click)
adjective_button.grid(column=0, row=1)

"""adverb_button"""
adverb_img = PhotoImage(file="images/adverb.png")
adverb_button = Button(image=adverb_img,
                       highlightthickness=0,
                       text='Adverb',
                       compound=CENTER,
                       font=("Ariel", 20, "bold"),
                       command=adverb_click)
adverb_button.grid(column=2, row=1)

"""adjective_merits"""
adjective_merits = canvas.create_text(104, 30,
                                      fill=YELLOW,
                                      text=f"Adjective score = {b.adjective_score_1} / 5",
                                      font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""noun_merits"""
noun_merits = canvas.create_text(312, 30,
                                 fill=GREEN,
                                 text=f"Noun score = {b.noun_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""adverb_merits"""
adverb_merits = canvas.create_text(512, 30,
                                   fill=ORANGE,
                                   text=f"Adverb score = {b.adverb_score_1} / 5",
                                   font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""verb_merits"""
verb_merits = canvas.create_text(711, 30,
                                 fill=PURPLE,
                                 text=f"Verb score = {b.verb_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

"""continue_button"""
continue_img = PhotoImage(file="images/clear.png")
continue_button = Button(image=continue_img,
                         fg="White",
                         highlightthickness=0,
                         text='Continue',
                         compound=CENTER,
                         font=("Ariel", 15),
                         command=start_game)
continue_button.grid(column=0, row=2)

"""end_button"""
end_img = PhotoImage(file="images/clear.png")
end_button = Button(image=end_img,
                    fg="White",
                    highlightthickness=0,
                    text='End',
                    compound=CENTER,
                    font=("Ariel", 15),
                    command=end_game)
end_button.grid(column=3, row=2)

"""Top Score"""
top_score_text = canvas.create_text(200, 450,
                                    fill="pink",
                                    text=f"Top score = {s.top_score}",
                                    font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

"""Old Score"""
old_score_text = canvas.create_text(400, 450,
                                    fill="pink",
                                    text=f"Old score = {s.old_score}",
                                    font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

"""New Score"""
new_score_text = canvas.create_text(600, 450,
                                    fill="pink",
                                    text=f"New score = {s.new_score}",
                                    font=("Ariel", 16, "bold"))
