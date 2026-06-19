from win32 import win32gui
import pyautogui
import requests
import time
import schedule
import threading
import pyperclip
from urllib.parse import urlsplit, parse_qs, parse_qsl, urlparse, urlunparse, urlencode
from pywinauto import Desktop, Application

keywords = []

def obter_sites_proibidos():
    url = "https://pedrotech.com.br/.main/fetch_control.php"

    form_data = {
        "-37vXj0zPm10RI": 'true',
        "control_class": "web_watch",
        "control_action": "read"
    }

    response = requests.post(url, data=form_data)

    global keywords
    keywords = [site['keyword'] for site in response.json()]

def pegar_janela_ativa():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def watch():
    titulo = pegar_janela_ativa()
    
    if "Google Chrome" in titulo or "Edge" in titulo:
        if 'Pesquisa Google' in titulo and 'i24IVfb30*D0>o2]0[<4<~b:' in keywords:
            desktop = Desktop(backend="uia")
            chrome_win = desktop.windows(title_re=".*Google Chrome.*")[0]
            caixas_texto = chrome_win.descendants(control_type="Edit")

            if caixas_texto:
                barra_endereco = caixas_texto[0]
                site_atual = barra_endereco.get_value()
                parsed_url = urlparse(site_atual)
                url_query = urlsplit(site_atual).query
                google_query = parse_qs(url_query)
                search = google_query.get('q', [''])[0]
                udm = google_query.get('udm', [''])[0]

                if (udm == '50' or udm == ''):
                    print(f"Detectado uso de IA na pesquisa. Redirecionando para pesquisa sem IA...")
                    new_query = urlencode({'q': search, 'udm': '14'})
                    modified_parsed = parsed_url._replace(query = new_query)
                    nova_url = urlunparse(modified_parsed)

                    pyperclip.copy(nova_url)
                    pyautogui.hotkey('ctrl', 'l') 
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.2)
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.press('escape')
            return
        for keyword in keywords:
            if keyword.lower() in titulo.lower():
                print(f"Detectado site proibido: {titulo}. Fechando aba...")
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                return

try:
    obter_sites_proibidos()
    schedule.every(5).seconds.do(obter_sites_proibidos)

    def start_watch():
        while True:
            schedule.run_pending()
            time.sleep(1)

    watch_thread = threading.Thread(target=start_watch)
    watch_thread.daemon = True
    watch_thread.start()

    print("Monitoramento iniciado...")
    while True:
        watch()
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Monitoramento encerrado.")