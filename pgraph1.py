#Long program
#Katie King 11/2/18
#Farm
from graphics import *
win = GraphWin("Graphics Window", 600,600)

import time

#background spring
rect = Rectangle(Point (0,0), Point(600,600))
rect.setFill('lightblue')
rect.setOutline('lightblue')
rect.draw(win)

#ground spring
rect = Rectangle(Point (0,320), Point(600,600))
rect.setFill('green')
rect.setOutline('green')
rect.draw(win)

#sun
Sun = Circle(Point(-30,310),30)
Sun.setOutline('Gold')
Sun.setFill('Gold')
Sun.draw(win)

time.sleep(3)

for i in range(125):
    Sun.move(2,-2)
    time.sleep(.02)

#barn
#walls
rect = Rectangle(Point (80,290), Point(170,390))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (290,390), Point(170,290))
rect.setFill('darkred')
rect.setOutline('darkred')
rect.draw(win)

rect = Rectangle(Point (170,290), Point(170,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#roof
rect = Rectangle(Point (120,290), Point(250,205))
rect.setFill('grey')
rect.setOutline('grey')
rect.draw(win)

aPolygon = Polygon(Point(80,290), Point(120,205), Point(170,290))
aPolygon.setFill('darkgrey')
aPolygon.setOutline('darkgrey')
aPolygon.draw(win)

aPolygon = Polygon(Point(290,290), Point(250,205), Point(250,290))
aPolygon.setFill('grey')
aPolygon.setOutline('grey')
aPolygon.draw(win)

#door
rect = Rectangle(Point (105,325), Point(150,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#tree
rect = Rectangle(Point (500,370), Point(530,470))
rect.setFill('brown')
rect.setOutline('brown')
rect.draw(win)

aCircle = Circle (Point(500,370),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

#apples
Apple = Circle(Point(495, 340),10)
Apple.setFill('pink')
Apple.setOutline('pink')
Apple.draw(win)
aCircle = Circle (Point(495,340),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

Apple = Circle(Point(485, 390),10)
Apple.setFill('pink')
Apple.setOutline('pink')
Apple.draw(win)
aCircle = Circle (Point(485,390),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

Apple = Circle(Point(545, 354),10)
Apple.setFill('pink')
Apple.setOutline('pink')
Apple.draw(win)
aCircle = Circle (Point(545,354),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

Apple = Circle(Point(516, 356),10)
Apple.setFill('pink')
Apple.setOutline('pink')
Apple.draw(win)
aCircle = Circle (Point(516,356),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

#fence post
rect = Rectangle(Point (500,400), Point(525,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (300,400), Point(325,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (100,400), Point(125,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

#fence
rect = Rectangle(Point (0,425), Point(600,450))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (0,525), Point(600,550))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

time.sleep(5)

#background summer
rect = Rectangle(Point (0,0), Point(600,600))
rect.setFill('lightblue')
rect.setOutline('lightblue')
rect.draw(win)

#ground summer
rect = Rectangle(Point (0,320), Point(600,600))
rect.setFill('green')
rect.setOutline('green')
rect.draw(win)

#sun
Sun = Circle(Point(-30,310),30)
Sun.setOutline('Gold')
Sun.setFill('Gold')
Sun.draw(win)

time.sleep(3)

for i in range(125):
    Sun.move(2,-2)
    time.sleep(.02)


#barn
#walls
rect = Rectangle(Point (80,290), Point(170,390))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (290,390), Point(170,290))
rect.setFill('darkred')
rect.setOutline('darkred')
rect.draw(win)

rect = Rectangle(Point (170,290), Point(170,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#roof
rect = Rectangle(Point (120,290), Point(250,205))
rect.setFill('grey')
rect.setOutline('grey')
rect.draw(win)

aPolygon = Polygon(Point(80,290), Point(120,205), Point(170,290))
aPolygon.setFill('darkgrey')
aPolygon.setOutline('darkgrey')
aPolygon.draw(win)

aPolygon = Polygon(Point(290,290), Point(250,205), Point(250,290))
aPolygon.setFill('grey')
aPolygon.setOutline('grey')
aPolygon.draw(win)

#door
rect = Rectangle(Point (105,325), Point(150,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#tree
rect = Rectangle(Point (500,370), Point(530,470))
rect.setFill('brown')
rect.setOutline('brown')
rect.draw(win)

aCircle = Circle (Point(500,370),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill('darkgreen')
aCircle.setOutline('darkgreen')
aCircle.draw(win)

#flowers
aCircle = Circle (Point(520,530),10)
aCircle.setFill('purple')
aCircle.setOutline('purple')
aCircle.draw(win)

aCircle = Circle (Point(520,530),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

aCircle = Circle (Point(370,350),10)
aCircle.setFill('darkblue')
aCircle.setOutline('darkblue')
aCircle.draw(win)

aCircle = Circle (Point(370,350),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)

aCircle = Circle (Point(200,430),10)
aCircle.setFill('pink')
aCircle.setOutline('pink')
aCircle.draw(win)

aCircle = Circle (Point(200,430),3)
aCircle.setFill('Gold')
aCircle.setOutline('Gold')
aCircle.draw(win)


#apples
Apple = Circle(Point(495, 340),10)
Apple.setFill('darkred')
Apple.setOutline('black')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(8):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(485, 390),10)
Apple.setFill('red')
Apple.setOutline('darkred')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(5):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(545, 354),10)
Apple.setFill('greenyellow')
Apple.setOutline('limegreen')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(8):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(516, 356),10)
Apple.setFill('red')
Apple.setOutline('darkred')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(8):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

#fence post
rect = Rectangle(Point (500,400), Point(525,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (300,400), Point(325,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (100,400), Point(125,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

#fence
rect = Rectangle(Point (0,425), Point(600,450))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (0,525), Point(600,550))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

time.sleep(3)

#background fall
rect = Rectangle(Point (0,0), Point(600,600))
rect.setFill('lightblue')
rect.setOutline('lightblue')
rect.draw(win)

#ground fall
rect = Rectangle(Point (0,320), Point(600,600))
rect.setFill(color_rgb(148, 165, 71))
rect.setOutline(color_rgb(148, 165, 71))
rect.draw(win)

#sun
Sun = Circle(Point(-30,310),30)
Sun.setOutline('Gold')
Sun.setFill('Gold')
Sun.draw(win)

time.sleep(3)

for i in range(125):
    Sun.move(2,-2)
    time.sleep(.02)

#barn
#walls
rect = Rectangle(Point (80,290), Point(170,390))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (290,390), Point(170,290))
rect.setFill('darkred')
rect.setOutline('darkred')
rect.draw(win)

rect = Rectangle(Point (170,290), Point(170,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#roof
rect = Rectangle(Point (120,290), Point(250,205))
rect.setFill('grey')
rect.setOutline('grey')
rect.draw(win)

aPolygon = Polygon(Point(80,290), Point(120,205), Point(170,290))
aPolygon.setFill('darkgrey')
aPolygon.setOutline('darkgrey')
aPolygon.draw(win)

aPolygon = Polygon(Point(290,290), Point(250,205), Point(250,290))
aPolygon.setFill('grey')
aPolygon.setOutline('grey')
aPolygon.draw(win)

#door
rect = Rectangle(Point (105,325), Point(150,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#tree
rect = Rectangle(Point (500,370), Point(530,470))
rect.setFill('brown')
rect.setOutline('brown')
rect.draw(win)

aCircle = Circle (Point(500,370),45)
aCircle.setFill('green')
aCircle.setOutline('green')
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill('green')
aCircle.setOutline('green')
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill('green')
aCircle.setOutline('green')
aCircle.draw(win)

time.sleep(1)

aCircle = Circle (Point(500,370),45)
aCircle.setFill(color_rgb(229, 213, 4))
aCircle.setOutline(color_rgb(229, 213, 4))
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill(color_rgb(229, 213, 4))
aCircle.setOutline(color_rgb(229, 213, 4))
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill(color_rgb(229, 213, 4))
aCircle.setOutline(color_rgb(229, 213, 4))
aCircle.draw(win)

time.sleep(1)

aCircle = Circle (Point(500,370),45)
aCircle.setFill(color_rgb(198, 116, 7))
aCircle.setOutline(color_rgb(198, 116, 7))
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill(color_rgb(198, 116, 7))
aCircle.setOutline(color_rgb(198, 116, 7))
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill(color_rgb(198, 116, 7))
aCircle.setOutline(color_rgb(198, 116, 7)) 
aCircle.draw(win)

time.sleep(1)

aCircle = Circle (Point(500,370),45)
aCircle.setFill('darkred')
aCircle.setOutline('darkred')
aCircle.draw(win)

aCircle = Circle (Point(530,364),45)
aCircle.setFill('darkred')
aCircle.setOutline('darkred')
aCircle.draw(win)

aCircle = Circle (Point(515,350),45)
aCircle.setFill('darkred')
aCircle.setOutline('darkred')
aCircle.draw(win)

#fence post
rect = Rectangle(Point (500,400), Point(525,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (300,400), Point(325,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (100,400), Point(125,600))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

#fence
rect = Rectangle(Point (0,425), Point(600,450))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (0,525), Point(600,550))
rect.setFill('chocolate')
rect.setOutline('black')
rect.draw(win)

time.sleep(3)

#background winter
rect = Rectangle(Point (0,0), Point(600,600))
rect.setFill('lightblue')
rect.setOutline('lightblue')
rect.draw(win)

#ground winter
rect = Rectangle(Point (0,320), Point(600,600))
rect.setFill('white')
rect.setOutline('white')
rect.draw(win)

#sun
Sun = Circle(Point(-30,310),30)
Sun.setOutline('Gold')
Sun.setFill('Gold')
Sun.draw(win)

time.sleep(3)

for i in range(125):
    Sun.move(2,-2)
    time.sleep(.02)

#barn
#walls
rect = Rectangle(Point (80,290), Point(170,390))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (290,390), Point(170,290))
rect.setFill('darkred')
rect.setOutline('darkred')
rect.draw(win)

rect = Rectangle(Point (170,290), Point(170,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#roof
roof = Rectangle(Point (120,290), Point(250,205))
roof.setFill('grey')
roof.setOutline('grey')
roof.draw(win)

roof = Rectangle(Point (120,250), Point(250,205))
roof.setFill('white')
roof.setOutline('white')
roof.draw(win)

roof = Polygon(Point(80,290), Point(120,205), Point(170,290))
roof.setFill('darkgrey')
roof.setOutline('darkgrey')
roof.draw(win)

roof = Polygon(Point(290,290), Point(250,205), Point(250,290))
roof.setFill('grey')
roof.setOutline('grey')
roof.draw(win)

roof = Polygon(Point(271,250), Point(250,205), Point(250,250))
roof.setFill('white')
roof.setOutline('white')
roof.draw(win)

#door
rect = Rectangle(Point (105,325), Point(150,390))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

#tree
rect = Rectangle(Point (500,370), Point(530,470))
rect.setFill('brown')
rect.setOutline('brown')
rect.draw(win)

rect = Rectangle(Point (550,400), Point(590,450))
rect.setFill(color_rgb(143, 133, 163))
rect.setOutline(color_rgb(143, 133, 163))
rect.draw(win)

rect = Rectangle(Point (550,420), Point(590,430))
rect.setFill(color_rgb(247, 241, 160))
rect.setOutline(color_rgb(247, 241, 160))
rect.draw(win)

rect = Rectangle(Point (570,400), Point(580,450))
rect.setFill(color_rgb(247, 241, 160))
rect.setOutline(color_rgb(247, 241, 160))
rect.draw(win)

tree = Polygon(Point(450,420), Point(510,300), Point(580,420))
tree.setFill('green')
tree.setOutline('green')
tree.draw(win)

aCircle = Circle (Point(480,400),5)
aCircle.setFill('hotpink')
aCircle.setOutline('deeppink')
aCircle.draw(win)

aCircle = Circle (Point(500,360),5)
aCircle.setFill('midnightblue')
aCircle.setOutline('navy blue')
aCircle.draw(win)

aCircle = Circle (Point(560,412),5)
aCircle.setFill('purple')
aCircle.setOutline('darkviolet')
aCircle.draw(win)

aCircle = Circle (Point(515,375),5)
aCircle.setFill('aquamarine')
aCircle.setOutline('mediumaquamarine')
aCircle.draw(win)

aCircle = Circle (Point(525,340),5)
aCircle.setFill('orangered')
aCircle.setOutline('red')
aCircle.draw(win)

rect = Rectangle(Point (460,450), Point(490,490))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (460,465), Point(490,475))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (470,450), Point(480,490))
rect.setFill('red')
rect.setOutline('red')
rect.draw(win)

rect = Rectangle(Point (530,450), Point(560,490))
rect.setFill(color_rgb(93, 34, 181))
rect.setOutline(color_rgb(93, 34, 181))
rect.draw(win)

rect = Rectangle(Point (530,465), Point(560,475))
rect.setFill(color_rgb(209, 209, 209))
rect.setOutline(color_rgb(209, 209, 209))
rect.draw(win)

rect = Rectangle(Point (540,450), Point(550,490))
rect.setFill(color_rgb(209, 209, 209))
rect.setOutline(color_rgb(209, 209, 209))
rect.draw(win)

rect = Rectangle(Point (480,495), Point(540,520))
rect.setFill('black')
rect.setOutline('black')
rect.draw(win)

rect = Rectangle(Point (480,505), Point(540,510))
rect.setFill(color_rgb(43, 229, 229))
rect.setOutline(color_rgb(43, 229, 229))
rect.draw(win)

rect = Rectangle(Point (505,495), Point(520,520))
rect.setFill(color_rgb(43, 229, 229))
rect.setOutline(color_rgb(43, 229, 229))
rect.draw(win)

#snow clouds
aCircle = Circle (Point(0,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(10,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(30,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(50,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(80,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(100,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(130,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(160,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(180,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(210,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(240,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(260,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(290,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(320,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(340,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(370,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(400,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(420,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(450,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(480,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(500,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(530,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(560,90),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

aCircle = Circle (Point(580,100),45)
aCircle.setFill('grey')
aCircle.setOutline('grey')
aCircle.draw(win)

#snow
Apple = Circle(Point(10, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(200, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(150, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(125, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(500, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(450, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(425, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(400, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(350, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(325, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(300, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(525, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(550, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)

Apple = Circle(Point(600, 155),10)
Apple.setFill('white')
Apple.setOutline('white')
Apple.draw(win)

time.sleep(3)

i = 0
for i in range(20):
    y = (i * 5)
    Apple.move(0,y)
    time.sleep(.2)
