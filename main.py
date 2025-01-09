#main.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from telas.contrato_hono.contrato_screen1 import ProcessoScreen
from telas.contrato_hono.contrato_screen2 import Processo2Screen
from telas.procuracao.PF.procuracao_queixa_crime.pf_poderes_screen_qc import PFPoderesQCScreen
from telas.homepage.home_screen import HomeScreen
from telas.procuracao.PF.procuracao_queixa_crime.pf_procuracao_screen_qc import PFProcuracaoQCScreen
from telas.procuracao.PF.procuracao_criminal.pf_procuracao_screen_cmn import PFProcuracaoCriminalScreen
from telas.procuracao.PF.procuracao_criminal.pf_poderes_screen_cmn import PFPoderesCriminalScreen
from telas.procuracao.home_procuracao_screen import HomeProcuracaoScreen
from telas.procuracao.PF.home_procuracao_screen_PF import HomeProcuracaoPFScreen
from telas.procuracao.PJ.home_procuracao_screen_PJ import HomeProcuracaoPJScreen
from telas.procuracao.PJ.procuracao_queixa_crime.pj_poderes_screen_qc import PoderesQCPJScreen
from telas.procuracao.PJ.procuracao_queixa_crime.pj_procuracao_screen_qc import ProcuracaoQCPJScreen
from telas.procuracao.PJ.procuracao_criminal.pj_procuracao_screen_cmn import ProcuracaoCriminalPJScreen
from telas.procuracao.PJ.procuracao_criminal.pj_poderes_screen_cmn import PoderesCriminalPJScreen

class MyApp(ScreenManager): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Adiciona as telas ao ScreenManager
        self.add_widget(HomeScreen(name="home_screen"))
        self.add_widget(PFPoderesQCScreen(name="poderes_queixa_crime_screen_PF"))
        self.add_widget(ProcessoScreen(name="contrato_screen1"))
        self.add_widget(Processo2Screen(name="contrato_screen2"))
        self.add_widget(PFProcuracaoQCScreen(name="procuracao_screen_queixa_crime_PF"))
        self.add_widget(PFProcuracaoCriminalScreen(name="procuracao_criminal_screen_PF"))
        self.add_widget(PFPoderesCriminalScreen(name="poderes_criminal_screen_PF"))
        self.add_widget(HomeProcuracaoScreen(name="home_procuracao_screen"))
        self.add_widget(HomeProcuracaoPFScreen(name="home_procuracao_screen_PF"))
        self.add_widget(HomeProcuracaoPJScreen(name="home_procuracao_screen_PJ"))
        self.add_widget(ProcuracaoQCPJScreen(name="procuracao_queixa_crime_pj_screen"))
        self.add_widget(PoderesQCPJScreen(name="poderes_queixa_crime_pj_screen"))
        self.add_widget(ProcuracaoCriminalPJScreen(name="procuracao_criminal_pj_screen"))
        self.add_widget(PoderesCriminalPJScreen(name="poderes_criminal_pj_screen"))
        
class MainApp(App):
    def build(self):
        # Retorna o ScreenManager configurado
        return MyApp()


if __name__ == "__main__":
    MainApp().run()
