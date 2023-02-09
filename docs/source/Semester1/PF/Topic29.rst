.. _s1-pf-t29:

29) 2D Arrays
-------------

| 2D Arrays are a form of matrix. Just like arrays you can think of them as an array of arrays.
|
| Think of a table. If you want one in programming you can use a 2D array.
| Here how it is declared.

.. code-block:: c++
   :lineos:
   
   int matrix[3][4];
      
| Here we are declaring a 2D array named matrix with 3 rows and 4 columns.
| More specifically it is an array of 3 arrays with each array having a size of four.
|
| We can access the elements of a 2D array using a nested for loop. Like this:

.. code-block:: c++
   :linenos:

   for (int i = 0; i < 3; i++){
      for (int j = 0; j < 4; j++) 
      {
       cout << matrix[i][j] << endl;
      }
   }
      
| This code lets you access individual elements of the 2D array. But this would give garbage values as this array was to initailized.
| ``matrix[i][j]`` is one cell of the 2D array matrix. You can perform any operation on this depending on the data type of it.
| But there are a catches when it comes to their declaration. For example:

.. code-block:: c++
   :linenos:
   
   int arr[3][3] = {}; //This is wrong declaration
   const int row = 3;
   const int col = 3;
   int arr[row][col]; // This is correct declaration

| 2D arrays have many uses in proramming. You can implement hashtables and databases and much more in programming using them.
