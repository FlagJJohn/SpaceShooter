try:
    import ctypes   
except ModuleNotFoundError:
    print('Não foi possível carregar algum módulo.')

# pega o tamanho do monitor do usuário
# gets the user monitor's size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# tamanho da janela
# window size
WINDOW_W = 500
WINDOW_H = 500

#tamanho do canvas
#canvas size
CANVAS_W = 300
CANVAS_H = 600

if __name__ == "__main__":
    print('Não é possível executar esse arquivo. Execute "SpaceShooter.py"')