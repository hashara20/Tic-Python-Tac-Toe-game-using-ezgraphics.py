#import module ezgraphics
from ezgraphics import *



# Create the graphics window.
win = GraphicsWindow(640, 640)
win.setTitle("Tic_Tac_Toe")
canvas = win.canvas()
canvas.drawRectangle(20, 20, 600, 600)



canvas.drawRectangle(20,20,200,200)
canvas.drawRectangle(220, 20, 200, 200)
canvas.drawRectangle(420, 20, 200, 200)

canvas.drawRectangle(20, 220, 200, 200)
canvas.drawRectangle(220,220, 200, 200)
canvas.drawRectangle(420,220, 200, 200)

canvas.drawRectangle(20, 420, 200, 200)
canvas.drawRectangle(220, 420, 200, 200)
canvas.drawRectangle(420, 420, 200, 200)

canvas.setFill("red")
canvas.drawRectangle(280,0,80,15)
canvas.setFill("black")
canvas.drawRectangle(290,0,60,15)

canvas.setOutline("white")
canvas.drawText(300,1,"QUITE")

#function to run the game
def get_click():
    swap1 = 0
    swap2 = 0
    swap3 = 0
    swap4 = 0
    swap5 = 0
    swap6 = 0
    swap7 = 0
    swap8 = 0
    swap9 = 0

    w1=0
    w2=0
    w3=0
    w4=0
    w5=0
    w6=0
    w7=0
    w8=0
    w9=0

    y1=0
    y2=0
    y3=0
    y4=0
    y5=0
    y6=0
    y7=0
    y8=0
    y9=0



    for i in range(0,9):
        #creating a list to store the clicking position
        x=list()

        #get the input as clicks
        x=win.getMouse()

        #for marker X

        if(x[0]>290 and x[0]<350 and x[1]>0 and x[1]<15):
            exit()


        if(x[0]>20 and x[0]<220 and x[1]>20 and x[1]<220 and i%2==0 and swap1==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(70,50,"X")
            swap1=1
            w1=1

        elif(x[0]>220 and x[0]<420 and x[1]>20 and x[1]<220 and i%2==0 and swap2==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(270,50,"X")
            swap2=1
            w2=1

        elif(x[0]>420 and x[0]<620 and x[1]>20 and x[1]<220 and i%2==0 and swap3==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(470, 50, "X")
            swap3=1
            w3=1

        elif(x[0]>20 and x[0]<220 and x[1]>220 and x[1]<420 and i%2==0 and swap4==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(70, 250, "X")
            swap4=1
            w4=1

        elif(x[0]>220 and x[0]<420 and x[1]>220 and x[1]<420 and i%2==0 and swap5==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(270, 250, "X")
            swap5=1
            w5=1

        elif(x[0]>420 and x[0]<620 and x[1]>220 and x[1]<420 and i%2==0 and swap6==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(470, 250, "X")
            swap6=1
            w6=1

        elif(x[0]>20 and x[0]<220 and x[1]>420 and x[1]<620 and i%2==0 and swap7==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(70, 450, "X")
            swap7=1
            w7=1

        elif(x[0]>220 and x[0]<420 and x[1]>420 and x[1]<620 and i%2==0 and swap8==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(270, 450, "X")
            swap8=1
            w8=1

        elif(x[0]>420 and x[0]<620 and x[1]>420 and x[1]<620 and i%2==0 and swap9==0):
            canvas.setFontSize(100)
            canvas.setOutline("blue")
            canvas.drawText(470, 450, "X")
            swap9=1
            w9=1

        #for marker O

        if (x[0] > 20 and x[0] < 220 and x[1] > 20 and x[1] < 220 and i % 2 == 1 and swap1==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(70, 50, "O")
            swap1=1
            y1=1

        elif (x[0] > 220 and x[0] < 420 and x[1] > 20 and x[1] < 220 and i % 2 == 1 and swap2==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(270, 50, "O")
            swap2=1
            y2=1

        elif (x[0] > 420 and x[0] < 620 and x[1] > 20 and x[1] < 220 and i % 2 == 1 and swap3==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(470, 50, "O")
            swap3=1
            y3=1

        elif (x[0] > 20 and x[0] < 220 and x[1] > 220 and x[1] < 420 and i % 2 == 1 and swap4==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(70, 250, "O")
            swap4=1
            y4=1

        elif (x[0] > 220 and x[0] < 420 and x[1] > 220 and x[1] < 420 and i % 2 == 1 and swap5==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(270, 250, "O")
            swap5=1
            y5=1

        elif (x[0] > 420 and x[0] < 620 and x[1] > 220 and x[1] < 420 and i % 2 == 1 and swap6==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(470, 250, "O")
            swap6=1
            y6=1

        elif (x[0] > 20 and x[0] < 220 and x[1] > 420 and x[1] < 620 and i % 2 == 1 and swap7==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(70, 450, "O")
            swap7=1
            y7=1

        elif (x[0] > 220 and x[0] < 420 and x[1] > 420 and x[1] < 620 and i % 2 == 1 and swap8==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(270, 450, "O")
            swap8=1
            y8=1

        elif (x[0] > 420 and x[0] < 620 and x[1] > 420 and x[1] < 620 and i % 2 == 1 and swap9==0):
            canvas.setFontSize(100)
            canvas.setOutline("red")
            canvas.drawText(470, 450, "O")
            swap9=1
            y9=1
        elif (i==8):
            canvas.setFill("yellow")
            canvas.drawRectangle(45, 180, 550, 300)

            canvas.setFontSize(50)
            canvas.setOutline("blue")
            canvas.drawText(100, 215,"it is a Tie")
        else:
            i=i-1

        if(w1==w2==w3!=0 or w4==w5==w6!=0 or w7==w8==w9!=0 or w1==w5==w9!=0 or w3==w5==w7!=0 or w1==w4==w7!=0 or w2==w5==w8!=0 or w3==w6==w9!=0 ):
            canvas.setFill("yellow")
            canvas.drawRectangle(45,180,550,300)

            canvas.setFontSize(50)
            canvas.setOutline("blue")
            canvas.drawText(60,215," 'X'\n is the Winner\n Congradulation!")

        if(y1==y2==y3!=0 or y4==y5==y6!=0 or y7==y8==y9!=0 or y1==y5==y9!=0 or y3==y5==y7!=0 or y1==y4==y7!=0 or y2==y5==y8!=0 or y3==y6==y9!=0):
            canvas.setFill("yellow")
            canvas.drawRectangle(45, 180, 550, 300)

            canvas.setFontSize(50)
            canvas.setOutline("red")
            canvas.drawText(60, 215, " 'O'\n is the Winner\n Congradulation!")




    win.wait()




get_click()
