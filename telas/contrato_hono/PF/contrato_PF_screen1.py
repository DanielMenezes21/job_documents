#processo_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.spinner import Spinner
from datetime import datetime
from telas.contrato_hono.PF.funcoes_PF_contrato_s1 import *
from logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput

class ContratoPFScreen(Screen):
    def __init__(self, **kwargs):
        super(ContratoPFScreen, self).__init__(**kwargs)
        
        self.caminho_modelo = r"10_MODELO_CONTRATACAO_PF_TESTE.docx"

        # Layout principal
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        nome_civil = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        cpf_rg_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        cid_est_CONT_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        tel_email_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)

        # Campos para entrada de dados
        self.num_contrato = FocusSwitchingTextInput(hint_text= "número do contrato", multiline=False, size_hint=(0.18, 0.18), pos_hint={"center_x": 0.5, "center_y": 0.1})
        layout.add_widget(self.num_contrato)
        
        self.nome_contratante = FocusSwitchingTextInput(hint_text="Digite o nome do contratante", multiline=False, size_hint=(0.6, 1))
        nome_civil.add_widget(self.nome_contratante)
        
        self.estado_civil = FocusSwitchingTextInput(hint_text="Digite o estado civil do contratante", multiline=False, size_hint=(0.4, 1))
        nome_civil.add_widget(self.estado_civil)
        
        layout.add_widget(nome_civil)

        self.contratante_cpf = MaskedFocusSwitchingTextInput(hint_text="Digite o CPF do contratante", multiline=False, mask="   .   .   -  ", max_length=11, size_hint_y=1, size_hint_x=0.6)
        cpf_rg_layout.add_widget(self.contratante_cpf)
        
        self.contratante_rg = FocusSwitchingTextInput(hint_text="Digite o RG do contratante", multiline=False, size_hint_y=1, size_hint_x=0.4)
        cpf_rg_layout.add_widget(self.contratante_rg)
        
        self.sec_rg = Spinner(text="SEC RG", values=("SSP", "PC", "DETRAN", "ITEP", "SESP", "SEDS", "SEJUSP", "SDS", "SEJUS", "SSPS", "SEAP", "SEDEC", "CGP", "SEF", "DPE", "PCMG", "SSPCM"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        cpf_rg_layout.add_widget(self.sec_rg)
        
        layout.add_widget(cpf_rg_layout)

        self.cidade_contratante = FocusSwitchingTextInput(hint_text="Digite a cidade do contratante", multiline=False, size_hint=(0.3, 1))
        cid_est_CONT_layout.add_widget(self.cidade_contratante)
        
        self.sigla_estado_contratante = Spinner(text="Estado", values=("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"), size_hint_y=1, size_hint_x=0.12, pos_hint={"center_x": 0.5, "center_y": 0.5})
        cid_est_CONT_layout.add_widget(self.sigla_estado_contratante)
        
        self.end_contratante = FocusSwitchingTextInput(hint_text="Digite o endereço do contratante", multiline=False, size_hint=(0.55, 1))
        cid_est_CONT_layout.add_widget(self.end_contratante)
        
        self.cep_cont = MaskedFocusSwitchingTextInput(hint_text="CEP do endereço do contratante", multiline=False, mask="     -   ", max_length=8, size_hint=(0.3, 1))
        cid_est_CONT_layout.add_widget(self.cep_cont)
        
        layout.add_widget(cid_est_CONT_layout)
        
        self.profissao = FocusSwitchingTextInput(hint_text="Digite a profissão do contratante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.profissao)
        
        self.telefone = MaskedFocusSwitchingTextInput(hint_text="Digite o telefone para contato", mask="(  )     -    ", max_length=11,multiline=False, size_hint=(0.4, 1))
        tel_email_layout.add_widget(self.telefone)
        
        self.email = FocusSwitchingTextInput(hint_text="Digite o email para contato", multiline=False, size_hint=(0.6, 1))
        tel_email_layout.add_widget(self.email)
        
        layout.add_widget(tel_email_layout)
        
        
        # Campo para selecionar o gênero
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

        # Botão para ir à tela de edição de poderes
        btn_poderes = Button(text="Continuar", size_hint=(0.2, 0.5), pos_hint={"x": 0.8, "y": 0.1})
        btn_poderes.bind(on_press=lambda instance: ir_para_processo2(self, instance))
        button_layout.add_widget(btn_poderes)
        
        btn_homepage = Button(text="Voltar para homepage", size_hint=(0.2, 0.5), pos_hint={"x": 0.0, "y": 0.1})
        btn_homepage.bind(on_press=lambda instance: ir_para_homepage(self, instance))  # Substitua "homepage" pelo ID da sua tela principal
        button_layout.add_widget(btn_homepage)
        
        layout.add_widget(button_layout)

        self.add_widget(layout)

