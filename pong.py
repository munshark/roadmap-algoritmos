import pygame
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong en Python")
RELOJ = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Paddles y Pelota
PADDLE_ANCHO, PADDLE_ALTO = 10, 100
pelota = pygame.Rect(ANCHO//2 - 7, ALTO//2 - 7, 15, 15)
jugador1 = pygame.Rect(10, ALTO//2 - PADDLE_ALTO//2, PADDLE_ANCHO, PADDLE_ALTO)
jugador2 = pygame.Rect(ANCHO - 20, ALTO//2 - PADDLE_ALTO//2, PADDLE_ANCHO, PADDLE_ALTO)

vel_pelota_x, vel_pelota_y = 7, 7
vel_paddle = 7

def dibujar():
    VENTANA.fill(NEGRO)
    pygame.draw.rect(VENTANA, BLANCO, jugador1)
    pygame.draw.rect(VENTANA, BLANCO, jugador2)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)
    pygame.draw.aaline(VENTANA, BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO))
    pygame.display.flip()

def mover_pelota():
    global vel_pelota_x, vel_pelota_y

    pelota.x += vel_pelota_x
    pelota.y += vel_pelota_y

    # Rebote vertical
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        vel_pelota_y *= -1

    # Rebote en paletas
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        vel_pelota_x *= -1

    # Reset si sale de pantalla
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.center = (ANCHO//2, ALTO//2)
        vel_pelota_x *= -1

def mover_jugadores(teclas):
    if teclas[pygame.K_w] and jugador1.top > 0:
        jugador1.y -= vel_paddle
    if teclas[pygame.K_s] and jugador1.bottom < ALTO:
        jugador1.y += vel_paddle
    if teclas[pygame.K_UP] and jugador2.top > 0:
        jugador2.y -= vel_paddle
    if teclas[pygame.K_DOWN] and jugador2.bottom < ALTO:
        jugador2.y += vel_paddle

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    mover_jugadores(teclas)
    mover_pelota()
    dibujar()
    RELOJ.tick(60)
