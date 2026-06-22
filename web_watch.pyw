from win32 import win32gui # Bibiliteca para pegar a janela ativa
import pyautogui # Biblioteca para controlar o mouse
import requests # Biblioteca para fazer requisições HTTP
import time
import schedule # Biblioteca para agendamento de tarefas
import threading # Biblioteca para trabalhar com threads
from urllib.parse import urlsplit, parse_qs, parse_qsl, urlparse, urlunparse, urlencode # Biblioteca para trabalhar com URLs
from pywinauto import Desktop, Application # Biblioteca para controlar o Windows
import os # Biblioteca para trabalhar com arquivos
import sys # Biblioteca para trabalhar com arquivos

keywords = [] # Lista para armazenar os sites proibidos

def obter_sites_proibidos():
    """"
    Função para obter os sites proibidos do servidor
    """
    url = "https://pedrotech.com.br/.main/fetch_control.php"

    form_data = {
        "-37vXj0zPm10RI": 'true',
        "control_class": "web_watch",
        "control_action": "read"
    }

    response = requests.post(url, data=form_data, verify=False)

    global keywords
    keywords = [site['keyword'] for site in response.json()]

def pegar_janela_ativa():
    """
    Função para pegar a janela ativa
    """
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def redirecionar(nova_url, browser_window, barra_endereco):
    """
    Função para redirecionar para uma nova URL
    """
    browser_window.set_focus()
    barra_endereco.click_input()
    time.sleep(0.2)
    barra_endereco.set_edit_text(nova_url)
    time.sleep(0.2)
    browser_window.type_keys('{ENTER}')
    time.sleep(2)
    return

def processar_pesquisa_ia(titulo, browser):
    """
    Função para processar as pesquisas com IA
    """
    def google_redirect(query, search, url_path, parsed_url, browser_window, barra_endereco):
        """
        Função para redirecionar para uma nova URL do Google
        """
        udm = query.get('udm', [''])[0] # Parametro do Google que muda a pesquisa ('' = Tudo, '14' = Web, '50' = IA)

        if (search != '' and (udm == '50' or udm == '')):
            print(f"Detectado uso de IA na pesquisa. Redirecionando para pesquisa sem IA...")
            new_query = urlencode({'q': search, 'udm': '14'}) # Cria uma nova query sem IA
            modified_parsed = parsed_url._replace(query = new_query)
            return redirecionar(urlunparse(modified_parsed), browser_window, barra_endereco) # Redireciona para a nova URL
        
    def bing_redirect(query, search, url_path, parsed_url, browser_window, barra_endereco):
        """
        Função para redirecionar para uma nova URL do Bing
        """
        mturn = query.get('mturn', [''])[0] # Parametro do Bing que muda a pesquisa ('' = Tudo, '1' = IA)
        allowed_paths = ['images', 'video', 'news', 'shop'] # Caminhos permitidos
        
        for allowed in allowed_paths:
            if allowed in url_path:
                return
        if search != '' and (mturn == '1' or mturn == ''):
            print(f"Detectado uso de IA na pesquisa. Redirecionando para pesquisa sem IA...")
            new_query = urlencode({'q': search + ' -ai' if ' -ai' not in search else search, 'mturn': '0'}) # Cria uma nova query sem IA
            modified_parsed = parsed_url._replace(query = new_query)
            return redirecionar(urlunparse(modified_parsed), browser_window, barra_endereco) # Redireciona para a nova URL
        
    if ('Pesquisa Google' in titulo or 'Pesquisar' in titulo) and 'i24IVfb30*D0>o2]0[<4<~b:' in keywords:
        desktop = Desktop(backend="uia")
        browser_window = desktop.window(title_re=f".*{browser}.*", found_index=0) # Encontra a janela do navegador
        caixas_texto = browser_window.descendants(control_type="Edit") # Encontra as caixas de texto (barra de pesquisa)

        if caixas_texto:
            barra_endereco = caixas_texto[0]
            site_atual = barra_endereco.get_value()
            parsed_url = urlparse(site_atual)
            url_query = urlsplit(site_atual).query
            url_path = urlsplit(site_atual).path
            query = parse_qs(url_query)
            search = query.get('q', [''])[0] # Parametro da pesquisa

            if browser == "Google Chrome" or 'Pesquisa Google' in titulo:
                return google_redirect(query, search, url_path, parsed_url, browser_window, barra_endereco)
            elif browser == "Edge" or 'Pesquisar' in titulo:                
                return bing_redirect(query, search, url_path, parsed_url, browser_window, barra_endereco)

def fechar_aba(titulo):
    """
    Função para fechar uma aba
    """
    for keyword in keywords:
        if keyword.lower() in titulo.lower():
            print(f"Detectado site proibido: {titulo}. Fechando aba...")
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            return

def watch():
    """
    Função para monitorar a janela ativa
    """
    titulo = pegar_janela_ativa()
    
    if 'Google Chrome' in titulo:
        try:
            fechar_aba(titulo)
            processar_pesquisa_ia(titulo, 'Google Chrome')
            return
        except Exception as e:
            print(f"Erro ao processar janela do Chrome: {e}")
            return
    elif 'Edge' in titulo:
        try:
            fechar_aba(titulo)
            processar_pesquisa_ia(titulo, 'Edge')
            return
        except Exception as e:
            print(f"Erro ao processar janela do Edge: {e}")
            return

def obter_pasta_exe(relative_path):
    """
    Função para obter a pasta do executável
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    """
    Função principal que inicia o monitoramento e trata todos os casos
    """
    try:
        if os.path.exists(r"C:\Users\lab136\web_watch.exe"):
            # Executa o script web_watch.bat caso ele não tenha sido executado ainda
            print("Executando web_watch.bat...")
            bat_path = obter_pasta_exe("web_watch.bat")
            os.system(f'"{bat_path}"')
        
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

main()