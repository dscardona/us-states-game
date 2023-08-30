import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

# Import image and add as turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

# Set turtle shape to image
turtle.shape(image)

# Pop up with prompt to enter State
answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")

# # Get coordinates of click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# Alternative to screen.exitonclick(), keeps window open
turtle.mainloop()

