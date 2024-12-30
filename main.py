
import sys
import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	# Group for pygame
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_HEIGHT / 2 , SCREEN_WIDTH / 2, shots)

	Shot.containers = (updatable, drawable)
	
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for object in updatable:
			object.update(dt)

		screen.fill('black')
		
		for object in drawable:
			object.draw(screen)
		
		pygame.display.update()

	
		for object in asteroids:
			if object.check_collision(player): 
				print("Game Over!")
				sys.exit()
		
		for object in asteroids:
			for bullet in shots:
				if bullet.check_collision(object):
					print("Shot hit!")
					bullet.kill()
					object.split()


		# Limit to 60FPS
		dt = clock.tick(60) / 1000
	

if __name__ == "__main__":
	main()
