import pygame, sys, os, csv
from pygame.locals import * 


def getX(x):
	return int(10 * float(x)) + 11 + 60
   #return int( 751 * (x + 46.9444) / ( -46.5453 + 46.9444 ))
   
def getY(y):
	return 434 - int(10 * float(y)) + 11 - 400
   #return int( 623 * (y + 23.3383) / ( -23.642 + 23.3383 ))

pygame.init() 
 
window = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('CNC Simulator') 
screen = pygame.display.get_surface() 

fundo_file_name = os.path.join("data","fundo.png")
radar_surface = pygame.image.load(fundo_file_name)

clock = pygame.time.Clock()

fresa = 5
broca = 9
velocidade = 1

first = 1
contador = 0
f = open("furos.txt")
x = getX(0)
y = getY(0)
cor = 'Black'
fresaAtual = fresa
brocaAtual = broca
lineCount = 0
try:
	for line in f:
		#print line.replace("\n",'').split(' ')
		codes = line.replace("\n",'').split(' ')
		lineCount = lineCount + 1
		for code in codes:
			#print code
			if len(code) > 0:
				if code[0] == 'X':
					x = getX(code[1:])
					
				if code[0] == 'Y':
					y = getY(code[1:])
					
				if code[0] == 'Z':
					z = float(code[1:])
					if(z > 0):
						cor = 'Green'
						fresaAtual = 1
					else:
						cor = 'Blue'
						fresaAtual = fresa
						pygame.draw.circle(radar_surface, pygame.Color('Red'), [x,y], brocaAtual, 1)
					
		if first == 1:
			first = 0
			x2 = x
			y2 = y
		else:
			x1 = x2
			y1 = y2
			x2 = x
			y2 = y
			pygame.draw.line(radar_surface, pygame.Color(cor), [x1,y1], [x2,y2], fresaAtual)
		
		contador = contador + 1
		if contador % velocidade == 0:
			if contador == velocidade:
				contador = 0
				screen.blit(radar_surface, (0,0)) 
				pygame.display.flip()
				print lineCount

finally:
	f.close()

screen.blit(radar_surface, (0,0)) 
pygame.display.flip()


def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
#      else: 
#         print event
        
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

while True: 
   input(pygame.event.get())
   clock.tick(60)