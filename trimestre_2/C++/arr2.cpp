#include <stdio.h>

int main()
{
    char arr[5];
    int i;
    
    for (i = 0; i < 5; i++)
    {
        printf("Introduce la letra %d: ", i);
        scanf(" %c", &arr[i]);
    }
    while (i >= 0)
    {
        printf("%c", arr[i--]);
    }
    printf("\n");
    return 0;
}   
