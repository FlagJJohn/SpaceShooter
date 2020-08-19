try:
    from modules.ships import *

except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')



def enemy_shoot(self, wave, enemy_health, boss_health, player_health, bullet_speed, gamemode):
    """
    função para o inimigo atirar /
    makes the enemies shoot
    """
    if wave == 1:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 2:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False
        
    if wave == 2:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False 

    if wave == 3:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 4:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 4:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        self.enemy_shot_vx.append(0)

        while len(self.enemy_shot_vx) > 1:
            self.enemy_shot_vx.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True
                    if i == 0:
                        from random import randint
                        self.enemy_shot_vx[i] = randint(-1, 1)


        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                if i == 0:
                    self.enemies[i].shot_y += self.enemy_shot_vy + 1
                    self.enemies[i].shot_x += self.enemy_shot_vx[i]
                elif i == 1:
                    self.enemies[i].shot_y += self.enemy_shot_vy
                elif i == 2:
                    self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 5:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 2:
            self.enemy_shooting.pop()

        self.enemy_shot_vx.append(0)
        self.enemy_shot_vx.append(0)

        while len(self.enemy_shot_vx) > 2:
            self.enemy_shot_vx.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True
                    from random import randint
                    self.enemy_shot_vx[i] = randint(-1, 1)

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                
                self.enemies[i].shot_y += self.enemy_shot_vy + 3
                self.enemies[i].shot_x += self.enemy_shot_vx[i]

                if self.enemies[i].shot_y > 600 or self.enemies[i].shot_x > 300 \
                                                or self.enemies[i].shot_x < 0:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 6:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 4:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 7:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        self.enemy_shot_vx.append(0)

        while len(self.enemy_shot_vx) > 1:
            self.enemy_shot_vx.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True
                    if i == 0:
                        from random import randint
                        self.enemy_shot_vx[i] = randint(-1, 1)


        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                if i == 0:
                    self.enemies[i].shot_y += self.enemy_shot_vy + 1
                    self.enemies[i].shot_x += self.enemy_shot_vx[i]
                elif i == 1:
                    self.enemies[i].shot_y += self.enemy_shot_vy
                elif i == 2:
                    self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 8:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 9:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

    if wave == 10:
        # checa se está atirando
        # checks if the enemy's shooting
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)
        self.enemy_shooting.append(False)

        while len(self.enemy_shooting) > 3:
            self.enemy_shooting.pop()

        for i in range(0, len(self.enemies)):
            if not self.enemy_shooting[i] and self.enemies[i].alive:
                if self.enemies[i].y > 0:
                    self.enemies[i].shot_x = self.enemies[i].x - 5
                    self.enemies[i].shot_y = self.enemies[i].y + 25
                    self.enemy_shooting[i] = True

        # cria a lista de tiros dos inimigos para animá-los, igual ao numero de enemies[]
        # creates a list of enemy shots to animate them, same length of enemies[]
        self.enemy_shots = ['', '', '']

        # anima o tiro
        # animates the shot
        for i in range(0, len(self.enemies)):
            if self.enemy_shooting[i]:     
                self.enemy_shots[i] = self.canvas.create_oval(self.enemies[i].shot_x, self.enemies[i].shot_y,
                                                            self.enemies[i].shot_x + self.shot_radius,
                                                            self.enemies[i].shot_y + self.enemy_shot_radius,
                                                            fill='red', outline='gold')
                self.enemies[i].shot_y += self.enemy_shot_vy

                if self.enemies[i].shot_y > 600:
                    self.canvas.delete(self.enemy_shots[i])
                    self.enemy_shooting[i] = False

def def_wave(self, wave, enemy_health, boss_health, player_health, bullet_speed, gamemode):
    """ 
    configura as ondas de inimigos /
    configures each wave
    """
    
    if wave == 1:
        if not self.wave_defined:
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy1()
            self.enemy2 = Enemy1()

            self.enemies.clear()

            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)

            self.enemies[0].health = enemy_health[0]
            self.enemies[0].x = 75
            self.enemies[0].y = -50
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 225
            self.enemies[1].y = -50
            self.enemies[1].alive = True
            
            self.move1 = 0
            self.move2 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 100 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 100:
                        self.move1 = 1

                if self.enemies[0].x > 30 and self.move1 == 1:
                    self.enemies[0].x -= 1
                    if self.enemies[0].x == 30:
                        self.move1 = 2

                if self.enemies[0].x < 120 and self.move1 == 2:
                    self.enemies[0].x += 1
                    if self.enemies[0].x == 120:
                        self.move1 = 1
            
            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 100 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 100:
                        self.move2 = 1

                if self.enemies[1].x > 180 and self.move2 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 180:
                        self.move2 = 2

                if self.enemies[1].x < 270 and self.move2 == 2:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 270:
                        self.move2 = 1

    elif wave == 2:
        if not self.wave_defined:
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy1()
            self.enemy2 = Enemy1()
            self.enemy3 = Enemy1()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)
            self.enemies.append(self.enemy3)

            self.enemies[0].health = enemy_health[0]
            self.enemies[0].x = 50
            self.enemies[0].y = -100
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 150
            self.enemies[1].y = -50
            self.enemies[1].alive = True

            self.enemies[2].health = enemy_health[0]
            self.enemies[2].x = 250
            self.enemies[2].y = -100
            self.enemies[2].alive = True
            
            self.move1 = 0
            self.move2 = 0
            self.move3 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 100 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 100:
                        self.move1 = 1

                if self.enemies[0].x > 20 and self.move1 == 1:
                    self.enemies[0].x -= 1
                    if self.enemies[0].x == 20:
                        self.move1 = 2

                if self.enemies[0].x < 120 and self.move1 == 2:
                    self.enemies[0].x += 1
                    if self.enemies[0].x == 120:
                        self.move1 = 1
            
            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 150 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 150:
                        self.move2 = 1

                if self.enemies[1].x > 120 and self.move2 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 120:
                        self.move2 = 2

                if self.enemies[1].x < 180 and self.move2 == 2:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 180:
                        self.move2 = 1

            # anima o inimigo 3
            # animates the enemy 3
            if self.enemies[2].alive:    
                self.enemies[2].canvas = self.canvas.create_image((self.enemies[2].x, self.enemies[2].y),
                                                                    image=self.enemies[2].image)

                if self.enemies[2].y < 100 and self.move3 == 0:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 100:
                        self.move3 = 1

                if self.enemies[2].x < 280 and self.move3 == 1:
                    self.enemies[2].x += 1
                    if self.enemies[2].x == 280:
                        self.move3 = 2

                if self.enemies[2].x > 180 and self.move3 == 2:
                    self.enemies[2].x -= 1
                    if self.enemies[2].x == 180:
                        self.move3 = 1

    elif wave == 3:
        if not self.wave_defined:
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy1()
            self.enemy2 = Enemy1()
            self.enemy3 = Enemy1()
            self.enemy4 = Enemy1()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)
            self.enemies.append(self.enemy3)
            self.enemies.append(self.enemy4)

            self.enemies[0].health = enemy_health[0]
            self.enemies[0].x = 60
            self.enemies[0].y = -120
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 240
            self.enemies[1].y = -120
            self.enemies[1].alive = True

            self.enemies[2].health = enemy_health[0]
            self.enemies[2].x = 60
            self.enemies[2].y = -50
            self.enemies[2].alive = True

            self.enemies[3].health = enemy_health[0]
            self.enemies[3].x = 240
            self.enemies[3].y = -50
            self.enemies[3].alive = True
            
            self.move1 = 0
            self.move2 = 0
            self.move3 = 0
            self.move4 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 70 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 70:
                        self.move1 = 1

                if self.enemies[0].x > 20 and self.move1 == 1:
                    self.enemies[0].x -= 1
                    if self.enemies[0].x == 20:
                        self.move1 = 2

                if self.enemies[0].x < 100 and self.move1 == 2:
                    self.enemies[0].x += 1
                    if self.enemies[0].x == 100:
                        self.move1 = 1

            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 70 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 70:
                        self.move2 = 1

                if self.enemies[1].x > 200 and self.move2 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 200:
                        self.move2 = 2

                if self.enemies[1].x < 280 and self.move2 == 2:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 280:
                        self.move2 = 1

            # anima o inimigo 3
            # animates the enemy 3
            if self.enemies[2].alive:
                self.enemies[2].canvas = self.canvas.create_image((self.enemies[2].x, self.enemies[2].y),
                                                                    image=self.enemies[2].image)
                
                if self.enemies[2].y < 140 and self.move3 == 0:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 140:
                        self.move3 = 2

                if self.enemies[2].x < 100 and self.move3 == 2:
                    self.enemies[2].x += 1
                    if self.enemies[2].x == 100:
                        self.move3 = 1

                if self.enemies[2].x > 20 and self.move3 == 1:
                    self.enemies[2].x -= 1
                    if self.enemies[2].x == 20:
                        self.move3 = 2

            # anima o inimigo 4
            # animates the enemy 4
            if self.enemies[3].alive:    
                self.enemies[3].canvas = self.canvas.create_image((self.enemies[3].x, self.enemies[3].y),
                                                                    image=self.enemies[3].image)

                if self.enemies[3].y < 140 and self.move4 == 0:
                    self.enemies[3].y += 2
                    if self.enemies[3].y == 140:
                        self.move4 = 2

                if self.enemies[3].x < 280 and self.move4 == 2:
                    self.enemies[3].x += 1
                    if self.enemies[3].x == 280:
                        self.move4 = 1

                if self.enemies[3].x > 200 and self.move4 == 1:
                    self.enemies[3].x -= 1
                    if self.enemies[3].x == 200:
                        self.move4 = 2
    
    elif wave == 4:
        if not self.wave_defined:
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy2()
            self.enemy2 = Enemy1()
            self.enemy3 = Enemy1()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)
            self.enemies.append(self.enemy3)

            self.enemies[0].health = enemy_health[1]
            self.enemies[0].x = CANVAS_W//2
            self.enemies[0].y = -120
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 250
            self.enemies[1].y = -50
            self.enemies[1].alive = True

            self.enemies[2].health = enemy_health[0]
            self.enemies[2].x = 50
            self.enemies[2].y = -50
            self.enemies[2].alive = True
            
            self.move1 = 0
            self.move2 = 0
            self.move3 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 70 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 70:
                        self.move1 = 1

            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 140 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 140:
                        self.move2 = 1

                if self.enemies[1].x > 220 and self.move2 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 220:
                        self.move2 = 2

                if self.enemies[1].x < 280 and self.move2 == 2:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 280:
                        self.move2 = 1

            # anima o inimigo 3
            # animates the enemy 3
            if self.enemies[2].alive:
                self.enemies[2].canvas = self.canvas.create_image((self.enemies[2].x, self.enemies[2].y),
                                                                    image=self.enemies[2].image)
                
                if self.enemies[2].y < 140 and self.move3 == 0:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 140:
                        self.move3 = 1

                if self.enemies[2].x < 80 and self.move3 == 1:
                    self.enemies[2].x += 1
                    if self.enemies[2].x == 80:
                        self.move3 = 2

                if self.enemies[2].x > 20 and self.move3 == 2:
                    self.enemies[2].x -= 1
                    if self.enemies[2].x == 20:
                        self.move3 = 1
    
    elif wave == 5:
        if not self.wave_defined:
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy2()
            self.enemy2 = Enemy2()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)

            self.enemies[0].health = enemy_health[1]
            self.enemies[0].x = 80
            self.enemies[0].y = -50
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[1]
            self.enemies[1].x = 220
            self.enemies[1].y = -50
            self.enemies[1].alive = True
            
            self.move1 = 0
            self.move2 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 100 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 100:
                        self.move1 = 1
                
                if self.enemies[0].x > 40 and self.move1 == 1:
                    self.enemies[0].x -= 1
                    if self.enemies[0].x == 40:
                        self.move1 = 2

                if self.enemies[0].x < 120 and self.move1 == 2:
                    self.enemies[0].x += 1
                    if self.enemies[0].x == 120:
                        self.move1 = 1

            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)
                
                if self.enemies[1].y < 100 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 100:
                        self.move2 = 1

                if self.enemies[1].x > 180 and self.move1 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 180:
                        self.move1 = 2

                if self.enemies[1].x < 260 and self.move1 == 2:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 260:
                        self.move1 = 1

    elif wave == 6:
        if not self.wave_defined:
            # recarrega vida do player
            # recharge the player's health
            
            if gamemode == 1:
                pass

            elif gamemode == 2:
                self.player.health = 50
                self.sound_regen.play()

            else:
                self.player.health = 30
                self.sound_regen.play()           
            
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy1()
            self.enemy2 = Enemy1()
            self.enemy3 = Enemy1()
            self.enemy4 = Enemy1()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)
            self.enemies.append(self.enemy3)
            self.enemies.append(self.enemy4)

            self.enemies[0].health = enemy_health[0]
            self.enemies[0].x = 225
            self.enemies[0].y = -200
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 225
            self.enemies[1].y = -40
            self.enemies[1].alive = True

            self.enemies[2].health = enemy_health[0]
            self.enemies[2].x = 75
            self.enemies[2].y = -200
            self.enemies[2].alive = True
            

            self.enemies[3].health = enemy_health[0]
            self.enemies[3].x = 75
            self.enemies[3].y = -40
            self.enemies[3].alive = True
            
            self.move1 = 0
            self.move2 = 0
            self.move3 = 0
            self.move4 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)

                if self.enemies[0].y < 50 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 50:
                        self.move1 = 1

                if self.enemies[0].y < 200 and self.move1 == 1:
                    self.enemies[0].y += 1
                    if self.enemies[0].y == 200:
                        self.move1 = 2
                
                if self.enemies[0].x > 75 and self.move1 == 2:
                    self.enemies[0].x -= 1
                    if self.enemies[0].x == 75:
                        self.move1 = 3

                if self.enemies[0].y > 50 and self.move1 == 3:
                    self.enemies[0].y -= 1
                    if self.enemies[0].y == 50:
                        self.move1 = 4

                if self.enemies[0].x < 225 and self.move1 == 4:
                    self.enemies[0].x += 1
                    if self.enemies[0].x == 225:
                        self.move1 = 1
                

            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 200 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 200:
                        self.move2 = 1
                
                if self.enemies[1].x > 75 and self.move2 == 1:
                    self.enemies[1].x -= 1
                    if self.enemies[1].x == 75:
                        self.move2 = 2

                if self.enemies[1].y > 50 and self.move2 == 2:
                    self.enemies[1].y -= 1
                    if self.enemies[1].y == 50:
                        self.move2 = 3

                if self.enemies[1].x < 225 and self.move2 == 3:
                    self.enemies[1].x += 1
                    if self.enemies[1].x == 225:
                        self.move2 = 4

                if self.enemies[1].y < 200 and self.move2 == 4:
                    self.enemies[1].y += 1
                    if self.enemies[1].y == 200:
                        self.move2 = 1

            # anima o inimigo 3
            # animates the enemy 3
            if self.enemies[2].alive:
                self.enemies[2].canvas = self.canvas.create_image((self.enemies[2].x, self.enemies[2].y),
                                                                    image=self.enemies[2].image)
                
                if self.enemies[2].y < 50 and self.move3 == 0:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 50:
                        self.move3 = 1

                if self.enemies[2].x < 225 and self.move3 == 1:
                    self.enemies[2].x += 1
                    if self.enemies[2].x == 225:
                        self.move3 = 2

                if self.enemies[2].y < 200 and self.move3 == 2:
                    self.enemies[2].y += 1
                    if self.enemies[2].y == 200:
                        self.move3 = 3

                if self.enemies[2].x > 75 and self.move3 == 3:
                    self.enemies[2].x -= 1
                    if self.enemies[2].x == 75:
                        self.move3 = 4

                if self.enemies[2].y > 50 and self.move3 == 4:
                    self.enemies[2].y -= 1
                    if self.enemies[2].y == 50:
                        self.move3 = 1
            
            # anima o inimigo 4
            # animates the enemy 4
            if self.enemies[3].alive:
                self.enemies[3].canvas = self.canvas.create_image((self.enemies[3].x, self.enemies[3].y),
                                                                    image=self.enemies[3].image)
                
                if self.enemies[3].y < 200 and self.move4 == 0:
                    self.enemies[3].y += 2
                    if self.enemies[3].y == 200:
                        self.move4 = 1

                if self.enemies[3].y > 50 and self.move4 == 1:
                    self.enemies[3].y -= 1
                    if self.enemies[3].y == 50:
                        self.move4 = 2

                if self.enemies[3].x < 225 and self.move4 == 2:
                    self.enemies[3].x += 1
                    if self.enemies[3].x == 225:
                        self.move4 = 3

                if self.enemies[3].y < 200 and self.move4 == 3:
                    self.enemies[3].y += 1
                    if self.enemies[3].y == 200:
                        self.move4 = 4

                if self.enemies[3].x > 75 and self.move4 == 4:
                    self.enemies[3].x -= 1
                    if self.enemies[3].x == 75:
                        self.move4 = 1

    elif wave == 7:
        if not self.wave_defined:
            
            # definir os inimigos
            # defines the enemies

            self.enemy1 = Enemy2()
            self.enemy2 = Enemy1()
            self.enemy3 = Enemy1()

            self.enemies.clear()
            
            self.enemies.append(self.enemy1)
            self.enemies.append(self.enemy2)
            self.enemies.append(self.enemy3)

            self.enemies[0].health = enemy_health[1]
            self.enemies[0].x = 150
            self.enemies[0].y = -120
            self.enemies[0].alive = True

            self.enemies[1].health = enemy_health[0]
            self.enemies[1].x = 250
            self.enemies[1].y = -40
            self.enemies[1].alive = True

            self.enemies[2].health = enemy_health[0]
            self.enemies[2].x = 50
            self.enemies[2].y = -200
            self.enemies[2].alive = True
            
            self.move1 = 0
            self.move2 = 0
            self.move3 = 0

            self.wave_defined = True

        if self.wave_defined:
            # anima o inimigo 1
            # animates the enemy 1
            if self.enemies[0].alive:
                self.enemies[0].canvas = self.canvas.create_image((self.enemies[0].x, self.enemies[0].y),
                                                                    image=self.enemies[0].image)
                
                if self.enemies[0].y < 130 and self.move1 == 0:
                    self.enemies[0].y += 2
                    if self.enemies[0].y == 130:
                        self.move1 = 1

            # anima o inimigo 2
            # animates the enemy 2
            if self.enemies[1].alive:    
                self.enemies[1].canvas = self.canvas.create_image((self.enemies[1].x, self.enemies[1].y),
                                                                    image=self.enemies[1].image)

                if self.enemies[1].y < 210 and self.move2 == 0:
                    self.enemies[1].y += 2
                    if self.enemies[1].y == 210:
                        self.move2 = 1
                
                if self.enemies[1].x > 50 and self.move2 == 1:
                    self.enemies[1].x -= 2
                    if self.enemies[1].x == 50:
                        self.move2 = 2

                if self.enemies[1].y > 50 and self.move2 == 2:
                    self.enemies[1].y -= 2
                    if self.enemies[1].y == 50:
                        self.move2 = 3

                if self.enemies[1].x < 250 and self.move2 == 3:
                    self.enemies[1].x += 2
                    if self.enemies[1].x == 250:
                        self.move2 = 0

            # anima o inimigo 3
            # animates the enemy 3
            if self.enemies[2].alive:
                self.enemies[2].canvas = self.canvas.create_image((self.enemies[2].x, self.enemies[2].y),
                                                                    image=self.enemies[2].image)
                
                if self.enemies[2].y < 50 and self.move3 == 0:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 50:
                        self.move3 = 1

                if self.enemies[2].x < 250 and self.move3 == 1:
                    self.enemies[2].x += 2
                    if self.enemies[2].x == 250:
                        self.move3 = 2

                if self.enemies[2].y < 210 and self.move3 == 2:
                    self.enemies[2].y += 2
                    if self.enemies[2].y == 210:
                        self.move3 = 3

                if self.enemies[2].x > 50 and self.move3 == 3:
                    self.enemies[2].x -= 2
                    if self.enemies[2].x == 50:
                        self.move3 = 4

                if self.enemies[2].y > 50 and self.move3 == 4:
                    self.enemies[2].y -= 2
                    if self.enemies[2].y == 50:
                        self.move3 = 1

    elif wave == 8:
        pass
    elif wave == 9:
        pass
    elif wave == 10:
        pass


def change_wave(self):
    """
    troca a onda quando todos os inimigos estiverem mortos /
    changes the wave when all the enemies are dead
    """
    enemies_alive = 0
    
    for i in range(0, len(self.enemies)):
        if self.enemies[i].alive:
            enemies_alive += 1

    if enemies_alive == 0:
        self.wave += 1
        self.wave_defined = False
  

if __name__ == "__main__":
    print('Não é possível executar esse arquivo. Execute "SpaceShooter.py"')