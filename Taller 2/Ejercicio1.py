from turtle import *
from math import *

setup(640,480,0,0)
title("Ejercicio1")

l=4;  n1=0;  xy1=-100;  xy2=-30

def ir(a,b):
    penup()
    goto(a,b)
    pendown()

def poligono(a,n,m):
    while(n<m):
        forward(-2*a)
        left(90)
        n+=1

ir(xy1,xy1)
while(n1<l):
    ir(xcor()+copysign(xy2,xcor()),ycor()+copysign(xy2,ycor()))
    n2=0
    poligono(xy2,n2,l)
    ir(xcor()-copysign(xy2,xcor()),ycor()-copysign(xy2,ycor()))
    penup()
    poligono(xy1,n1,1+n1)
    n1+=1