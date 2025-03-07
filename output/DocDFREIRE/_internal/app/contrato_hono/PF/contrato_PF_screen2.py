#processo2_screen
from app.contrato_hono.PF.funcoes_PF_contrato_s2 import *

from app.contrato_hono.PF.texto_clausula import TEXTOS_CLAUSULAS
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Ellipse, Color
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from docx import Document


class CircularButton(Button):
    def __init__(self, **kwargs):
        super(CircularButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.background_normal = ''  # Remove fundo padrão
        self.background_color = (0.2, 0.6, 0.8, 1)  # Cor azul clara
        self.color = (1, 1, 1, 1)  # Texto branco
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)
            self.ellipse = Ellipse(size=self.size, pos=self.pos)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_size)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos

    def update_graphics_size(self, *args):
        self.ellipse.size = self.size

class ContratoPF2Screen(Screen):
    def __init__(self, **kwargs):
        super(ContratoPF2Screen, self).__init__(**kwargs)
        self.dados = None  # Armazenar os dados da tela anterior
        self.placeholders = {}

        # Layout principal
        layout = BoxLayout(orientation="vertical", padding=50, spacing=10)

        # Botão de voltar
        btn_voltar = Button(
            text="< Voltar",
            size_hint=(None, None),
            size=(100, 40)
        )
        btn_voltar.bind(on_press=self.poderes_voltar)
        layout.add_widget(btn_voltar)

        layout.add_widget(Widget())  # Espaço vazio

        # Spinner para seleção de cláusulas
        self.spinner = Spinner(
            text="Selecione a cláusula",
            values=list(TEXTOS_CLAUSULAS.keys()),
            size_hint=(1, 0.2),
        )
        self.spinner.bind(text=self.poderes_on_selected)
        layout.add_widget(self.spinner)

        # Campo de texto com rolagem interna
        self.text_input = TextInput(
            hint_text="Texto da cláusula",
            multiline=True,      # Ativa a rolagem interna
            size_hint=(1, 0.6),  # Define o tamanho do campo de texto
            cursor_blink=True    # Cursor pisca para visibilidade
        )
        self.text_input.bind(text=self.text_change)
        layout.add_widget(self.text_input)

        # Botão para salvar
        save_button = Button(
            text="Salvar Texto",
            size_hint=(None, None),
            size=(150, 50)
        )
        save_button.bind(on_press=lambda instance: self.poderes_salvar_texto(self))  # Passa 'self' corretamente
        
        layout.add_widget(save_button)

        # Adicionar o layout à tela
        self.add_widget(layout)

    def text_change(self, instance, value):
        on_text_change(self, instance, value)
        
    def poderes_on_selected(self, spinner, text):
        on_spinner_select(self, spinner, text)

    def poderes_voltar(self, instance):
        voltar(self, instance)

    def poderes_atualizar_dados(screen_instance, dados):
        atualizar_dados(screen_instance, dados)

    def poderes_salvar_texto(self, screen_instance):
        salvar_texto(self, screen_instance)  # Salva o texto editado

    def poderes_mostrar_popup(self, titulo, mensagem):
        mostrar_popup(self, titulo, mensagem)