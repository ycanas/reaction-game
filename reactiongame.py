"""

Juego de tiempo de reacción (2 jugadores)
Created by: @ycanas
09/10/2023

Entradas:

    - GP12: Boton Player2
    - GP13: Boton Player1
    - GP15: Boton Inicio

Salidas:
    
    - GP18: Led Player1
    - GP19: Led Player2 
    - GP16: Led Inicio

"""


from machine import Pin
from utime   import sleep_ms
from random  import choice


def init():
    GAME.value(False)
    LPLAYER1.value(False)
    LPLAYER2.value(False)
    

def interrupt(pin):
    global pressed
    
    if not pressed:
        if pin is PLAYER1:
            pressed = True
            LPLAYER1.value(True)
            
        if pin is PLAYER2:
            pressed = True
            LPLAYER2.value(True)


# Declaración de las variables del juego
pressed = True
times   = [1500, 3000, 3800, 1800, 7000, 4200, 3100, 2700, 2400, 6500, 6000, 6100, 1900, 1100, 2100, 5300, 5900]
time    = 0

# Declaración de las entradas (Pulsadores)
PLAYER1 = Pin(13, Pin.IN, Pin.PULL_UP)
PLAYER2 = Pin(12, Pin.IN, Pin.PULL_UP)
START   = Pin(15, Pin.IN, Pin.PULL_UP)

# Declaración de las salidas (Leds)
LPLAYER1 = Pin(18, Pin.OUT)
LPLAYER2 = Pin(19, Pin.OUT)
GAME     = Pin(16, Pin.OUT)

# Declaración de las interrupciones
PLAYER1.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)
PLAYER2.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)

init()
sleep_ms(100)

while True:
    if not START.value():
        init()
        
        time = choice(times)
        sleep_ms(time)
        GAME.value(True)
        pressed = False
            