import pygame, terrain
from pygame.locals import *
from sys import exit

def main():

	pygame.init()

	pygame.display.set_caption('Before The After The Fall Of The Before')
	pygame.display.set_icon(pygame.image.load("32x32.png"))
	screen = pygame.display.set_mode((920,740),pygame.HWSURFACE)
	FramePerSec = pygame.time.Clock()
	FPS = 60

	all_sprites = pygame.sprite.Group()
	person = terrain.Terrain()
	all_sprites.add(person)
	pygame.display.set_icon(pygame.image.load("32x32.png"))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		screen.fill((0,0,0))

		for entity in all_sprites:
			screen.blit(entity.surf, entity.rect)

		pygame.display.update()
		FramePerSec.tick(FPS)



if __name__ == "__main__":
	main()