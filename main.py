import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

#Import image and add as turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

#Set turtle shape to image
turtle.shape(image)


screen.exitonclick()