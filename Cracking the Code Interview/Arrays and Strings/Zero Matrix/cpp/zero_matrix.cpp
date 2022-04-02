#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        void nullifyRow( int ** matrix, int N, int row ) {
            for ( int j = 0; j < N; ++j ) {
                matrix[row][j] = 0;
            }
        }

        void nullifyCol( int ** matrix, int M, int col ) {
            for ( int i = 0; i < M; ++i ) {
                matrix[i][col] = 0;
            }
        }


        void nullifyMatrix( int ** matrix, int M, int N ) {
            bool firstRow = false;

            //first row
            for( int i = 0; i < N; ++i ) {
                if ( matrix[0][i] == 0 ) {
                    firstRow = true;
                    break;
                }
            }

            //rest of the matrix
            for( int i = 1; i < M; ++i ) {
                bool nullifyThisRow = false;
                for ( int j = 0; j < N; ++j ) {
                    if ( matrix[i][j] == 0 ) {
                        matrix[0][j] = 0;
                        nullifyThisRow = true;
                    }
                }
                if (nullifyThisRow)
                    nullifyRow(matrix, N, i);
            }

            //now we know which column to be nullify using information stored in previous step.
            //cols first
            for ( int j = 0; j < N; ++j ) {
                if ( matrix[0][j] == 0 ) {
                    nullifyCol(matrix, M,  j);
                }
            }

            //now first row
            if ( firstRow ) {
                nullifyRow(matrix, N, 0);
            }

        }

        void printMatrix( int ** matrix, int M, int N ) {
            for ( int i = 0; i < M; ++i ) {
                for ( int j = 0; j < N; ++j ) {
                    cout << matrix[i][j] << "  ";
                }
                cout << endl;
            }
            cout << endl;
        }

};


int main() {

    Solution solution;
    int M=3, N=2;
    int input[M][N] = {{0,1}, {2,0}, {4,5}};
	int ** matrix = new int*[M];
	for ( int i =0; i < M; ++i ) {
		matrix[i] = new int[N];
	}

	for ( int i = 0; i < M; ++i ) {
		for ( int j = 0; j < N; ++j ) {
			matrix[i][j] = input[i][j];
		}
	}

	cout << "Matrix Before:\n";
	solution.printMatrix(matrix, M, N);
	solution.nullifyMatrix(matrix, M, N);
	cout << "Matrix After:\n";
	solution.printMatrix(matrix, M, N);
	return 0;
}