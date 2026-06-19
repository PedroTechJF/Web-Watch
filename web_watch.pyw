from win32 import win32gui
import pyautogui
import time

SITES_PROIBIDOS = ["artificial", "inteligência artificial", "Gemini", "Chat", "GPT", "ChatGPT", "Bard", "Claude", "Ernie Bot", "LLaMA", "Mistral", "Manus", "NotebookLM", "Copa", "Cup", "Caze", "Cazé", "TV", "CazéTV", "cazetv"]

def pegar_janela_ativa():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

print("Monitoramento iniciado...")
try:
    while True:
        titulo = pegar_janela_ativa()
        
        # Verifica se o Chrome ou Edge é a janela ativa e se contém um site proibido
        if "Google Chrome" in titulo or "Edge" in titulo:
            for site in SITES_PROIBIDOS:
                if site.lower() in titulo.lower():
                    print(f"Detectado site proibido: {titulo}. Fechando aba...")
                    # Simula o atalho Ctrl + W para fechar a aba atual
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(1) # Pequena pausa para evitar múltiplos comandos
                    
        time.sleep(0.5) # Verifica a cada meio segundo
except KeyboardInterrupt:
    print("Monitoramento encerrado.")
