.. _s1-pf-t17:

17) IF Statements and Strings
-----------------------------

| You can do comparisons on characters since they're just stored via integer. But what about strings?


.. code-block:: c++
   :linenos:

	string1 = "Bill";
	string2 = "bill";
	if (string1 == string2)
	if (string1 < string2)
	if (string1 > string2)

| The first ``if`` is self explanatory. If they're both the same, then it gets triggered. They have to be the exact same for it to work.
|
| The second and third however can be confusing. Here's how the comparison works:
|
| When two strings are compared, they aren't compared fully. They're compared letter by letter.
| ``if (string1 == string2)`` checks this:
*    is first letter of string1 == first letter of string2?
*    if yes, is second letter of string1 == second letter of string2?
*    if yes, is third letter of string1 == third letter of string2?
*    if yes, is fourth letter of string1 == fourth letter of string2?
| And so on. It checks until there aren't any more letters to check. If at some point they're not equal then the overall check is considered ``false``.
| For ``<`` and ``>``, it goes through the exact same steps, with just the symbols replaced.
|
| ``if (string1 > string2)`` checks this:
*    is first letter of string1 > first letter of string2?
*    if yes, is second letter of string1 > second letter of string2?
*    if yes, is third letter of string1 > third letter of string2?
*    if yes, is fourth letter of string1 > fourth letter of string2?
| And so on.
| ``<`` would do the exact same thing too.
|
| But what if the strings are different sized?
| Doesn't matter. The thing is, the process only goes until it either breaks or it gets through every single string.
|
| One thing to note, though,
| Doing (string1 > string2) is VERY different from doing ("Bill" > "bill") or ("Bill" < "bill").
|
| This is not something that concerns beginners much, but all you have to know is, a set of characters written inside some "double quotation marks" is just a String **Literal**. It is NOT a String!
|
| We'll learn this later. Don't worry about it for now. Remember, declare your variables!