# procuracao_screen.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.uix.label import Label
from telas.procuracao.PJ.procuracao_queixa_crime.pj_funcoes_procuracao_qc import *
from logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput
class ProcuracaoQCPJScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
         # Area layout
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        cnpj_layout=BoxLayout(orientation="horizontal", size_hint_y=0.18)
        cpf_rg_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        cep_end_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        empresa_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        cidade_estado_layout = BoxLayout(orientation="horizontal", size_hint_y=0.18)
        
        titulo = Label(
            text="Procuração Queixa Crime PJ",
            font_size=20,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.3}  # Centraliza o título
        )
        layout.add_widget(titulo)

        # Criação dos campos de entrada com a função auxiliar
        self.nome_outorgante = FocusSwitchingTextInput(hint_text="Digite o nome do outorgante", 
                                         multiline=False,
                                         size_hint_y=0.18)
        layout.add_widget(self.nome_outorgante)
        
        self.nome_empresa = FocusSwitchingTextInput(hint_text="Digite o nome da empresa",
                                      multiline=False,
                                      size_hint_y=1,
                                      size_hint_x=1)
        cnpj_layout.add_widget(self.nome_empresa)
        
        self.cnpj = MaskedFocusSwitchingTextInput(
            mask="  .   .   /    -  ",  
            max_length=14,
            hint_text="Digite o CNPJ da empresa",
            multiline=False,
            size_hint_y=1,
            size_hint_x=1,
        )
        cnpj_layout.add_widget(self.cnpj)
        
        layout.add_widget(cnpj_layout)
        
        self.end_empresa = FocusSwitchingTextInput(hint_text = "Informe o endereço da empresa",
                                     multiline=False,
                                     size_hint_y=1,
                                     size_hint_x=1)
        empresa_layout.add_widget(self.end_empresa)
        
        self.cep_empresa = MaskedFocusSwitchingTextInput(hint_text="Informe o CEP da empresa",
                                                         max_length=8,
                                                         multiline=False,
                                                         size_hint_y=1,
                                                         size_hint_x=1,
                                                         mask="     -   ")
        empresa_layout.add_widget(self.cep_empresa)
        
        layout.add_widget(empresa_layout)

        self.cpf = MaskedFocusSwitchingTextInput(
            mask="   .   .   -  ",
            max_length=11,
            hint_text="Digite o CPF do outorgante",
            multiline=False,
            size_hint_y=1,
            size_hint_x=1,
        )
        cpf_rg_layout.add_widget(self.cpf)
        
        self.rg = FocusSwitchingTextInput(hint_text="Digite o RG do outorgante",
                            multiline=False,
                            size_hint_y=1,
                            size_hint_x=0.6,)
        cpf_rg_layout.add_widget(self.rg)
        
        # Adiciona o cpf_rg_layout
        layout.add_widget(cpf_rg_layout)
        
        self.endereco = FocusSwitchingTextInput(hint_text="Digite o endereco do outorgante",
                                  multiline=False, 
                                  size_hint_y=1,
                                  size_hint_x=1)
        cep_end_layout.add_widget(self.endereco)
        
        self.cep = MaskedFocusSwitchingTextInput(hint_text="Digite o cep do outorgante",
                                                 max_length=8,
                                                 mask="     -   ",
                                                 multiline=False,
                                                 size_hint_y=1,
                                                 size_hint_x=0.7,)
        cep_end_layout.add_widget(self.cep)
        
        layout.add_widget(cep_end_layout)
        
        self.cidade_outorgante_input = FocusSwitchingTextInput(hint_text="Digite a cidade do outorgante",
                             multiline=False, 
                             size_hint_y=1,
                             size_hint_x=1)
        cidade_estado_layout.add_widget(self.cidade_outorgante_input)
        
        self.sigla_estado_outorgante_input= FocusSwitchingTextInput(hint_text="Digite a sigla do estado do outorgante",
                             multiline=False, 
                             size_hint_y=1,
                             size_hint_x=1)
        cidade_estado_layout.add_widget(self.sigla_estado_outorgante_input)
        
        layout.add_widget(cidade_estado_layout)
        
        self.estado_civil= FocusSwitchingTextInput(hint_text="Digite o estado civil",
                             multiline=False, 
                             size_hint_y=0.18)
        layout.add_widget(self.estado_civil)
        
        self.nacionalidade_spinner = Spinner(
            text="Selecione a Nacionalidade",
            values=("Brasileiro", "Outro"),
            size_hint_y=0.1, size_hint_x=0.3
        )
        self.nacionalidade_spinner.bind(
            text=lambda spinner, text: on_nacionalidade_change(self, spinner, text)
        )
        layout.add_widget(self.nacionalidade_spinner)
        
        self.inscrita_o_spinner = Spinner(
            text='Selecione o Gênero',
            values=('Masculino', 'Feminino'),
            size_hint_y=0.1, size_hint_x=0.3
        )
        layout.add_widget(self.inscrita_o_spinner)

        self.nacionalidade_input = FocusSwitchingTextInput(
            hint_text="Digite a nacionalidade",
            multiline=False,
            readonly=True,
            size_hint_y=0.18
        )
        layout.add_widget(self.nacionalidade_input)
        
        self.nome_arquivo_input = FocusSwitchingTextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nome_arquivo_input)
        
        button_layout = FloatLayout(size_hint_y=0.2)

        # Botão para editar poderes (canto inferior direito)
        btn_poderes = Button(
            text="Editar Poderes",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"x": 0.75, "y": 0.1}
        )
        btn_poderes.bind(on_press=lambda instance: ir_para_poderes(self, instance))
        button_layout.add_widget(btn_poderes)

        # Botão para voltar para a homepage (canto inferior esquerdo)
        btn_homepage = Button(
            text="Voltar para procuração",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"x": 0.05, "y": 0.1}
        )
        btn_homepage.bind(on_press=lambda instance: ir_para_procuracao(self, instance))
        button_layout.add_widget(btn_homepage)

        # Adiciona o layout dos botões ao layout principal
        layout.add_widget(button_layout)

        # Adiciona tudo ao widget principal
        self.add_widget(layout)

            
        