#include <bits/stdc++.h>

using namespace std;

struct Item {
    int vertex, distance;
};

class MinHeap {
    public:
        vector<Item> heap;
        unordered_map<int, int> vertexMap;

        MinHeap(vector<Item> array) {
            for(auto item: array) {
                vertexMap[item.vertex] = item.vertex;
            }
            heap = buildHeap(array);
        }

        vector<Item> buildHeap(vector<Item> &array) {
            int firstParentIdx = (array.size() - 2) / 2;
            for (int currentIdx = firstParentIdx + 1; currentIdx >= 0; currentIdx--) {
                siftDown(currentIdx, array.size() - 1, array);
            }
            return array;
        }

        bool isEmpty() { return heap.size() == 0;}

        void siftDown(int currentIdx, int endIdx, vector<Item> &heap) {
            int childOneIdx = currentIdx * 2 + 1;
            while (childOneIdx <= endIdx) {
                int childTwoIdx = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
                int idxToSwap;
                if (childTwoIdx != -1 && heap[childTwoIdx].distance < heap[childOneIdx].distance) {
                    idxToSwap = childTwoIdx;
                } else {
                    idxToSwap = childOneIdx;
                }
                if (heap[idxToSwap].distance < heap[currentIdx].distance) {
                    swap(currentIdx, idxToSwap);
                    currentIdx = idxToSwap;
                    childOneIdx = currentIdx * 2 + 1;
                } else {
                    return;
                }
            }
        }

        void siftUp(int currentIdx) {
            int parentIdx = (currentIdx - 1) / 2;
            while (
                currentIdx > 0 &&
                heap[currentIdx].distance < heap[parentIdx].distance
            ) {
                swap(currentIdx, parentIdx);
                currentIdx = parentIdx;
                parentIdx = (currentIdx - 1) / 2;
            }
        }

        Item remove() {
            swap(0, heap.size() - 1);
            auto [vertex, distance] = heap.back();
            heap.pop_back();
            vertexMap.erase(vertex);
            siftDown(0, heap.size()-1, heap);
            return Item{vertex, distance};
        }

        void update(int vertex, int value) {
            heap[vertexMap[vertex]] = Item{vertex, value};
            siftUp(vertexMap[vertex]);
        }

        void swap(int i, int j) {
            vertexMap[heap[i].vertex] = j;
            vertexMap[heap[j].vertex] = i;
            auto temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
};

class Solution {
    public:
        vector<int> dijkstrasAlgorithmArray(int start, vector<vector<vector<int>>> edges) {
            int numberOfVertices = edges.size();

            vector<int> minDistances(edges.size(), numeric_limits<int>::max());
            minDistances[start] = 0;

            set<int> visited;

            while( visited.size() != numberOfVertices ) {
                auto [vertex, currentMinDistance] = getVertexWithMinDistances(minDistances, visited);
                if (currentMinDistance == numeric_limits<int>::max()) {
                    break;
                }

                visited.insert(vertex);

                for (auto edge: edges[vertex]) {
                    auto destination = edge[0];
                    auto distanceToDestination = edge[1];

                    if (visited.find(destination) != visited.end()) {
                        continue;
                    }

                    auto newPathDistance = currentMinDistance + distanceToDestination;
                    auto currentDestinationDistance = minDistances[destination];
                    if (newPathDistance < currentDestinationDistance) {
                        minDistances[destination] = newPathDistance;
                    }
                }
            }

        vector<int> finalDistances;
        for (auto distance: minDistances) {
            if (distance == numeric_limits<int>::max()) {
                finalDistances.push_back(-1);
            } else {
                finalDistances.push_back(distance);
            }
        }

        return finalDistances;
    }

    tuple<int, int> getVertexWithMinDistances(vector<int> distances, set<int> visited) {
        int currentMinDistance = numeric_limits<int>::max();
        int vertex = -1;
        for (int vertexIdx = 0; vertexIdx < distances.size(); vertexIdx++) {
            int distance = distances[vertexIdx];

            if (visited.find(vertexIdx) != visited.end()) {
                continue;
            }

            if (distance <= currentMinDistance) {
                vertex = vertexIdx;
                currentMinDistance = distance;
            }
        }
        return {vertex, currentMinDistance};
    }

        vector<int> dijkstrasAlgorithmHeap(int start, vector<vector<vector<int>>> edges) {

            vector<int> minDistances(edges.size(), numeric_limits<int>::max());
            minDistances[start] = 0;

            vector<Item> minDistancesPairs;

            for (int i = 0; i < edges.size(); i++) {
                minDistancesPairs.push_back(Item{i, numeric_limits<int>::max()});
            }

            MinHeap minDistancesHeap(minDistancesPairs);
            minDistancesHeap.update(start, 0);

            while( !minDistancesHeap.isEmpty() ) {
                auto [vertex, currentMinDistance] = minDistancesHeap.remove();
                if (currentMinDistance == numeric_limits<int>::max()) {
                    break;
                }

                for (auto edge: edges[vertex]) {
                    auto destination = edge[0];
                    auto distanceToDestination = edge[1];
                    auto newPathDistance = currentMinDistance + distanceToDestination;
                    auto currentDestinationDistance = minDistances[destination];
                    if (newPathDistance < currentDestinationDistance) {
                        minDistances[destination] = newPathDistance;
                        minDistancesHeap.update(destination, newPathDistance);
                    }
                }
            }

        vector<int> finalDistances;
        for (auto distance: minDistances) {
            if (distance == numeric_limits<int>::max()) {
                finalDistances.push_back(-1);
            } else {
                finalDistances.push_back(distance);
            }
        }

        return finalDistances;
    }

};


int main() {

    auto start = 0;
    vector<vector<vector<int>>> edges = {
            {{1, 7}}, {{2, 6}, {3, 20}, {4, 3}}, {{3, 14}}, {{4, 2}}, {}, {}
        };

    Solution solution;
    vector<int> result = solution.dijkstrasAlgorithmArray(start, edges);

    for( auto res : result ) {
        cout << res << endl;
    }

    cout << endl;

    vector<int> result2 = solution.dijkstrasAlgorithmHeap(start, edges);

    for( auto res : result2 ) {
        cout << res << endl;
    }

    return 0;
}