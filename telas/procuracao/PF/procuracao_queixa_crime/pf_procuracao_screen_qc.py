# procuracao_screen.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.uix.label import Label
from telas.procuracao.PF.procuracao_queixa_crime.pf_funcoes_procuracao_qc import on_nacionalidade_change, ir_para_poderes, ir_para_procuracao

class PFProcuracaoQCScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        
        titulo = Label(
            text="Procuração Queixa Crime PF",
            font_size=20,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.3}  # Centraliza o título
        )
        layout.add_widget(titulo)

        self.nome_outorgante = TextInput(hint_text="Digite o nome do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.nome_outorgante)

        self.cpf = TextInput(hint_text="Digite o CPF do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.cpf)
        
        self.rg = TextInput(hint_text="Digite o RG do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.rg)
        
        self.endereco = TextInput(hint_text="Digite o endereco do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.endereco)
        
        self.cep = TextInput(hint_text="Digite o cep do endereco do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.cep)
        
        self.estado_civil = TextInput(hint_text="Digite o estado civil do do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.estado_civil)

        self.cidade_outorgante_input = TextInput(hint_text="Digite a cidade do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.cidade_outorgante_input)

        self.sigla_estado_outorgante_input = TextInput(hint_text="Digite a sigla do estado do outorgante", multiline=False, size_hint_y=0.18)
        layout.add_widget(self.sigla_estado_outorgante_input)

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

        self.nacionalidade_input = TextInput(
            hint_text="Digite a nacionalidade",
            multiline=False,
            readonly=True,
            size_hint_y=0.18
        )
        layout.add_widget(self.nacionalidade_input)
        
        self.nome_arquivo_input = TextInput(hint_text="Digite o nome do arquivo", multiline=False, size_hint_y=0.18)
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
            text="Voltar para procuracao",
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
            
        