# TODO: 1. Create the screen
import turtle as t
import time
from paddle import Pong
from ball import Ball
# TODO: 8. Keep score.
from scoreboard import Score

screen = t.Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)

# TODO: 2. Create and move the paddle
right_score = Score(320)
left_score = Score(-320)
r_pong = Pong(350, 0)
screen.listen()
screen.onkey(r_pong.up, "Up")
screen.onkey(r_pong.down, "Down")
# TODO: 3. Create another paddle
l_pong = Pong(-350, 0)
screen.onkey(l_pong.up, "w")
screen.onkey(l_pong.down, "s")
# TODO: 4. Create the ball and make it move
the_ball = Ball()

while True:
    time.sleep(the_ball.sleep_time)
    screen.update()
    the_ball.move()

    # TODO: 5. Detect collision with the wall and bounce
    if the_ball.ycor() > 295 or the_ball.ycor() < -295:
        the_ball.bounce()

    # TODO: 6. Detect collision with the paddle
    if the_ball.distance(r_pong) < 50 and the_ball.xcor() > 320 or the_ball.distance(l_pong) < 50 and the_ball.xcor() <\
            -320:
        print("Made Contact")
        the_ball.paddle_bounce()

    # TODO: 7. Detect when the paddle misses and not add to the score
    if the_ball.xcor() > 360:
        left_score.update_score()
        the_ball.new_move()
    elif the_ball.xcor() < -360:
        right_score.update_score()
        the_ball.new_move()

screen.exitonclick()
