try:
    from modules.ships import *

    from modules.draw import *

except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')

def check_health(self):
    """
    checa a vida do player e atribui uma imagem correspondente a barra de vida /
    check the player's health and defines its health bar image
    """

    if self.GAMEMODE == 1:
        if self.player.health == 100:
            self.current_health = self.health_bar_n[0]

        elif self.player.health == 90:
            self.current_health = self.health_bar_n[1]

        elif self.player.health == 80:
            self.current_health = self.health_bar_n[2]

        elif self.player.health == 70:
            self.current_health = self.health_bar_n[3]

        elif self.player.health == 60:
            self.current_health = self.health_bar_n[4]

        elif self.player.health == 50:
            self.current_health = self.health_bar_n[5]

        elif self.player.health == 40:
            self.current_health = self.health_bar_n[6]

        elif self.player.health == 30:
            self.current_health = self.health_bar_n[7]

        elif self.player.health == 20:
            self.current_health = self.health_bar_n[8]

        elif self.player.health == 10:
            self.current_health = self.health_bar_n[9]

        else:
            self.current_health = self.health_bar_n[10]
            self.player_alive = False

    elif self.GAMEMODE == 2:
        if self.player.health == 50:
            self.current_health = self.health_bar_h[0]

        elif self.player.health == 40:
            self.current_health = self.health_bar_h[1]

        elif self.player.health == 30:
            self.current_health = self.health_bar_h[2]

        elif self.player.health == 20:
            self.current_health = self.health_bar_h[3]

        elif self.player.health == 10:
            self.current_health = self.health_bar_h[4]

        else:
            self.current_health = self.health_bar_h[5]
            self.player_alive = False

    elif self.GAMEMODE == 3:
        if self.player.health == 30:
            self.current_health = self.health_bar_hc[0]
        
        elif self.player.health == 20:
            self.current_health = self.health_bar_hc[1]
        
        elif self.player.health == 10:
            self.current_health = self.health_bar_hc[2]

        else:
            self.current_health = self.health_bar_hc[3]
            self.player_alive = False

def check_enemy_health(self):  
    """
    checa a vida do inimigo para saber se está morto /
    checks the enemy's life to know if it's dead
    """      
    for i in range(0, len(self.enemies)):
        if self.enemies[i].health < 1:
            self.enemies[i].alive = False
            self.enemy_shooting[i] = False
            self.enemy_shots[i] = ''

def check_collision(self):
    """
    checa as colisões dos tiros /
    check the shot collisions
    """

    # tiro do player
    # player's shot
    if self.shooting:

        # checa cada um dos inimigos
        # checks each enemy
        for i in range(0, len(self.enemies)):
            p_box = self.canvas.bbox(self.player_shot)
            if self.enemies[i].alive:
                e_box = self.canvas.bbox(self.enemies[i].canvas)

                if (e_box[0] < p_box[0] < e_box[2] or e_box[0] < p_box[2] < e_box[2]) and \
                (e_box[1] < p_box[1] < e_box[3] or e_box[1] < p_box[3] < e_box[3]):

                    # dá dano ao inimigo
                    # damages the enemy
                    self.enemies[i].health -= 10
                    

                    # muda a imagem do inimigo para vermelho
                    # change the enemy's image to red
                    if isinstance(self.enemies[i], Enemy1):
                        self.enemies[i].image = Enemy1().image_hit   

                    elif isinstance(self.enemies[i], Enemy2):
                        self.enemies[i].image = Enemy2().image_hit   
    
                    elif isinstance(self.enemies[i], Boss):
                        self.enemies[i].image = Boss().image_hit

                    # volta a imagem normal
                    # returns to the original image
                    self.root.after(150, lambda enemy=self.enemies[i]: enemy_hit(self, enemy))

                    self.shooting = False
    
    # tiro de cada inimigo
    # each enemy's shot
    for i in range(0, len(self.enemy_shots)):
        if self.enemy_shooting[i]:
            if self.enemy_shots[i] != '':
                p_box = self.canvas.bbox(self.player.ship)
                e_box = self.canvas.bbox(self.enemy_shots[i])

                if (p_box[0] < e_box[0] < p_box[2] or p_box[0] < e_box[2] < p_box[2]) and \
                    (p_box[1] < e_box[1] < p_box[3] or p_box[1] < e_box[3] < p_box[3]):

                    # dá dano ao player
                    # damages the player
                    self.player.health -= 10

                    # troca a imagem do player para vermelho
                    # changes the player's image to red
                    self.p_hit = True

                    # imagem volta ao normal
                    # returns to the original image
                    self.root.after(150, lambda: switch_hit(self))

                    self.enemy_shooting[i] = False


if __name__ == "__main__":
    print('Não é possível executar esse arquivo. Execute "SpaceShooter.py"')