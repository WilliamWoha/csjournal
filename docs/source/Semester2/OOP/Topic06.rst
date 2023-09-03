.. _s2-oop-t06:

6) More about Structures
------------------------

| There's gonna be a loooot of different stuff about Structures to explain. It's basic stuff, just a lot of it. You'll get the hang of it with practice.

Initializing a Structure
^^^^^^^^^^^^^^^^^^^^^^^^

| On the previous page you saw code that assigned values to the Structure using multiple lines. This can be tedious to do. There's an easier way, which is extremely similar to initializing the values of an array.

.. code-block:: c++
   :linenos:

   StructName object = {Value1, Value2, ...};

| Here's an example:

.. code-block:: c++
   :linenos:

    struct Employee {
        string name;
        int ID;
        double payRate;
        double hours;
        char gender;
    };

    int main() {
        Employee e1 = {"John Cena", 314, 25.5, 7, 'M'};
    
| It's necessary for the values to be written in the same way they're written in the actual blueprint. Since ``name`` comes first, we write ``"John Cena"`` first. It's in the same sequence.
| You can also just use ``cin`` or whatever other method you want after it's declared normally. It just depends on you what you wanna do, I'm just listing the options.
| You're also allowed to initialize only some members, but you can't skip over specific variables.

.. code-block:: c++
   :linenos:

    // This is fine. The others just become 0.
    Employee e1 = {"John Cena"};
    // This is NOT fine.
    Employee e2 = {"Dwayne Johnson", 315, , 9, 'M'};
    // You can't skip over.

| You can also give the default values inside the structure definition itself, similar to a function's arguments. In this case I've made it so it's easy to identify if the variable has valid values or not. You can have other placeholder values as well.

.. code-block:: c++
   :linenos:

    struct Employee {
        string name = "\0";
        int ID = 0;
        double payRate = 0;
        double hours = 0;
        char gender = '\0';
    };
    
Structures as Variables
^^^^^^^^^^^^^^^^^^^^^^^

| This is where the real magic happens. This is how structures make your life easier to manage data. Now that the intro's done, here's how to use it like a regular variable so it makes your life easier.
|
| A structure can be assigned to another variable only if they're both the exact same structure. I'll write this now but explain later, this can be done ONLY if the Structures are all using Static memory. If any form of dynamic memory is involved, this method won't work. I'll explain the details later but all you need to know now is, if you were wondering why there's basically zero pointers on the previous page and this one, it's because the heap in structures makes things slightly complicated. One step at a time.

.. code-block:: c++
   :linenos:

    Employee e1 = {"John Cena", 314, 25.5, 7, 'M'};
    Employee e2 = e1;
    Employee e3;
    e3 = e2;
    
| You can't compare structures directly. ``if (e1 == e2)`` isn't valid. You have to compare them using their individual members.
|
| A Structure having the same nature as a regular variable means you can also create an Array out of it.

.. code-block:: c++
   :linenos:

    Employee employees[100];

| Each individual index in the array ``employees`` is an individual structure, each with its own individual value. This is what makes it so helpful in managing data. You didn't need any 2-Dimensional pointers. Just a Structure for an Employee, and boom you just turn that into an Array and you're all set.
| You can also initialize values the same way you would for a regular array.

.. code-block:: c++
   :linenos:

    Employee employees[4] = {{"John Cena", 314, 25.5, 7, 'M'}, {}, {"Dwayne"}};

| It's also possible to have an array inside the definition of the Structure itself. You can also initialize that using the methods above.

.. code-block:: c++
   :linenos:

    struct Employee {
        string name = "\0";
        int ID = 0;
        double payRate = 0;
        double hours = 0;
        char gender = '\0';
        string workingDays[7] = {};
    };
    
    Employee e1 = {"J", 2, 200, 40, 'F', {"Monday", "Wednesday", "Friday"}};