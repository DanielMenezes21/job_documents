import os
import sys
from kivy.uix.image import Image

def resource_path(relative_path):
    """ Obtenha o caminho absoluto ao recurso, lidando com o PyInstaller """
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho nela
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Use resource_path para obter o caminho correto dos arquivos
image_path = resource_path("image/download.jpeg")
db_path = resource_path("advogados.db")

class BackgroundImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = image_path
        self.allow_stretch = True
        self.keep_ratio = False
        self.resource_path = resource_path(image_path)