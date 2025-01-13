import pygame as py ; import random
py.init()

width = 600 ; height = 500
screen = py.display.set_mode((width,height))
py.display.set_caption("BRICK-OUT")
py.display.set_icon(py.image.load("icon.png"))
clock = py.time.Clock()

#game images and fonts
font = py.font.Font("pooh.ttf",32)
#title and button
title = py.image.load("title.png")
button = py.Rect(190,320,190,49)
button_ = py.Rect(187,317,196,55)
winner = py.image.load("win.png")

def game():
    clock.tick(30)
    #paddle pos. and contraint
    posx = 260 ; posy = 470 ; dx = 0
    blue = (13,158,255) ; green = (55,237,88) ; red = (237,0,71)

    prob = random.randint(0,2)
    if prob == 0:
        d_x = 0.1
    else:
        d_x = -0.1

    ballx = random.randint(240,326) ; bally = 435 ; padx = ballx - 1.5 ; pady = bally - 1.5 ;  d_y = -0.1

    row1 = 30 ; row1_1 = 30; row2 = 70 ; row2_1 = 30; row3 = 110 ;row3_1 = 30 # just get rid of all variables
    row1_2 = 140 ; row2_2 = 140 ; row3_2 = 140 # use values as it is
    row1_3 = 250 ; row2_3 = 250 ; row3_3 = 250 # put values directly into bb_coll func.
    row1_4 = 360 ; row2_4 = 360 ; row3_4 = 360 #check values if they are even correct....
    row1_5 = 470; row2_5 = 470 ; row3_5 = 470


    def bb_coll(x1,y1,x2,y2): #row[0] row[1] and ballx, bally
        distx = abs(x1-x2)
        disty = abs(y1-y2)
        if (distx <= 82 and distx>=1) and disty <= 31:
            return True


    def pb_coll(x1,y1,x2,y2): #posx , posy and ballx, bally
        global one_half, two_half , mid
        one_half = False ; two_half = False ;mid = False
        distx = abs(x1-x2)
        disty = abs(y1-y2)
        if (distx <=35 and distx >=0) and disty <= 16:
            one_half = True
            return
        elif (distx > 30 and distx < 50) and disty <=16:
            mid = True
            return
        elif (distx >= 50 and distx <=78) and disty <= 16:
            two_half = True
            return


    run = True
    while run :
        for e in py.event.get():
            if e.type == py.QUIT:
                run = False
            if e.type == py.KEYDOWN:
                if e.key == py.K_LEFT :
                    dx = -0.3
                if e.key == py.K_RIGHT:
                    dx = 0.3
            elif e.type == py.KEYUP:
                dx = 0
                if e.key == py.K_ESCAPE:
                    run = False
                    return False

        #player boundaries
        posx += dx
        if posx >= 510:
            posx = 510
        elif posx <= 10:
            posx = 10

        #ball pos. and boundaries
        ballx += d_x ; bally += d_y ; padx += d_x ; pady += d_y
        if ballx >= 575 and padx >= 573.5:
            d_x = -0.1
        if ballx <= 10 and padx <= 8.5:
            d_x= 0.1
        if bally <= 11 and pady <= 9.5:
            d_y = 0.1
        if bally >= 515 and pady >= 513.5:
            d_y = -0.1



        # sequential rendering of screen
        screen.fill((147,217,255))
        py.draw.rect(screen,(0,0,0),(posx-2.5,posy-2.5,85.8,26),100) #black padding
        py.draw.rect(screen,(255,255,255),(posx,posy,80,20),100) # white padding

        py.draw.rect(screen,(0,0,0),(padx,pady,19,19),100) # black outline
        py.draw.rect(screen,(255,255,255),(ballx,bally,15,15),100) #white part of the ball


        # bricks
        py.draw.rect(screen,blue,(row1_1,row1,100,30)) ; py.draw.rect(screen,blue,(row1_2,row1,100,30)) ; py.draw.rect(screen,blue,(row1_3,row1,100,30)) ;py.draw.rect(screen,blue,(row1_4,row1,100,30)) ; py.draw.rect(screen,blue,(row1_5,row1,100,30))
        py.draw.rect(screen,green,(row2_1,row2,100,30)) ; py.draw.rect(screen,green,(row2_2,row2,100,30)) ; py.draw.rect(screen,green,(row2_3,row2,100,30)); py.draw.rect(screen,green,(row2_4,row2,100,30)) ;py.draw.rect(screen,green,(row2_5,row2,100,30))
        py.draw.rect(screen,red,(row3_1,row3,100,30)) ; py.draw.rect(screen,red,(row3_2,row3,100,30)) ; py.draw.rect(screen,red,(row3_3,row3,100,30)); py.draw.rect(screen,red,(row3_4,row3,100,30)) ;py.draw.rect(screen,red,(row3_5,row3,100,30))
        
        # collision between BRICKS and BALL

        #row1
        bb_coll(row1_1,row1,ballx,bally)
        bb_coll(row1_2,row1,ballx,bally)
        bb_coll(row1_3,row1,ballx,bally)
        bb_coll(row1_4,row1,ballx,bally)
        bb_coll(row1_5,row1,ballx,bally)

        if bb_coll(row1_1,row1,ballx,bally):
            d_y = 0.1 ; row1_1 = -1000
        elif bb_coll(row1_2,row1,ballx,bally):
            d_y = 0.1 ;row1_2 = -1000
        elif bb_coll(row1_3,row1,ballx,bally):
            d_y = 0.1 ; row1_3 = -1000
        elif bb_coll(row1_4,row1,ballx,bally):
            d_y = 0.1 ; row1_4 = -1000
        elif bb_coll(row1_5,row1,ballx,bally):
            d_y = 0.1 ; row1_5 = -1000





        #row 2
        bb_coll(row2_1,row2,ballx,bally)
        bb_coll(row2_2,row2,ballx,bally)
        bb_coll(row2_3,row2,ballx,bally)
        bb_coll(row2_4,row2,ballx,bally)
        bb_coll(row2_5,row2,ballx,bally)

        if bb_coll(row2_1,row2,ballx,bally):
            d_y = 0.1 ; row2_1 = -1000
        elif bb_coll(row2_2,row2,ballx,bally):
            d_y = 0.1 ;row2_2 = -1000
        elif bb_coll(row2_3,row2,ballx,bally):
            d_y = 0.1 ; row2_3 = -1000
        elif bb_coll(row2_4,row2,ballx,bally):
            d_y = 0.1 ; row2_4 = -1000
        elif bb_coll(row2_5,row2,ballx,bally):
            d_y = 0.1 ; row2_5 = -1000



        #row 3:
        bb_coll(row3_1,row3,ballx,bally)
        bb_coll(row3_2,row3,ballx,bally)
        bb_coll(row3_3,row3,ballx,bally)
        bb_coll(row3_4,row3,ballx,bally)
        bb_coll(row3_5,row3,ballx,bally)

        if bb_coll(row3_1,row3,ballx,bally):
            d_y = 0.1 ; row3_1 = -1000
        elif bb_coll(row3_2,row3,ballx,bally):
            d_y = 0.1 ;row3_2 = -1000
        elif bb_coll(row3_3,row3,ballx,bally):
            d_y = 0.1 ; row3_3 = -1000
        elif bb_coll(row3_4,row3,ballx,bally):
            d_y = 0.1 ; row3_4 = -1000
        elif bb_coll(row3_5,row3,ballx,bally):
            d_y = 0.1 ; row3_5 = -1000
        
        
        # TODO : collsion between PADDLE and BALL
        pb_coll(posx,posy,ballx,bally)
        if one_half == True:
            d_y = -0.1 ; d_x = -0.1
        elif two_half == True:
            d_y = -0.1 ; d_x = 0.1
        elif mid == True:
            d_y = -0.1 ; d_x = 0

        global win
        win = False
        if  row1_1 == -1000 and row1_2 == -1000 and row1_3 == -1000 and row1_4 == -1000 and row1_5 == -1000 and row2_1 == -1000 and row2_3 == -1000 and row2_3 == -1000 and row2_4 == -1000 and row2_5 == -1000 and row3_1 == -1000 and row3_2 == -1000 and row3_3 == -1000 and row3_4 == -1000 and row3_5 == -1000:
            win = True
            run = False
            return True
        
        
        py.display.update()
            




# starting menu and stuff
def menu():
    clock.tick(30)
    def start():
        text = font.render("START",True,(0,0,0))
        screen.blit(text,(255,330))
    r = 255 ; g = 255 ; b = 255

    run = True
    while run :
        for e in py.event.get():
            if e.type == py.QUIT:
                run = False
                py.quit()
                return False

            if e.type == py.KEYDOWN:
                if e.key == py.K_RETURN:
                    r = 255 ; g = 225 ; b = 2
                
            if e.type == py.KEYUP:
                if e.key == py.K_RETURN:
                    r = 255 ; g = 255 ; b = 255
                    run = False
                    return True
                
                if e.key == py.K_ESCAPE:
                    run = False
                    return False

        #screen color through out
        screen.fill((147,217,255))
        screen.blit(title,(100,90))
        py.draw.rect(screen,(0,0,0),button_)
        py.draw.rect(screen,(r,g,b),button)
        start()
        py.display.update()


def victory():

    clock.tick(30)
    def restart():
        text = font.render("RESTART",True,(0,0,0))
        screen.blit(text,(140,380))

    def quit_text():
        text = font.render("QUIT",True,(0,0,0))
        screen.blit(text,(370,380))
    
    r = 255 ; g = 255 ; b = 255
    r1 = 255 ; g1 = 255 ; b1 = 255



    run = True
    while run :
        for e in py.event.get():
            if e.type == py.QUIT:
                run = False
                return False

            if e.type == py.KEYDOWN:
                if e.key == py.K_RETURN:
                    r = 255 ; g = 225 ; b = 2

                if e.key == py.K_ESCAPE:
                    r1 = 255 ; g1 = 255 ; b1 =2
                
            if e.type == py.KEYUP:
                if e.key == py.K_RETURN:
                    r = 255 ; g = 255 ; b = 255
                    run = False
                    return True
                
                if e.key == py.K_ESCAPE:
                    r1 = 255 ; g1 = 255 ; b1 = 255
                    run = False
                    return False

    #screen color through out
        screen.fill((147,217,255))
        screen.blit(winner,(85,190))
        py.draw.rect(screen,(0,0,0),(98,368,196,55))
        py.draw.rect(screen,(0,0,0),(298,368,196,55))
        py.draw.rect(screen,(r,g,b),(100,370,190,49))
        py.draw.rect(screen,(r1,g1,b1),(300,370,190,49))
        restart() ; quit_text()
        py.display.update()


while True:
    if menu():
        if game():
            if victory():
                continue
            else:
                break
        else:
            continue
    else:
        break