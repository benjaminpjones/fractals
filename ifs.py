#  this module is a list of Iterated Function Systems to
#  be used with the fractal module. For more info, see:
#  https://en.wikipedia.org/wiki/Iterated_function_system

import math
import random

def linear(A, point, affine):
    xNew = A[0] * point[0] + A[1] * point[1] + affine[0]
    yNew = A[2] * point[0] + A[3] * point[1] + affine[1]
    return (xNew,yNew)

def simpleLin(scalar, point, affine): return linear((scalar, 0, 0, scalar), point, affine)




def tree1(point): return linear((0.5, 0.0, 0.0, 0.5), point, (0.0, -0.25))
def tree2(point): return linear((0.5, 0.0, 0.0, 0.5), point, (0.0, 0.25))
def tree3(point): return linear((0.25, -0.25 * math.sqrt(3), 0.25 * math.sqrt(3), 0.25), point, (-math.sqrt(3)*.125, 0.125))
def tree4(point): return linear((0.25, 0.25 * math.sqrt(3), -0.25 * math.sqrt(3), 0.25), point, (math.sqrt(3)*.125, 0.125))

treeIFS = [tree1,tree2,tree3,tree4]




def dragon1(point): return linear((0.5, -0.5, 0.5, 0.5), point, (0.0, 0.0))
def dragon2(point): return linear((-0.5, -0.5, 0.5, -0.5), point, (1.0, 0.0))
def dragonUnbounded(point):
    twoPower = 20
    return (random.randint(-1,1)*2.0**twoPower,random.randint(-1,1)*2.0**twoPower)

dragonIFS = [dragon1, dragon2]



phi = (1.0 + math.sqrt(5.0))/2.0
c1 = (math.sqrt(5.0)-1)/4.0
c2 = (math.sqrt(5.0)+1)/4.0
s1 = math.sqrt(10.0+2*math.sqrt(5.0))/4.0
s2 = math.sqrt(10.0-2*math.sqrt(5.0))/4.0

def star1(point): return simpleLin(1.0/(phi**2), point, (0,1))
def star2(point): return simpleLin(1.0/(phi**2), point, (-s1,c1))
def star3(point): return simpleLin(1.0/(phi**2), point, (-s2,-c2))
def star4(point): return simpleLin(1.0/(phi**2), point, (s2,-c2))
def star5(point): return simpleLin(1.0/(phi**2), point, (s1,c1))

starIFS = [star1, star2, star3, star4, star5]



def sierp1(point): return simpleLin(1.0/2.0, point, (-0.25,0.0))
def sierp2(point): return simpleLin(1.0/2.0, point, (0.25,0.0))
def sierp3(point): return simpleLin(1.0/2.0, point, (0.0,0.5))

sierpIFS = [sierp1, sierp2, sierp3]



def fern1(point): return linear((0.0,0.0,0.0,0.16), point, (0.0,0.0))
def fern2(point): return linear((0.85,0.04,-0.04,0.85), point, (0.0,1.6))
def fern3(point): return linear((0.2,-0.26,0.23,0.22), point, (0.0,1.6))
def fern4(point): return linear((-0.15,0.28,0.26,0.24), point, (0.0,0.44))

fernIFS = [fern1, fern2, fern3, fern4]




def carpetFuncMake(affine):
    def carpetFunc(point): return simpleLin(1.0/3.0, point, (affine[0]/3.0,affine[1]/3.0))
    return carpetFunc

carpetIFS = []
for i in range(3):
    for j in range(3):
        if not (i == 1 and j == 1):
            carpetIFS.append(carpetFuncMake((float(i),float(j))))


theta = math.pi/4

def pythTree1(point): 
    return linear((math.cos(theta)**2, -math.cos(theta) * math.sin(theta), math.cos(theta) * math.sin(theta), math.cos(theta)**2), point, (0,1))
def pythTree2(point):
    return linear((math.sin(theta)**2, math.cos(theta) * math.sin(theta), -math.cos(theta) * math.sin(theta), math.sin(theta)**2), point, (math.cos(theta)**2, 1 + math.cos(theta) * math.sin(theta)))
def pythTree3(point):
    return (random.random(), random.random())

pythagorasIFS = [pythTree1, pythTree2, pythTree3]


def brocco1(point): return linear((math.sqrt(2)/4, -math.sqrt(2)/4, math.sqrt(2)/4, math.sqrt(2)/4), point, (1,0))
def brocco2(point): return linear((math.sqrt(2)/4, math.sqrt(2)/4, -math.sqrt(2)/4, math.sqrt(2)/4), point, (-1,0))
def brocco3(point): return simpleLin(1.0/2.0, point, (0,-0.5))

broccoIFS = [brocco1, brocco2, brocco3]


def blancmange1(point): return linear((0.5, 0, -0.5, 0.5), point, (0.5, 0.5))
def blancmange2(point): return linear((0.5, 0, 0.5, 0.5), point, (0.0, 0.0))
def blancvar(point): return simpleLin(1.0/3.0, point, (1.0/3.0, 0.0))

blancmangeIFS = [blancmange1, blancmange2]



def cantor1(point): return simpleLin(1.0/3.0, point, (0.0,0.0))
def cantor2(point): return simpleLin(1.0/3.0, point, (2.0/3.0,0.0))

cantorIFS = [cantor1, cantor2]



def shell1(point): return linear((0.5, -0.5, 0.5, 0.5), point, (0.25, -0.75))
def shell2(point): return linear((0.5, 0.0, 0.0, 0.5), point, (0.0, -0.0))

shellIFS = [shell1,shell2]



andrewsIFS = []
for n in range(1, 10):
    def function(point): return (n/40.0,n/40.0)
    andrewsIFS.append(function)



#    def function(point): return((point[0]*n+ point[1] + 1)/(n**n + 1), ((point[1] + 1)*n - point[0])/(n**n + 1))

