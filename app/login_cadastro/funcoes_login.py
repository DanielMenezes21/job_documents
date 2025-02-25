import sqlite3
from time import sleep
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.popup import Popup

def check_credentials(username, password):
    """Verifica se o usuário e senha existem no banco."""
    conn = sqlite3.connect("advogados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM advogados WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def validate_login(self, instance):
        user = self.username.text
        pwd = self.password.text

        if check_credentials(user, pwd):
            show_popup(self, "Sucesso", "Login bem-sucedido!")
            sleep(1)
            self.manager.current = "home_screen"
        else:
            show_popup(self, "Erro", "Usuário ou senha incorretos!")

def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        popup_layout.add_widget(Button(text="OK", on_press=lambda x: popup.dismiss()))

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(300, 200))
        popup.open()
import sqlite3

def buscar_pessoas_por_nome(filtro):
    """Busca clientes pelo nome ou CPF que começam com o texto digitado."""
    conn = sqlite3.connect("advogados.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username FROM advogados
        WHERE username LIKE ? OR password LIKE ? 
        LIMIT 10
    """, (filtro + "%", filtro + "%"))
    
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def go_to_register(self, instance):
        self.manager.current = "register_page"