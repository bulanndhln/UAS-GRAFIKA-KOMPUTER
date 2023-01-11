#Nama : Bulan Fitri Dahlan
#NIM : 09021282025071
#Kelas : 4 Reguler B
# PROJECT UAS GRAFKOM


import pygame
import random
import os

from OpenGL.GL import *
from OpenGL.GLU import *


from pygame.locals import *
from constants import *
from MeshRendere import LMesh
os.environ["SDL_VIDEO_CENTERED"]='1'


def main():
    pygame.init()
    display = (500,500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45,(display[0]/display[1]),0,50.0)
   
    glTranslatef(-5,5,-45)
    glRotatef(-90,0,-90,-90)
    

main()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    glRotatef(4,0,-10,90)
        
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    LMesh()

    pygame.display.flip()
    pygame.time.wait(75)
pygame.quit()
quit()
    
        