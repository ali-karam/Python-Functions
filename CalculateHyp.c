#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double calculateHyp(char *input1, char *input2)
{
    printf("%s\n", input1);
    double num1 = atof(input1);
    double num2 = atof(input2);

    if(num1 <= 0 || num2 <= 0){
        return -1;
    }
    printf("%f\n",sqrt(num1 * num1 + num2 * num2) );
    return sqrt(num1 * num1 + num2 * num2);
 }

