.. _s1-pf-t27:

27) Arrays
----------

| Arrays are a simple yet wonderful topic.
|
| Arrays are a form of a Data Structure. You'll learn more about those way later but for now, just understand that this is one of the ways to store very large amounts of data easily. If you want to store 500 numbers or names then instead of declaring 500 variables by typing them manually, you can just write this one line.
|
| An Array is a collection of Variables. Here's how it's declared:

.. code-block:: c++
   :linenos:

	int numbers[4];

| It's the exact same way of storing a Variable, just that [Square Brackets] are used to declare the Array Size.
| Right now, [4] is written there, meaning that the Array has 4 locations.
|
| We can insert values into that array as well.

.. code-block:: c++
   :linenos:

	int numbers[4];
	numbers[4] = {10, 20, 30, 40};

| And then if you did

.. code-block:: c++
   :linenos:

	cout << numbers[0] << endl;
	cout << numbers[1] << endl;
	cout << numbers[2] << endl;
	cout << numbers[3] << endl;

| Then you'd get 10 20 30 40 (In different lines) as the output.
| The value inside the [] during declaration defines the number of variables to declare, while if it's called outside of the declaration, it's instead used to access those values. The count starts from 0, so for an ``int num[20]`` array, you can access the values from ``num[0]`` to ``num[19]``. ``num[20]`` gives an error. It doesn't exist.
|
| There's other ways to declare Arrays too.

.. code-block:: c++
   :linenos:

	int marks[5] = {10, 20, 30, 40, 50};// 10 20 30 40 50
	int marks[] = {10, 20, 30, 40, 50}; // 10 20 30 40 50
	int marks[] = {10, 20, 30};         // 10 20 30
	int marks[5] = {10, 20, 30};        // 10 20 30 0 0
	int marks[5] = {10};        		// 10 0 0 0 0
	int marks[10] = {};					// All zero's
	int marks[10];						// All Garbage Values
	
	int a;
	int marks[10];
	cin >> a; // This is fine
	cin >> marks; // This is NOT fine
	cin >> marks[1]; // This is fine
	cin >> marks[0]; // This is fine
	cin >> marks[10];// This is NOT fine
	cin >> marks[-1];// You experiment with this