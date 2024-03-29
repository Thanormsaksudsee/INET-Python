
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600


score = 0
game_over = False


fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200


def draw():
    screen.fill('white')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white', topleft=(10, 10))
    if game_over:
        screen.fill('red')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10, 10), fontsize=50)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def update():
    global score
    if fox.x == 800:
        fox.x = fox.y = 0
    elif fox.x == 0:
        fox.x = fox.y = 800
    if fox.y == 600:
        fox.y = fox.y = 0
    elif fox.y == 0:
        fox.y = fox.y = 600
    if keyboard.left:
        fox.x = fox.x - 20
    elif keyboard.right:
        fox.x = fox.x + 20
    elif keyboard.up:
        fox.y = fox.y - 20
    elif keyboard.down:
        fox.y = fox.y + 20
    

    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1


def time_up():
    global game_over
    game_over = True


clock.schedule(time_up, 10.0)
place_coin()
pgzrun.go()
