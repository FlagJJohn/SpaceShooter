try:
    from tkinter import *
    from modules.constants import *
except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')

# principalmente carrega as imagens dos respectivos tipos de naves do jogo
# mainly load the image of each type of ship in the game

class Boss(object):
    def __init__(self):
        self.image = PhotoImage(file='images/sprites/Boss.gif')
        self.image_hit = PhotoImage(file='images/sprites/Boss_hit.gif')


class Enemy1(object):
    # inimigo menor
    # smaller enemy
    def __init__(self):
        self.image = PhotoImage(file='images/sprites/Enemy_1.gif')
        self.image_hit = PhotoImage(file='images/sprites/Enemy_1_hit.gif')

class Enemy2(object):
    # inimigo maior
    # bigger enemy
    def __init__(self):
        self.image = PhotoImage(file='images/sprites/Enemy_2.gif')
        self.image_hit = PhotoImage(file='images/sprites/Enemy_2_hit.gif')


class Player(object):
    def __init__(self):
        self.image = [PhotoImage(file=f'images/sprites/Player/player_{i}.gif') for i in range(0, 3)]
        self.image_hit = [PhotoImage(file=f'images/sprites/Player_Hit/player_hit_{i}.gif') for i in range(0, 3)]
        
        self.x = CANVAS_W//2
        self.y = 525
        self.vx = 3
        self.vy = 3


if __name__ == '__main__':
    print('Não é possível executar esse arquivo. Execute "SpaceShooter.py"')
