try:
    from modules.constants import *
except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')

def player_move(self):
    """
    move o player de acordo com as teclas pressionadas /
    moves the player as certain keys are pressed
    """
    if self.pressing['Up'] or self.pressing['w'] or self.pressing['W']:
        move_up(self)

    if self.pressing['Down'] or self.pressing['s'] or self.pressing['S']:
        move_down(self)

    if self.pressing['Left'] or self.pressing['a'] or self.pressing['A']:
        move_left(self)

    if self.pressing['Right'] or self.pressing['d'] or self.pressing['D']:
        move_right(self)

def move_up(self):
    """
    move o player para cima /
    moves the player up
    """
    if self.player.y > 30:
        self.canvas.delete(self.player.ship)
        self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                    image=self.player.image[0])
        self.canvas.move(self.player.ship, 0, -self.player.vy)
        self.player.y -= self.player.vy

def move_down(self):
    """
    move o player para baixo /
    moves the player down
    """
    if self.player.y < CANVAS_H - 30:
        self.canvas.delete(self.player.ship)
        self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                    image=self.player.image[0])
        self.canvas.move(self.player.ship, 0, self.player.vy)
        self.player.y += self.player.vy

def move_left(self):
    """
    move o player para a esquerda /
    moves the player left
    """
    if self.player.x > 30:
        self.canvas.delete(self.player.ship)
        self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                    image=self.player.image[-1])
        self.canvas.move(self.player.ship, -self.player.vx, 0)
        self.player.x -= self.player.vx
        self.p_ship = 'left'
        if self.pressing['d'] or self.pressing['Right']:
            self.p_ship = 'center'

def move_right(self):
    """
    move o player para a direita /
    moves the player right
    """
    if self.player.x < CANVAS_W - 30:
        self.canvas.delete(self.player.ship)
        self.player.ship = self.canvas.create_image((self.player.x, self.player.y),
                                                    image=self.player.image[1])
        self.canvas.move(self.player.ship, self.player.vx, 0)
        self.player.x += self.player.vx
        self.p_ship = 'right'
        if self.pressing['a'] or self.pressing['Left']:
            self.p_ship = 'center'

def pressed(self, event):
    """
    checa se uma tecla de self.pressing[] está apertada e atribui valor True a ela /
    checks if any key from self.pressing[] is pressed, and sets True to them
    """
    self.pressing[event.keysym] = True

def released(self, event):
    """
    checa se uma tecla foi solta e atribui o valor False a ela /
    checks if any key from self.pressing[] is released, and sets False to them
    """
    self.pressing[event.keysym] = False
    self.p_ship = 'center'

if __name__ == "__main__":
    print('Não é possível executar esse arquivo. Execute "main.py"')