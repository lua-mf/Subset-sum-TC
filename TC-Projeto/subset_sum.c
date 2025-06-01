#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

bool subsetSum(int arr[], int n, int target) {
    if (target == 0)
        return true;
    else if (n == 0)
        return false;
    else if (arr[n-1] > target)
        return subsetSum(arr, n-1, target);
    else
        return subsetSum(arr, n-1, target) ||
               subsetSum(arr, n-1, target - arr[n-1]);
}

double tempo_em_segundos(struct timespec inicio, struct timespec fim) {
    return (fim.tv_sec - inicio.tv_sec) + (fim.tv_nsec - inicio.tv_nsec) / 1e9;
}

void medirExecucao(int arr[], int n, int target, int repeticoes, const char *descricao, const char *nomeCSV) {
    double tempos[repeticoes];
    struct timespec inicio, fim;

    FILE *csv = fopen(nomeCSV, "w");
    if (!csv) {
        printf("Erro ao abrir arquivo %s\n", nomeCSV);
        return;
    }

    fprintf(csv, "repeticao,tempo_segundos\n");

    for (int i = 0; i < repeticoes; i++) {
        clock_gettime(CLOCK_MONOTONIC, &inicio);
        subsetSum(arr, n, target);
        clock_gettime(CLOCK_MONOTONIC, &fim);
        tempos[i] = tempo_em_segundos(inicio, fim);
        fprintf(csv, "%d,%.8f\n", i + 1, tempos[i]);
    }

    double soma = 0;
    for (int i = 0; i < repeticoes; i++)
        soma += tempos[i];
    double media = soma / repeticoes;

    double desvio = 0;
    for (int i = 0; i < repeticoes; i++)
        desvio += (tempos[i] - media) * (tempos[i] - media);
    desvio = sqrt(desvio / repeticoes);

    fprintf(csv, "\nMedia,%.8f\n", media);
    fprintf(csv, "DesvioPadrao,%.8f\n", desvio);
    fclose(csv);

    printf("\nEntrada: %s\n", descricao);
    printf("Repetições: %d\n", repeticoes);
    printf("Tempo médio: %.8f segundos\n", media);
    printf("Desvio padrão: %.8f segundos\n", desvio);
    printf("Arquivo salvo: %s\n", nomeCSV);
}

int main() {
    int arr1[] = {3, 34, 4, 12, 5, 2};
    int n1 = sizeof(arr1)/sizeof(arr1[0]);
    medirExecucao(arr1, n1, 9, 20, "Pequena (6 elementos)", "tempos_pequena_c.csv");

    int arr2[] = {1, 3, 9, 2, 8, 4, 7, 10, 6, 5, 11, 13, 15};
    int n2 = sizeof(arr2)/sizeof(arr2[0]);
    medirExecucao(arr2, n2, 25, 20, "Média (13 elementos)", "tempos_media_c.csv");

    int arr3[20];
    for (int i = 0; i < 20; i++) arr3[i] = i + 1;
    medirExecucao(arr3, 20, 100, 15, "Grande (20 elementos)", "tempos_grande_c.csv");

    return 0;
}
