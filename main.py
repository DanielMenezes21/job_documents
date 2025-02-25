from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from app.login_cadastro.login_page import LoginPage
from app.login_cadastro.register_page import RegisterPage
from app.contrato_hono.PJ.contrato_PJ_screen1 import ProcessoScreen
from app.contrato_hono.PJ.contrato_PJ_screen2 import Processo2Screen
from app.contrato_hono.home_contrato_screen import HomeContratoScreen
from app.contrato_hono.PF.contrato_PF_screen1 import ContratoPFScreen
from app.contrato_hono.PF.contrato_PF_screen2 import ContratoPF2Screen
from app.homepage.home_screen import HomeScreen
from app.procuracao.PF.procuracao_criminal.pf_procuracao_screen_cmn import PFProcuracaoCriminalScreen
from app.procuracao.PF.procuracao_criminal.pf_poderes_screen_cmn import PFPoderesCriminalScreen
from app.procuracao.home_procuracao_screen import HomeProcuracaoScreen
from app.procuracao.PJ.procuracao_criminal.pj_procuracao_screen_cmn import ProcuracaoCriminalPJScreen
from app.procuracao.PJ.procuracao_criminal.pj_poderes_screen_cmn import PoderesCriminalPJScreen
from app.declaracao_hipo.PF.dados_pessoais_screen_dec import DadosPessoaisPFScreen
from app.declaracao_hipo.PJ.dados_pessoais_PJ_screen_dec import DadosPessoaisPJScreen
from app.declaracao_hipo.dec_home import Dec_homepage

from updater import check_for_updates
class MyApp(ScreenManager): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Adiciona as telas ao ScreenManager
        self.add_widget(LoginPage(name="login_page"))
        self.add_widget(RegisterPage(name="register_page"))
        self.add_widget(HomeScreen(name="home_screen"))
        self.add_widget(HomeContratoScreen(name="home_contrato_screen"))
        self.add_widget(ProcessoScreen(name="contrato_screen1"))
        self.add_widget(Processo2Screen(name="contrato_screen2"))
        self.add_widget(ContratoPFScreen(name="contrato_PF_screen1"))
        self.add_widget(ContratoPF2Screen(name="contrato_PF_screen2"))
        self.add_widget(PFProcuracaoCriminalScreen(name="procuracao_criminal_screen_PF"))
        self.add_widget(PFPoderesCriminalScreen(name="poderes_criminal_screen_PF"))
        self.add_widget(HomeProcuracaoScreen(name="home_procuracao_screen"))
        self.add_widget(ProcuracaoCriminalPJScreen(name="procuracao_criminal_pj_screen"))
        self.add_widget(PoderesCriminalPJScreen(name="poderes_criminal_pj_screen"))
        self.add_widget(Dec_homepage(name="homepage_declaracao"))
        self.add_widget(DadosPessoaisPFScreen(name="declaracao_PF"))
        self.add_widget(DadosPessoaisPJScreen(name="declaracao_PJ"))
        
class MainApp(App):
    def build(self):
        # Retorna o ScreenManager configurado
        return MyApp()
 


if __name__ == "__main__":
    MainApp().run()
