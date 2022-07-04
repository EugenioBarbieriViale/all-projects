#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main() {
	int r = 10000;
	int x,y;
	int in=0;

	srand(time(NULL));
	for (int i=0; i<(r*r); i++) {
		int x = rand() % r;
		int y = rand() % r;
		if ((x*x+y*y)<=r*r) in++;
	}
	printf("%0.10lf\n", (double)in*4/(r*r));
}
