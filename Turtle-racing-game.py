import random
import turtle

myscreen= turtle.Screen()

myscreen.bgcolor('#76EEC6')
myscreen.setup(1.0,1.0)
myscreen.title('Turtle Racing Game')

pen=turtle.Turtle()

pen.speed(0)
pen.penup()
pen.goto(-200,200)

pen.pendown()

for i in range(1,11):
	pen.write(i,font=('times',15))
	pen.setheading(-90)
	pen.forward(250)
	if i==10:
		pen.write(" FINISH LINE ",font=('times',20))
	pen.back(250)
	pen.penup()
	pen.setheading(0)
	pen.forward(50)
	pen.down()

finishLineX=250

def createTurtlePlayer(color, startx, starty): 
	player=turtle.Turtle()
	player.color(color)
	player.shape("turtle")
	player.penup()
	player.goto(startx, starty)
	player.pendown()
	return player

p1=createTurtlePlayer('magenta',-210,150)
p2=createTurtlePlayer('cyan',-210,100)
p3=createTurtlePlayer('black',-210,50)
p4=createTurtlePlayer('green',-210,0)

while True:
	p1.forward(random.randint(5,10))
	if p1.pos()[0]>=finishLineX:
		p1.write(' I won!!!',font=('Times',20))
		break
	p2.forward(random.randint(5,10))
	if p2.pos()[0]>=finishLineX:
		p2.write(' I won!!!',font=('Times',20))
		break
	p3.forward(random.randint(5,10))
	if p3.pos()[0]>=finishLineX:
		p3.write(' I won!!!',font=('Times',20))
		break
	p4.forward(random.randint(5,10))
	if p4.pos()[0]>=finishLineX:
		p4.write(' I won!!!',font=('Times',20))
		break

turtle.done()