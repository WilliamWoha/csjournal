.. _s3-dsa-t06:

6) Arrays
---------

| Yep, Arrays are a Data Structure. It came as a surprise to me as well but technically speaking even something like an ``int`` or a ``float`` is also a Data Structure. A Data Structure is just a way to store data, so an ``int`` is a Data Structure that stores a number. An ``array`` is a Data Structure that stores a collection of data in a continuous memory block, and it's also a Data Structure.
|
| Most of the Data Structures you'll see throughout the semester have to be implemented by yourself, but Arrays almost always come with the language already because of their extremely wide use case, diversity, and how fast they are for accessing. Arrays are also the most basic Data Structure, and most other Data Structures are built on top of Arrays.
|
| The operations you can do on an Array are as such:
*   Access element in Array
*   Find element in Array
*   Sort Array
*   Iterate through Array
*   Add element to Array
*   Remove element from Array
| And so on. You can use it however you want but those basic operations above are the basic ones. Adding and Removing elements however are less common, because Arrays have a fixed size. There's two ways to deal with this: The first is to use ``vector``s, which are Arrays that can grow and shrink by moving all the elements from one array to another. The second is to have a large fixed size array, keep empty areas, and eventually as the array fills up you use the empty areas to add more elements. I did this in my Semester 2 Project for having an array that would keep track of all bullets on screen, and if spawning a new bullet would exceed the array size, I just replaced the first bullet in the array with the new bullet, kind of like a 'circular buffer'. This approach sped up my game by over 300% because there were no calls being made to allocate or delete memory, and the array was always the same size. It made such a major difference because originally it was allocating and deleting memory *every time a bullet was spawned or despawned*, and it's an expensive operation to call.

Array Searching
---------------

| Accessing an element in an Array is extremely fast, and the computer is able to access it in Constant Time (which in Big-O notation is ``O(1)``). Constant Time just means, no matter what the size of the Array is, it will always take the same amount of time to access an element, and you'll see how this differs when we do something like a Linked List later on.
|
| Finding an element in an Array is also fast, but for extremely large arrays it can become slow. A simple ``linear search`` function would be as follows:

.. code-block:: c++
   :linenos:

    int linearSearch(int array[], int size, int element) {
        for (int i = 0; i < size; i++) {
            if (array[i] == element) {
                return i;
            }
        }
        return -1;
    }

| This works for most situations but if you're looking through an array of size One Million then in the worst case it would do One Million comparisons. One way to improve upon this would be a search function called ``binarySearch`` which is much faster, but requires the array to be sorted. This is because it uses the fact that the array is sorted to cut the search space in half every time, and it's much faster than a linear search. The code for this is as follows:

.. code-block:: c++
   :linenos:

    int binarySearch(int array[], int size, int element) {
        int left = 0;
        int right = size - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (array[middle] == element) {
                return middle;
            }
            if (array[middle] < element) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return -1;
    }

| So if your array happens to be sorted, you can use this algorithm instead for extremeley fast searching. It cuts the searching down from ``O(n)`` to ``O(log n)`` which is a huge improvement. To put that into perspective, on an array of size One Million, Linear Search would require One Million comparisons in its worst case, but Binary Search would only require Twenty Comparisons in its worst case. That's a huge improvement. But as stated before, it requires the array to be sorted, and usually sorting is an expensive operation. If you're working with a small array then a Linear Search is fine, but if you're working with a large array which is sorted, then a Binary Search is much faster.
|
| Let's talk about Sorting then.

Array Sorting
-------------

| We covered four algorithms for sorting in Classes:
*   Bubble Sort
*   Selection Sort
*   Insertion Sort
*   Quick Sort
| There's many more out there, such as Merge Sort, and all of them have their own advantages and disadvantages. Unfortunately I can't explain in detail *how* all of these Sorting Algorithms work because of how many diagrams it needs, and on top of that there's already so many sites that visualize it step by step in a much better way than I could. Seriously, just google them, there's thousands of results and they explain the algorithms in fantastic detail. Different algorithms are going to be better for different situations, but generally Merge Sort or Quick Sort is preferred because of their abilities to do the entire sorting in O(n log n) instead of O(n\ :sup:`2`\) like the others.
|
| This time I won't just say "it depends on the situation" and end it there, because these specific algorithms actually got asked about in my exam so do give it some practice. Specifically try to see which of the sorting algorithms above (not including Quick Sort) is the best for these situations:
*   Array is already sorted
*   Array is sorted in reverse order
*   Most of the elements of the Array are where they're supposed to be, but a few elements are not
*   None of the elements of the Array are where they're supposed to be, but most of the elements are close to where they're supposed to be
| This was asked from me in an exam and I got it wrong. The university didn't actually tell which answers were the right ones so, if I find the right answers I'll write them here, and if I forget to or if you figure it out on your own then please contact me so I can write them here.