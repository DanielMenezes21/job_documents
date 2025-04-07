#processo_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.spinner import Spinner
from app.contrato_hono.PJ.contrato_PJ_screen2 import Processo2Screen
from kivy.uix.scrollview import ScrollView
from datetime import datetime
from app.contrato_hono.PJ.funcoes_PJ_contrato_s1 import *
from modules.logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput

class ProcessoScreen(Screen):
    def __init__(self, **kwargs):
        super(ProcessoScreen, self).__init__(**kwargs)
        
        self.caminho_modelo = r"10_MODELO_CONTRATACAO_PJ_TESTE - Copia.docx"

        self.scrollview = ScrollView(size_hint=(1, 1))

        # Layout principal
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        layout.bind(minimum_height=layout.setter('height'))

        # Campos para entrada de dados
        self.num_contrato = FocusSwitchingTextInput(hint_text= "número do contrato", multiline=False, size_hint=(0.18, 0.18), pos_hint={"center_x": 0.5, "center_y": 0.1})
        layout.add_widget(self.num_contrato)
        
        self.nome_cliente = FocusSwitchingTextInput(hint_text="Digite o nome do cliente", multiline=False, size_hint=(0.6, 1))
        layout.add_widget(self.nome_cliente)
        
        self.estado_civil = FocusSwitchingTextInput(hint_text="Digite o estado civil do cliente", multiline=False, size_hint=(0.4, 1))
        layout.add_widget(self.estado_civil)

        self.cliente_cpf = MaskedFocusSwitchingTextInput(hint_text="Digite o CPF do cliente", multiline=False, mask="   .   .   -  ", max_length=11, size_hint_y=1, size_hint_x=0.6)
        layout.add_widget(self.cliente_cpf)
        
        self.cliente_rg = FocusSwitchingTextInput(hint_text="Digite o RG do cliente", multiline=False, size_hint_y=1, size_hint_x=0.4)
        layout.add_widget(self.cliente_rg)
        
        self.sec_rg = Spinner(text="SEC RG", values=("SSP", "PC", "DETRAN", "ITEP", "SESP", "SEDS", "SEJUSP", "SDS", "SEJUS", "SSPS", "SEAP", "SEDEC", "CGP", "SEF", "DPE", "PCMG", "SSPCM"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout.add_widget(self.sec_rg)
        
        self.nome_empresa = FocusSwitchingTextInput(hint_text="Digite o nome da empresa", multiline=False, size_hint=(0.6, 1))
        layout.add_widget(self.nome_empresa)
        
        self.cnpj = MaskedFocusSwitchingTextInput(hint_text="Digite o CNPJ da empresa", multiline=False, mask="  .   .   /    -  ", max_length=14, size_hint=(0.4, 1))
        layout.add_widget(self.cnpj)
        
        self.end_empresa = FocusSwitchingTextInput(hint_text="Digite o endereço da empresa", multiline=False, size_hint_y=1, size_hint_x=0.7)
        layout.add_widget(self.end_empresa)
        
        self.cep_empresa = MaskedFocusSwitchingTextInput(hint_text="Digite o CEP da empresa", multiline=False, mask="     -   ", max_length=8, size_hint_y=1, size_hint_x=0.3)
        layout.add_widget(self.cep_empresa)
        
        self.cid_empresa = FocusSwitchingTextInput(hint_text="Digite a cidade da empresa", multiline=False, size_hint=(0.6, 1))
        layout.add_widget(self.cid_empresa)
        
        self.est_empresa = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout.add_widget(self.est_empresa)

        self.cidade_cliente = FocusSwitchingTextInput(hint_text="Digite a cidade do cliente", multiline=False, size_hint=(0.3, 1))
        layout.add_widget(self.cidade_cliente)
        
        self.sigla_estado_cliente = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout.add_widget(self.sigla_estado_cliente)
        
        self.end_cliente = FocusSwitchingTextInput(hint_text="Digite o endereço do cliente", multiline=False, size_hint=(0.55, 1))
        layout.add_widget(self.end_cliente)
        
        self.cep_cont = MaskedFocusSwitchingTextInput(hint_text="CEP do endereço do cliente", multiline=False, mask="     -   ", max_length=8, size_hint=(0.3, 1))
        layout.add_widget(self.cep_cont)

        self.inscrita_o_spinner = Spinner(
            text='Selecione o Gênero',
            values=('Masculino', 'Feminino'),
            size_hint_y=0.1, size_hint_x=0.3
        )
        layout.add_widget(self.inscrita_o_spinner)
        
        self.nacionalidade_spinner = Spinner(
            text="Selecione a Nacionalidade",
            values=("Brasileiro", "Outro"),
            size_hint_y=0.1, size_hint_x=0.3
        )
        self.nacionalidade_spinner.bind(
            text=lambda spinner, text: on_nacionalidade_change(self, spinner, text)
        )
        layout.add_widget(self.nacionalidade_spinner)

        self.nacionalidade_input = FocusSwitchingTextInput(
            hint_text="Digite a nacionalidade",
            multiline=False,
            readonly=True,
            size_hint_y=0.18
        )
        layout.add_widget(self.nacionalidade_input)
        
        self.nome_arquivo = FocusSwitchingTextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nome_arquivo)
        
        button_layout = FloatLayout(size_hint_y=0.2)

        btn_poderes = Button(text="Continuar", size_hint=(0.2, 0.5), pos_hint={"x": 0.8, "y": 0.1})
        btn_poderes.bind(on_press=lambda instance: ir_para_processo2(self, instance))
        button_layout.add_widget(btn_poderes)
        
        btn_homepage = Button(text="Voltar para homepage", size_hint=(0.2, 0.5), pos_hint={"x": 0.0, "y": 0.1})
        btn_homepage.bind(on_press=lambda instance: ir_para_homepage(self, instance))
        button_layout.add_widget(btn_homepage)
        
        layout.add_widget(button_layout)

        self.add_widget(layout)

