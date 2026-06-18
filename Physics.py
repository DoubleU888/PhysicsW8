Web VPython 3.2

from vpython import *

ball = sphere(
    pos=vector(5,0,0),
    radius=0.3,
    color=color.green,
    make_trail=True
)

wall = box(
    pos=vector(-0.15,0,0),
    size=vector(0.3,2,2),
    color=color.green
)

spring = helix(
    pos=vector(0,0,0),
    axis=ball.pos,
    radius=0.2,
    color=color.green
)
scene.background = vec(0,0.9,0.8)

m = 1
k = 1
x0=2.5

v = vector(0,0,0)

dt = 0.01

info = label(pos=vector(0,2,0))

while True:
    rate(100)

    F = -k * (ball.pos.x -x0)

    a = F / m

    v.x = v.x + a * dt

    ball.pos.x = ball.pos.x + v.x * dt

    spring.axis = ball.pos
    
    info.text = (
        "x = " + str(round(ball.pos.x,2))
        + "\n"
        + "v = " + str(round(v.x,2))
    )
