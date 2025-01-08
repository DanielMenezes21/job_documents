# funcoes_procuracao.py
from telas.procuracao.procuracao_criminal.funcoes_poderes_cmn import *
from telas.procuracao.procuracao_criminal.poderes_screen_cmn import PoderesScreen
from datetime import datetime

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

def ir_para_homepage(self, instance):
    
    self.manager.current =  "home_screen"

def obter_dados(screen_instance):
    try:
        caminho_modelo = os.path.join(os.path.dirname(__file__), "11_PROCURACAO_TESTE.docx")
        
        if not os.path.exists(caminho_modelo):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_modelo}")
        # Gerar a data formatada
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")  # Debug para confirmar a data
        
        print(caminho_modelo)

        dados = {
            "caminho_modelo": caminho_modelo,
            "nome_outorgante": screen_instance.nome_outorgante.text,
            "cpf": screen_instance.cpf.text,
            "rg": screen_instance.rg.text,
            "cidade_outorgante": screen_instance.cidade_outorgante_input.text,
            "sigla_estado_outorgante": screen_instance.sigla_estado_outorgante_input.text,
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

def ir_para_poderes(screen_instance, instance):
    """
    Navega para a tela PoderesScreen e envia os dados coletados.
    """
    dados = obter_dados(screen_instance)
    if dados:
        poderes_screen = screen_instance.manager.get_screen("poderes_screen")
        poderes_screen.poderes_atualizar_dados(dados)  # Certifique-se de que o nome corresponde
        screen_instance.manager.current = "poderes_screen"

