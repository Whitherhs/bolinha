import pygame

pygame.mixer.init()

def som_menu():
    pygame.mixer.music.load('./mp3/ping_pong_8bit_beeep.mp3')
    pygame.mixer.music.play()

def som_colisao():
    pygame.mixer.music.load('./mp3/ping_pong_8bit_beeep.mp3')
    pygame.mixer.music.play()