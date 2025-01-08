#processo2_screen
from telas.contrato_hono.funcoes_contrato_s1 import voltar, atualizar_dados, on_text_selected, salvar_texto, mostrar_popup, on_text_selected2

from telas.contrato_hono.texto_clausula_adv import TEXTOS_CLAUSULA1, ADVOGADOS_OAB, TEXTOS_CLAUSULA3
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

class Processo2Screen(Screen):
    def __init__(self, **kwargs):
        super(Processo2Screen, self).__init__(**kwargs)
        self.dados = None  # Armazenar todos os dados recebidos da ProcessoScreen

        # ScrollView para permitir rolagem caso o layout seja maior que a tela
        scroll_view = ScrollView(size_hint=(1, 1))
        
        # Layout principal em grade
        layout = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))  # Ajusta a altura automaticamente
        scroll_view.add_widget(layout)

        # Botão de voltar
        btn_voltar = Button(
            text="< Voltar",
            size_hint=(None, None),
            size=(100, 40)
        )
        btn_voltar.bind(on_press=self.poderes_voltar)
        layout.add_widget(btn_voltar)
        layout.add_widget(Widget())  # Espaço vazio para alinhar os elementos

        # Campo para o nome do arquivo
        layout.add_widget(Label(text="Nome do Arquivo:", size_hint=(None, None), height=30))
        self.nome_arquivo_input = TextInput(hint_text="Digite o nome do arquivo", multiline=False)
        layout.add_widget(self.nome_arquivo_input)

        # Spinner para selecionar advogado
        layout.add_widget(Label(text="Advogado:", size_hint=(None, None), height=30))
        self.adv_spinner = Spinner(
            text="Selecione um advogado",
            values=list(ADVOGADOS_OAB.keys())
        )
        layout.add_widget(self.adv_spinner)

        # Spinner para a cláusula 1
        layout.add_widget(Label(text="Modelo Cláusula 1:", size_hint=(None, None), height=30))
        self.modelo_spinner = Spinner(
            text="Selecione um modelo",
            values=list(TEXTOS_CLAUSULA1.keys())
        )
        self.modelo_spinner.bind(text=self.poderes_on_text_selected)
        layout.add_widget(self.modelo_spinner)

        # Campo de texto para a cláusula 1
        layout.add_widget(Label(text="Cláusula 1:", size_hint=(None, None), height=30))
        self.text_input = TextInput(
            hint_text="O texto selecionado aparecerá aqui para edição...",
            multiline=True,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.text_input)

        # Spinner para a cláusula 3
        layout.add_widget(Label(text="Modelo Cláusula 3:", size_hint=(None, None), height=30))
        self.modelo_spinner2 = Spinner(
            text="Selecione um modelo",
            values=list(TEXTOS_CLAUSULA3.keys())
        )
        self.modelo_spinner2.bind(text=self.poderes_on_text_selected2)
        layout.add_widget(self.modelo_spinner2)

        # Campo de texto para a cláusula 3
        layout.add_widget(Label(text="Cláusula 3:", size_hint=(None, None), height=30))
        self.text_input2 = TextInput(
            hint_text="O texto selecionado aparecerá aqui para edição...",
            multiline=True,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.text_input2)

        # Botão para salvar alterações
        save_button = Button(
            text="Salvar Texto",
            size_hint=(None, None),
            size=(150, 50)
        )
        save_button.bind(on_press=self.poderes_salvar_texto)
        layout.add_widget(save_button)
        layout.add_widget(Widget())  # Espaço vazio para alinhar

        # Adicionar o layout ao ScrollView
        self.add_widget(scroll_view)
      

    def poderes_voltar(self, instance):
        voltar(self, instance)  # Chama a função voltar
    
    def poderes_atualizar_dados(screen_instance, dados):
        atualizar_dados(screen_instance, dados)

    def poderes_on_text_selected(self, modelo_spinner, text):
        on_text_selected(self, modelo_spinner, text)  # Atualiza o texto selecionado
        
    def poderes_on_text_selected2(self, modelo_spinner2, text):
        on_text_selected2(self, modelo_spinner2, text)
    
    def poderes_salvar_texto(screen_instance, self):
        salvar_texto(screen_instance, self)  # Salva o texto editado

    def poderes_mostrar_popup(self, titulo, mensagem):
        mostrar_popup(self, titulo, mensagem)  # Exibe o popup
