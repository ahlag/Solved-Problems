#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        int numberOfBinaryTreeTopologiesRecursion(int n) {
	
            if (n == 0)	return 1;
            
            int numberOfTrees = 0;
            for (int leftTreeSize = 0; leftTreeSize < n; leftTreeSize++) {
                int rightTreeSize = n - 1 - leftTreeSize;
                int numberOfLeftTrees = numberOfBinaryTreeTopologiesRecursion(leftTreeSize);
                int numberOfRightTrees = numberOfBinaryTreeTopologiesRecursion(rightTreeSize);
                numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
            }
            
            return numberOfTrees;
        }

        int numberOfBinaryTreeTopologiesMemo(int n) {
            unordered_map<int, int> cache{{0, 1}};
            return helper(n, &cache);
        }

        int helper(int n, unordered_map<int, int> *cache) {
            if (cache->find(n) != cache->end())	return cache->at(n);
                
                int numberOfTrees = 0;
                for (int leftTreeSize = 0; leftTreeSize < n; leftTreeSize++) {
                    int rightTreeSize = n - 1 - leftTreeSize;
                    int numberOfLeftTrees = helper(leftTreeSize, cache);
                    int numberOfRightTrees = helper(rightTreeSize, cache);
                    numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
                }
                cache->insert({n, numberOfTrees});
            return cache->at(n);
        }

        int numberOfBinaryTreeTopologiesOptimized(int n) {

        vector<int> cache{1};
            
            for(int m = 1; m <= n; m++) {
                int numberOfTrees = 0;
                for (int leftTreeSize = 0; leftTreeSize < m; leftTreeSize++) {
                    int rightTreeSize = m - 1 - leftTreeSize;
                    int numberOfLeftTrees = cache[leftTreeSize];
                    int numberOfRightTrees = cache[rightTreeSize];
                    numberOfTrees += numberOfLeftTrees * numberOfRightTrees;
                }
                cache.push_back(numberOfTrees);
            }
            
            return cache[n];
        }

};


int main() {

    int n = 3;

    Solution solution;
    cout <<  solution.numberOfBinaryTreeTopologiesRecursion(n) << endl;
    cout <<  solution.numberOfBinaryTreeTopologiesMemo(n) << endl;
    cout <<  solution.numberOfBinaryTreeTopologiesOptimized(n) << endl;

    return 0;
}