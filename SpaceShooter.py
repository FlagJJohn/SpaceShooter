try:
    from tkinter import *

    from modules.constants import *

    from modules.space_shooter import Game
    
except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')


ENEMY_HEALTH = [10, 30]
BOSS_HEALTH = 100
PLAYER_HEALTH = 10
BULLET_SPEED = 0
GAME_CONTROL = 0
GAMEMODE = 0


class ConfigWindow(object):
    def __init__(self):
        self.bg = 'lightsteelblue'
        # iniciamos a janela
        # initiate window
        self.root = Tk()
        self.root.title('Space Shooter')
        self.root.geometry(f'+{screensize[0] // 3}+{screensize[1] // 4}')
        self.root['bg'] = self.bg
        self.root.resizable(False, False)

        # criamos checkbuttons para dificuldade
        # difficulty checkbuttons
        self.v_normal = IntVar()
        self.check_normal = Checkbutton(self.root, text='Normal', font=('Courier', 15), command=self.normal,
                                        bg=self.bg, activebackground=self.bg, variable=self.v_normal)

        self.v_hard = IntVar()
        self.check_hard = Checkbutton(self.root, text='Hard', font=('Courier', 15), command=self.hard,
                                      bg=self.bg, activebackground=self.bg, variable=self.v_hard)

        self.v_hardcore = IntVar()
        self.check_hardcore = Checkbutton(self.root, text='Hardcore', font=('Courier', 15, 'bold'), fg='red',
                                          activeforeground='red', bg=self.bg, activebackground=self.bg,
                                          command=self.hardcore, variable=self.v_hardcore)

        # criamos checkbuttons para controle
        # control checkbuttons
        self.v_wasd = IntVar()
        self.check_wasd = Checkbutton(self.root, text='WASD + ENTER', font=('Courier', 15),
                                      command=self.wasd, bg=self.bg, activebackground=self.bg, variable=self.v_wasd)

        self.v_arrows = IntVar()
        self.check_arrows = Checkbutton(self.root, text='SETAS + ESPAÇO', font=('Courier', 15),
                                        command=self.arrows, bg=self.bg, activebackground=self.bg,
                                        variable=self.v_arrows)

        # criamos botão start
        # start button
        self.b_start = Button(self.root, command=self.start_game, text='START', font=('Courier', 15, 'bold'),
                              bg='CadetBlue', activebackground='CadetBlue')

        # label título
        # title label
        self.l_title = Label(self.root, text='SPACE SHOOTER', font=('Times', 30, 'bold'), bg=self.bg,
                             activebackground=self.bg)

        # label dificuldade e controles
        # difficulty and control labels        
        self.l_dif = Label(self.root, text='Dificuldade:', font=('Courier', 15), bg=self.bg, activebackground=self.bg)
        self.l_cont = Label(self.root, text='Controles:', font=('Courier', 15), bg=self.bg, activebackground=self.bg)

        # elementos no grid
        # put elements on the grid
        self.l_title.grid(row=0, column=0, columnspan=5, rowspan=2, pady=30, padx=30)
        self.l_dif.grid(row=2, column=1, rowspan=2, sticky=W, padx=20)
        self.l_cont.grid(row=2, column=3, rowspan=2, sticky=W, padx=20)

        self.check_normal.grid(row=4, column=1, sticky=W, padx=20)
        self.check_hard.grid(row=5, column=1, sticky=W, padx=20)
        self.check_hardcore.grid(row=6, column=1, sticky=W, padx=20)

        self.check_wasd.grid(row=4, column=3, sticky=W, padx=20)
        self.check_arrows.grid(row=5, column=3, sticky=W, padx=20)

        self.b_start.grid(row=7, columnspan=5, rowspan=2, pady=20)

        # bool pra saber se a dificuldade e controles foram selecionados
        # bool value to check if the configs are chosen
        self.dif_chosen = False
        self.control_chosen = False

        self.root.mainloop()

    def start_game(self):
        """
        inicia o jogo principal se as configurações foram escolhidas /
        starts the main game if both the configs are chosen
        """

        if self.dif_chosen and self.control_chosen:
            global ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAMECONTROL, GAMEMODE
            self.quit()
            Game(ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAME_CONTROL, GAMEMODE, True)

    def normal(self):
        """
        Seleciona a dificuldade normal /
        Chooses the normal difficulty
        """
        global ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAMEMODE

        ENEMY_HEALTH[0] *= 2
        ENEMY_HEALTH[1] *= 2
        BOSS_HEALTH *= 2
        PLAYER_HEALTH *= 10
        BULLET_SPEED = 5
        GAMEMODE = 1

        if self.v_normal.get() == 1:
            self.check_hard.deselect()
            self.check_hardcore.deselect()
            self.dif_chosen = True

        elif self.v_normal.get() == 0:
            self.dif_chosen = False

    def hard(self):
        """
        Seleciona a dificuldade difícil /
        Chooses the hard difficulty
        """
        global ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAMEMODE

        ENEMY_HEALTH[0] *= 5
        ENEMY_HEALTH[1] *= 5
        BOSS_HEALTH *= 4
        PLAYER_HEALTH *= 5
        BULLET_SPEED = 6
        GAMEMODE = 2

        if self.v_hard.get() == 1:
            self.check_normal.deselect()
            self.check_hardcore.deselect()
            self.dif_chosen = True

        elif self.v_hard.get() == 0:
            self.dif_chosen = False

    def hardcore(self):
        """
        Seleciona a dificuldade hardcore /
        Chooses the hardcore difficulty
        """
        global ENEMY_HEALTH, BOSS_HEALTH, PLAYER_HEALTH, BULLET_SPEED, GAMEMODE

        ENEMY_HEALTH[0] *= 5
        ENEMY_HEALTH[1] *= 5
        BOSS_HEALTH *= 4
        PLAYER_HEALTH *= 3
        BULLET_SPEED = 7
        GAMEMODE = 3

        if self.v_hardcore.get() == 1:
            self.check_hard.deselect()
            self.check_normal.deselect()
            self.dif_chosen = True

        elif self.v_hardcore.get() == 0:
            self.dif_chosen = False

    def wasd(self):
        """
        Seleciona o controle como teclas WASD e ENTER /
        Chooses the game controls as WASD + ENTER
        """
        global GAME_CONTROL
        GAME_CONTROL = 1

        if self.v_wasd.get() == 1:
            self.check_arrows.deselect()
            self.control_chosen = True

        elif self.v_wasd.get() == 0:
            self.control_chosen = False

    def arrows(self):
        """
        Seleciona os controles como teclas direcionais e espaço /
        Chooses the game controls as ARROWS + SPACE
        """
        global GAME_CONTROL
        GAME_CONTROL = 2

        if self.v_arrows.get() == 1:
            self.check_wasd.deselect()
            self.control_chosen = True

        elif self.v_arrows.get() == 0:
            self.control_chosen = False

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    ConfigWindow()