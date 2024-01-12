.. _s3-dsa-t04:

4) Complexity Analysis
----------------------

| Ho boy this is where the fun begins. Now we'll be moving away from C++ specific things and towards Programming specific things. I'll try my best to explain what I've been taught in a way that is both accurate and makes sense.
|
| Given two or more algorithms to solve the same problem, how do we select the best one? There's a few factors:
*   Is it easy to implement, understand, and modify?
*   How long does it take to run?
*   How much memory does it use?
| Software Engineering is primarily concerned with the first criteria. In this course, we'll be focusing on the second and third criteria.
|
| Time Complexity is defined as the amount of time an algorithm needs to run to completion, while Space Complexity is defined as the amount of memory an algorithm needs to run to completion. Each algorithm has its own time and space complexity.
|
| We can measure both based on the input we give it, and they both usually grow with input size. So instead of measuring the time directly, we try to anaylze the running time as a function of the input size. The input affects how long it takes to run.

.. code-block:: c++
   :linenos:

    int find_max(int arr[], int n) {
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

| This function finds the maximum value in an array of integers. We can see that the running time of this function is dependent on the size of the array, n. We can also see that the running time is dependent on the number of times the loop runs. If we have an array of size 10, the loop will run 10 times. If we have an array of size 100, the loop will run 100 times. If we have an array of size n, the loop will run n times. So we can say that the running time of this function is ``O(n)``, or linear time. This is because the running time is directly proportional to the input size.
|
| This is an example where the algorithm will always run to ``n``, and there are times where algorithms can be stopped early. For this reason, we analyze running time under different cases:
*   Best Case
*   Worst Case
*   Average Case
| The best case is the case where the algorithm runs the fastest. The worst case is the case where the algorithm runs the slowest. The average case is the case where the algorithm runs somewhere in between the best and worst case. We usually analyze the worst case, because we want to know how long the algorithm will take to run in the worst case scenario.
|
| To get the most accurate comparison, you can run two algorithms on multiple inputs and plot it on a graph. The limitations of this, however, are requiring the same machine, the same compiler, and the same input. This is why we use Big-O notation. Big-O notation is a way to describe the running time of an algorithm without having to run it. It works more on the pseudocode and the theoretical time instead of the actual time. The idea is to call one instruction as one 'cycle', and then count the number of cycles the algorithm takes to complete depending on the input.

.. code-block:: c++
   :linenos:

    int sumArray(int arr[], int n) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }
        return sum;
    }

*   ``int sum = 0`` takes ``1 cycle`` as it's only executed once.
*   ``int i = 0`` takes ``1 cycle`` as it's only executed once.
*   ``i < n`` takes ``n + 1 cycles`` as it's executed n + 1 times. It's true n times, and false once. The total number of checks made are n + 1.
*   ``arr[i]`` (Dereferencing array) takes ``n cycles`` as it's executed n times
*   ``sum += arr[i]`` takes ``n cycles`` as it's executed n times
*   ``i++`` takes ``n cycles`` as it's executed n times
*   ``return sum`` takes ``1 cycle`` as it's only executed once
| So the total number of cycles is ``T(n) = 4n + 4``, where n is the number of inputs (Size of array). With different values of n, the running times we get are:
*   n = 10, T(n) = 44
*   n = 20, T(n) = 84
*   n = 100, T(n) = 404
*   n = 1000, T(n) = 4,004
*   n = 1000000, T(n) = 4,000,004
| The complexity of the algorithm grows linearly with the input size. Hence, we say the algorithm is ``O(n)``, or linear time.
|
| Here's another example:

.. code-block:: c++
   :linenos:

    void bubbleSort(int arr[], int n) {
        int temp = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - 1; j++) {
                if(arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

| I know there's some keen eyed among you that have worked with Bubble Sort and know I wrote an inefficient method of it. We'll get to that later, I want to use this as an example to showcase another time complexity. Let's count the number of cycles:
*   ``int temp = 0`` takes ``1 cycle`` as it's only executed once.
*   ``int i = 0`` takes ``1 cycle`` as it's only executed once.
*   ``i < n`` takes ``n + 1 cycles`` as it's executed n + 1 times. It's true n times, and false once. The total number of checks made are n + 1.
*   ``int j = 0`` takes ``n cycles`` as it's executed n times. It's executed n times because it's inside the outer ``i`` loop, which is executed n times.
*   ``j < n - 1`` takes ``n * n cycles``. It's executed ``n - 1`` times for when the condition is true, and once more for when the condition ``j < n - 1`` is false. So it runs ``(n - 1) + 1`` times, or ``n`` times for the inner ``j`` loop. This inner ``j`` loop, however, is run once for every ``i`` of the outer loop, and that outer ``i`` is run n times. So the total number of checks is ``n * n``, or n squared.
*   The swapping part depends on the data in question. Although it's something to measure, this is where the differences between Best, Worst, and Average case come. If the data is already sorted, it doesn't run at all, and hence takes ``0 cycles``. If the data is sorted in descending order, it runs the maximum number of times, which is ``n(n + 1)`` cycles. If the data is in random order, it runs somewhere in between. For the worst case scenario, we'll say it takes ``n(n + 1)`` cycles.
| So the total number of cycles in the worst case is T(n) = 3n\ :sup:`2`\ + 4n + 3, where n is the number of inputs (Size of array). With different values of n, the running times we get are:
*   n = 10, T(n) = 343
*   n = 20, T(n) = 1,283
*   n = 100, T(n) = 30,403
*   n = 1000, T(n) = 3,004,003
*   n = 1000000, T(n) = 3,000,004,000,003
| The complexity of the algorithm grows quadratically with the input size. Hence, we say the algorithm is O(\ :sup:`2`\), or quadratic time.
|
| Changing the hardware or software environment affects how long T(n) takes, but it doesn't affect the growth rate of T(n) with respect to n. This is why we use Big-O notation, as it's independent of the hardware and software environment. The notation also generally ignores coefficients, constant factors, and lower order terms, so 4n + 4 would just be n, and n\ :sup:`2`\ + 2n + 1 would just be n\ :sup:`2`\. However, this is also where programmers can mess up the comparison between two algorithms. The *notation* ignores coefficients, but they still make a big difference. If you compare two algorithms, one with T(n) = 0.1n\ :sup:`2`\ (which would be something like two nested loops but the second one only runs for every 10th iteration of the first one), and one with T(n) = 1000n (and you'll especially notice when you plot these equations on a graph), up until a value of n == 10000 the first algorithm will be faster. But after that, the second algorithm will be faster. So it's important to keep in mind that the notation ignores coefficients, but they still make a difference. There is no 'perfect algorithm', each one will be faster or slower depending on the data it's working with, and the size of the data. Big-O notation only simplifies the comparison between algorithms, it doesn't make it perfect.
|
| Space Complexity works similarly except with how much space is allocated. This is looked at less but still matters for algorithms that use a lot of space, like Recursion which takes up space on the stack while it's running. We'll be looking at the more detailed algorithms in the next semester, where there's a subject straight up called ``Design and Analysis of Algorithms``. All that matters for now is a small intro to Time and Space Complexity as different implementations of Data Structures aims to reduce these complexities to solve different problems. Take for example an Array and a Linked List. An Array has a constant time complexity for accessing an element, but a linear time complexity for inserting an element. A Linked List has a linear time complexity for accessing an element, but a constant time complexity for inserting an element. And a Linked List can grow infinitely (as long as there's memory), while an Array is a fixed size unless you copy over all of its contents to a bigger array, which is a rather expensive operation in comparison. So depending on the problem, you'd use one or the other. There is no "right answer", it's all about what you need to do.