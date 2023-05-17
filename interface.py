from tkinter import PhotoImage, Canvas, CENTER, Tk, Button
from button_class import WordButton
from gameplay_class import GamePlay
from score_class import ScoreClass

s = ScoreClass()
g = GamePlay()

noun_word_button = WordButton("Noun")
adverb_word_button = WordButton("Adverb")
verb_word_button = WordButton("Verb")
adjective_word_button = WordButton("Adjective")

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

card_text_sentence = canvas.create_text(400, 263,
                                        text="",
                                        fill="Black",
                                        font=("Ariel", 20, "italic"))
canvas.grid(column=0, row=0)

card_text_word = canvas.create_text(397, 150,
                                    text="",
                                    fill="Black",
                                    font=("Ariel", 56, "bold"))
canvas.grid(column=0, row=0)

card_text_grammar_des = canvas.create_text(397, 360,
                                           text="",
                                           justify=CENTER,
                                           fill="Black",
                                           font=("Ariel", 14, "bold"))
canvas.grid(column=0, row=0)

verb_img = PhotoImage(file="images/verb.png")
verb_button = Button(image=verb_img,
                     highlightthickness=0,
                     text='Verb',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=lambda: g.click_button(s, verb_word_button))
verb_button.grid(column=3, row=1)

noun_img = PhotoImage(file="images/noun.png")
noun_button = Button(image=noun_img,
                     highlightthickness=0,
                     text='Noun',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=lambda: g.click_button(s, noun_word_button))
noun_button.grid(column=1, row=1)

adjective_img = PhotoImage(file="images/adjective.png")
adjective_button = Button(image=adjective_img,
                          highlightthickness=0,
                          text='Adjective',
                          compound=CENTER,
                          font=("Ariel", 20, "bold"),
                          command=lambda: g.click_button(s, adjective_word_button))
adjective_button.grid(column=0, row=1)

adverb_img = PhotoImage(file="images/adverb.png")
adverb_button = Button(image=adverb_img,
                       highlightthickness=0,
                       text='Adverb',
                       compound=CENTER,
                       font=("Ariel", 20, "bold"),
                       command=lambda: g.click_button(s, adverb_word_button))
adverb_button.grid(column=2, row=1)

adjective_merits = canvas.create_text(104, 30,
                                      fill=YELLOW,
                                      text=f"Adjective score = {s.adjective_score_1} / 5",
                                      font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

noun_merits = canvas.create_text(312, 30,
                                 fill=GREEN,
                                 text=f"Noun score = {s.noun_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

adverb_merits = canvas.create_text(512, 30,
                                   fill=ORANGE,
                                   text=f"Adverb score = {s.adverb_score_1} / 5",
                                   font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

verb_merits = canvas.create_text(711, 30,
                                 fill=PURPLE,
                                 text=f"Verb score = {s.verb_score_1} / 5",
                                 font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0)

continue_img = PhotoImage(file="images/clear.png")
continue_button = Button(image=continue_img,
                         fg="White",
                         highlightthickness=0,
                         text='Continue',
                         compound=CENTER,
                         font=("Ariel", 15),
                         command=g.start_game)
continue_button.grid(column=0, row=2)

end_img = PhotoImage(file="images/clear.png")
end_button = Button(image=end_img,
                    fg="White",
                    highlightthickness=0,
                    text='End',
                    compound=CENTER,
                    font=("Ariel", 15),
                    command=g.end_game)
end_button.grid(column=3, row=2)

top_score_text = canvas.create_text(200, 450,
                                    fill="pink",
                                    text=f"Top score = {s.top_score}",
                                    font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

old_score_text = canvas.create_text(400, 450,
                                    fill="pink",
                                    text=f"Old score = {s.old_score}",
                                    font=("Ariel", 16, "bold"))
canvas.grid(column=0, row=0)

new_score_text = canvas.create_text(600, 450,
                                    fill="pink",
                                    text=f"New score = {s.new_score}",
                                    font=("Ariel", 16, "bold"))
