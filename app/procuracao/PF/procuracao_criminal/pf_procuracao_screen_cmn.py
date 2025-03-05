# procuracao_screen.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from app.procuracao.PF.procuracao_criminal.pf_funcoes_procuracao_cmn import *
from modules.logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput
class PFProcuracaoCriminalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.scroll = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        titulo = Label(
                    text="Procuração Pessoa Física",
                    font_size=20,
                    size_hint=(None, None),
                    size=(200, 50),
                    pos_hint={"center_x": 0.5, "center_y": 0.3}  # Centraliza o título
                )
                
        layout.add_widget(titulo)
        
        self.nome_cliente = FocusSwitchingTextInput(hint_text="Digite o nome do cliente", multiline=False, size_hint_y=None, size=(200, 50))
        layout.add_widget(self.nome_cliente)
        
        self.profissao = FocusSwitchingTextInput(hint_text="Digite a profissão do cliente", multiline=False, size_hint_y=None, size=(200, 50))
        layout.add_widget(self.profissao)

        self.cpf = MaskedFocusSwitchingTextInput(
            mask="   .   .   -  ",
            max_length=11,
            hint_text="Digite o CPF do cliente",
            multiline=False,
            size_hint_y=None,
            size_hint_x=0.6,
            size=(120, 50)
        )
        layout.add_widget(self.cpf)
        
        self.rg = FocusSwitchingTextInput(hint_text="Digite o RG do cliente", multiline=False, size_hint_y=None, size_hint_x=0.4, size=(80, 50))
        layout.add_widget(self.rg)
        
        self.sec_rg = Spinner(text="SEC RG", values=("SSP", "PC", "DETRAN", "ITEP", "SESP", "SEDS", "SEJUSP", "SDS", "SEJUS", "SSPS", "SEAP", "SEDEC", "CGP", "SEF", "DPE", "PCMG", "SSPCM"), size_hint_y=None, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5}, size=(30, 50))
        layout.add_widget(self.sec_rg)
        
        self.est_rg = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=None, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5}, size=(30, 50))
        layout.add_widget(self.est_rg)
        
        self.endereco = FocusSwitchingTextInput(hint_text="Digite o endereco do cliente", multiline=False, size_hint_y=None, size_hint_x=0.7, size=(120, 50))
        layout.add_widget(self.endereco)
        
        self.cep = MaskedFocusSwitchingTextInput(hint_text="Digite o cep do cliente",
                                                 max_length=8,
                                                 mask="     -   ",
                                                 multiline=False,
                                                 size_hint_y=None,
                                                 size_hint_x=0.3,
                                                 size=(80, 50))
        layout.add_widget(self.cep)

        self.estado_civil = FocusSwitchingTextInput(hint_text="Digite o estado civil do do cliente", multiline=False, size_hint_y=None, size=(120, 50))
        layout.add_widget(self.estado_civil)

        self.cidade_cliente_input = FocusSwitchingTextInput(hint_text="Digite a cidade do cliente", multiline=False, size_hint=(1, None), size=(120, 50))
        layout.add_widget(self.cidade_cliente_input)

        self.sigla_estado_cliente_input = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=None, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5}, size=(30, 50))
        layout.add_widget(self.sigla_estado_cliente_input)

        self.nacionalidade_spinner = Spinner(
            text="Selecione a Nacionalidade",
            values=("Brasileiro", "Outro"),
            size_hint_y=None, size_hint_x=0.3, size=(50, 50)
        )
        self.nacionalidade_spinner.bind(
            text=lambda spinner, text: on_nacionalidade_change(self, spinner, text)
        )
        layout.add_widget(self.nacionalidade_spinner)
        
        self.inscrita_o_spinner = Spinner(
            text='Selecione o Gênero',
            values=('Masculino', 'Feminino'),
            size_hint_y=None, size_hint_x=0.3, size=(50, 50)
        )
        layout.add_widget(self.inscrita_o_spinner)

        self.nacionalidade_input = FocusSwitchingTextInput(
            hint_text="Digite a nacionalidade",
            multiline=False,
            readonly=True,
            size_hint_y=None,
            size=(100, 50)
        )
        layout.add_widget(self.nacionalidade_input)
        
        self.nome_arquivo_input = FocusSwitchingTextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint_y=None, size=(120, 50))
        layout.add_widget(self.nome_arquivo_input)
        
        button_layout = FloatLayout(size_hint_y=None)

        btn_poderes = Button(
            text="Editar Poderes",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"x": 0.75, "y": 0.1}
        )
        btn_poderes.bind(on_press=lambda instance: ir_para_poderes(self, instance))
        button_layout.add_widget(btn_poderes)

        btn_homepage = Button(
            text="Voltar para procuração",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"x": 0.05, "y": 0.1}
        )
        btn_homepage.bind(on_press=lambda instance: ir_para_procuracao(self, instance))
        button_layout.add_widget(btn_homepage)

        layout.add_widget(button_layout)
        self.scroll.add_widget(layout)

        self.add_widget(self.scroll)
