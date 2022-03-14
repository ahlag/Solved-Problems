import java.util.*;

public class DijkstraAlgoExpert {

    public static int[] dijkstrasAlgorithmHeap(int start, int[][][] edges)  {

        int numberOfVertices = edges.length;

        int[] minDistances = new int[numberOfVertices];
        Arrays.fill(minDistances, Integer.MAX_VALUE);
        minDistances[start] = 0;

        List<Item> minDistancesPairs = new ArrayList<Item>();

        for (int i = 0; i < numberOfVertices; i++) {
            Item item = new Item(i, Integer.MAX_VALUE);
            minDistancesPairs.add(item);
        }

        MinHeap minDistancesHeap = new MinHeap(minDistancesPairs);
        minDistancesHeap.update(start, 0);

        while( !minDistancesHeap.isEmpty() ) {
            Item heapItem = minDistancesHeap.remove();
            int vertex = heapItem.vertex;
            int currentMinDistance = heapItem.distance;

            if (currentMinDistance == Integer.MAX_VALUE) {
                break;
            }

            for (int[] edge: edges[vertex]) {
                int destination = edge[0];
                int distanceToDestination = edge[1];
                int newPathDistance = currentMinDistance + distanceToDestination;
                int currentDestinationDistance = minDistances[destination];
                if (newPathDistance < currentDestinationDistance) {
                    minDistances[destination] = newPathDistance;
                    minDistancesHeap.update(destination, newPathDistance);
                }
            }
        }

        int[] finalDistances = new int[minDistances.length];
        for (int i = 0; i < minDistances.length; i++) {
            int distance = minDistances[i];
            if (distance == Integer.MAX_VALUE) {
                finalDistances[i] = -1;
            } else {
                finalDistances[i] = distance;
            }
        }

        return finalDistances;
    }

    public static int[] dijkstrasAlgorithmArray(int start, int[][][] edges) {
        int numberOfVertices = edges.length;

        int[] minDistances = new int[edges.length];
        Arrays.fill(minDistances, Integer.MAX_VALUE);
        minDistances[start] = 0;

        Set<Integer> visited = new HashSet<Integer>();

        while( visited.size() != numberOfVertices ) {
            int[] getVertexData = getVertexWithMinDistances(minDistances, visited);
            int vertex = getVertexData[0];
            int currentMinDistance = getVertexData[1];

            if (currentMinDistance == Integer.MAX_VALUE) {
                break;
            }

            visited.add(vertex);

            for (int[] edge: edges[vertex]) {
                int destination = edge[0];
                int distanceToDestination = edge[1];

                if (visited.contains(destination)) {
                    continue;
                }

                int newPathDistance = currentMinDistance + distanceToDestination;
                int currentDestinationDistance = minDistances[destination];
                if (newPathDistance < currentDestinationDistance) {
                    minDistances[destination] = newPathDistance;
                }
            }
        }

        int[] finalDistances = new int[minDistances.length];
        for (int i = 0; i < minDistances.length; i++) {
            int distance = minDistances[i];
            if (distance == Integer.MAX_VALUE) {
                finalDistances[i] = -1;
            } else {
                finalDistances[i] = distance;
            }
        }

        return finalDistances;
    }

    public static int[] getVertexWithMinDistances(int[] distances, Set<Integer> visited) {
        int currentMinDistance = Integer.MAX_VALUE;
        int vertex = -1;

        for (int vertexIdx = 0; vertexIdx < distances.length; vertexIdx++) {
            int distance = distances[vertexIdx];

            if (visited.contains(vertexIdx)) {
                continue;
            }

            if (distance <= currentMinDistance) {
                vertex = vertexIdx;
                currentMinDistance = distance;
            }
        }
        return new int[]{vertex, currentMinDistance};
    }

    public static void main(String[] args) {
        int start = 0;
        int[][][] edges = {
                {{1, 7}},
                {{2, 6}, {3, 20}, {4, 3}},
                {{3, 14}},
                {{4, 2}},
                {},
                {}
        };
        int[] expected = {0, 7, 13, 27, 10, -1};
        int[] result = dijkstrasAlgorithmArray(start, edges);

        System.out.println(Arrays.toString(result));

        int[] result2 = dijkstrasAlgorithmHeap(start, edges);
        System.out.println(Arrays.toString(result2));
    }
}
