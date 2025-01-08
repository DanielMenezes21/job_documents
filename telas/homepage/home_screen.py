from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Adiciona um título à tela inicial
        titulo = Label(
            text="Tela Inicial",
            font_size=30,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.8}  # Centraliza o título
        )
        layout.add_widget(titulo)

        # Campo clicável para navegar até a tela de Procuracao
        btn_procuracao = Button(
            text="Ir para Procuração",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.6},  # Ajuste na posição do botão
            on_press=self.ir_para_procuracao
        )
        layout.add_widget(btn_procuracao)

        # Campo clicável para navegar até a tela de Processo
        btn_processo = Button(
            text="Ir para Processo",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.4},  # Ajuste na posição do botão
            on_press=self.ir_para_processo
        )
        layout.add_widget(btn_processo)

        # Adiciona o layout à tela
        self.add_widget(layout)

    def ir_para_procuracao(self, instance):
        """
        Função para ir até a tela de ProcuracaoScreen
        """
        self.manager.current = "procuracao_screen"
        
    def ir_para_processo(self, instance):
        """
        Função para ir até a tela de ProcessoScreen
        """
        self.manager.current = "processo_screen"
