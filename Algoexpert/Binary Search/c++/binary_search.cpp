#include <bits/stdc++.h>

using namespace std;

int binarySearchIterative(vector<int> array, int target) {

	int l = 0, r = array.size() - 1;
	
	while (l <= r) {
		
		int mid = (l + r) / 2;
		
		if (array[mid] == target) {
			return mid;
		} else if (array[mid] < target) {
			l = mid + 1;
		} else if (array[mid] > target) {
			r = mid - 1;
		}
		
	}
	
    return -1;
}

int binarySearchHelper(vector<int> array, int left, int right, int target) {
	if (left > right) {
		return -1;
	}
	int mid = (left + right) / 2;
	if (array[mid] == target) {
		return mid;
	} else if (target < array[mid]) {
		return binarySearchHelper(array, 0, mid - 1, target);
	} else {
		return binarySearchHelper(array, mid + 1, right, target);
	}
}

int binarySearchRecursive(vector<int> array, int target) {
	return binarySearchHelper(array, 0, array.size() - 1, target);
}

int main() {
    vector<int> array{ 0, 1, 21, 33, 45, 45, 61, 71, 72, 73 };
    int target = 33;

    cout << binarySearchIterative(array, target) << endl;
	cout << binarySearchRecursive(array, target) << endl;

    return 0;
}

