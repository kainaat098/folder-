#include <stdio.h>

int main() {
    int num1, num2, sum;

    // Input from user
    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    // Addition
    sum = num1 + num2;

    // Output
    printf("Sum: %d\n", sum);

    return 0;
}
