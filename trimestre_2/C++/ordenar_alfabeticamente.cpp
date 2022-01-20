#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
            if (strcmp(l[j+1],l[j]) < 0)
            {
                tmp = l[j];
                l[j] = l[j+1];
                l[j+1] = tmp;
            }
    for (i = 0; i < 3; i++)
        printf("%s\n", l[i]);

    return 0;
}
