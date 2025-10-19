#include <stdio.h>
#include <cilk/cilk.h>
#include <cilk/cilk_api.h>

#define N 4

void print_matrix(int a[N][N]) {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void stencil(int a[N][N]) {
    // First phase - row-wise computation
    for(int cr = 1; cr < N; cr++) {
        cilk_for(int i = cr; i < N; i++) {
            for(int j = 1; j < N; j++) {
                a[i][j] += a[i-1][j];
            }
        }
    }
    
    // Second phase - column-wise computation
    for(int cc = 1; cc < N; cc++) {
        cilk_for(int j = cc; j < N; j++) {
            for(int i = 1; i < N; i++) {
                a[i][j] += a[i][j-1];
            }
        }
    }
    
    // Third phase - diagonal subtraction
    for(int i = 1; i < N; i++) {
        for(int j = 1; j < N; j++) {
            a[i][j] -= a[i-1][j-1];
        }
    }
}

int main() {
    int a[N][N] = {
        {2, 0, 2, 3},
        {1, 0, 0, 0},
        {3, 0, 0, 0},
        {2, 0, 0, 0}
    };
    
    printf("Original matrix:\n");
    print_matrix(a);
    
    stencil(a);
    
    printf("Matrix after stencil operation:\n");
    print_matrix(a);
    
    return 0;
}