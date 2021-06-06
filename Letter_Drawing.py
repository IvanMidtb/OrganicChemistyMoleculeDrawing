####################################
# Ivan Midtbust Heger, Jackson Sims
# CSCI 150
# Final Project
####################################


from typing import *
import turtle

n = 1

def test_function():
    complete = False
    while not complete:
        t = turtle.Turtle()
        t.speed(0)
        for i in range(1):
            t.penup()
            t.goto(0, 100 * (i - 2))
            t.pendown()
            letter_cl(t, n, 100)
        complete = input('Would you like to go again?')


def letter_o(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        t.left(90)
        letter_o(t, n - 1, size / 2)
        t.right(90)
        letter_o(t, n - 1, size / 2)
        t.right(90)
        letter_o(t, n - 1, size)
        t.right(90)
        letter_o(t, n - 1, size / 2)
        t.right(90)
        letter_o(t, n - 1, size / 2)


def letter_h(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        t.left(90)
        letter_h(t, n - 1, size / 2)
        t.right(180)
        letter_h(t, n - 1, size)
        t.left(180)
        letter_h(t, n - 1, size / 2)
        t.right(90)
        letter_h(t, n - 1, size / 2)
        t.left(90)
        letter_h(t, n - 1, size / 2)
        t.right(180)
        letter_h(t, n - 1, size)
        t.left(180)
        letter_h(t, n - 1, size / 2)


def letter_cl(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        # C begins
        t.left(90)
        letter_cl(t, n - 1, size / 2)
        t.right(90)
        letter_cl(t, n - 1, size / 3)
        t.right(180)
        letter_cl(t, n - 1, size / 3)
        t.left(90)
        letter_cl(t, n - 1, size)
        t.left(90)
        letter_cl(t, n - 1, size / 3)
        t.right(180)
        letter_cl(t, n - 1, size / 3)
        t.right(90)
        letter_cl(t, n - 1, size)
        # C is complete at this point; moving to L
        t.penup()
        t.right(90)
        letter_cl(t, n - 1, size / 1.5)
        t.right(90)
        t.pendown()
        letter_cl(t, n - 1, size)
        t.left(90)
        letter_cl(t, n - 1, size / 3)


def letter_fl(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        # F begins
        t.right(90)
        letter_fl(t, n - 1, size / 2)
        t.right(180)
        letter_fl(t, n - 1, size / 2)
        t.right(90)
        letter_fl(t, n - 1, size / 2)
        t.left(180)
        letter_fl(t, n - 1, size / 2)
        t.right(90)
        letter_fl(t, n - 1, size / 2)
        t.right(90)
        letter_fl(t, n - 1, size / 2)
        t.right(180)
        letter_fl(t, n - 1, size / 2)
        t.right(180)
        # F complete, moving to L
        t.penup()
        letter_fl(t, n - 1, size / 1.5)
        t.right(90)
        t.pendown()
        letter_fl(t, n - 1, size)
        t.left(90)
        letter_fl(t, n - 1, size / 3)


def letter_i(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        t.penup()
        letter_i(t, n - 1, size / 3)
        t.pendown()
        t.left(90)
        letter_i(t, n - 1, size / 2)
        t.left(90)
        letter_i(t, n - 1, size / 3)
        t.right(180)
        letter_i(t, n - 1, size / 1.5)
        t.right(180)
        letter_i(t, n - 1, size / 3)
        t.left(90)
        letter_i(t, n - 1, size)
        t.right(90)
        letter_i(t, n - 1, size / 3)
        t.right(180)
        letter_i(t, n - 1, size / 1.5)


def letter_br(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        letter_br(t, n - 1, size / 2)
        t.left(90)
        letter_br(t, n - 1, size / 2)
        t.left(90)
        letter_br(t, n - 1, size / 2)
        t.left(90)
        letter_br(t, n - 1, size)
        t.left(90)
        letter_br(t, n - 1, size / 2)
        t.left(90)
        letter_br(t, n - 1, size / 2)
        t.right(90)
        t.penup()
        letter_br(t, n - 1, size / 3)
        t.left(90)
        t.pendown()
        letter_br(t, n - 1, size / 2)
        t.right(90)
        letter_br(t, n - 1, size / 2)
        t.right(90)
        letter_br(t, n - 1, size / 3)
        t.right(180)
        letter_br(t, n - 1, size / 3)
        t.left(90)
        letter_br(t, n - 1, size / 2)
        t.left(90)
        letter_br(t, n - 1, size)

