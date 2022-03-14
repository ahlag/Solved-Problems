import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinHeap {
    List<Item> heap = new ArrayList<Item>();
    Map<Integer, Integer> vertexMap = new HashMap<Integer, Integer>();

    public MinHeap(List<Item> array) {
        for(int i = 0; i < array.size(); i++) {
            Item item = array.get(i);
            vertexMap.put(item.vertex, item.vertex);
        }
        heap = buildHeap(array);
    }

    List<Item> buildHeap(List<Item> array) {
        int firstParentIdx = (array.size() - 2) / 2;
        for (int currentIdx = firstParentIdx + 1; currentIdx >= 0; currentIdx--) {
            siftDown(currentIdx, array.size() - 1, array);
        }
        return array;
    }

    boolean isEmpty() { return heap.size() == 0;}

    void siftDown(int currentIdx, int endIdx, List<Item> heap) {
        int childOneIdx = currentIdx * 2 + 1;
        while (childOneIdx <= endIdx) {
            int childTwoIdx = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
            int idxToSwap;
            if (childTwoIdx != -1 && heap.get(childTwoIdx).distance < heap.get(childOneIdx).distance) {
                idxToSwap = childTwoIdx;
            } else {
                idxToSwap = childOneIdx;
            }
            if (heap.get(idxToSwap).distance < heap.get(currentIdx).distance) {
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
                        heap.get(currentIdx).distance < heap.get(parentIdx).distance
        ) {
            swap(currentIdx, parentIdx);
            currentIdx = parentIdx;
            parentIdx = (currentIdx - 1) / 2;
        }
    }

    Item remove() {
        if (isEmpty()) {
            return null;
        }

        swap(0, heap.size() - 1);
        Item lastItem = heap.get(heap.size() - 1);
        int vertex = lastItem.vertex;
        int distance = lastItem.distance;
        heap.remove(heap.size() - 1);
        vertexMap.remove(vertex);
        siftDown(0, heap.size()-1, heap);
        return new Item(vertex, distance);
    }

    void update(int vertex, int value) {
        heap.set(vertexMap.get(vertex), new Item(vertex, value));
        siftUp(vertexMap.get(vertex));
    }

    void swap(int i, int j) {
        vertexMap.put(heap.get(i).vertex, j);
        vertexMap.put(heap.get(j).vertex, i);
        Item temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

}
