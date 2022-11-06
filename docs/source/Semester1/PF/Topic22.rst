.. _s1-pf-t22:

22) Escaping Infinite Loops (Sentinel and Break)
------------------------------------------------

| So I kind of lied about the whole "You can't break out of infinite loops" thing. That was only to explain about the variables being used.
| There can be situations where you're programming loops and you don't want to run them a specific amount of times, but instead you want to run them as many times as you *need* them to, and when you don't want it to continue further, you just have some kind of button or key word to tell it to stop.
| This page tells about those situations.
|
| Let's say you have a code where you want the average marks of 50 students. That's simple, you just make a loop run 50 times to enter the values, and then to find the average, you just divide the sum by 50 to find the result!
|
.. code-block:: c++
   :linenos:
	
	int marks = 0;
	int sum = 0;
	float avg = 0;
	for(int i = 1; i <= 50; i++)
	{
		cin >> marks;
		sum = sum + marks;
	}
	avg = float(sum)/50 // The float is there to make sure it checks for decimal values

| There's a limit with that though. It only works if there's exactly 50 students.
| You can make it so that the user defines how many students there are, and hence how many times the loop will run, by doing this:

.. code-block:: c++
   :linenos:
	
	int marks = 0;
	int sum = 0;
	float avg = 0;
	int students = 0;
	cin >> students;
	for(int i = 1; i <= students; i++)
	{
		cin >> marks;
		sum = sum + marks;
	}
	avg = float(sum)/students;

| This DOES give more flexibility.
| But that's not what the Title is.
|
| What if we want to keep a loop running until I press a specific button or value to stop it?
| Now we're talking. That's where Sentinel Values come in.

Sentinel Controlled Loops
^^^^^^^^^^^^^^^^^^^^^^^^^

| It can also go by the name of Terminating Value.

.. code-block:: c++
   :linenos:
	
	int marks = 0;
	int sum = 0;
	int students = 0;
	while (marks != -1)
	{
		sum = sum + marks;
		cin >> marks;
		students++;
	}
	avg = float(sum)/students;

| This can go one time, ten times, or even a million times. It's gonna continue until the user enters the value of ``-1``, at which point it will stop.
| The sum statement is above the marks statement because, if ``-1`` is entered, it's not supposed to be added to the sum.
|
| So ``-1`` is the Sentinel Value here.
| It can be multiple values too. Setting WHILE to ``while (marks >= 0)`` would make it so that the sentinel value is *any* negative value. It's versatile, you can do whatever you want with it.

Break and Continue
^^^^^^^^^^^^^^^^^^

| Didn't expect to see this again after SWITCH statements did you? Well it's back. And this time it's actually pretty useful.
| ``break;`` lets you terminate a Loop pretty much exactly the same way as a Sentinel Value. The only difference is:
|
| Sentinel Values were dependent on the Condition check of the loop
|
| ``break;`` can make the loop stop no matter what the situation or condition
|
| It's more versatile and can do everything a Sentinel Value can, and more. The only reason Sentinel Values were even talked about was because it exists as an option and because my university can ask questions about it.

.. code-block:: c++
   :linenos:
	
	int marks = 0;
	int sum = 0;
	int students = 0;
	while (2 > 1) // Infinite Loop
	{
		sum = sum + marks;
		cin >> marks;
		students++;
		if (marks > 500)
			break;
	}
	avg = float(sum)/students;

| The code above is the Sentinel Value code converted so that it uses a ``break;`` statement to end the loop instead. The condition in the IF statement can be anything you want it to be. ``break;`` will cause the loop to end and the rest of the code to continue.