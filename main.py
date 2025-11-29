import numpy as np
import plotly.express as px
import os

# Configurações Globais
FILENAME_A = 'vetor_a.txt'
FILENAME_B = 'vetor_b.txt'
FILENAME_C = 'vetor_c.txt'

def gerar_dados_mock():
    """
    Gera dados sintéticos e salva em arquivos .txt para simular
    uma fonte de dados externa.
    """
    print("🔄 Gerando dados sintéticos...")
    vetor_a = np.linspace(10, 1000, 100)
    vetor_b = np.linspace(10, 3000, 100)
    vetor_c = np.linspace(10, 8000, 100)

    # Salvando arquivos (Simulando persistência)
    np.savetxt(FILENAME_A, vetor_a, fmt='%f', delimiter=';')
    np.savetxt(FILENAME_B, vetor_b, fmt='%f', delimiter=';')
    np.savetxt(FILENAME_C, vetor_c, fmt='%f', delimiter=';')
    print("✅ Dados gerados e salvos com sucesso.")

def carregar_e_processar():
    """
    Carrega os dados dos arquivos txt e os consolida em uma única matriz.
    """
    print("🔄 Carregando e processando dados...")
    
    # Verificação de segurança
    if not os.path.exists(FILENAME_A):
        gerar_dados_mock()

    # Load (Extract)
    try:
        array_a = np.loadtxt(FILENAME_A, dtype=np.float64, delimiter=';')
        array_b = np.loadtxt(FILENAME_B, dtype=np.float64, delimiter=';')
        array_c = np.loadtxt(FILENAME_C, dtype=np.float64, delimiter=';')

        # Transform (Stack & Transpose)
        # Empilha os arrays verticalmente e depois transpõe para formato de colunas
        matriz_final = np.vstack([array_a, array_b, array_c]).transpose()
        
        print(f"✅ Processamento concluído. Shape final: {matriz_final.shape}")
        return matriz_final
        
    except Exception as e:
        print(f"❌ Erro ao processar dados: {e}")
        return None

def visualizar_dados(dados):
    """
    Gera um gráfico interativo utilizando Plotly.
    """
    if dados is not None:
        print("📊 Gerando visualização...")
        fig = px.line(dados, title="Análise de Vetores Processados (NumPy + Plotly)")
        fig.show()
    else:
        print("⚠️ Sem dados para visualizar.")

if __name__ == "__main__":
    # Pipeline de Execução
    gerar_dados_mock()      # Passo 1: Gerar/Garantir dados
    dados = carregar_e_processar() # Passo 2: ETL
    visualizar_dados(dados) # Passo 3: Visualização
