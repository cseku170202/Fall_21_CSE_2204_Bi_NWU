function performHeapSort() {
    const input = document.getElementById('array-input').value.trim();
    const array = input.split(' ').map(Number);

    const binaryTree = document.getElementById('binary-tree');
    binaryTree.innerHTML = '';

    heapSort(array);

    function heapify(arr, n, i) {
        let largest = i;
        let left = 2 * i + 1;
        let right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest])
            largest = left;

        if (right < n && arr[right] > arr[largest])
            largest = right;

        if (largest !== i) {
            swap(arr, i, largest);
            heapify(arr, n, largest);
        }
    }

    function heapSort(arr) {
        const n = arr.length;

        for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
            heapify(arr, n, i);

        let sortedIndex = n - 1;
        let sortedArray = [];

        let interval = setInterval(() => {
            if (sortedIndex > 0) {
                swap(arr, 0, sortedIndex);
                sortedArray.unshift(arr[sortedIndex]);
                visualizeHeapSort(arr, sortedIndex);
                heapify(arr, sortedIndex, 0);
                sortedIndex--;
            } else {
                sortedArray.unshift(arr[0]);
                visualizeHeapSort(arr, 0, sortedArray);
                clearInterval(interval);
                showResult(sortedArray);
            }
        }, 1000);
    }

    function swap(arr, i, j) {
        const temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    function visualizeHeapSort(arr, sortedIndex, sortedArray = []) {
        binaryTree.innerHTML = '';

        const maxDepth = Math.ceil(Math.log2(arr.length + 1));
        const maxWidth = Math.pow(2, maxDepth) - 1;

        let levels = [];
        let level = 0;
        let nodeIndex = 0;
        let nodesInLevel = 1;
        let nodesProcessed = 0;

        while (nodesProcessed < arr.length) {
            let levelNodes = '';

            for (let i = 0; i < nodesInLevel && nodeIndex < arr.length; i++) {
                const nodeValue = arr[nodeIndex];
                let nodeClass = 'node';

                if (nodeIndex <= sortedIndex) {
                    if (nodeValue === sortedArray[0]) {
                        nodeClass += ' highlight';
                        sortedArray.shift();
                    } else {
                        nodeClass += ' sorted';
                    }
                }

                levelNodes += `<div class="${nodeClass}">${nodeValue}</div>`;
                nodeIndex++;
                nodesProcessed++;
            }

            levels.push(`<div class="level">${levelNodes}</div>`);
            level++;
            nodesInLevel *= 2;
        }

        binaryTree.innerHTML = levels.join('');
    }

    function showResult(sortedArray) {
        const resultContainer = document.getElementById('result');
        resultContainer.innerHTML = `Sorted Array: ${sortedArray.join(' ')}`;
        resultContainer.classList.remove('hidden');
    }
}
