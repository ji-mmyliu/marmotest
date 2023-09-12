#include <stdio.h>

int main() {
	int Q, A, M;
	scanf("%d %d %d", &Q, &A, &M);
	double F1 = (5000.0 - 5 * Q - 20 * A - 30 * M) / 45;
	double F2 = (3750.0 - 30 * M) / 45;
	double Fm = F1 > F2 ? F1 : F2;
	printf("%d\n", (int)Fm);
}