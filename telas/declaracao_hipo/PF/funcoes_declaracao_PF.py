from telas.declaracao_hipo.PF.extracao_dec import *
import os
from datetime import datetime

def ir_para_home_dec(self, instance):
    
    self.manager.current =  "home_procuracao_screen"
def obter_dados(screen_instance):
    try:

        caminho_declaracao = os.path.join(os.path.dirname(__file__), "13_DECLARACAO_HIPOSSUFICIENCIA_PF_TESTE.docx")
        
        if not os.path.exists(caminho_declaracao):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_declaracao}")
        # Gerar a data formatada
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")  # Debug para confirmar a data
        
        print(caminho_declaracao)

        dados = {
            "caminho_modelo": caminho_declaracao,
            "caminho_declaracao": caminho_declaracao,
            "nome_outorgante": screen_instance.nome_outorgante.text,
            "profissao":screen_instance.profissao.text,
            "sec_rg":screen_instance.sec_rg.text,
            "est_rg": screen_instance.est_rg.text,
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
        poderes_screen = screen_instance.manager.get_screen("poderes_criminal_screen_PF")
        poderes_screen.poderes_atualizar_dados(dados)  # Certifique-se de que o nome corresponde
        screen_instance.manager.current = "poderes_criminal_screen_PF"