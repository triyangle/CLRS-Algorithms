import java.util.*;

class Insert {
    public static void main(String[] args) {
        int[] a = {5, 2, 4, 6, 1, 3};
        insertionSort(a, false);
        System.out.println(Arrays.toString(a));
        insertionSort(a, true);
        System.out.println(Arrays.toString(a));
    }
    public static void insertionSort(int[] arr, boolean reversed) {
        for (int j = 1; j < arr.length; j++) {
            int key = arr[j];
            int i = j - 1;
            while(i >= 0 && compare(arr, i, key, reversed)) {
                arr[i + 1] = arr[i];
                i--;
            }
            arr[i + 1] = key;
        }
    }
    public static boolean compare(int[] arr, int index, int key, boolean reversed) {
        return reversed ? arr[index] < key : arr[index] > key;
    }
}

// TODO add 2.1-3 search
