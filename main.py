import numpy as np
import plotly.express as px
import os

# Configurações Globais
FILENAME_A = 'vetor_a.txt'
FILENAME_B = 'vetor_b.txt'
FILENAME_C = 'vetor_c.txt'


def gerar_dados_mock():
    """Gera dados sintéticos caso os arquivos não existam."""
    print("🔄 Verificando integridade dos dados...")
    # Gera apenas se não existir, para não sobrescrever sempre
    if not os.path.exists(FILENAME_A):
        print("⚠️ Dados não encontrados. Gerando novos...")
        vetor_a = np.linspace(10, 1000, 100)
        vetor_b = np.linspace(10, 3000, 100)
        vetor_c = np.linspace(10, 8000, 100)

        np.savetxt(FILENAME_A, vetor_a, fmt='%f', delimiter=';')
        np.savetxt(FILENAME_B, vetor_b, fmt='%f', delimiter=';')
        np.savetxt(FILENAME_C, vetor_c, fmt='%f', delimiter=';')
        print("✅ Dados gerados e salvos.")
    else:
        print("✅ Dados já existentes carregados.")


def carregar_e_processar():
    """Pipeline de ETL: Carrega, Transforma e Retorna a Matriz."""
    try:
        # EXTRACT
        array_a = np.loadtxt(FILENAME_A, dtype=np.float64, delimiter=';')
        array_b = np.loadtxt(FILENAME_B, dtype=np.float64, delimiter=';')
        array_c = np.loadtxt(FILENAME_C, dtype=np.float64, delimiter=';')

        # TRANSFORM (Stack & Transpose)
        matriz_final = np.vstack([array_a, array_b, array_c]).transpose()
        print(f"✅ Processamento concluído. Shape final: {matriz_final.shape}")
        return matriz_final

    except Exception as e:
        print(f"❌ Erro crítico no processamento: {e}")
        return None


def visualizar_dados(dados):
    """Gera o gráfico e salva em HTML."""
    if dados is not None:
        print("📊 Gerando arquivo HTML...")
        fig = px.line(dados, title="Análise de Vetores Processados (ETL)")

        # Correção: Salva o arquivo e abre automaticamente (não depende de servidor)
        fig.write_html("grafico_final.html", auto_open=True)
        print("✅ Gráfico salvo como 'grafico_final.html' e aberto no navegador.")


if __name__ == "__main__":
    gerar_dados_mock()
    dados_processados = carregar_e_processar()
    visualizar_dados(dados_processados)
