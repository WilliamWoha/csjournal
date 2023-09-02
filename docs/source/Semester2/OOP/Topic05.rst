.. _s2-oop-t05:

5) Intro to Object Oriented Programming
---------------------------------------

| As the name suggests, this is a specific style or method of programming, that exists to deal with specific types of data. Object Oriented Programming, or OOP for short, lets you make your own data types using the primitive or base data types that C++ offers so you can deal with problems more effectively.
| Say for example you're running a company and want to hire 10 employees. Each employee will have their own gender, date of birth, ID, education experience, contact information, and so on. Every single one of these need their own variable, and that's just for one employee. When you're dealing with more employees you'd then have to turn it into a 2D array as well. And if it's a thousand employees it just gets out of hand really quickly.
| The main limitation of Arrays is that they only store one data type. What if there's another situation where you want to have an Array but for multiple varieties of data types and group them together for easy access?
| Using OOP, you can make it so instead of having an array for gender, an array for ID, an array for contact information, and so on, and then having a second dimension to it, or instead of having multiple variables and then naming them similarly to associate them, you can just make it so there's a single data type called ``Employee`` that stores all of that information for you. Sounds confusing, since there's no data type called ``Employee``. There's ``int``, ``char``, ``float``, ``double``, ``bool``, but no ``Employee``. That's because it doesn't exist yet. We're gonna make it, using Structures.

Intro to Structures
^^^^^^^^^^^^^^^^^^^

| A ``Structure`` is a user-defined data type. It's a container that lets multiple types of variables be grouped together, kind of like an Array, but without the limitation of having the same data type. Don't confuse it for an alternate of an array though, it works really differently. Structures are used to organize related data together, like ``int employeeID``, ``string name``, ``double hours``, ``double payRate``, and so on. The variables in a Structure can be of any type, and here's how to write it.

.. code-block:: c++
   :linenos:

    struct structName {
        dataType variable1;
        dataType variable2;
        // As many variables as necessary.
    };

| Here's an example of it being used practically for that employee we mentioned earlier.

.. code-block:: c++
   :linenos:

    struct Employee {
        string name;
        int ID;
        double payRate;
        double hours;
        char gender;
    };

| Now to explain it.
|
| The code written is basically what you're using to define the Structure. The {Curly Brackets} are the definition of the Structure, and anything written between them is included. The semicholon at the end is necessary. I don't know the specifics of why it's necessary, all I know is that the syntax says it's necessary. This is among the only times you'll ever write a semicholon after a set of {Curly Brackets}. Don't forget to write it!
|
| As for the part that's defined inside the Structure, you can recognize it. It's just declaring variables. That's all we're really doing with the Structure, declaring variables. Or, well, specifically in regards to this we're making a blueprint but I'll get to that later. What we're doing here is telling the Structure what kind of things we want to group together, and then later when we're working with the data, all of it will be grouped for us. It puts it all into a single package and all we have to do is refer to that package. Here's how we use it.

.. code-block:: c++
   :linenos:

    struct Employee {
        string name;
        int ID;
        double payRate;
        float hours;
        char gender;
    };

    int main() {
        Employee person1;
        person1.name = "John Cena";
        person1.ID = 314;
        person1.payRate = 25.50;
        person1.hours = 7;
        person1.gender = 'M';
        cout << "Name: " << person1.name << "\nID:" << person1.ID << "\nPay Rate: " << person1.payRate << "\nHours Per Day: " << person1.hours << "\nGender: " << person1.gender << endl;
    }

| Similar to how you used ``[]`` for accessing values of an array, you use the dot ``.`` to access the different variables that belong to a Structure. In some editors and IDE's, depending on the addons you have, you can type the . and then press tab or some other button to see what variables are available for you to call which belong to the Struct. This is especially useful if you can't remember the exact name or the name is a bit complicated. After the dot, you write the variable name, then use it like a regular variable.

Structures in Memory
^^^^^^^^^^^^^^^^^^^^

| They're just variables, there's nothing more about them. Variables that belong to a Structure are called Members. More specifically, they're called Member Variables. You'll notice in Line 10 how I declared a variable called ``person1`` of Data Type ``Employee``. This is similar to declaring the array. Later, we're using the members of the Structure, just like using elements of an Array. Giving values and outputting them. You could also use ``cin`` to give values, or randomly generate them, or do whatever you like. They're still variables and follow the rules of the primitive data types in the end.
| Any variable declared with the data type of the Structure is called an Object. In this case, ``person1`` is the object. An object can only be declared if the program recognizes the Structure first. If ``Employee`` as a Structure was defined after ``int main()`` then there would've been an error, just like calling a function that doesn't exist or is declared later. 
| One major thing to understand about a Structure is that it's a blueprint. I made the comparison to arrays to explain what it is but it's still very very different and operates differently. I hope the definition of it is understood. A Structure is a blueprint, in the sense that the variables you declare in it don't actually take up any space in memory when the Structure is defined. They only take up space when the Object is made. In this case, ``Employee`` has a string, int, double, float, and char. For simplicity's sake we'll assume a string is 4 bytes. So the total space taken would be 4+4+8+4+1, or 21 total bytes. If you were able to monitor memory usage though, you'd see that those 21 bytes aren't being allocated until ``person1`` as an Object is created. When the line is processed for creating the object, only then does it create further smaller variables and takes up space in memory.
| This means the scope the Object is made in also determines the nature of the data. Although the Structure itself is defined outside of ``int main()``, meaning it's written in the global scope, if the Object is made in ``int main()``, such as in the case of ``person1``, the variables within the Structure will have the nature of local variables. They'll have garbage values instead of being set to 0 which is what would happen if you declared an Object outside of ``int main()`` instead.