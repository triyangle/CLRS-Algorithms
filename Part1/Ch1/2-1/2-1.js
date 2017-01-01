// 2.1-2
function insertionSort(arr, reverse) {
    for(var j = 1; j < arr.length; j++) {
        var key = arr[j];
        var i = j - 1;
        function condition(i) {
            return reverse ? arr[i] < key : arr[i] > key;
        }
        while (i >= 0 && condition(i)) {
            arr[i + 1] = arr[i];
            i--;
        }
        arr[i + 1] = key
    }
}

// 2.1-3
function search(arr, v) {
    var i = 0;
    while (i < arr.length && arr[i] != v) {
        i++;
    }
    return (i == arr.length) ? null : i;
}
