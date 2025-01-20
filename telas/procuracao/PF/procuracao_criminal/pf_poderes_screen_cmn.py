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
from telas.procuracao.PF.procuracao_criminal.pf_texto_poderes_cmn import TEXTOS_PODERES_A, ADVOGADO_OAB
from telas.procuracao.PF.procuracao_criminal.pf_funcoes_poderes_cmn import *
from docx import Document
import os

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

class PFPoderesCriminalScreen(Screen):
    def __init__(self, **kwargs):
        super(PFPoderesCriminalScreen, self).__init__(**kwargs)
        self.dados = None  # Armazenar todos os dados recebidos da HomeScreen

        # Layout principal
        layout = FloatLayout()

        # Botão de voltar (circular, pequeno e no canto superior esquerdo)
        btn_voltar = CircularButton(text="<")
        btn_voltar.pos_hint = {"x": 0.02, "top": 0.98}
        btn_voltar.bind(on_press=self.poderes_voltar)
        layout.add_widget(btn_voltar)

        # Título
        titulo = Label(
            text="Editar Poderes Pessoa Física",
            font_size=20,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.9},
        )
        layout.add_widget(titulo)

        # Spinner para selecionar texto predefinido
        self.modelo_spinner = Spinner(
            text="Selecione um modelo",
            values=list(TEXTOS_PODERES_A.keys()),  # Carrega os nomes dos textos do dicionário
            size_hint=(0.8, None),
            height=44,
            pos_hint={"center_x": 0.5, "top": 0.8},
        )
        self.modelo_spinner.bind(text=self.poderes_on_text_selected)  # Bind no modelo_spinner
        layout.add_widget(self.modelo_spinner)

        # Spinner para selecionar advogado
        self.adv_spinner = Spinner(
            text="Selecione um advogado",
            values=list(ADVOGADO_OAB.keys()),  # Carrega os nomes dos advogados do dicionário
            size_hint=(0.8, None),
            height=44,
            pos_hint={"center_x": 0.5, "top": 0.7},
        )
        layout.add_widget(self.adv_spinner)

        # Área de texto editável
        self.text_input = TextInput(
            hint_text="O texto selecionado aparecerá aqui para edição...",
            multiline=True,
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "top": 0.6},
        )
        layout.add_widget(self.text_input)

        # Botão para salvar alterações
        save_button = Button(
            text="Salvar Texto",
            size_hint=(0.5, None),
            height=50,
            pos_hint={"center_x": 0.5, "top": 0.2},
        )
        save_button.bind(on_press=self.poderes_salvar_texto)
        layout.add_widget(save_button)

        self.add_widget(layout)

        # Caminho do arquivo modelo, que será atualizado pela HomeScreen
        self.caminho_modelo = None
        self.caminho_declaracao = "13_DECLARACAO_HIPOSSUFICIENCIA_PF_TESTE.docx"

    def poderes_voltar(self, instance):
        voltar(self, instance)  # Chama a função voltar
    
    def poderes_atualizar_dados(self, dados):
        """
        Atualiza os dados recebidos na tela PoderesScreen.
        """
        self.dados = dados
        self.caminho_modelo = dados.get("caminho_modelo", None)
        print(f"Dados recebidos: {self.dados}")

    def poderes_on_text_selected(self, modelo_spinner, text):
        return on_text_selected(self, modelo_spinner, text)  # Atualiza o texto selecionado

    def poderes_salvar_texto(self, instance):
        salvar_texto(self, self)  # Salva o texto editado

    def poderes_mostrar_popup(self, titulo, mensagem):
        mostrar_popup(self, titulo, mensagem)  # Exibe o popup
