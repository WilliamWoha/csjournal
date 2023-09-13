.. _s2-oop-t14:

14) Static Class Members
------------------------

Static Member Variables
"""""""""""""""""""""""

| Let's say you have the following code:

.. code-block:: c++
   :linenos:

    class Circle {
    public:
        float x;
        float y;
        float radius;
        Circle(float x1 = 0, float y1 = 0, float r = 0) {
            x = x1;
            y = y1;
            radius = r;
        }
    };
    int main() {
        Circle c1(1,3,4);
        Circle c2(2,5,11);
        Circle c3(-3,-8, 5);
    }
    
| It's obvious that each individual circle is going to have its own set of values for ``x``, ``y``, and ``radius``. They're not shared. It's separate variables within each Object. However, there are situations where we might want all the Objects to share a variable. Kind of similar to a Shallow Copy, but this time we *want* to do it, so there's a better approach. That's what Static Class Members do. They make it so that no matter what the Object Count is, even if it's 0, the variable is already declared in the ``DATA`` portion of the Memory. It doesn't exist within the confines of a single object, and every instance of the Class (meaning every individual Object) has access to it. You can think of them as belonging to the class instead of the object. Here's the syntax for it:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 6, 11, 14, 17
   
    class Circle {
    public:
        float x;
        float y;
        float radius;
        static int circleCount;
        Circle(float x1 = 0, float y1 = 0, float r = 0) {
            x = x1;
            y = y1;
            radius = r;
            circleCount++;
        }
        ~Circle() {
            circleCount--;
        }
    };
    int Circle::circleCount = 0;
    int main() {
        Circle c1(1,3,4);
        Circle c2(2,5,11);
        Circle c3(-3,-8, 5);
        cout << c1.circleCount << endl;
        Circle* c4 = new Circle;
        Circle* c5 = new Circle;
        cout << c4->circleCount << endl;
        delete c4;
        cout << Circle::circleCount << endl;
    }
    
| Lines 6 and 17 are highlighted. They're the lines that define the static member. It is *NECESSARY* for a static variable to be declared as in-line then defined out-of-line. You can't just do ``static int circleCount = 0`` in Line 6 to initialize it. It gives an error. Also, that `` = 0`` at the end of it also isn't necessary. If it's not written it automatically sets itself to 0, but if you want to initialize it to some other value then it's necessary to write `` = value``.
|
| The variable is made only once, at compile time. It can be both Public or Private.
*   In the case of Public, it can be accessed like normal public members, such as doing ``c1.circleCount``, but it can also be accessed just by writing the class name directly (which is arguably way cooler), by doing ``Circle::circleCount`` instead. Both non-static and static Member Functions can be used to access it as well. We'll get to what static Member Functions are later in the page.
*   In the case of Private, it can't be accessed through normal means. ``c1.circleCount`` won't work, and neither will ``Circle::circleCount``. You'll have to use a Getter function for it, like you normally do for private members.
| The lifetime of the static member variable is the lifetime of the entire running program. It's created the moment the program starts, and ends the moment the program ends. Objects can be made and destroyed anywhere in the middle, but the static data member is beyond these operations. It already exists before a single object of a class has the opportunity to.

Static Member Functions
"""""""""""""""""""""""

| These are Member Functions with just one key difference: They operate *only* on Static Data Members, and if you try to use regular Data Members within the function definition then it'll give an error. This limit exists for a very specific reason: Just like static Data Members, static Member Functions can also be called by writing ``Class::Function()`` (if it's public). You don't need to create an object in order to access them. This is why, if they try to access non-static data members or non-static functions, then it'll call an error at compile time because those are specific to Objects. For this reason, they're more used for Utility Classes, which are Classes that are specifically filled with static Member Functions and maybe a few const static variables, and exist purely to provide functions within a namespace. If I have my own ``math`` class, for example, I'd have const static members for pi, and functions for calculating exponent or logarithm or anything really. You've already been using utility classes, but you just didn't know that because of ``using namespace std``. The functions you call, such as ``pow(a, b)``, or even ``cout``, are in reality ``std::pow(a, b)`` and ``std::cout``.
|
| Ok the truth is, ``pow(a, b)`` and ``cout`` aren't actually from utility classes, they're just local functions within the ``std`` (meaning standard) namespace. A namespace just happens to be a set of {curly braces}, and between those braces, whatever function you write has to be accessed via ``namespace::function()``. But it acts close enough that I can put it here to explain the concept. You can't actually do ``using namespace Math``. It's a different thing that just happens to operate very very similarly. One's a class, the other is a namespace, and there's a difference in how they're written in code, but in terms of functionality they're basically identical. Here's a code of a sample Math Utility Class:

.. code-block:: c++
   :linenos:
   
    #include <iostream>
    // using namespace std;
    class Math {
        public:
        static int add(int a, int b) {return a+b;}
        static int mul(int a, int b) {return a*b;}
    };
    int main() {
        std::cout << Math::add(3,4) << std::endl;
        std::cout << Math::mul(3,4) << std::endl;
    }
    
| And just like Public and Private Data Members, they can either be called if public through an object or through the class name directly, or if they're private then they can be called from within the Class itself.