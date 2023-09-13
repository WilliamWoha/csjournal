.. _s2-oop-t16:

16) Member Initializer List and Const Members
---------------------------------------------

| This is a way to initialize values within a Constructor. It's a stylistic choice and not that important, except for one key feature which makes it critical to know about. This is the code for a regular Initializer List: 

.. code-block:: c++

    int arr[] = {1, 2, 3, 4, 5};

| And just like that, we can initialize values of a Class using an Initializer List with the Constructor as well.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 6, 13

    class Student {
        int studentID;
        string name;
        float GPA;
    public:
        Student(int id, string n, float gpa): studentID(id), name(n), GPA(gpa) {}
    };
    class Circle {
        float x;
        float y;
        float radius;
    public:
        Circle(float x, float y, float radius): x(x), y(y), radius(radius) {}
    };

| It also seems kind of pointless and unreadable. Writing it line by line within the definition of the Constructor is far more user friendly, and it also prevents confusion from things like trying to understand what ``x(x)`` is supposed to mean. But, there's a super important use, which I'm getting to. For now, here's the details:
|
| The syntax for the Member Initializer List is ``Class(var1, var2, var3): member1(var1), member2(var2), member3(var3), member4(value) {}``. Within the ``{}`` you can continue writing the definition of the Constructor like normal. The order doesn't matter for this, only the variable names do. You can also just write the values directly. But you might be thinking, this is all possible within the Constructor Definition, so what's the reason for having them at all?
|
| They're the *only* way to initialize ``const`` and ``&`` (Reference) members of the Class. Ok, well, more specifically, they're the only way to *initialize* ``const`` and Reference members of a class. If you just write ``const float pi = 3.14159`` into the definition of the Class then it'll work completely fine, but sometimes you want to put a const value into an object, define it once, and beyond that have it be unchangeable. This can happen if you want different Objects to have different const values, which are only initialized once. So just like Member Functions, the Data Members themselves can also be ``const``, but they NEED to be initialized using the Member Initializer List.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 3, 7

    class Student {
    public:
        const long int ID;
        string name;
        char gender;
        float gpa;
        Student(long int id, string name, char gender, float gpa) : ID(id) {
            this->name = name;
            this->gender = gender;
            this->gpa = gpa;
        }
    };
    int main() {
        Student s1(31405, "john", 'M', 3.5);
        Student s2(31406, "micheal", 'M', 3.24);
    }

| So wherever you need some data to be ``const`` but it's not fully decided yet what that data is supposed to be, you use Member Initializer Lists. It exists specifically to address the challenge that different Objects might need different ``const`` Member values. It can also be used for assigning variables by reference but...I've never used it, or seen anyone use it for that. You can play around with it yourself if you want to, I won't go into details for it. Still worth a look if your uni has a habit of giving curveball questions.