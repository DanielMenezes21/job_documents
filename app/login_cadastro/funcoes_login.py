import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.screenmanager import SlideTransition

def check_credentials(username, password):
    """Verifica se o usuário e senha existem no banco através da API."""
    response = requests.get('http://127.0.0.1:5000/buscar_adv', params={'filtro': username})
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user[0] == username and user[1] == password:
                return user[0]
    return None

def validate_login(self, instance):
    user = self.username.text
    pwd = self.password.text

    advogado_id = check_credentials(user, pwd)
    if advogado_id:
        show_popup(self, "Sucesso", "Login bem-sucedido!")
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "home_screen"
        self.manager.advogado_id = advogado_id
    else:
        show_popup(self, "Erro", "Usuário ou senha incorretos!")

def show_popup(self, title, message):
    popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
    popup_layout.add_widget(Label(text=message))
    popup_layout.add_widget(Button(text="OK", on_press=lambda x: popup.dismiss()))

    popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(300, 200))
    popup.open()
    
def buscar_pessoas_por_nome(filtro):
    """Busca clientes pelo nome que começam com o texto digitado através da API."""
    response = requests.get('http://127.0.0.1:5000/buscar_adv', params={'filtro': filtro})
    if response.status_code == 200:
        return response.json()
    return []

def go_to_register(self, instance):
    self.manager.transition = SlideTransition(direction='left')
    self.manager.current = "register_page"