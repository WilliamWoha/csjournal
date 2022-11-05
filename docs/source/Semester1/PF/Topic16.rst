.. _s1-pf-t16:

16) IF Statements and FLAGS
---------------------------

| This is honestly my favourite thing to use with IF statements, it just makes things SO much easier.
| Here's some code for checking a leap year.


.. code-block:: c++
   :linenos:

	int year;
	cout << "Enter year number: ";
	cin >> year;
	if (year % 4 == 0)
	{
		if (year % 100 == 0)
		{
			if (year % 400 == 0)
			{
				cout << "Hey, good news!" << endl;
				cout << "The number you entered?" << endl;
				cout << "It's!" << endl;
				cout << "a!" << endl;
				cout << "Leap!" << endl;
				cout << "Year!" << endl;
			}
			else
			{
				cout << "Hey....I got some bad news." << endl;
				cout << "The number you entered?" << endl;
				cout << "It's...." << endl;
				cout << "not a leap year." << endl;
				cout << "I'm sorry." << endl;
			}
		}
		else
		{
			cout << "Hey, good news!" << endl;
			cout << "The number you entered?" << endl;
			cout << "It's!" << endl;
			cout << "a!" << endl;
			cout << "Leap!" << endl;
			cout << "Year!" << endl;
		}
	}
	else
	{
		cout << "Hey....I got some bad news." << endl;
		cout << "The number you entered?" << endl;
		cout << "It's...." << endl;
		cout << "not a leap year." << endl;
		cout << "I'm sorry." << endl;
	}

| If you've never done the code for a Leap year before, now you know it's that.
| If you think there's too many lines and you could just write one ``cout`` statement to say ``cout << "Leap year" << endl;`` or ``cout << "Not a Leap Year" << endl`` then yes, you can in fact do that. But I did this on purpose.
| The code works fine, but the problem is that it repeats itself.
|
| It's either a Leap Year or it's not a Leap Year, and we have multiple conditions to check, but the thing is, if mutliple of those end up doing the same thing, then there's a lot of repitition involved. So, we use Flags to reduce that repitition.

.. code-block:: c++
   :linenos:

	bool flag;
	int year;
	cout << "Enter year number: ";
	cin >> year;
	if (year % 4 == 0)
	{
		if (year % 100 == 0)
		{
			if (year % 400 == 0)
			{
				flag = true;
			}
			else
			{
				flag = false;
			}
		}
		else
		{
			flag = true;
		}
	}
	else
	{
		flag = false;
	}
	//
	if (flag == true)
	{
		cout << "Hey, good news!" << endl;
		cout << "The number you entered?" << endl;
		cout << "It's!" << endl;
		cout << "a!" << endl;
		cout << "Leap!" << endl;
		cout << "Year!" << endl;
	}
	else
	{
		cout << "Hey....I got some bad news." << endl;
		cout << "The number you entered?" << endl;
		cout << "It's...." << endl;
		cout << "not a leap year." << endl;
		cout << "I'm sorry." << endl;
	}
|
| The {} aren't necesary, but I kept them because it's easier to see which ``else`` statement belongs to which ``if`` statement.
|
| Anyways. You might be looking at that and thinking that this only increased the number of lines being used.
| Well you'd be right, but not for long. If the part being repeated was longer, or if there were more repititions, then the code would *very* easily become shorter with flags. The point is to reduce repetitions so the number of lines is less, and in some cases it can also be used to make sure there's only one output. I can't show the code since it was around 700 lines but Flags were the key in making sure that Output statements also didn't end up repeating themselves.