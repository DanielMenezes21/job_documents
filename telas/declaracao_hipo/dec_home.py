from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Dec_homepage(Screen):
    def __init__(self, **kwargs):
        super(Dec_homepage, self).__init__(**kwargs)
        
        layout=BoxLayout(orientation="vertical", padding=50, spacing=20)
        
        titulo = Label(text="Tela de Declaração",
                       font_size=30,
                       size_hint=(None, None),
                       size=(200, 50),
                       pos_hint={"center_x": 0.5, "center_y": 0.3})
        layout.add_widget(titulo)
        
        btn_voltar = Button(
            text="<",
            size_hint=(None, None),
            size= (50,50),
            pos_hint={"x": 0.1, "y": 0.1},
            on_press=self.voltar
        )
        layout.add_widget(btn_voltar)
        
        btn_decPF = Button(text="ir para Declaração PF",
                           size_hint=(None, None),
                           size=(200, 50),
                           pos_hint={"center_x": 0.5, "top": 0.6},
                           on_press=self.declaracao_pf)
        layout.add_widget(btn_decPF)
        
        btn_decPJ = Button(text="Ir para Declaração PJ",
                           size_hint=(None, None),
                           size=(200, 50),
                           pos_hint={"center_x": 0.5, "top": 0.4},
                           on_press=self.declaracao_pj)
        layout.add_widget(btn_decPJ)
        self.add_widget(layout)
        
    def voltar(self, instance):
        """voltar

        Args:
            instance (botton): função para voltar para a tela de home_screen
        """
        
        self.manager.current = "home_screen"
        
    def declaracao_pf(self, instance):
            """Função de caminho declaração PF

            Args:
                instance (button): ir para Declaração de Pessoa Física
            """
            
            self.manager.current = "declaracao_PF"
            
    def declaracao_pj(self, instance):
        """Função de caminho declaração PJ

        Args:
            instance (button): ir para Declaração de Pessoa Jurídica
        """
        
        self.manager.current = "declaracao_PJ"