#processo_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.spinner import Spinner
from telas.contrato_hono.contrato_screen2 import Processo2Screen
from datetime import datetime
from telas.contrato_hono.funcoes_contrato_s2 import on_nacionalidade_change, on_sec_rg_change, ir_para_processo2, ir_para_homepage
from logic_tab import FocusSwitchingTextInput
class ProcessoScreen(Screen):
    def __init__(self, **kwargs):
        super(ProcessoScreen, self).__init__(**kwargs)
        
        self.caminho_modelo = r"14 CRIMINAL -  CONT, PROC - teste.docx"

        # Layout principal
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Campos para entrada de dados
        self.nome_contratante = FocusSwitchingTextInput(hint_text="Digite o nome do contratante", multiline=False, size_hint_y=0.1)
        layout.add_widget(self.nome_contratante)
        
        self.rg = FocusSwitchingTextInput(hint_text="Digite o Registro Geral do contratante", multiline=False, size_hint_y=0.1)
        layout.add_widget(self.rg)

        self.contratante_cpf = FocusSwitchingTextInput(hint_text="Digite o CPF do contratante", multiline=False, size_hint_y=0.1)
        layout.add_widget(self.contratante_cpf)

        self.cidade_contratante = FocusSwitchingTextInput(hint_text="Digite a cidade do contratante", multiline=False, size_hint_y=0.1)
        layout.add_widget(self.cidade_contratante)
        
        self.sigla_estado_contratante = FocusSwitchingTextInput(hint_text="Digite a sigla do estado do contratante", multiline=False, size_hint_y=0.1)
        layout.add_widget(self.sigla_estado_contratante)

        # Campo para selecionar o gênero
        self.inscrita_o_spinner = Spinner(
            text='Selecione o Gênero',
            values=('Masculino', 'Feminino'),
            size_hint_y=0.1, size_hint_x=0.3
        )
        layout.add_widget(self.inscrita_o_spinner)

        # Campo para selecionar a nacionalidade
        self.nacionalidade_spinner = Spinner(
            text="Selecione a Nacionalidade",
            values=("Brasileiro", "Outro"),
            size_hint_y=0.1, size_hint_x=0.3
        )
        self.nacionalidade_spinner.bind(
        text=lambda spinner, text: on_nacionalidade_change(self, spinner, text))
        layout.add_widget(self.nacionalidade_spinner)

        # Campo para editar a nacionalidade (inicialmente oculto)
        self.nacionalidade_input = FocusSwitchingTextInput(
            hint_text="Digite a nacionalidade",
            multiline=False,
            readonly=True,  # Inicialmente desabilitado
            size_hint_y=0.1
        )
        layout.add_widget(self.nacionalidade_input)
        
                # Campo para selecionar o RG
        self.sec_rg_spinner = Spinner(
            text="Selecione a secretaria do RG",
            values=("SSP", "Outro"),
            size_hint_y=0.1, size_hint_x=0.3
        )
        self.sec_rg_spinner.bind(
        text=lambda spinner, text: on_sec_rg_change(self, spinner, text))
        layout.add_widget(self.sec_rg_spinner)

        # Campo para editar a secretaria do RG (inicialmente oculto)
        self.sec_rg_input = TextInput(
            hint_text="Digite a secretaria pertencedora do RG",
            multiline=False,
            readonly=True,  # Inicialmente desabilitado
            size_hint_y=0.1
        )
        layout.add_widget(self.sec_rg_input)
        
        self.est_rg_input = FocusSwitchingTextInput(
            hint_text="Digite o estado pertencedor da secretaria ",
            multiline=False,
            readonly=False,  # Inicialmente desabilitado
            size_hint_y=0.1
        )
        layout.add_widget(self.est_rg_input)
        
        button_layout = FloatLayout(size_hint_y=0.2)

        # Botão para ir à tela de edição de poderes
        btn_poderes = Button(text="Continuar", size_hint=(0.2, 0.5), pos_hint={"x": 0.8, "y": 0.1})
        btn_poderes.bind(on_press=lambda instance: ir_para_processo2(self, instance))
        button_layout.add_widget(btn_poderes)
        
        btn_homepage = Button(text="Voltar para homepage", size_hint=(0.2, 0.5), pos_hint={"x": 0.0, "y": 0.1})
        btn_homepage.bind(on_press=lambda instance: ir_para_homepage(self, instance))  # Substitua "homepage" pelo ID da sua tela principal
        button_layout.add_widget(btn_homepage)
        
        layout.add_widget(button_layout)

        self.add_widget(layout)

