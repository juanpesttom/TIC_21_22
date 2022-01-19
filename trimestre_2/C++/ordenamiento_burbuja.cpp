#include <stdio.h>

void swap(int *p, int *q)
{
    int tmp;
    
    tmp = *p;
    *p= *q;
    *q = tmp;
}

int main(void)
{
    int i, j;
    int l[3] = {3,2,5};
    
    for (i = 1; i < 3; i++)
        for(j = 0; j < 3-i; j++)
            if (l[j+1] < l[j])
                swap(&l[i], &l[j]);
    for (i = 0; i < 3; i++)
        printf("%d\n", l[i]);

    return 0;
}
