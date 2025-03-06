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
from app.procuracao.PJ.procuracao_criminal.pj_texto_poderes_cmn import TEXTOS_PODERES_A, ADVOGADO_OAB
from app.procuracao.PJ.procuracao_criminal.pj_funcoes_poderes_cmn import *
from docx import Document
import os

class CircularButton(Button):
    def __init__(self, **kwargs):
        super(CircularButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.background_normal = ''  
        self.background_color = (0.2, 0.6, 0.8, 1) 
        self.color = (1, 1, 1, 1) 
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)
            self.ellipse = Ellipse(size=self.size, pos=self.pos)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_size)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos

    def update_graphics_size(self, *args):
        self.ellipse.size = self.size

class PoderesCriminalPJScreen(Screen):
    def __init__(self, **kwargs):
        super(PoderesCriminalPJScreen, self).__init__(**kwargs)
        self.dados = None 

        layout = FloatLayout()

        btn_voltar = CircularButton(text="<")
        btn_voltar.pos_hint = {"x": 0.02, "top": 0.98}
        btn_voltar.bind(on_press=self.poderes_voltar)
        layout.add_widget(btn_voltar)

        titulo = Label(
            text="Editar Poderes Pessoa Jurídica",
            font_size=20,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.9},
        )
        layout.add_widget(titulo)

        self.modelo_spinner = Spinner(
            text="Selecione um modelo",
            values=list(TEXTOS_PODERES_A.keys()), 
            height=44,
            pos_hint={"center_x": 0.5, "top": 0.8},
        )
        self.modelo_spinner.bind(text=self.poderes_on_text_selected)  
        layout.add_widget(self.modelo_spinner)

        self.text_input = TextInput(
            hint_text="O texto selecionado aparecerá aqui para edição...",
            multiline=True,
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "top": 0.6},
        )
        layout.add_widget(self.text_input)

        save_button = Button(
            text="Salvar Texto",
            size_hint=(0.5, None),
            height=50,
            pos_hint={"center_x": 0.5, "top": 0.2},
        )
        save_button.bind(on_press=self.poderes_salvar_texto)
        layout.add_widget(save_button)

        self.add_widget(layout)

    def poderes_voltar(self, instance):
        voltar(self, instance)  
    
    def poderes_atualizar_dados(self, dados):
        """
        Atualiza os dados recebidos na tela PoderesScreen.
        """
        atualizar_dados(self, dados)

    def poderes_on_text_selected(self, modelo_spinner, text):
        return on_text_selected(self, modelo_spinner, text)  

    def poderes_salvar_texto(self, instance):
        salvar_texto(self, self)  

    def poderes_mostrar_popup(self, titulo, mensagem):
        mostrar_popup(self, titulo, mensagem)  
