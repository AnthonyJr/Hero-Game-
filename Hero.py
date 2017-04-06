import turtle



def go_up():
	if   turtle.ycor() > (turtle.window_height() / 2)-10 :
		return;
	turtle.shape("hero_back.gif")
	turtle.setheading(90)
	turtle.forward(10)

def go_down():
	if turtle.ycor() < - (turtle.window_height() /2) +10:
		return;
	turtle.shape("hero_front.gif")
	turtle.setheading(270)
	turtle.forward(10)



def go_right():
	if   turtle.xcor() > (turtle.window_width() / 2)-10:
		return;
	turtle.shape("hero_right.gif")
	turtle.setheading(0)
	turtle.forward(10)



def go_left():
	if turtle.xcor() < - (turtle.window_width() /2) +10:
		return;
	turtle.shape("hero_left.gif")
	turtle.setheading(180)
	turtle.forward(10)

#i like to have fun sometimes lol

def peel_muffin_cap_black_blue():
	bullet = turtle.Turtle()
	bullet.hideturtle()
	bullet.penup()
	bullet.setheading(turtle.heading())
	bullet.goto(turtle.xcor(),turtle.ycor())
	bullet.showturtle()
	bullet.forward(turtle.window_height() /2)

def enemy(): #no weeknd
	enemy = turtle.Turtle()
	enemy.hideturtle()
	enemy.penup()
	enemy.goto(250,250)
	enemy.showturtle()
	enemy.goto(0,0)
	if enemy.distance(turtle) == 0:
		print "you win"




def main():
	#register the different shapes for each direction and such 
	turtle.register_shape("hero_front.gif")
	turtle.register_shape("hero_back.gif")
	turtle.register_shape("hero_left.gif")
	turtle.register_shape("hero_right.gif")

	#turtle still confuses me smh
	turtle.penup()
	turtle.title("my turtle")
	turtle.setup(500,500)
	


	#bind keys to our functions 
	turtle.onkey(go_up, "Up")
	turtle.onkey(go_down, "Down")
	turtle.onkey(go_right, "Right")
	turtle.onkey(go_left, "Left")
	turtle.onkey(peel_muffin_cap_black_blue, "b")
	turtle.onkey(enemy, "e")

	#listen for the user to hit a button
	turtle.listen()

	turtle.exitonclick()

main()