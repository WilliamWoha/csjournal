.. _s1-pf-t31:

31) Passing Arrays to Functions
-------------------------------

| This is also from the class where I didn't have my register with me. I'll try not to miss anything, but some obscure thing might end up being asked on in my exams to come.
|
| We can both pass and return arrays from functions. The syntax for passing an array to a function is:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 1,3,5,7
   
    dataType function(dataType arrayName[size]);
    // For example:
    int sum(int num[5]);
    // An integer array of size 5 is passed.
    double average(double numbers[10]);
    // A double array of size 10 is passed.
    char firstLetter(char name[]);
    // A character array of unknown size is passed.
    // This line above is completely valid.

| I'll get to why the syntax is valid in Line 7. All you need to know is, Line 1 is how you pass a 1D array to a function. Then you can use it the same way you would normally use an array.
| For passing a 2D array, the syntax is the same, but you type the row and column size.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 1,3,5,7
   
    dataType function(dataType arrayName[rows][cols]);
    // For example:
    int sum(int num[5][10]);
    // An integer array of 5 rows and 10 columns is passed.
    double average(double numbers[][3]);
    // A double array of unknown rows and 3 columns is passed.
    char firstLetter(char name[3][6]);
    // A character array of 3 rows and 6 columns is passed.

| And again you might notice on line 5 that there's a value missing. But this is still valid. The rule is, the square brackets closest to the name of the array can be left empty. It's completely optional to do so. So for a 1D Array, the square brackets can be left empty. For a 2D Array, the Column Size is necessary. For a 3D Array, which would be [x][y][z], it can be passed as [][y][z] as well.
| You don't have to do 3D Arrays. They're distracting. The bigger thing to focus on now, is Pointers.
|
| That's also how Arrays are returned. With Pointers. But first you need to actually figure out what Pointers are. Make sure to revise on :ref:`s1-pf-t30`, specifically in the section where the computer's memory and storage are explained. Pointers work on that concept.
    