#include <stdio.h>

int main()
{
    int arr[10];
    int i, suma = 0;
    float media;
    
    for (i = 0; i < 10; i++)
    {
        printf("Dame un numero: ");
        scanf("%d", &arr[i]);
    }
    for (i = 0; i < 10; i++)
    {
        printf("%d\n", arr[i]);
        suma += arr[i];
    }
    media = suma/10.0;
    printf("La media vale: %f\n", media);
    
    return 0;
}
