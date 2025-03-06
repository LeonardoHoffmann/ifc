#include <stdio.h>

int main() {
     printf("Insira um número: ");
     int n1;
     scanf("%d", &n1);

     printf("Insira um número: ");
     int n2;
     scanf("%d", &n2);

     printf("Insira outro número: ");
     int n3;
     scanf("%d", &n3);

     printf("Insira outro número: ");
     int n4;
     scanf("%d", &n4);

     printf("Insira outro número: ");
     int n5;
     scanf("%d", &n5);

     printf("Insira outro número: ");
     int n6;
     scanf("%d", &n6);

     printf("Insira outro número: ");
     int n7;
     scanf("%d", &n7);

     printf("Insira outro número: ");
     int n8;
     scanf("%d", &n8);

     printf("Insira outro número: ");
     int n9;
     scanf("%d", &n9);

     printf("Insira um último número: ");
     int n10;
     scanf("%d", &n10);

     int soma = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10;
     int resultado = soma / 10;
     printf("A Média dos 10 números é de: %d ", resultado);

     return 0;
}
