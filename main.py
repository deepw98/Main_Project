import turtle as t
import time
import random
screen = t.Screen()
screen.setup(800, 700)
# co-ordinates for creating the main snake body
seg_pos = [(0, 0), (-20, 0), (-40, 0)]
# List for storing turtle objects for creating snake body
seg_list = []
screen.tracer(0)


# The function for creating snake body
def body():
    t_obj = t.Turtle("square")
    t_obj.hideturtle()
    screen.tracer(0)
    t_obj.color("red")
    t_obj.penup()
    if for_original:
        t_obj.goto(pos)
        t_obj.showturtle()
    screen.update()
    seg_list.append(t_obj)


# Loop for creating original turtle body
for pos in seg_pos:
    for_original = True
    body()


# Functions for movement of snake body
def do_up():
    if seg_list[0].heading() != 270:
        seg_list[0].setheading(90)


def do_down():
    if seg_list[0].heading() != 90:
        seg_list[0].setheading(270)


def do_left():
    if seg_list[0].heading() != 0:
        seg_list[0].setheading(180)


def do_right():
    if seg_list[0].heading() != 180:
        seg_list[0].setheading(0)


# Function for creating snake food in random coordinates
def food():
    list_x = []
    list_y = []
    for pos1 in range(380, -390, -10):
        list_x.append(pos1)
    print(list_x)
    for pos2 in range(280, -330, -10):
        list_y.append(pos2)
    print(list_y)

    pos_x = random.choice(list_x)
    pos_y = random.choice(list_y)
    t.penup()
    t.goto(pos_x, pos_y)
    t.dot(10)
    t.hideturtle()
    print(t.pos())


# Creating turtle for score writing
score = 0
t_write = t.Turtle()
t_write.hideturtle()
pen = t_write.getpen()


# Function for score writing
def write(score):
    t_write.penup()
    t_write.hideturtle()
    t_write.goto(x=-50, y=300)

    pen.clear()
    pen.write(f"Score:{score}", font=("calibari", 20, "bold"))


# Setting first score as zero
write(0)

# Creating turtle for drawing a line to separate the score and the game
t_line = t.Turtle()
t_line.hideturtle()
t_line.penup()
t_line.goto(x=-550, y=291)
t_line.pendown()
t_line.goto(x=550, y=291)

screen.listen()      # function for being able to use keyboard
moving = True       # Setup for moving loop
food()             # Generating first food

# Moving loop is used for making the snake move constantly
while moving:
    screen.update()     # It is used so that the new segments of turtle
    time.sleep(0.1)    # It is used for slowing the turtle down enough to move

    # This for block is used for the various segments to follow each other in various direction
    # even after appended with new segments
    for seg in range(len(seg_list)-1, 0, -1):
        new_x = seg_list[seg-1].xcor()
        new_y = seg_list[seg-1].ycor()
        seg_list[seg].goto(new_x, new_y)
        seg_list[seg].showturtle()
    print(seg_list[0].pos())
    t_x = t.xcor()    # food turtle x- coordinate
    t_y = t.ycor()    # food turtle y- coordinate

    # This if block is used for replacing food that is black dot with white dot and
    # Creating new food and incrementing the score
    if t_x+12 > seg_list[0].xcor() > t_x-12:
        if t_y+12 > seg_list[0].ycor() > t_y-12:
            t.goto(t_x, t_y)
            t.dot(10, "white")
            screen.update()
            for_original = False
            body()
            screen.update()
            food()
            score += 1
            write(score)

    # This if block is used for collision of snake with left and right walls
    if seg_list[0].xcor() > 380 or seg_list[0].xcor() < -390:
        t_stop = t.Turtle()
        t_stop.hideturtle()
        t_stop.penup()
        t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
        t_stop.goto(-135, -40)
        t_stop.write("You hit a wall", font=("caliberi", 20, "bold"))
        t_stop.goto(-135, -80)
        t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
        break
    # This if block is used for collision of snake with up and down walls
    if seg_list[0].ycor() > 280 or seg_list[0].ycor() < -330:
        t_stop = t.Turtle()
        t_stop.hideturtle()
        t_stop.penup()
        t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
        t_stop.goto(-135, -40)
        t_stop.write("You hit a wall", font=("caliberi", 20, "bold"))
        t_stop.goto(-135, -80)
        t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
        break

    # Making the snake always move forward
    seg_list[0].forward(10)
    # Making the keyboard keys operable
    screen.onkey(key="Up", fun=do_up)
    screen.onkey(key="Down", fun=do_down)
    screen.onkey(key="Left", fun=do_left)
    screen.onkey(key="Right", fun=do_right)
    # Creating a second list without the first segment of snake and
    # calling the first segment head
    seg_list2 = []
    for i in range(1, len(seg_list)):
        seg_list2.append(seg_list[i])
    head = seg_list[0]
    flag = 1

    # This for loop is used for detection of collision of snake with its tail
    for segments in seg_list2:
        if head.distance(segments) < 5:
            flag = 0
            t_stop = t.Turtle()
            t_stop.hideturtle()
            t_stop.penup()
            t_stop.write("Game over", align="center", font=("caliberi", 40, "bold"))
            t_stop.goto(-135, -40)
            t_stop.write("The snake bit itself", font=("caliberi", 20, "bold"))
            t_stop.goto(-135, -80)
            t_stop.write("Click on the screen to exit", font=("caliberi", 20, "bold"))
            break

    if flag == 0:
        break

# Exit game after clicking on screen
screen.exitonclick()
