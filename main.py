from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

  

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()
        
    
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -400: 
        ball.reset_position()
        score.r_point()

screen.exitonclick()