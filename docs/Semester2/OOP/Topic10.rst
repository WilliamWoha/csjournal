.. _s2-oop-t10:

10) Constructors
----------------

Intro to Constructors
"""""""""""""""""""""

| This part right here is crucial for classes. Back in :ref:`s2-oop-t08` I mentioned with Access Specifiers that Classes are ``private`` by default. If you experimented with them, you'll also notice that you can't initialize the values the same way you can with a Struct.
|
| With a Struct, and also a Class where the data members are Public, this is possible:

.. code-block:: c++
   :linenos:

    Employee e1 = {"John Cena"};
    Employee e2 = {"Dwayne Johnson", 315, 9, 'M'};

| But when the Data Members are Private, this is no longer possible. It gives an error. We want to be able to initialize it, and while at it, we also want to be able to do some other things as well that all gets handled for us. Say for example, if we're making our own Class for a game, and this Class is for an enemy. Every time a new Enemy is created in the Heap, we want it to be properly initialized with stats and values. Setting variables to default values is extremely limiting, as you might want to run other code while the new Object is being created, for example running a random number generator to see what kind of enemy actually spawns or randomizing the coordinates of where it spawns, or playing a specific cutscene *only* when the Enemy is created. The Constructor allows us to not only initialize values for the Data Members, but also lets us run any code we want when an Object is created. It gives more freedom, while at the same time also putting it all behind a function, just like Member Functions.
|
| In simpler words, a Constructor is a Function that's called the moment the Object is created, and in *most cases* you want to use it for initializing values properly, but you can use it for whatever you want and however you want, because it's still a function. Here's the syntax for it:

.. code-block:: c++
   :linenos:

    class Employee {
    public:
        Employee() {
            string name = "\0";
            int ID = 0;
            double payRate = 0;
            double hours = 0;
            char gender = '\0';
            string workingDays[7] = {};
        }
    };

| You *ALWAYS* want the Constructor to be ``public``. There are only a very small amount of situations where the Constructor is supposed to be Private, and every single one of those involves making a limited amount of Objects (Singleton Pattern), or zero Objects (Utility Class, Abstract Class), and at this level you won't be doing that (Abstract Classes do come later but there's a far better way to do so than setting a constructor to Private). Now for the details.
*   A Constructor is automatically called when an Object is created
*   The purpose is to 'Construct' the Object
*   The Function Name is the Class Name
*   There is no Return Type
*   Constructors can have Out-Of-Line Declaration
*   There can be more than one Constructor
| Here's the syntax for an Out-Of-Line Constructor, and also how to actually use the Constructor when making an Object.

.. code-block:: c++
   :linenos:

    class Employee {
    private:
        string name;
        int ID;
        double payRate;
        double hours;
        char gender;
        string workingDays;
    public:
        Employee();
    };

    Employee::Employee() {
        ID = 0;
        payRate = 0;
        hours = 0;
        gender = '\0';
        // It's not necessary to set strings to be empty as they're
        // set to be empty whenever they're made.
    }

    int main() {
        Employee e1;
        Employee* e2 = new Employee;
        // There's a catch.
        // This isn't possible anymore.
        Employee e3("Dwayne Johnson", 314, 25, 7, 'M', "Monday Tuesday Wednesday");
        Employee e4("John Cena", 315, 26, 8, 'M', "Tuesday Wednesday Thursday");
        Employee e5("Ryan Gosling");
        // This is where we get to the next topic.
    }

| There's a catch, though. I found this out later and now I'm editing the page. If you make your own constructor, it replaces the constructor the Compiler makes for you, and that constructor is responsible for letting you declare classes like Structs. So the lines where ``e3``, ``e4``, ``e5`` are declared, are now invalid. I'll explain why this is happening after I explain the Parameterized Constructor.

Parameterized Constructor
"""""""""""""""""""""""""

| I wrote that there can be more than one Constructor. You might think that's strange since you're just initializing to default values. You wouldn't need more than one Constructor but...that's what's different. You're not initializing to default or empty values. You're initializing to values which you need depending on the specific data you're working with, and instead of making an Empty Object then using Setters to update values, it's easier to just put it all into the Constructor. On top of that, you can do different things depending on the type of data entered. Remember, the Constructor is just a Function. How would it differentiate between different Constructors? The same way regular Functions differentiate themselves if their names are the same: Overloading. Aka setting different parameters. Here's an example of a Parameterized Constructor:

.. code-block:: c++
   :linenos:

    class Circle {
    private:
        float x;
        float y;
        float radius;
    public:
        Circle(float x1, float y1, float radius1);
    };

    Circle::Circle(float x1, float y1, float radius1) {
        x = x1;
        y = y1;
        radius = radius1;
    }

    int main() {
        Circle c1(3, 4, 5);
        Circle c2(0, 0, 0);
        // The next declarations will give an error.
        Circle c3(3, 4);
        Circle c4(3);
        Circle c5;
    }

| A Parameterized Constructor is just a Constructor with Arguments. I set the names in the Constructor to be ``x1``, ``y1``, and ``radius1``, because you can't set them to the same names as the actual Data Members. The code however doesn't showcase having more than one Constructor at the same time. This is because I first wanted to demonstrate how Parametrized Constructors worked. There's only two other things to know about them:
*   You can set default arguments just like in regular Function Arguments
*   You can't have any other Constructors with the same or less Argument Count
| Going back to that circle, if you try to run that code, you'd get an error. This is because the declarations of ``c3``, ``c4``, and ``c5`` don't have enough information. There's two ways to deal with this. The first is to have multiple Constructors:

.. code-block:: c++
   :linenos:

    public:
        Circle();
        Circle(float x1);
        Circle(float x1, float y1);
        Circle(float x1, float y1, float r1);
    };

    Circle::Circle() {}
    Circle::Circle(float x1) {
        x = x1;
    }
    Circle::Circle(float x1, float y1) {
        x = x1;
        y = y1;
    }
    Circle::Circle(float x1, float y1, float r1) {
        x = x1;
        y = y1;
        radius = r1;
    }

| This works fine, but there's too much redundant code. A constructor is still just a function, and we can treat it like one. So we can also give it Default Arguments: 

.. code-block:: c++
   :linenos:

    public:
        Circle(float x1 = 0, float y1 = 0, float radius1 = 0);
    };

    Circle::Circle(float x1 = 0, float y1 = 0, float radius1 = 0) {
        x = x1;
        y = y1;
        radius = radius1;
    }

| You can also have multiple constructors accepting different data types as well.
|
| Something to note here, ``Circle::Circle() {}`` is (almost) the constructor the Compiler makes for you by default if you don't end up creating your own code. That's why on earlier pages there weren't any errors for writing Classes without Constructors. The compiler just handled it automatically. I say almost, I'll explain that in just a couple of paragraphs.
|
| Before I get to the last point of the page, I want to mention this. Absolutely any code can be written in those lines. You can write ``x = x1*3`` or ``y = pow(x1, y1)`` (if you imported the ``cmath`` library), or whatever else you want. It's a function and you can do whatever you want with the Arguments, beyond just putting their values into the Data Members. You can perform calculations then put them in or do whatever you wish for. It's completely up to you. It can accept any arguments at all and you can use that however you wish for the existing data types. This is just a basic example, the control is in your hands. Though the constructor with the Default Arguments would be better to implement in this specific scenario.
|
| Alright, now remember earlier on the page when I said that if you make a constructor with zero arguments, just above the Parameterized Constructor portion, that it won't accept declarations of ``Employee e3("Dwayne Johnson", 314, 25, 7, 'M', "Monday Tuesday Wednesday");``, and so on? This is because the default constructor isn't actually ``Constructor()``. It's actually ``Constructor(<brace-enclosed initializer list>)``. We've been using it a lot already, but never as a function argument. https://en.cppreference.com/w/cpp/language/list_initialization has more info about what it is and its syntax but it can be a bit hard to understand. A ``<brace-enclosed initializer list>`` is just an array-like piece of data ``{stored, between, curly, braces}`` and separated by commas. Now, although there's multiple things present between the ``{braces}``, they make it so the entire thing is technically just one piece of data, kind of like an array or struct. It's like a ``"string literal"``, it can't be stored into a data type, and the data between commas can be anything. This is extremely useful to know about because this is the easiest way to give data to constructors, even through pointer based declarations.
|
| If you don't replace the compiler's constructor, then it generates a Constructor that takes any sized ``<brace-enclosed initializer list>``. But keep something in mind: if ANY of your data members are private, it WILL NOT take any arguments for a constructor. If you use any private member you are FULLY EXPECTED to make a proper constructor. You're expected to give it something as soon as it exists because garbage values are going to cause problems. Don't just make it have garbage then use setters later, deal with it now.
|
| The whole reason I bring up the existence of this concept is because this thing is compatible with any function, and can be used to send data to a function (including constructors) in an easy manner.

.. code-block:: c++
   :linenos:

    // If all data members were public,
    // And the constructor wasn't replaced,
    // the following are all valid.
    Employee e1 = {"Dwayne Johnson1"};
    Employee e2({"Dwayne Johnson2", 315});
    Employee* e3 = new Employee({"Dwayne Johnson3", 316, 9});
    Employee* e4 = new Employee{"Dwayne Johnson4", 317, 10, 'M'};

| And here's how you'd use it if you did replace the Constructor.

.. code-block:: c++
   :linenos:

    class Employee {
    private:
        string name;
        int ID;
        double payRate;
        double hours;
        char gender;
        string workingDays;
    public:
        Employee(string n, int i, double pR, double h, char g, string wD = "Any Day") {
            name = n;
            ID = i;
            payRate = pR;
            hours = h;
            gender = g;
            workingDays = wD;
        }
        void print() {
            cout << name << '\n' << ID << '\n' << payRate << '\n' << hours << '\n' << gender << '\n' << workingDays << '\n' << endl;
        }
    };

    int main() {
        Employee e1("Dwayne Johnson", 314, 25, 7, 'M', "Monday Tuesday Wednesday");
        Employee e2({"John Cena", 315, 26, 8, 'M', "Tuesday Wednesday Thursday"});
        Employee* e3 = new Employee({"Ryan Gosling", 316, 27, 9, 'M', "Friday"});
        // Take note that even though Samuel L Jackson's arguments aren't complete,
        // this still compiles because the compiler is smart enough to pass the
        // brace-enclosed initializer list until the second last argument, and then
        // use the Default Value written for wD above. If that default value
        // wasn't present, the line would be giving an error.
        Employee* e4 = new Employee{"Samuel L Jackson", 317, 28, 10, 'M'};
        e4->print();
        
        Employee* e5 = new Employee[3]{{"A",1,1,1,'A',"A"}, {"B",2,2,2,'B',"B"}, {"C",3,3,3,'C',"C"}};
        e5[0].print();
        e5[1].print();
        e5[2].print();
    }

Default Constructors
""""""""""""""""""""

| I know, I know. This page is already really long. But this part is relevant to Parameterized Constructors so I might as well put it here, it's not much, just a little thing to note. Take a look at this code:

.. code-block:: c++
   :linenos:

    public:
        Circle(float x1 = 0, float y1 = 0, float r1 = 0);
        Circle(float a, float b);
        void print() {cout << x << " " << y << " " << radius << endl;}
    };

    Circle::Circle(float x1, float y1, float r1) {
        x = x1;
        y = y1;
        radius = r1;
    }
    Circle::Circle(float a, float b) {
        x = a + b;
        y = a - b;
        radius = a * b;
    }

    int main() {
        Circle c1(3, 4, 5);
        c1.print();
        Circle c2(4, 5);
        c2.print();
    }

| This looks fine until you try to make ``c2``. It'll give an error, because it doesn't know which of the two Constructors to call.
|
| A Default Constructor is either a Constructor with Zero Parameters (``Class() {}``), or every Parameter has a Default Value. Pretty simple. If it exists then an Object doesn't need any arguments passed into it to be brought into existence, however if a Default Constructor *doesn't* exist then the arguments are NECESSARY for the Object to be created.
|
| The only other thing to note here is, if you have a Default Constructor, then you can't have any other Constructor which has the same amount or less arguments, or the Compiler will be confused on which one to actually use. Regarding the code above, should it go into the first one, and set ``r1`` to 0? Or should it go into the second one, where ``r1`` as an argument doesn't even exist? This will only happen, however, if the Data Types are the same. If you turn ``(float a, float b)`` into ``(int a, float b)``, it'll work fine, as it's a different set of arguments entirely and there's no ambiguity present there.
|
| These errors and confusions can be avoided through Common Sense and practice, but I bring it up because my university in question has an infamous reputation of giving extremely difficult curveball questions, and if you happen to be from that same university, or any other university that does the same, then I want you to be prepared for whatever insanity it has in store.