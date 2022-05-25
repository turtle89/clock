from turtle import *
from datetime import datetime


def jump(distance, angle=0):
    penup()
    right(angle)
    forward(distance)
    left(angle)
    pendown()


def hand(length, top):
    fd(length*1.15)
    rt(90)
    fd(top/2.0)
    lt(120)
    fd(top)
    lt(120)
    fd(top)
    lt(120)
    fd(top/2.0)


def makeHandShape(name, length, top):
    reset()
    jump(-length*0.15)
    begin_poly()
    hand(length, top)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)


def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)


def setup():
    global secondHand, minuteHand, hourHand, writer
    mode("logo")
    makeHandShape("secondHand", 125, 25)
    makeHandShape("minuteHand",  130, 25)
    makeHandShape("hourHand", 90, 25)
    clockface(160)
    secondHand = Turtle()
    secondHand.shape("secondHand")
    secondHand.color("gray20", "gray80")
    minuteHand = Turtle()
    minuteHand.shape("minuteHand")
    minuteHand.color("blue1", "red1")
    hourHand = Turtle()
    hourHand.shape("hourHand")
    hourHand.color("blue3", "red3")
    for hand in secondHand, minuteHand, hourHand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()

    writer.ht()
    writer.pu()
    writer.bk(85)


def weekday(t):
    weekday = ["Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday[t.weekday()]


def date(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)


def tick():
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    try:
        tracer(False)
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(weekday(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(date(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        tracer(True)
        secondHand.setheading(6*second)
        minuteHand.setheading(6*minute)
        hourHand.setheading(30*hour)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass


def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"


if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
