import os
import requests
import shutil
import subprocess

# Configuração
UPDATE_URL = "http://seuservidor.com/update_info.json"
LOCAL_VERSION_FILE = "version.txt"
EXECUTABLE_NAME = "job_documents.exe"  # Nome do executável local

def check_for_updates():
    try:
        # Obtém as informações de atualização do servidor
        response = requests.get(UPDATE_URL)
        update_info = response.json()
        latest_version = update_info["version"]

        # Verifica a versão local
        local_version = get_local_version()
        if local_version != latest_version:
            print(f"Nova versão disponível: {latest_version} (atual: {local_version})")
            download_update(update_info["update_url"], EXECUTABLE_NAME)
        else:
            print("Você já está usando a versão mais recente.")

    except Exception as e:
        print(f"Erro ao verificar atualizações: {e}")

def get_local_version():
    # Lê o número da versão local do arquivo 'version.txt'
    if os.path.exists(LOCAL_VERSION_FILE):
        with open(LOCAL_VERSION_FILE, "r") as f:
            return f.read().strip()
    return "0.0.0"  # Versão padrão caso não exista

def download_update(update_url, executable_name, latest_version):
    try:
        print("Baixando atualização...")
        response = requests.get(update_url, stream=True)
        with open(f"{executable_name}.new", "wb") as f:
            shutil.copyfileobj(response.raw, f)

        # Substitui o executável atual pelo novo
        os.replace(f"{executable_name}.new", executable_name)
        print("Atualização concluída. Reiniciando o aplicativo...")
        
        # Atualiza o arquivo de versão local
        with open(LOCAL_VERSION_FILE, "w") as f:
            f.write(latest_version)

        # Reinicia o aplicativo
        subprocess.Popen([executable_name])
        exit()

    except Exception as e:
        print(f"Erro ao baixar a atualização: {e}")

if __name__ == "__main__":
    check_for_updates()
