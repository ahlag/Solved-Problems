#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        void helper_transpose(int **matrix, int N) {
            for( int i = 0; i < N; ++i ) {
                for( int j = i+1; j < N; ++j ) {
                    if ( i != j ) {
                        swap(matrix[i][j], matrix[j][i]);
                    }
                }
            }
        }

        void helper_reverse( int * row, int N ) {
            for ( int i = 0; i < N/2; ++i ) {
                swap(row[i], row[N-i-1]);
            }
        }

        void rotate1(int ** matrix, int N) {
            //transpose matrix
            helper_transpose(matrix, N);
            // reverse each row
            for ( int i = 0; i < N; ++i ) {
                helper_reverse(matrix[i], N);
            }
        }

        void rotate2(int ** matrix, int N) {
            for( int i = 0; i < N/2; ++i ) {
                for( int j = i; j < N-i-1; ++j ) {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][N-i-1];
                    matrix[j][N-i-1] = matrix[N-i-1][N-j-1];
                    matrix[N-i-1][N-j-1]= matrix[N-j-1][i];
                    matrix[N-j-1][i] = temp;
                }
            }
        }

        void printMatrix(int ** matrix, int N) {
            for ( int i = 0; i < N; ++i ) {
                for( int j = 0; j < N; ++j ) {
                    cout << matrix[i][j] << " ";
                }
                cout << endl;
            }
        }

};


int main() {

	int N = 3;
	int ** matrix = new int*[N];
    int input[N][N] = {{0,1,1}, {2,3,2}, {4,5,6}};

    Solution solution;

	for ( int i = 0; i < N; ++i ) {
		matrix[i] = new int[N];
	}

	for ( int i = 0; i < N; ++i) {
		for ( int j = 0; j < N; ++j ) {
			matrix[i][j] = input[i][j];
		}
	}

	cout << "Rotated matrix by 90 (clockwise):\n";
	solution.rotate1(matrix, N);
	solution.printMatrix(matrix, N);

	cout << "Rotated matrix again by 90(anticlockwise):\n";
	solution.rotate2(matrix, N);
	solution.printMatrix(matrix, N);

    return 0;
}