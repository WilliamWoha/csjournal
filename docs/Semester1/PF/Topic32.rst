.. _s1-pf-t32:

32) Recursions
--------------

| There's two ways to solve a problem that iterates:
*	1) Iterative Solutions (Loops)
*	2) Recursive Solutions (Recursions)
| There's nothing that can be solved only with Recursive Solutions.
| If something can be done with Recursive Solutions, then it can also be done with Loops.
|
| Iterative Solutions are usually faster and take less memory, but Recursive Solutions are easier from a designing perspective, and are especially useful for Tree Like structures and shortening code.
| But it's still limited. There's solutions that *can* be done with Loops but *can't* be done with Recursions.
|
| Data Structures is where the fun begins. I'll be doing that in Semester 3.

.. code-block:: c++
   :linenos:

	void func()
	{
		cout << "Hello World!" << endl;
	}

	for(int i = 0; i < 5; i++)
	{
		func();
	}

| This outputs `Hello World!` 5 times.
|
| A function is called a Recursive Function if it calls itself within its own code.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 4

	void message()
	{
		cout << "Hello World!" << endl;
		message(); // This is the part that makes this a Recursion.
	}

	int main()
	{
		message();
	}

| Don't actually test run that. It's an infinite loop. It will cause a Stack Overflow. Yes, just like the website. It's an infinite loop because there's no stopping condition.
| For a Recursive Function, there's two requirements:
*	1) Base Condition
*	2) Recursive Call
| A Base Condition is necessary so the recursion only continues until that point. When that condition is no longer true, it stops.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 4

	void message(int n)
	{
		if(n < 1)
			return;
		cout << "Hello World!" << endl;
		message(n-1); // This is the part that makes this a Recursion.
		// The objective is to put a new value into the Recursion, so it doesn't
		// repeat itself.
		// You could do n-- and then do message(n), but it's (according to my teachers)
		// better practice to NOT modify the original variable.
	}

	int main()
	{
		int n = 5;
		message(n);
	}

| The only way to actually properly understand Recursion is through a visual explanation of how Stacks work. Unfortunately, at the time of writing, Recursion is a weak topic of mine and I'm not very skilled at it yet. On top of that, this is only a minor topic of Semester 1 for my CS Program, so I'll go way more in depth in Semester 2, where it's a major topic.
| But if you want to know more about them then there's many YouTube videos explaining them. It's important to know how the memory itself works so this can be understood.
