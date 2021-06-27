# Faça um  programa em python que abra e reproduza o áudio de um arquivos MP3
import pygame


pygame.mixer.init()
pygame.mixer.music.load('somteste.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
