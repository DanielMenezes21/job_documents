# funcoes_procuracao.py
from app.procuracao.PF.procuracao_criminal.pf_funcoes_poderes_cmn import *
from app.procuracao.PF.procuracao_criminal.pf_poderes_screen_cmn import PFPoderesCriminalScreen
from datetime import datetime
from modules.logic_tab import FocusSwitchingTextInput

def on_nacionalidade_change(screen_instance, spinner, text):
    if text == "Outro":
        screen_instance.nacionalidade_input.text = ""
        screen_instance.nacionalidade_input.readonly = False
    else:
        inscrita_o = screen_instance.inscrita_o_spinner.text
        if inscrita_o == "Feminino":
            screen_instance.nacionalidade_input.text = "brasileira"
            screen_instance.inscrita_o_spinner.text = "inscrita"
        else:
            screen_instance.nacionalidade_input.text = "brasileiro"
            screen_instance.inscrita_o_spinner.text = "inscrito"
        screen_instance.nacionalidade_input.readonly = True
        
def ir_para_procuracao(self, instance):
    
    self.manager.current =  "home_procuracao_screen"

def obter_dados(screen_instance):
    try:
        caminho_modelo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..","..", "assets", "11_PROCURACAO_TESTE.docx"))
        caminho_declaracao = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..","..", "assets", "13_DECLARACAO_HIPOSSUFICIENCIA_PF_TESTE.docx"))

        
        if not os.path.exists(caminho_modelo):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_modelo}")
        if not os.path.exists(caminho_declaracao):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_declaracao}")
        # Gerar a data formatada
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")  # Debug para confirmar a data
        
        print(caminho_modelo)

        dados = {
            "caminho_modelo": caminho_modelo,
            "caminho_declaracao": caminho_declaracao,
            "nome_cliente": screen_instance.nome_cliente.text,
            "profissao":screen_instance.profissao.text,
            "sec_rg":screen_instance.sec_rg.text,
            "est_rg": screen_instance.est_rg.text,
            "cpf": screen_instance.cpf.text,
            "rg": screen_instance.rg.text,
            "cidade_cliente": screen_instance.cidade_cliente_input.text,
            "sigla_estado_cliente": screen_instance.sigla_estado_cliente_input.text,
            "inscrita_o": screen_instance.inscrita_o_spinner.text,
            "nacionalidade": screen_instance.nacionalidade_input.text,
            "nome_arquivo": screen_instance.nome_arquivo_input.text,
            "endereco": screen_instance.endereco.text,
            "estado_civil": screen_instance.estado_civil.text,
            "cep": screen_instance.cep.text,
            "data_agora": data_agora,
        }

        print(f"Dados coletados: {dados}")  # Verificar todos os dados coletados
        return dados

    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return None
def popup(screen_instance, titulo, mensagem):
    conteudo = BoxLayout(orientation='vertical', padding=10, spacing=10)
    conteudo.add_widget(Label(text=mensagem, halign='center'))
    btn_fechar = Button(text='Fechar', size_hint=(1, 0.3))
    btn_fechar.bind(on_press=lambda instance: popup.dismiss())
    
    conteudo.add_widget(btn_fechar)
    popup = Popup(title=titulo, content=conteudo, size_hint=(0.7, 0.5))
    popup.open()
    
def ir_para_poderes(screen_instance, instance):
    """
    Navega para a tela PoderesScreen e envia os dados coletados.
    """
    dados = obter_dados(screen_instance)
    if dados:
        if len(screen_instance.nome_arquivo_input.text) == 0:
            popup(screen_instance, "Erro", "o campo nome do arquivo é obrigatório")
        else:
            poderes_screen = screen_instance.manager.get_screen("poderes_criminal_screen_PF")
            poderes_screen.poderes_atualizar_dados(dados)  # Certifique-se de que o nome corresponde
            screen_instance.manager.current = "poderes_criminal_screen_PF"

