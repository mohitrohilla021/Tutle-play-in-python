import turtle
wn=turtle.Screen()          # Asking for the graphics screen

wn.bgcolor("lightgreen")    # For background Color
# A beautiful thing is that this color written in the bracket is not "case-sensitive"

robort_1=turtle.Turtle()    # Robort 1 is created to apply commands on it, its a turtle object
robort_1.pensize(5)         # pen sie can be varied
robort_1.shape("turtle")    # Shape of the robort changed

robort_2=turtle.Turtle()    # Robort 2 is created to apply diff commands on it
robort_2.color("hotpink")   # Color can be changed, as done here

# robort_1.up()             # This doesn't show the previously covered path
# robort_1.stamp()          # This command leaves a stamp of the pointer where it is executed
robort_1.forward(150)       # Robort 1 taking action
robort_1.left(90)
robort_1.forward(90)
robort_1.left(90)
robort_1.forward(90)
robort_1.left(90)
robort_1.forward(90)
robort_1.left(90)

# robort_2.up()             # This doesn't show the previously covered path
# robort_2.stamp()          # This command leaves a stamp of the pointer where it is executed
robort_2.forward(150)       # Robort 2 taking action
robort_2.left(90)
robort_2.forward(50)
robort_2.left(90)
robort_2.forward(50)
robort_2.left(90)
robort_2.forward(50)
robort_2.left(90)


wn.exitonclick()           # To retain the sreen till we click on it
