from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from telas.declaracao_hipo.PF.funcoes_declaracao_PF import *
from logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput

class DadosPessoaisPFScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        cpf_rg_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        end_cep_laytout = BoxLayout(orientation="horizontal", size_hint_y = 0.18)
        cid_est_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
                
        titulo = Label(text="Declaração Hipossuficiencia de Pessoa Física", 
                       font_size=15,
                       size_hint=(None,None),
                       size=(200, 50),
                       pos_hint={"center_x": 0.5, "center_y": 0.3})
        
        layout.add_widget(titulo)
        
        self.nome_outorgante = FocusSwitchingTextInput(hint_text="Digite o nome do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nome_outorgante)
        
        self.nacionalidade = FocusSwitchingTextInput(hint_text="Digite a nacionalidade", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nacionalidade)
        
        self.estado_civil = FocusSwitchingTextInput(hint_text="Digite o estado civil do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.estado_civil)
        
        self.profissao = FocusSwitchingTextInput(hint_text="Digite a profissão", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.profissao)
        
        self.cpf = MaskedFocusSwitchingTextInput(hint_text="Digite o CPf do outorgante", mask="   .   .   -  ", max_length=11, multiline=False, size_hint=(0.5, 1))
        cpf_rg_layout.add_widget(self.cpf)
        
        self.rg = FocusSwitchingTextInput(hint_text="informe o RG do outorgante", multiline=False, size_hint=(0.15, 1))
        cpf_rg_layout.add_widget(self.rg)
        
        self.est_rg = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=1, size_hint_x=0.15, pos_hint={"center_x": 0.5, "center_y": 0.5})
        cpf_rg_layout.add_widget(self.est_rg)
        
        self.sec_rg = Spinner(text= "SEC_RG", values=("SSP", "PC", "DETRAN", "ITEP", "SESP", "SEDS", "SEJUSP", "SDS", "SEJUS", "SSPS", "SEAP", "SEDEC", "CGP", "SEF", "DPE", "PCMG", "SSPCM"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        cpf_rg_layout.add_widget(self.sec_rg)
        
        layout.add_widget(cpf_rg_layout)
        
        self.endereco = FocusSwitchingTextInput(hint_text="Digite o endereço do outorgado", multiline=False, size_hint=(0.55, 1))
        end_cep_laytout.add_widget(self.endereco)
        
        self.cep = MaskedFocusSwitchingTextInput(hint_text="Digite o CEP do outorgante", mask="     -  ", max_length=8, multiline=False, size_hint=(0.25, 1))
        end_cep_laytout.add_widget(self.cep)
        
        layout.add_widget(end_cep_laytout)
        
        self.cidade = FocusSwitchingTextInput(hint_text="Digite a cidade do outorgante", multiline=False, size_hint=(0.7, 1))
        cid_est_layout.add_widget(self.cidade)
        
        self.estado = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        cid_est_layout.add_widget(self.estado)
        
        layout.add_widget(cid_est_layout)
        
        self.nome_arquivo = FocusSwitchingTextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nome_arquivo)
        
        button_layout = FloatLayout(size_hint_y=0.2)
        
        self.btn_homepage = Button(text="voltar para homepage", 
                                   size_hint=(None, None), 
                                   size=(150, 50), 
                                   pos_hint={"x": 0.15, "y": 0.1})
        self.btn_homepage.bind(on_press= lambda instance:ir_para_home_dec(self, instance))
        button_layout.add_widget(self.btn_homepage)
        
        self.btn_salvar = Button(text="salvar",
                                 size_hint=(None, None),
                                 size=(150,50),
                                 pos_hint={"x": 0.75, "y": 0.1})
        self.btn_salvar.bind(on_press= self.salvar_doc)
        button_layout.add_widget(self.btn_salvar)
        
        layout.add_widget(button_layout)
        
        self.add_widget(layout)
        
    def salvar_doc(self, instance):
        obter_dados(self, self)