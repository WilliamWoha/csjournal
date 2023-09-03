.. _s2-oop-t07:

7) Finalizing Structures
------------------------

| This isn't even close to the end because there's still Classes, Lifetimes, Operator Overloading, Inheritance, and Polymorphism. But every single one of those is just further minute details about Structures and using them in the most effective way possible. So there's definitely a little bit of knowledge involved but the overall topic count will be less than in Semester 1. You'll still have to put in the effort and practice.
| On this page we'll be covering Nested Structures, Structures and Pointers, Member Functions, and Structures and Functions.

Nested Structures
^^^^^^^^^^^^^^^^^

| It's pretty simple. You just make a Struct, then have that Struct be a member in the definition of another Struct. You can go for as long as you want, it doesn't matter. Just treat it like a regular variable. All you wanna do is make sure that the Structure is defined before another Structure or Function tries to use it. So putting the definition of Coordinate after Circle will give an error.
| You can initialize it using {curly braces inside of more {curly braces}}.

.. code-block:: c++
   :linenos:

    struct Coordinate {
        float x = 0;
        float y = 0;
    };
    struct Circle {
        Coordinate center = {0, 0};
        float radius = 0;
        float diameter = 2*radius;
    };
    int main() {
        Circle c = {{1, 1}, 5};
        cout << c.diameter << endl;
    }
    
Structures and Pointers
^^^^^^^^^^^^^^^^^^^^^^^

| And now we return. The power of the Heap. Dynamic Memory. Pointers. But, don't worry about it. With enough practice it'll make sense.
|
| There's two things to talk about when referring to Pointers and Structures. The first is using a Structure as a regular variable, and the second is having a Pointer be a member of a Structure. The first one is ridiculously easy since we've already been doing it.

Structures as regular Variables
"""""""""""""""""""""""""""""""

.. code-block:: c++
   :linenos:

    int* ptr = new int;
    float* ptr2 = new float;
    Circle* ptr3 = new Circle;
    Circle* ptr4 = new Circle[5];
    Circle** ptr5 = new Circle*[3];

| And that's it you're done. It's the same as previous pointer usage, you just change the data type. The complications begin with trying to actually dereference and use these pointers. Unlike before, you're using a pointer to access the individual members of the Structure. So this time, you have to dereference it.

.. code-block:: c++
   :linenos:

    Circle c;
    c.center.x = 2;
    c.center.y = 3;
    c.radius = 4;
    c.diameter = c.radius * 2; // We have to update the diameter because it only sets itself to 2*radius at the time of declaration. It doesn't automatically update.
    Circle* c_ptr;
    c_ptr = &c;
    Circle* ptr;
    ptr = new Circle;
    *ptr.center.x = 4;
    *ptr.center.y = 5;
    *ptr.radius = 3;
    *ptr.diameter = *ptr.radius * 2;

| But this can be tedious to do. So a new symbol was brought up specifically for this purpose. Instead of having to write ``*struct.member``, you can just write ``struct->member``. You might have even seen this before if your teacher gave you an assignment or lab question with these. That's all it is, "Dereference this pointer and get this specific member".

.. code-block:: c++
   :linenos:

    Circle* ptr = new Circle;
    ptr->center.x = 4;
    ptr->center.y = 5;
    ptr->radius = 3;
    ptr->diameter = ptr->radius * 2;

| Keep in mind that this is specifically for Pointers so although it looks flashy, don't use it for regular Stack declared Structures. Keep to the dot for that. And also the syntax for it is more specifically ``*(struct + 0).member``, so if you try to use it for an Array of Structures then it'll only work on Index 0. For an Array of Structures you just want to do ``struct[i].member`` instead, since the ``[Subscript Notation]`` automatically does the pointer dereferencing for you.

Pointers as Structure Members
"""""""""""""""""""""""""""""

| This one is actually also pretty simple. It only gets complicated when you try and make duplicates of Structures. Although that may seem like a very small thing, it's a way bigger deal than you might think because copying values is how you have an array that can grow or shrink itself, and that's a very important functionality for a lot of situations.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 14

    struct Array {
        int* ptr;
        int size;
    };
    int main() {
        Array a1 = {new int[5], 5};
        for(int i = 0; i < 5; i++)
            a1.ptr[i] = i+1;

        Array a2 = {new int[10], 10};
        for(int i = 0; i < 10; i++)
            a2.ptr[i] = i+1;
        
        Array a3 = a1; // This is where the complications begin.
        for(int i = 0; i < 5; i++)
            cout << &a1.ptr[i] << ", " << &a3.ptr[i] << endl;
    }

| Up until line 14, the code is simple. It has two Structures, each with its own Pointer, and values are being assigned into it. They're both being given their own spaces in the Heap. All is well. But in Line 14, I wrote ``Array a3 = a1``. The way this works is that if the same Structure is used, then it copies all values from the Structure on the right (in this case a1) to the Structure on the left (in this case a3). But that's where the problem lies. It's not copying all the values of the array inside a1. All it's doing is copying the ADDRESS which ``ptr`` stores in a1. So despite a3 being a different structure, the ``ptr`` in a3 is pointing to the same location in the Heap as the ``ptr`` in a1. This is what we call a Shallow Copy. What we actually *wanted* was for a3 to have its own array with the same values as a1. That's called a Deep Copy. For now all you have to understand is that if there is any sort of Pointer, and more importantly, Heap involved in any Structure's members, you can't make a duplicate of it using ``structure2 = structure1``. I won't go into how to make the proper duplicate of it *yet* but it'll come later.
| If you run that code you'll have confirmation that the address of a1's array are the same as the addresses of a3's array.
|
| Beyond this one scenario, you can use a pointer as a member the same way you'd use a pointer for any other situation, doesn't matter. But you can be given curveball questions from this functionality so be very careful!

Anonymous Structures
^^^^^^^^^^^^^^^^^^^^

| So I holded off on presenting the next written code because I've never practically seen it used, but it can get asked and be shown in specific exam questions so now's a good time as any. Other than doing ``structName objectName`` in any function, such as ``Circle c``, you can also declare an Object by writing its name directly after the Structure Definition.

.. code-block:: c++
   :linenos:

    struct Circle {
        float centerX = 0;
        float centerY = 0;
        float radius = 0;
    } c1, c2;

| So now c1 and c2 are declared as global structures (if this was made outside of a function) or as local structures (if this was made inside of a function). It's a super quick and easy way to make them directly.
| 
| As for Anonymous Structures, they're structures without a name. The above methodology is the only way to actually make them.

.. code-block:: c++
   :linenos:

    struct {
        float centerX = 0;
        float centerY = 0;
        float radius = 0;
    } c1, c2;

| So now c1 and c2 are Anonymous Structures. You can't declare any further structures with this kind of body, but you can use c1 and c2 the same way you'd normally use a structure. This is a very very niche functionality though so I won't go into the details because I myself have never used it. It exists and might get asked in exams which is why it's the only reason I mention it. I don't know how to associate a pointer with them, if it's even possible, or what happens if I do c1 = c2.

Structures and Functions
^^^^^^^^^^^^^^^^^^^^^^^^

| Honestly this would just be a massive copy paste of the Pointers section so all you have to understand regarding using Structures as return types or arguments for pointers is that they should be defined before the function's definition....and that's it. Then you can use them like regular variables. You can either pass members of Structures for specific functions, or pass the entire Structure if you want. You can still pass by reference or by value. The thing to note is that passing by Value can be super slow if the Structure is very large and complex, so passing by reference is significantly faster. But doing so can cause changes in the Struct you might not want, which is why if you're dealing with a Large Structure and don't want changes when passing to a function, then pass by Const Reference.

.. code-block:: c++
   :linenos:

    void func(const Circle& c) {
        // Commands
    }

| Just depends on the use case what you want to do.
|
| The reason why this would be a copy paste is because just like Pointers can be part of the Structure Definition, so can Functions. And this may not make sense since Pointers and Functions are very different, and a Pointer is more of a Variable, but I'll explain.
|
| Structures can have Functions inside of them. We call these Member Functions. Structures are more than just a way to group variables together, they're also a way to assign functionality to specific pieces of data and make things easier to manage. Here's an example:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 5, 8, 11

    struct Circle {
        float centerX = 0;
        float centerY = 0;
        float radius = 0;
        float findArea() {
            return radius * radius * 3.1416;
        }
        void printCenter() {
            cout << "(" << centerX << ", " << centerY << ")" << endl;
        }
        void updateCenter(float x, float y) {
            centerX = x;
            centerY = y;
        }
    };
    int main() {
        Circle c = {1, 1, 5};
        cout << c.findArea() << endl;
        c.printCenter();
        c.updateCenter(2,3);
        c.printCenter();
    }

| The functions were defined as normal, but there's a few things to note here. The first being that variables defined inside the Structure didn't need to be defined again in the Function. As far as the Function is concerned, they already exist. It has access to those variables. The second thing is that you call the functions the same way you access member variables: with the dot ``.`` operator.
| The other rules of return types, arguments, and everything else, will still apply. They're still functions. But they're intended to specifically be used with the Structure.
| You can send data which has absolutely nothing to do with the function, but you NEED an Object to exist to be able to call it. This is why the Functions in question are called Member Functions. They're not normal functions, they're associated with that specific Structure.
|
| That's it, we're done. Structures is finished. But now the real fun begins.