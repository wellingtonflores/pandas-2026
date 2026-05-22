import pyautogui
import keyboard
import threading
import time

clicando = False


def auto_click():
    global clicando
    while True:
        if clicando:
            pyautogui.click()
            time.sleep(0.1)  # velocidade do clique (0.1 = rápido)
        else:
            time.sleep(0.1)


def toggle():
    global clicando
    clicando = not clicando
    print("Auto click:", "ON" if clicando else "OFF")


# tecla F1 liga/desliga
keyboard.add_hotkey("F1", toggle)

# thread pra não travar o programa
threading.Thread(target=auto_click, daemon=True).start()

print("Pressione F1 para iniciar/parar o auto click.")
keyboard.wait()  # mantém o script rodando
