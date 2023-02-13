.. _s1-pf-t28:

28) Character Arrays
--------------------

.. code-block:: c++
   :linenos:

	#include <string>
	string name = "John";
	cout << sizeof(name) << endl; // Outputs 5, because of a Null Character.

| Strings and Character Arrays are very similar but it's still important to learn separately. The major difference between the two is that Character Arrays were used in the C language before Strings existed, and in some cases you can import libraries not written in C++, so C Strings become compatible. Character Array manipulation is going to be asked a lot in exams through Dry Runs (for me at least).
|
| You declare Character Arrays just like regular Arrays.

.. code-block:: c++

	char arr[] = {'H', 'e', 'l', 'l', 'o', '\0'};
	cout << sizeof(arr) << endl; // Outputs 6.
	cout << sizeof(arr[0]) << endl; // Outputs 1.

| You can do input and output just like any other data type as well.

.. code-block:: c++

	char arr[] = "Hello World";
	cout << arr << endl; // Outputs "Hello World".
	// This is possible ONLY for character arrays because of the existence of '\0' at the end.
	// But doing cin >> arr will cause problems.
	// Instead you use cin.getline(arr, 10);

| Strings have extra functions to them which I wrote in detail but I never ended up using so I didn't pay much attention to them, but they're in my notes. If you want to look at them further, you can check official documentation, or other programming pages that explain them. They're functions of the ``#include <string>`` library, and have things like Strlen (checks String length), Strcat (Concatenates one string to another), Strcpy (copies one string to another variable), and Strcmp (Compares strings to see if they're equal or not).