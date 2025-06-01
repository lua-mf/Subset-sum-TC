import time
import csv

def subset_sum(arr, n, target):
    if target == 0:
        return True
    elif n == 0:
        return False
    elif arr[n-1] > target:
        return subset_sum(arr, n-1, target)
    else:
        return subset_sum(arr, n-1, target) or subset_sum(arr, n-1, target - arr[n-1])

def medir_execucao(arr, target, repeticoes, nome_csv):
    tempos = []
    n = len(arr)

    with open(nome_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["repeticao", "tempo_segundos"])

        for i in range(repeticoes):
            inicio = time.perf_counter()
            subset_sum(arr, n, target)
            fim = time.perf_counter()
            duracao = fim - inicio
            tempos.append(duracao)
            writer.writerow([i+1, duracao])

        media = sum(tempos) / repeticoes
        desvio = (sum([(t - media) ** 2 for t in tempos]) / repeticoes) ** 0.5

        writer.writerow([])
        writer.writerow(["Media", media])
        writer.writerow(["DesvioPadrao", desvio])

    print(f"{nome_csv} gerado: média = {media:.8f}, desvio = {desvio:.8f}")

# Exemplo para rodar
if __name__ == "__main__":
    medir_execucao([3, 34, 4, 12, 5, 2], 9, 20, "tempos_pequena_py.csv")
    medir_execucao([1, 3, 9, 2, 8, 4, 7, 10, 6, 5, 11, 13, 15], 25, 20, "tempos_media_py.csv")
    medir_execucao(list(range(1, 21)), 100, 15, "tempos_grande_py.csv")
