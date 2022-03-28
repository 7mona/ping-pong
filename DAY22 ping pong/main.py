import turtle,paddle,ball,time,score

screen = turtle.Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PING-PONG")

screen.tracer(0)

paddle1 = paddle.Paddle(350,0)
paddle2 = paddle.Paddle(-350,0)
striker = ball.Ball()
scoring = score.Scoreboard()

screen.update()

screen.listen()
screen.onkeypress(paddle1.go_up,"Up")
screen.onkeypress(paddle1.go_down,"Down")
screen.onkeypress(paddle2.go_up,"w")
screen.onkeypress(paddle2.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(striker.move_speed)
    screen.update()
    striker.move()
    if striker.ycor() > 280 or striker.ycor() < -280:
        striker.bounce_y()

    if striker.distance(paddle1) < 50 and striker.xcor() > 330 or striker.distance(paddle2) < 50 and striker.xcor() <-330:
        striker.bounce_x()
    if striker.xcor()>380:
        scoring.l_score += 1
        scoring.update_score()
        striker.reset_position()
        
        
    if striker.xcor()<-380:
        scoring.r_score += 1
        scoring.update_score()
        striker.reset_position()
        

screen.exitonclick()