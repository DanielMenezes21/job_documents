# procuracao_screen.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from telas.procuracao.PF.procuracao_queixa_crime.pf_funcoes_procuracao_qc import on_nacionalidade_change, ir_para_poderes, ir_para_procuracao, handle_key_down

class PFProcuracaoQCScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        self.inputs = []
        
        print("Lista inicial de inputs:")
        for i, input_field in enumerate(self.inputs):
            print(f"Input {i}: {input_field.hint_text}")

        Window.bind(on_key_down=lambda window, key, scancode, codepoint, modifiers: handle_key_down(self, window, key, scancode, codepoint, modifiers))
        
        def create_text_input(hint_text):
            input_field = TextInput(
                hint_text=hint_text,
                multiline=False,
                size_hint_y=0.18
            )

            # Capturar eventos de tecla pressionada para este campo
            def on_key_down(window, key, scancode, codepoint, modifiers):
                if key == 9:  # Código da tecla TAB
                    return True  # Bloqueia a inserção do caractere no campo
                return False

            # Vincula o evento ao TextInput
            input_field.bind(on_key_down=on_key_down)

            self.inputs.append(input_field)  # Adiciona à lista de campos
            return input_field

        # Criação dos campos de entrada com a função auxiliar
        self.nome_outorgante = create_text_input("Digite o nome do outorgante")
        layout.add_widget(self.nome_outorgante)

        self.cpf = create_text_input("Digite o CPF do outorgante")
        layout.add_widget(self.cpf)

        self.rg = create_text_input("Digite o RG do outorgante")
        layout.add_widget(self.rg)

        self.endereco = create_text_input("Digite o endereço do outorgante")
        layout.add_widget(self.endereco)

        self.cep = create_text_input("Digite o CEP do endereço do outorgante")
        layout.add_widget(self.cep)

        self.estado_civil = create_text_input("Digite o estado civil do outorgante")
        layout.add_widget(self.estado_civil)

        self.cidade_outorgante_input = create_text_input("Digite a cidade do outorgante")
        layout.add_widget(self.cidade_outorgante_input)

        self.sigla_estado_outorgante_input = create_text_input("Digite a sigla do estado do outorgante")
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

        self.nacionalidade_input = create_text_input("Digite a nacionalidade")
        self.nacionalidade_input.readonly = True
        layout.add_widget(self.nacionalidade_input)

        self.nome_arquivo_input = create_text_input("Digite o nome do arquivo")
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
        
        if self.inputs:
            self.inputs[0].focus = True

        # Adiciona tudo ao widget principal
        self.add_widget(layout)
            
        