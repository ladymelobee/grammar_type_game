from gameplay_functions import start_game
from interface import window

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


start_game()

window.mainloop()
