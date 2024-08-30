import tkinter as tk
from tkinter import ttk
import random

app = tk.Tk()
app.title("Rock Paper Scissors")
app.geometry("430x350")

select_list = ["✊Rock", "✋Paper", "✂️Scissors"]

user = ""
computer = ""
score = 0
c_score = 0


def rock():
    global user
    user = select_list[0]
    main()


def paper():
    global user
    user = select_list[1]
    main()


def scissors():
    global user
    user = select_list[2]
    main()


def main():
    computer = random.choice(select_list)
    output_user_lbl.config(text="Your Choice: " + user)
    output_computer_lbl.config(text="Computer Choice: " + computer)
    global score
    global c_score
    winner = ""
    if user == computer:
        winner = "Tie"
    elif user == select_list[0]:
        if computer == select_list[1]:
            winner = "Computer won"
            c_score += 1
        else:
            winner = "You won"
            score += 1
    elif user == select_list[1]:
        if computer == select_list[2]:
            winner = "Computer won"
            c_score += 1
        else:
            winner = "You won"
            score += 1

    elif user == select_list[2]:
        if computer == select_list[0]:
            winner = "Computer won"
            c_score += 1
        else:
            winner = "You won"
            score += 1

    output_winner_lbl.config(text=winner)
    output_winner_lbl.place(x=170, y=200)
    score_lbl.config(text="Your score: " + str(score))
    c_score_lbl.config(text="Computer score: " + str(c_score))

    if score == 3:
        input_btn_r.place_forget()
        input_btn_p.place_forget()
        input_btn_s.place_forget()
        input_lbl.place_forget()
        cong.config(text="You Won, congratulations")
        cong.place(x=0, y=300)
        reset_btn.place(x=220, y=300)
    if c_score == 3:
        input_btn_r.place_forget()
        input_btn_p.place_forget()
        input_btn_s.place_forget()
        input_lbl.place_forget()
        cong.config(text="You Lost")
        cong.place(x=0, y=300)
        reset_btn.place(x=80, y=300)


def reset():
    global score
    global c_score
    score = 0
    c_score = 0
    user = ""
    computer = ""
    input_btn_r.place(x=155, y=300)
    input_btn_p.place(x=240, y=300)
    input_btn_s.place(x=320, y=300)
    input_lbl.place(x=0, y=300)
    cong.place_forget()
    score_lbl.config(text="Your score: " + str(score))
    c_score_lbl.config(text="Computer score: " + str(c_score))
    output_user_lbl.config(text="")
    output_computer_lbl.config(text="")
    reset_btn.place_forget()
    output_winner_lbl.place_forget()


win_lbl = tk.Label(
    app, text="Rock Paper Scissors", font=("Arial", 14, "bold"), fg="red"
)
win_lbl.place(x=100, y=0)

input_lbl = tk.Label(
    app, text="Select Your Hand: ", font=("Arial", 13, "bold"), fg="red"
)
input_lbl.place(x=0, y=300)

rock_img = tk.PhotoImage(file = "rock.png") 
paper_img = tk.PhotoImage(file = "paper.png") 
sc_img = tk.PhotoImage(file = "sc.png") 

input_btn_r = tk.Button(
    app,
    cursor="hand2",
    image=rock_img,
    command=lambda: rock(),
)
input_btn_r.place(x=155, y=290)

input_btn_p = tk.Button(
    app,
    image= paper_img,
    cursor="hand2",
    command=lambda: paper(),
    height= 55,
)
input_btn_p.place(x=240, y=291)

input_btn_s = tk.Button(
    app,
    image= sc_img,
    cursor="hand2",
    command=lambda: scissors(),
    height= 55,
)
input_btn_s.place(x=320, y=290)


output_user_lbl = tk.Label(app, text="", font=("Arial", 18, "bold"), fg="red")
output_user_lbl.place(x=0, y=120)

output_computer_lbl = tk.Label(
    app, text="", font=("Arial", 18, "bold"), fg="red")
output_computer_lbl.place(x=0, y=170)

output_winner_lbl = tk.Label(
    app, text="", font=("Arial", 18, "bold"), fg="green")
output_winner_lbl.place(x=80, y=220)

score_lbl = tk.Label(app, text="Your score: 0",
                     font=("Arial", 14, "bold"), fg="green")
score_lbl.place(x=50, y=30)

c_score_lbl = tk.Label(
    app, text="Computer score: 0", font=("Arial", 14, "bold"), fg="green"
)
c_score_lbl.place(x=200, y=30)

cong = tk.Label(app, text="", font=("Arial", 14, "bold"), fg="green")
cong.place_forget()

reset_btn = tk.Button(
    app,
    text="Reset",
    font=("Arial", 13, "bold"),
    fg="red",
    bg="green",
    cursor="hand2",
    command=lambda: reset(),
)
reset_btn.place_forget()

app.mainloop()