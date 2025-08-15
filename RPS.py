"""
This file is a graphical version of Rock Paper Scissors
"""
import tkinter as tk
from random import choice

class RockPaperScissors:
    """
    Rock_Paper_scissors class
    """
    def __init__(self):
        self.possibilities = {"rock": "\U0001faa8", "paper": "\U0001f4c3", "scissors": "\U00002704"}
        self.user_score = 0
        self.computer_score = 0
        self.losing_pairs = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}

        self.root = tk.Tk()
        self.root.geometry("608x358")
        self.root.title("Rock Paper Scissors")
        self.root.resizable(height=False, width=False)

        tk.Button(self.root, text=self.possibilities["rock"], command=lambda: self.play("rock"),\
        font=("", 30), padx=20, pady=20).place(x=0, y=0)
        tk.Button(self.root, text=self.possibilities["paper"], command=lambda: self.play("paper"),\
        font=("", 30), padx=20, pady=20).place(x=0, y=120)
        tk.Button(self.root, text=self.possibilities["scissors"], \
        command=lambda: self.play("scissors"),font=("", 30), padx=21.4, pady=20).place(x=1, y=240)

        self.game_label = tk.Label(self.root)
        self.game_label.place(x=200, y=7)

        tk.Label(self.root, text="You        Computer", font=("", 24)).place(x=230, y=240)

        self.score_label = tk.Label(self.root, text=f"{self.user_score}\
                 {self.computer_score}", font=("", 24))
        self.score_label.place(x=251, y=290)

        self.root.mainloop()

    def score_manager(self, game_state):
        """
        This function manages the scores of computer and user
        """
        if game_state == "You won":
            self.user_score += 1
        elif game_state == "You lose":
            self.computer_score += 1

    def play(self, user_choice):
        """
        This function is the main function which handles the game
        """
        computer_choice = choice(list(self.possibilities))
        if computer_choice == user_choice:
            game_state = "Draw"
        elif (computer_choice, user_choice) in self.losing_pairs:
            game_state = "You lose"
        else:
            game_state = "You won"

        self.score_manager(game_state)

        self.game_label.config(text=\
        f"{game_state}\n\ncomputer choice: {self.possibilities[computer_choice]}\nyour choice: {self.possibilities[user_choice]}", font=("", 26))
        self.score_label.config(text=f"{self.user_score}                 {self.computer_score}")

if __name__ == "__main__":
    RockPaperScissors()
