.. _s3-dsa-t01:

2) Function Templates
---------------------

| This is normally covered under OOP, but I guess our pace was slow so they're forced to cover this under Data Structures now. Templates aren't an actual Data Structure, and they have way more to do with Classes and Functions. It's only being written in Semester 3 because I myself am studying it in Semester 3.
|
| Templates come in two types: Function Templates, and Class Templates. They exist when we want to generalize code for multiple data types and reduce repetition.
|
| Consider the following example:

.. code-block:: c++
   :linenos:

    void printArray(int* array, int size) {
        for(int i = 0; i < size; i++)
            cout << array[i] << " ";
        cout << endl;
    }
    void printArray(float* array, int size) {
        for(int i = 0; i < size; i++)
            cout << array[i] << " ";
        cout << endl;
    }
    void printArray(double* array, int size) {
        for(int i = 0; i < size; i++)
            cout << array[i] << " ";
        cout << endl;
    }

| Three different function overloads for a function that does the exact same thing every single time. If you didn't look at the Function Arguments you wouldn't even notice that they're different pieces of code.
|
| Not only is the code repetitive, it's also extra work to manage. Let's say you wanted to change the outputs, so that instead of ``1 2 3 4 5`` it prints ``1, 2, 3, 4, 5``. You'd have to make the changes in the code for every single function overload. It's just a lot of work, and it's unnecessary.
