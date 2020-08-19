try:
    from tkinter import *

    from modules.constants import *

    from modules.ships import *

    from modules.movement import *

    from modules.waves import *

    from modules.checks import *

    from modules.draw import draw

    import pygame

except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')




class Game(object):
    def __init__(self, ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAME_CONTROL, GAMEMODE, ALIVE):
        self.ENEMY_HEALTH = ENEMY_HEALTH
        self.BOSS_HEALTH = BOSS_HEALTH
        self.PLAYER_HEALTH = PLAYER_HEALTH
        self.BULLET_SPEED = BULLET_SPEED
        self.GAME_CONTROL = GAME_CONTROL
        self.GAMEMODE = GAMEMODE

        # iniciamos a janela
        # init window
        self.root = Tk()
        self.root.geometry(f'{CANVAS_W}x{CANVAS_H}'
                           f'+{screensize[0] // 2 - CANVAS_W // 2}+{screensize[1] // 2 - CANVAS_H // 2}')
        self.root.title('Space Shooter')
        self.root.resizable(False, False)

        # imagens background
        # background images
        self.bg = []

        # criamos o canvas
        # create canvas
        self.canvas = Canvas(self.root, width=CANVAS_W, height=CANVAS_H)
        self.canvas.pack()

        # criamos sprite do background do jogo
        # create the bg sprite
        self.spritesheet_bg = [PhotoImage(file=f'images/sprites/BG/{i}.gif') for i in range(1, 114)]
        self.current_bg = 0
        self.bg_limit = 112

        # definimos sprite da vida do player
        # player's health sprite
        if self.GAMEMODE == 1:
            self.health_bar_n = [PhotoImage(file=f'images/sprites/Heart_Normal/bar_{i}.gif') for i in range(0, 11)]

        elif self.GAMEMODE == 2:
            self.health_bar_h = [PhotoImage(file=f'images/sprites/Heart_Hard/bar_{i}.gif') for i in range(0, 6)]

        elif self.GAMEMODE == 3:
            self.health_bar_hc = [PhotoImage(file=f'images/sprites/Heart_Hardcore/bar_{i}.gif') for i in range(0, 4)]

        # criamos sprite do player
        # create player's sprite
        self.player = Player()
        self.player.health = self.PLAYER_HEALTH
        self.p_ship = 'center'

        # definimos a velocidade, posição e raio dos tiros do player
        # velocity, position and radius of player's shot
        self.shot_radius = 11
        self.shot_x = 0
        self.shot_y = 0
        self.shot_v = 15

        # definimos a velocidade, posição e raio dos tiros do inimigo
        # velocity, position and radius of enemy's shot
        self.enemy_shot_radius = 11
        self.enemy_shot_x = 0
        self.enemy_shot_y = 0
        self.enemy_shot_vy = self.BULLET_SPEED
        self.enemy_shot_vx = []

        # definimos a lista dos inimigos (muda a cada onda)
        # list of enemies (changes each wave)
        self.enemies = []

        # definimos a lista de tiros dos inimigos (muda a cada onda)
        # list of enemy shots (changes each wave)
        self.enemy_shots = []

        # bool para saber se estamos atirando
        # bool if player's shooting
        self.shooting = False

        # inimigo atirando
        # bool if enemy's shooting
        self.enemy_shooting = []

        # onde de inimigos definida
        # if the wave if defined
        self.wave_defined = False

        # definimos a variável para as ondas
        # wave number
        self.wave = 0

        # bool pra saber se o player foi acertado
        # bool if player was shot
        self.p_hit = False
        
        # player vivo
        # bool player alive
        self.player_alive = ALIVE

        # criamos um botão de restart quando houver gameover
        # create a restart button when gameover happens
        self.button_gameover = Button(self.root, text='RESTART?', font=('Courier', 15, 'bold'), command=self.restart,
                                      bg='SlateBlue2', activebackground='SlateBlue2')

        # quais teclas estamos apertando
        # which keys we're pressing
        self.pressing = {"Up": False, "Down": False, "Left": False, "Right": False, "space": False,
                         "w": False, "s": False, "a": False, "d": False, "Return": False,
                         "W": False, "S": False, "A": False, "D": False}

        # setamos os comandos das teclas
        # set the key bindings
        if self.GAME_CONTROL == 1:
            for char in ["w", "W", "a", "A", "s", "S", "d", "D", "Return"]:
                self.canvas.bind(f"<KeyPress-{char}>", lambda event: pressed(self, event))
                self.canvas.bind(f"<KeyRelease-{char}>", lambda event: released(self, event))
        else:
            for char in ["Up", "Left", "Down", "Right", "space"]:
                self.canvas.bind(f"<KeyPress-{char}>", lambda event: pressed(self, event))
                self.canvas.bind(f"<KeyRelease-{char}>", lambda event: released(self, event))

        # adicionamos sons do jogo
        # add game sounds
        pygame.mixer.init()

        self.sound_player_shot = pygame.mixer.Sound('sounds\\shot.wav')
        self.sound_gameover = pygame.mixer.Sound('sounds\\gameover.wav')
        self.sound_regen = pygame.mixer.Sound('sounds\\regen.wav')

        pygame.mixer.music.load('sounds\\soundtrack.wav')
        pygame.mixer.music.play(-1)

        self.game()
        self.root.mainloop()

    def game(self):
        """
        loop principal do jogo /
        main game loop
        """

        # se o player está vivo, o jogo roda
        # if player alive, the game runs
        if self.player_alive:
            self.canvas.focus_force()

            player_move(self)

            check_collision(self)
            check_health(self)
            check_enemy_health(self)

            change_wave(self)

            draw(self)

            self.root.after(10, self.game)
        
        # se não, tela de restart
        # else, restart screen
        else:
            pygame.mixer.music.stop()
            self.sound_gameover.play()

            self.canvas.create_text((CANVAS_W//2, CANVAS_H//2+5), text='GAME OVER', font=('Courier', 41, 'bold'),
                                    fill='black')
            self.canvas.create_text((CANVAS_W//2, CANVAS_H//2), text='GAME OVER', font=('Courier', 40, 'bold'),
                                    fill='red')
            
            self.canvas.create_window(CANVAS_W//2, CANVAS_H//2+70, window=self.button_gameover)

    def restart(self):
        """
        recomeça o jogo com as configurações já definidas /
        restart the game with the defined configs
        """
        self.root.destroy()

        if self.GAMEMODE == 1:
            self.ENEMY_HEALTH[0] = 20
            self.ENEMY_HEALTH[1] = 60
            self.BOSS_HEALTH = 200
            self.PLAYER_HEALTH = 100
            self.BULLET_SPEED = 5

        elif self.GAMEMODE == 2:
            self.ENEMY_HEALTH[0] = 50
            self.ENEMY_HEALTH[1] = 150
            self.BOSS_HEALTH = 400
            self.PLAYER_HEALTH = 50
            self.BULLET_SPEED = 6

        elif self.GAMEMODE == 3:
            self.ENEMY_HEALTH[0] = 50
            self.ENEMY_HEALTH[1] = 150
            self.BOSS_HEALTH = 400
            self.PLAYER_HEALTH = 30
            self.BULLET_SPEED = 7

        Game(self.ENEMY_HEALTH, self.BOSS_HEALTH, self.PLAYER_HEALTH, self.BULLET_SPEED, self.GAME_CONTROL, self.GAMEMODE, True)


if __name__ == '__main__':
    print('Não é possível executar esse arquivo. Execute "SpaceShooter.py"')
