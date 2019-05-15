import numpy as np
import pygame as pg

#start

f = open("map.lif", "r")
database = f.readlines()
f.close()

pg.init()
pg.display.set_caption("Game of Life")
xmax = 800
ymax = 800
nx = 50
ny = 50
sx = xmax/nx
sy = ymax/ny
res = (xmax,ymax)
scr = pg.display.set_mode(res)
thickness = 1

#colors
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
purple = (128,0,255)
red = (255,0,0)

scr.fill(black)    
t = 0
t = pg.time.get_ticks()*0.001

world = np.zeros((nx,ny))
#print(world)
##world[1:4,1:4]= np.array([[0,1,0],
##                          [0,0,1],
##                          [1,1,1]])
##world[5:8,5:8]= np.array([[0,1,0],
##                          [0,0,1],
##                          [1,1,1]])
##world[9:12,9:12]=np.array([[0,1,0],
##                          [0,0,1],
##                          [1,1,1]])
##world[1:4,9:12]=np.array([[0,1,0],
##                          [0,0,1],
##                          [1,1,1]])
##world[5:8,9:12]=np.array([[0,1,0],
##                          [0,0,1],
##                          [1,1,1]])


for line in database: 
         column = line.split()
         data = True
         if column[0] == "#":
             data = False
         if data:
             xpos = int(column[0])
             ypos = int(column[1])
             world[ypos+25, xpos+25] = 1

#print(world)
newworld = np.copy(world)


def cond(x, y):
    sumcells = np.sum(world[x - 1:x + 2, y - 1:y + 2]) - world[x, y]
    if world[x, y] == 1:
        pg.draw.rect(scr, red, (0 + x * sx, 0 + y * sy, sx, sy))
        if sumcells < 2 or sumcells > 3:
            pg.draw.rect(scr, black, (0 + x * sx, 0 + y * sy, sx, sy))
            #pg.draw.rect(scr, green, (0 + x * sx, 0 + y * sy, sx, sy), thickness)
            newworld[x, y] = 0
    elif world[x, y] == 0:
        pg.draw.rect(scr, black, (0 + x * sx, 0 + y * sy, sx, sy))
        #pg.draw.rect(scr, green, (0 + x * sx, 0 + y * sy, sx, sy), thickness)
        if sumcells == 3:
            newworld[x, y] = 1
            pg.draw.rect(scr, red, (0 + x * sx, 0 + y * sy, sx, sy))

def gen():
    global world
    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            cond(i, j)
    for k in range(nx):
        pg.draw.rect(scr, purple, (0 + k*sx, 0, sx, sy))
        pg.draw.rect(scr, purple, (0 + k*sx, (nx-1) * sx, sx, sy))
        world[k,0]=0
    for p in range(ny):
        pg.draw.rect(scr, purple, (0, 0 + p * sy, sx, sy))
        pg.draw.rect(scr, purple, ((ny-1) * sx, 0 + p * sy, sx, sy))
        world[0,p]=0
                     
    world = np.copy(newworld)


life = True
while life and t<100 :
    pg.event.pump()
    t0 = t
    t = 0.001*pg.time.get_ticks()
    dt = t - t0
    gen()
    #flip screen
    pg.display.flip()

    for event in pg.event.get():
        if event.type==pg.QUIT:
            life = False

#escape
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        life=False


#kill window 
pg.quit()
print("ready.")

