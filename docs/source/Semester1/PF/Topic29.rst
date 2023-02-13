.. _s1-pf-t29:

29) 2D Arrays
-------------

| 2D Arrays are a form of matrix. Just like arrays you can think of them as an array of arrays.
| If 10 students have marks of Maths then you'd just declare an array of size 10 to store all those marks. But what if there were more subjects?
| 1D Arrays are just a single row or single column. 2D Arrays are like a grid. You can have both rows and columns. That's not how they're stored in memory, but we can understand them easily this way.

.. code-block:: c++
   
   int programming[10];
   int maths[10];
   int physics[10];
   int english[10];

| ``programming`` is one array. ``maths`` is also one array. ``english`` and ``physics`` are also one array. But what if there were more subjects, maybe even hundreds or thousands? Instead of having to type out that many arrays, we just use a single 2D Array instead.

.. code-block:: c++

   int subjects[4][10];
   
| Here we've declared a 2D Array called subjects. You could also call it marks, it doesn't really matter. In the example above this one, you'd access the array by typing things like ``programming[3]`` or ``maths[0]``. Here, just replace those names with the Row index of the 2D Array. So if we say programming, maths, physics, english are the 4 rows of ``subjects[4][10]``, then ``subjects[0]`` is programming, ``subjects[1]`` is maths, ``subjects[2]`` is physics, and ``subjects[3]`` is english. And if I want to access ``programming[3]``, then I'd just type ``subjects[0][3]``, and if I want to access ``maths[0]``, then I'd write ``subjects[1][0]``.
|
| 2D Arrays are usually handled via Nested loops. The outer loop deals with rows, and the inner loop deals with individual values (or columns) of each row.

.. code-block:: c++
   :linenos:

   for (int i = 0; i < 4; i++){
      for (int j = 0; j < 10; j++) 
      {
         cout << subjects[i][j] << endl;
      }
   }
      
| This code lets you access individual elements of the 2D array. But this would give garbage values as this array wasn't initailized. Initialization is similar to a 1D Array but becomes a bit more specific. The declaration should also be looked at carefully. For example:

.. code-block:: c++
   :linenos:
   
   int arr[3][3] = {}; // This is wrong declaration
   const int row = 3;
   const int col = 3;
   int arr[row][col]; // This is correct declaration

| The above isn't something I understand, but I've been told by multiple teachers and really intelligent students that even though Compilers may sometimes work, the proper practice is the Correct declaration. As for Initialization:

.. code-block:: c++
   :linenos:

   int marks[5] = {5,4,3,2,1}; // 5 4 3 2 1
   int marks[5] = {0}; // 0 0 0 0 0
   int marks[5] = {}; // 0 0 0 0 0
   const int row = 4;
   const int col = 10;
   int arr[row][col] = {40,39,38,37,36,35, ... , 1};
   // The dots aren't actual syntax. Just assume I actually wrote it all the way to one.
   // The contents of the 2D Array would be:
   // 40 39 38 37 36 35 34 33 32 31
   // 30 29 28 27 26 25 24 23 22 21
   // 20 19 18 17 16 15 14 13 12 11
   // 10  9  8  7  6  5  4  3  2  1

   // If it were written only till 33 then it would be
   // 40 39 38 37 36 35 34 33  0  0
   //  0  0  0  0  0  0  0  0  0  0
   //  0  0  0  0  0  0  0  0  0  0
   //  0  0  0  0  0  0  0  0  0  0

   // Also, you can't make the values go into the next row unless you tell it to.
   int arr[row][col] = {{40,39,38}, {0}, {1,2}, {30,29,28,27}};
   // The contents of the array would be:
   // 40 39 38  0  0  0  0  0  0  0
   //  0  0  0  0  0  0  0  0  0  0
   //  1  2  0  0  0  0  0  0  0  0
   // 30 29 28 27  0  0  0  0  0  0
   
| 2D arrays have many uses in programming. You can implement hashtables and databases and much more in programming using them.
