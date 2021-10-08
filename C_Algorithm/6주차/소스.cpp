
/*Program that times Binomial function calls*/
#include <time.h>
#include <iostream>
using namespace std;

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_VERTICES 5
#define INF 1000L

int B[101][101];

//Recursive binomial
int bino_rec(int n, int k) {
	//아래를 완성하시오
	if (k == 0 || n == k)
		return 1;
	else
		return bino_rec(n - 1, k - 1) + bino_rec(n - 1, k);
}

//Dynamic programming binomial
int bino_dyn(int n, int k) {
	int min;

	for (int i = 0; i <= n; i++) {
		if (i < k) min = i;
		else min = k;
		//아래를 완성하시오
		for (int j = 0; j <= min; j++) {
			if (j == 0 || j == i)
				B[i][j] = 1;
			else 
				B[i][j] = B[i - 1][j - 1] + B[i - 1][j];

		}
	}
	return B[n][k];
}

int main() {
	printf("binomail coefficient\n");
	time_t begin, end;

	int N, k;
	cout << ("Enter positive integer N(<=100): ");
	cin >> N;
	cout << ("Enter positive integer k(<=100): ");
	cin >> k;
	begin = time(NULL);
	cout << "Binomial recursive     : " << bino_rec(N, k) << endl;
	end = time(NULL);
	cout << "\ttime = " << difftime(end, begin) << " s" << endl;

	begin = time(NULL);
	cout << "Fibonacci dynamic prog.: " << bino_dyn(N, k) << endl;
	end = time(NULL);
	cout << "\ttime = " << difftime(end, begin) << " s" << endl << endl;

	printf("floyd shortest path\n");
	typedef struct GraphType {
		int n;	// 정점의 개수
		int W[MAX_VERTICES][MAX_VERTICES];
	} GraphType;

	GraphType g = { 5,
		{{ 0, 1, INF, 1, 5 },
		{ 9,  0, 3, 2, INF },
		{ INF, INF, 0, 4, INF },
		{ INF, INF, 2, 0, 3  },
		{ 3, INF, INF, INF, 0  }}
	};
	int P[MAX_VERTICES][MAX_VERTICES] = { 0 };
	int D[MAX_VERTICES][MAX_VERTICES];

	memset(P, -1, sizeof(int) * MAX_VERTICES * MAX_VERTICES);
	memcpy(D, g.W, sizeof(int) * MAX_VERTICES * MAX_VERTICES);
	printf("W:\n");
	for (int i = 0; i < g.n; i++) {
		for (int j = 0; j < g.n; j++) {
			if (g.W[i][j] < INF)
				printf("%3d", g.W[i][j]);
			else
				printf("  -");
		}
		printf("\n");
	}
	//아래를 완성하시오	
	for (int n = 0; n < g.n; n++) {
		for (int i = 0; i < g.n; i++) {
			for (int j = 0; j < g.n; j++) {
				if (g.W[i][n] + g.W[n][j] < g.W[i][j]) {
					g.W[i][j] = g.W[i][n] + g.W[n][j];
					P[i][j] = n;
					D[i][j] = g.W[i][j];
				}
					
			}
		}
	}
	

	printf("D:\n");
	for (int i = 0; i < g.n; i++) {
		for (int j = 0; j < g.n; j++) {
			if (D[i][j] < INF)
				printf("%3d", D[i][j]);
			else
				printf("  -");
		}
		printf("\n");
	}
	printf("P:\n");
	for (int i = 0; i < g.n; i++) {
		for (int j = 0; j < g.n; j++) {
			if (P[i][j] < 0)
				printf("%3d", 0);
			else
				printf("%3d", P[i][j] + 1);
		}
		printf("\n");
	}

	return 0;
}
/*예시 출력
binomail coefficient
Enter positive integer N(<=100): 50
Enter positive integer k(<=100): 8
Binomial recursive     : 536878650
		time = 2 s
Fibonacci dynamic prog.: 536878650
		time = 0 s

floyd shortest path
W:
  0  1  -  1  5
  9  0  3  2  -
  -  -  0  4  -
  -  -  2  0  3
  3  -  -  -  0
D:
  0  1  3  1  4
  8  0  3  2  5
 10 11  0  4  7
  6  7  2  0  3
  3  4  6  4  0
P:
  0  0  4  0  4
  5  0  0  0  4
  5  5  0  0  4
  5  5  0  0  0
  0  1  4  1  0
계속하려면 아무 키나 누르십시오 . . .
*/
/*실제출력
binomail coefficient
Enter positive integer N(<=100): 50
Enter positive integer k(<=100): 8
Binomial recursive     : 536878650
		time = 29 s
Fibonacci dynamic prog.: 536878650
		time = 0 s

floyd shortest path
W:
  0  1  -  1  5
  9  0  3  2  -
  -  -  0  4  -
  -  -  2  0  3
  3  -  -  -  0
D:
  0  1  3  1  4
  8  0  3  2  5
 10 11  0  4  7
  6  7  2  0  3
  3  4  6  4  0
P:
  0  0  4  0  4
  5  0  0  0  4
  5  5  0  0  4
  5  5  0  0  0
  0  1  4  1  0

C:\Users\nicky\Desktop\3-2학기\알고리즘\6주차\Project1\Debug\Project1.exe(프로세스 27240개)이(가) 종료되었습니다(코드: 0개).
이 창을 닫으려면 아무 키나 누르세요...


*/