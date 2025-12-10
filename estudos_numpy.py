import numpy as np
import time


# ==========================================
# 🧪 ARQUIVO DE ESTUDO E PERFORMANCE
# ==========================================
# Objetivo: Demonstrar a superioridade do NumPy sobre listas nativas

def testar_performance():
    print("--- 1. Comparativo de Performance (Listas vs NumPy) ---")
    tamanho = 10_000_000  # 10 milhões

    # Teste com Lista Nativa (Usando perf_counter para alta precisão)
    start_time = time.perf_counter()
    lista = [0] * tamanho
    end_time = time.perf_counter()
    tempo_lista = end_time - start_time
    print(f'Criação de LISTA python: {tempo_lista:.6f} segundos')

    # Teste com NumPy
    start_time = time.perf_counter()
    ndarray = np.zeros(tamanho)
    end_time = time.perf_counter()
    tempo_numpy = end_time - start_time
    print(f'Criação de ARRAY NumPy:  {tempo_numpy:.6f} segundos')

    # Proteção contra divisão por zero (caso o NumPy seja rápido demais)
    if tempo_numpy > 0:
        print(f"🚀 Conclusão: NumPy foi {tempo_lista / tempo_numpy:.2f}x mais rápido.\n")
    else:
        print("🚀 Conclusão: NumPy foi instantâneo (rápido demais para medir!)\n")


def testar_funcionalidades():
    print("--- 2. Manipulação de Matrizes e Ordenação ---")
    rng = np.random.default_rng()

    # Criando matriz 4x4
    matriz = rng.random([4, 4])
    print(f'Matriz Original:\n{matriz}\n')

    # Ordenando
    m_coluna = np.sort(matriz, axis=0)
    print(f'Ordenada por coluna:\n{m_coluna}')


if __name__ == "__main__":
    testar_performance()
    testar_funcionalidades()
