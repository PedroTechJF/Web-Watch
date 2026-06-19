import sqlite3
import shutil
import os
from datetime import datetime, timedelta

# Caminhos padrão (Substitua USERNAME pelo seu usuário do Windows)
# Windows: f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
# Mac: f"/Users/{os.getlogin()}/Library/Application Support/Google/Chrome/Default/History"
# Linux: f"/home/{os.getlogin()}/.config/google-chrome/Default/History"

caminho_original = r"C:\Users\pedro\AppData\Local\Google\Chrome\User Data\Default\History"
caminho_copia = "History_temp"

try:
    # 1. Copia o arquivo para não dar erro de bloqueio
    shutil.copyfile(caminho_original, caminho_copia)
    
    # 2. Conecta na cópia
    conn = sqlite3.connect(caminho_copia)
    cursor = conn.cursor()
    
    # 3. Executa a query
    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10")
    results = cursor.fetchall()
    
    for row in results:
        url, title, visit_time = row
        # Ajuste do timestamp do Chrome (Webkit epoch: inicia em 01/01/1601)
        # tempo_epoch = datetime(1601, 1, 1) + timedelta(microseconds=visit_time)
        # print(f"Data: {tempo_epoch} | Título: {title} | URL: {url}")
        print(url)
    conn.close()

finally:
    # 4. Remove a cópia temporária após o uso
    if os.path.exists(caminho_copia):
        os.remove(caminho_copia)
