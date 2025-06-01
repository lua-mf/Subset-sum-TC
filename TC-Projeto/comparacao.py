import pandas as pd
import matplotlib.pyplot as plt

# Extrai a Media ou desvio padrão do CSV
def extrair_valor(caminho, chave):
    try:
        df = pd.read_csv(caminho, skip_blank_lines=True, encoding="latin1")
        if df.empty:
            print(f"[ERRO] Arquivo {caminho} está vazio.")
            return None

        # Localiza a linha com a chave ("Media" ou "DesvioPadrao")
        for i, row in df.iterrows():
            if str(row[0]).strip().lower() == chave.lower():
                return float(row[1])
        print(f"[ERRO] '{chave}' não encontrado em {caminho}.")
        return None

    except Exception as e:
        print(f"[ERRO] ao ler {caminho}: {e}")
        return None

# Tamanhos das entradas
entradas = [6, 13, 20]

# Tempos médios
tempos_c = [
    extrair_valor("TC-Projeto/output/tempos_pequena_c.csv", "Media"),
    extrair_valor("TC-Projeto/output/tempos_media_c.csv", "Media"),
    extrair_valor("TC-Projeto/output/tempos_grande_c.csv", "Media"),
]

tempos_py = [
    extrair_valor("tempos_pequena_py.csv", "Media"),
    extrair_valor("tempos_media_py.csv", "Media"),
    extrair_valor("tempos_grande_py.csv", "Media"),
]

# Desvios padrão
desvios_c = [
    extrair_valor("TC-Projeto/output/tempos_pequena_c.csv", "DesvioPadrao"),
    extrair_valor("TC-Projeto/output/tempos_media_c.csv", "DesvioPadrao"),
    extrair_valor("TC-Projeto/output/tempos_grande_c.csv", "DesvioPadrao"),
]

desvios_py = [
    extrair_valor("tempos_pequena_py.csv", "DesvioPadrao"),
    extrair_valor("tempos_media_py.csv", "DesvioPadrao"),
    extrair_valor("tempos_grande_py.csv", "DesvioPadrao"),
]

# Gráfico 1: Tempo médio
plt.figure(figsize=(10, 6))
plt.plot(entradas, tempos_c, marker='o', label="C")
plt.plot(entradas, tempos_py, marker='x', label="Python")
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Tempo médio (segundos)")
plt.title("Comparação de desempenho - C vs Python")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Gráfico 2: Desvio padrão
plt.figure(figsize=(10, 6))
plt.plot(entradas, desvios_c, marker='o', label="C")
plt.plot(entradas, desvios_py, marker='x', label="Python")
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Desvio padrão (segundos)")
plt.title("Comparação de variação (desvio padrão) - C vs Python")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
