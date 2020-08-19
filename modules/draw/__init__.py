try:
    from modules.constants import *

    from modules.ships import *

    from modules.waves import *

except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')

def draw(self):
        """
        apaga e desenha os elementos na tela (update) /
        updates the elements onscreen
        """
        self.canvas.delete(ALL)
        animate_bg(self)
        shoot(self)

        def_wave(self, self.wave, self.ENEMY_HEALTH, self.BOSS_HEALTH, self.PLAYER_HEALTH,
                 self.BULLET_SPEED, self.GAMEMODE)
        enemy_shoot(self, self.wave, self.ENEMY_HEALTH, self.BOSS_HEALTH, self.PLAYER_HEALTH,
                    self.BULLET_SPEED, self.GAMEMODE)
                    
        health_bar(self)
        draw_player(self)

def animate_bg(self):
    """
    anima o fundo do jogo /
    animates the game background
    """
    self.canvas.create_image((CANVAS_W / 2, CANVAS_H / 2), image=self.spritesheet_bg[self.current_bg])
    if self.current_bg == self.bg_limit:
        self.current_bg = 0
    else:
        self.current_bg += 1

def health_bar(self):
    """
    desenha a barra de vida do player /
    draws the player's health bar
    """

    self.canvas.create_image((250, 570), image=self.current_health)
            
def switch_hit(self):
    """
    trocar para player não está mais sendo acertado /
    change to player's not getting hit
    """
    self.p_hit = False

def enemy_hit(self, enemy):
    """
    troca a imagem do inimigo para sua versão normal depois de levar dano /
    changes the enemy's image to normal after being hit
    """
    if isinstance(enemy, Enemy1):
        enemy.image = Enemy1().image   

    elif isinstance(enemy, Enemy2):
        enemy.image = Enemy2().image   
    
    elif isinstance(enemy, Boss):
        enemy.image = Boss().image

def draw_player(self):
    """
    usa o estado da imagem do player para desenhar se está reto ou para os lados /
    uses the state of player's image to draw it centered or to the sides
    """

    # se o player não está levando dano
    # if player's not getting hit
    if not self.p_hit:
        if self.p_ship == 'center':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image[0])
        elif self.p_ship == 'left':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image[-1])
        elif self.p_ship == 'right':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image[1])

    # se o player está levando dano
    # if player's getting hit
    else:
        if self.p_ship == 'center':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image_hit[0])
        elif self.p_ship == 'left':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image_hit[-1])
        elif self.p_ship == 'right':
            self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                        image=self.player.image_hit[1])

def shoot(self):
    """
    função para o player atirar /
    function to player's shooting
    """

    if self.pressing['space'] or self.pressing['Return']:
        # checa se o tiro foi pressionado sem estar atirando antes
        # check if the shot button is pressed while not shooting
        if not self.shooting:                
            self.sound_player_shot.play()

            # define a posição do tiro na frente da nave
            # defines the shot position in front of the ship
            self.shot_x = self.player.x - 6
            self.shot_y = self.player.y - 25
            self.shooting = True
            

    # anima o tiro apenas se estiver atirando
    # animates the shot only when player's shooting
    if self.shooting:            
        self.player_shot = self.canvas.create_oval(self.shot_x, self.shot_y, self.shot_x + self.shot_radius,
                                                    self.shot_y + self.shot_radius, fill='gold', outline='yellow')
        self.canvas.move(self.player_shot, 0, - self.shot_v)
        self.shot_y -= self.shot_v

        # remove o tiro quando sai da tela
        # deletes the shot when it's offscreen
        if self.shot_y < 11:
            self.canvas.delete(self.player_shot)
            self.shooting = False
