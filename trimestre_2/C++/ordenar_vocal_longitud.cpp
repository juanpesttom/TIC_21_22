#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int num_vocales(char *p)
{
    char c;
    int count = 0;
    
    while (*p != '\0')
    {
        c = tolower(*p++);
        if (c == 'a' ||
            c == 'e' ||
            c == 'i' ||
            c == 'o' ||
            c == 'u')
            count++;
    }
    return count;   
}

int main(void)
{
    int i, j;
    char *l[3];
    char buf[BUFSIZ];
    char *tmp;
    
    for (i = 0; i < 3; i++)
    {
        scanf("%s", buf);
        l[i] = (char *) malloc(strlen(buf)+1);
        strcpy(l[i], buf);
    }
    
    for (i = 1; i < 3; i++)
        for(j = 0; j < 3-i; j++)
            //if (strlen(l[j+1) < strlen[j])
            if (num_vocales(l[j+1]) < num_vocales(l[j]))
            {
                tmp = l[j];
                l[j] = l[j+1];
                l[j+1] = tmp;
            }
    for (i = 0; i < 3; i++)
        printf("%s\n", l[i]);

    return 0;
}
