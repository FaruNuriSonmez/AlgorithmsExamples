#include <iostream>

using namespace std;
#define SIZE 5

// the maze problem
int maze[SIZE][SIZE] = {
        {0, 1, 0, 1, 1},
        {0, 0, 0, 0, 0},
        {1, 0, 1, 0, 1},
        {0, 0, 1, 0, 0},
        {1, 0, 0, 1, 0}
};

//matrix to store the solution
int solution[SIZE][SIZE];

//function to print the solution matrix
void printsolution() {
    int i, j;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d\t",solution[i][j]);
        }
        printf("\n\n");
    }
}

int solvemaze(int r, int c){
    if ((r==SIZE-1) && (c==SIZE-1)){
        solution[r][c] = 1;
        return 1;
    }
    if (r >= 0 && c >= 0 && r < SIZE && c < SIZE && solution[r][c] == 0 && maze[r][c] == 0){
        solution[r][c] = 1;
        if (solvemaze(r+1, c))
            return 1;
        if (solvemaze(r,c+1))
            return 1;
        if (solvemaze(r-1, c))
            return 1;
        if (solvemaze(r,c-1))
            return 1;

        solution[r][c] = 2;
        return 0;
    }
    return 0;
}

int main() {
    cout << "Maze with backtracking" << endl;
    int k, l;
    for (int k = 0; k < SIZE; k++) {
        for (int l = 0; l < SIZE; l++) {
            printf("%d\t",maze[k][l]);
        }
        printf("\n\n");
    }

    int i, j;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            solution[i][j] = 0;
        }
    }
    cout << "Solve Maze \n" << endl;
    if (solvemaze(0,0))
        printsolution();
    else
        printf("No solution\n");
    return 0;
}