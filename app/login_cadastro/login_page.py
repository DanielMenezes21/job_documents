from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from modules.logic_tab import FocusSwitchingTextInput
from kivy.clock import Clock
from app.login_cadastro.funcoes_login import buscar_pessoas_por_nome, validate_login, go_to_register
from modules.resource_path import BackgroundImage

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with self.canvas.before:
            self.background = BackgroundImage()
            self.bind(size=self._update_background, pos=self._update_background)
        
        self.username = FocusSwitchingTextInput(hint_text="Usuário", multiline=False, size_hint_y=0.06)
        self.username.bind(text=self.atualizar_sugestoes) 

        self.password = FocusSwitchingTextInput(hint_text="Senha", password=True, multiline=False, size_hint_y=0.06)
        self.login_button = Button(text="Entrar", size_hint=(0.18, 0.04), pos_hint={'x': 0.41}, on_press=self.login_validate)
        self.register_button = Button(text="Cadastrar", size_hint=(0.18, 0.04), pos_hint={'x': 0.41}, on_press=self.login_to_go_register)

        self.dropdown = DropDown()  

        layout.add_widget(Label(text="Login", font_name="Roboto", font_size=30, size_hint_y=0.20))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.login_button)
        layout.add_widget(self.register_button)

        self.add_widget(layout)

    def _update_background(self, *args):
        self.background.size = self.size
        self.background.pos = self.pos

    def atualizar_sugestoes(self, instance, text):
        """Atualiza as sugestões conforme o usuário digita."""
        self.dropdown.dismiss()
        self.dropdown.clear_widgets()
        if text:
            nomes = buscar_pessoas_por_nome(text)
            for nome in nomes:
                str(nome)
                btn = Button(text=nome[0], size_hint_y=None, height=40)
                btn.bind(on_release=lambda btn: self.preencher_username(btn.text))
                self.dropdown.add_widget(btn)
            if nomes:
                Clock.schedule_once(lambda dt: self.dropdown.open(self.username), 0.04) 

    def preencher_username(self, nome):
        """Preenche o campo de usuário com o nome selecionado e fecha o menu."""
        self.username.text = nome
        self.dropdown.dismiss()

    def login_validate(self, instance):
        validate_login(self, instance)

    def login_to_go_register(self, instance):
        go_to_register(self, instance)