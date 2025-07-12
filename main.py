from turtle import Turtle, Screen

# Create the main turtle that will draw
tim = Turtle()
screen = Screen()

tim.speed(9)
# Default pen size
tim.pensize(1)  
# Start with pen up to prevent initial drawing
tim.penup()  
# Ensure the turtle is visible
tim.showturtle()  

# Change Pen Color
def set_color_red():
    tim.pencolor("red")

def set_color_green():
    tim.pencolor("green")

def set_color_blue():
    tim.pencolor("blue")

def set_color_black():
    tim.pencolor("black")

# Pen Thickness
def increase_thickness():
    current_thickness = tim.pensize()
    tim.pensize(current_thickness + 1)

def decrease_thickness():
    current_thickness = tim.pensize()
    if current_thickness > 1:
        tim.pensize(current_thickness - 1)

# Clear the screen
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Speed Control
def increase_speed():
    current_speed = tim.speed()
    if current_speed < 10:
        tim.speed(current_speed + 1)

def decrease_speed():
    current_speed = tim.speed()
    if current_speed > 1:
        tim.speed(current_speed - 1)

# Move forward
def move_forward():
    tim.pendown()
    tim.forward(10)

# Move backward
def move_backward():
    tim.pendown()
    tim.backward(10)

# Turn left
def move_left():
    tim.pendown()
    # Rotate 10 degrees to the left
    tim.left(10)  

# Turn right
def move_right():
    new_state = tim.heading() - 10
    tim.setheading(new_state)

# Key bindings
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.onkey(key="r", fun=set_color_red)
screen.onkey(key="g", fun=set_color_green)
screen.onkey(key="b", fun=set_color_blue)
screen.onkey(key="k", fun=set_color_black)

screen.onkey(key="+", fun=increase_thickness)
screen.onkey(key="-", fun=decrease_thickness)

screen.onkey(key="u", fun=increase_speed)
screen.onkey(key="p", fun=decrease_speed)

# Start the main event loop
screen.mainloop()