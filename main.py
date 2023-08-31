from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Import image and add as turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

# Set turtle shape to image
turtle.shape(image)

# Import CSV
data = pandas.read_csv("50_states.csv")
states = data.state
states_list = states.to_list()

# Keep track of correct answers
correct_answers = []

# Game loop
game_is_on = True
while game_is_on:

    # Pop-up with prompt to enter State
    answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()

    if answer_state in states_list:
        pass
    else:
        pass


# # Get coordinates of click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# Alternative to screen.exitonclick(), keeps window open
# turtle.mainloop()

