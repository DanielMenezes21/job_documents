import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import SlideTransition

def add_user(username, password, identidade_OAB):
    """Adiciona um novo usuário ao banco de dados."""
    conn = sqlite3.connect("advogados.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO advogados (username, password, identidade_OAB) VALUES (?, ?, ?)", (username, password, identidade_OAB))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
        
def register_user(self, instance):
        user = self.username.text
        pwd = self.password.text
        oab = self.identidade_OAB.text

        if user and pwd and oab:
            if add_user(user, pwd, oab):
                show_popup(self, "Sucesso", "Usuário cadastrado com sucesso!")
                self.manager.current = "login_page"
            else:
                show_popup(self, "Erro", "Usuário já existe!")
        else:
            show_popup(self, "Erro", "Preencha todos os campos!")

def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        popup_layout.add_widget(Button(text="OK", on_press=lambda x: popup.dismiss()))

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(300, 200))
        popup.open()

def go_to_login(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = "login_page"
