import pygame

pygame.mixer.init()
pygame.mixer.music.load('../01 All the Rage Back Home.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

