import winsound

def som_menu():
    winsound.PlaySound('./wav/ping_pong_8bit_plop.wav', winsound.SND_ASYNC)

def som_colisao():
    winsound.PlaySound('./wav/ping_pong_8bit_beeep.wav', winsound.SND_ASYNC)
    pass