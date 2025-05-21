int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num = 6;
    int fact = factorial(num);
    printf("%d", fact);
    return 0;
}