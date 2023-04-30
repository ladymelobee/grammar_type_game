from tkinter import *
from button_objects import *


BACKGROUND_COLOR = "#C5f2f6"
YELLOW = "#e9bc4b"
GREEN = "#65c941"
ORANGE = "#ee8231"
PURPLE = "#b35ed8"

#INTERFACE SETUP
window = Tk()
window.title("Grammar Practice")
window.configure(padx=50,
                 pady=50,
                 bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,
                height=526,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
clear_button = PhotoImage(file="images/clear1.png")
card_background = canvas.create_image(411, 263,
                                      image=card_front_img)
canvas.grid(column=0, row=0, columnspan=4)

#TEXT
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
card_text_grammar_des = canvas.create_text(397, 360, text="",
                                           justify=CENTER,
                                           fill="Black",
                                           font=("Ariel", 14, "bold"))
canvas.grid(column=0, row=0)


#BUTTONS
"""verb_button"""
verb_img = PhotoImage(file="images/verb.png")
verb_button = Button(image=verb_img,
                     highlightthickness=0,
                     text='Verb',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=verb_button)
verb_button.grid(column=3, row=1)

"""noun_button"""
noun_img = PhotoImage(file="images/noun.png")
noun_button = Button(image=noun_img,
                     highlightthickness=0,
                     text='Noun',
                     compound=CENTER,
                     font=("Ariel", 20, "bold"),
                     command=noun)
noun_button.grid(column=1, row=1)

"""adjective_button"""
adjective_img = PhotoImage(file="images/adjective.png")
adjective_button = Button(image=adjective_img,
                          highlightthickness=0,
                          text='Adjective',
                          compound=CENTER,
                          font=("Ariel", 20, "bold"),
                          command=adjective)
adjective_button.grid(column=0, row=1)

"""adverb_button"""
adverb_img = PhotoImage(file="images/adverb.png")
adverb_button = Button(image=adverb_img,
                       highlightthickness=0,
                       text='Adverb',
                       compound=CENTER,
                       font=("Ariel", 20, "bold"),
                       command=adverb)
adverb_button.grid(column=2, row=1)

"""continue_button"""
continue_img = PhotoImage(file="images/clear.png")
continue_button = Button(image=continue_img,
                         fg="White",
                         highlightthickness=0,
                         text='Continue',
                         compound=CENTER,
                         font=("Ariel", 15),
                         command=gameplay.start_game)
continue_button.grid(column=0, row=2)

"""end_button"""
end_img = PhotoImage(file="images/clear.png")
end_button = Button(image=end_img,
                    fg="White",
                    highlightthickness=0,
                    text='End',
                    compound=CENTER,
                    font=("Ariel", 15),
                    command=gameplay.end)
end_button.grid(column=3, row=2)


#SCORES
"""adjective_merits"""
adjective_merits = canvas.create_text(104, 30,
                                      fill=YELLOW,
                                      text=