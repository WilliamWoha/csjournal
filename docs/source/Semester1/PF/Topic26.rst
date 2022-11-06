.. _s1-pf-t26:

26) Local, Global, and Static Variables
---------------------------------------

| Ho boy the more we learn the more we have to go back and re-learn about things we thought we knew. First the ``void`` return type, and now this.
| Though don't worry, there's gonna be even more to learn in Object Oriented Programming. That's gonna be fun.
| Also my End Of Semester Project is supposed to be an entirely functional game with a GUI and everything so....it's gonna *actually* be fun. And also time consuming and painful. But still fun. So all these concepts do get put to use.

Local Variables
^^^^^^^^^^^^^^^

.. code-block:: c++
   :linenos:

	void func1()
	{
		int n = 10;
	}

	void func2()
	{
		int n = 20;
	}

    	int main()
	{
		int n = 30;
	}

| In each of those Functions above there's a variable called ``n`` and they all have different values. Yet if you run that code, it would run completely fine.
| The reason, is that ``n`` here is a Local Variable. This means that outside of the {curly brackets} it was created in, as far as the program is concerned, it doesn't exist. So those other functions can just make their own variables called ``n`` as well.
| Arguments passed to a Function are also local. That's why the names of Arguments can be the same as the variables passed into them. You can have ``a`` and ``b`` in ``int main()`` which are passed into a function which is declared as ``int sum(int x, int y);``, and it would use ``x`` and ``y`` in its Code, but it can also just be declared as ``int sum(int a, int b);`` and it would be completely fine. In fact, that practice is usually promoted because it makes it easier to keep track of variables.

Global Variables
^^^^^^^^^^^^^^^^

.. code-block:: c++
   :linenos:
	
	int n = 10;

	void func1()
	{
		int n = 10;
	}

	void func2()
	{
		int n = 20;
	}
		
    	int main()
	{	
		int n = 30;	
	}

| This is the same code from above but with one extra line, and this line is outside of every single function. This means it was declared as a Global Variable. Global Variables are variables that can be accessed by any function. They behave like any regular function, the access is just global. This means multiple functions can also change it in different ways and make it harder to keep track of it.
| For this reason, Global Variables are usually just declared as Constants, so they can be *read* from any function, but not modified. If you need to update variables across functions, just ``return`` them from the function.
| If you initialize a value inside a function without a value, you get garbage. But if you do it globally, you get the default value as 0.

Static Variables
^^^^^^^^^^^^^^^^

| Static Variables are always Local, not Global. They work with Functions.

.. code-block:: c++
   :linenos:

	void func1()
	{
		int n = 10;
		cout << n << endl;
		n++;
	}

| If you were to call that function three times, you'd get the output of ``10``, ``10``, ``10``, all in different lines. The ``n++`` operator is there in the function, but when the Function ends and is called again, it doesn't remember the previous value. To solve this, Static Variables are used. They remember the values of previous Static Data Types.

.. code-block:: c++
   :linenos:

	void func1()
	{
		static int n = 10;
		cout << n << endl;
		n++;
	}

| *Now* if you were to call the function three times, you'd instead get ``10``, ``11``, ``12``, all in different lines. It's not re-declaring the value of ``n`` every time the function is called.
|
| The value of the static variable is only reset when the entire program ends.