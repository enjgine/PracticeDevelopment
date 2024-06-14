import pygame, terrain
from pygame.locals import *
from sys import exit

def main():

	pygame.init()

	pygame.display.set_caption('Before The After The Fall Of The Before')
	pygame.display.set_icon(pygame.image.load("32x32.png"))
	screen = pygame.display.set_mode((32*40,32*30),pygame.HWSURFACE)
	clock = pygame.time.Clock()
	FPS = 10

	terrainblock = terrain.Terrain()
	all_sprites = []
	all_sprites.append(terrainblock)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		screen.fill((0,0,0))

		for entity in all_sprites:
			screen.blit(entity.surf, entity.rect)

		pygame.display.update()
		clock.tick(FPS)



if __name__ == "__main__":
	main()