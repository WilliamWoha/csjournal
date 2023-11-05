.. _s2-oop-t20:

20) Every Operator Overloaded
-----------------------------

| So this page just serves as an entire list on how to overload pretty much every single Operator. It'll be divided into three categories:
*   Most Used
*   Less Used
*   Never Used
| These aren't real terminologies, I just categorized into that myself. I'll be researching and putting the *entire* list you saw on the previous page here. Here's the list again so you don't have to scroll back:
|
.. list-table:: Operators that can be overloaded
   :widths: auto
   :align: center

   * - ``+``
     - ``-``
     - ``*``
     - ``/``
     - ``%``
     - ``^``
     - ``&``
     - ``|``
   * - ``~``
     - ``!``
     - ``=``
     - ``<``
     - ``>``
     - ``+=``
     - ``-=``
     - ``*=``
   * - ``/=``
     - ``%=``
     - ``^=``
     - ``&=``
     - ``|=``
     - ``<<``
     - ``>>``
     - ``<<=``
   * - ``>>=``
     - ``==``
     - ``!=``
     - ``<=``
     - ``>=``
     - ``&&``
     - ``||``
     - ``++``
   * - ``--``
     - ``->*``
     - ``,``
     - ``->``
     - ``[]``
     - ``()``
     - ``new``
     - ``delete``
   * - ``new[]``
     - ``delete[]``
     -
     -
     -
     -
     -
     -

|
.. list-table:: Operators that can't be overloaded
   :widths: auto
   :align: center

   * - ``.``
     - ``.*``
     - ``::``
     - ``?:``
     - ``sizeof``

|
| There's plenty of other categorizations for the Operators, as shown on https://www.geeksforgeeks.org/operator-overloading-cpp/. It's not important though. All you have to understand is how to actually overload the operator *properly* so it behaves similar to the existing base data types we currently have. This will depend significantly on the actual Class you're trying to implement, though. For example, if you have a ``Car`` class, you can't exactly add or multiply two cars together. So I'll have four sample classes to cover the entire list:
*   Complex Real Number (Covers ``+``, ``-``, ``*``, ``/``, ``=``, ``+=``, ``-=``, ``*=``, ``/=``, ``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``, ``++``, ``--``)
*   Complex Integer Number (Covers all of the above, ``%``, ``%=``)
*   Set (Covers ``^``, ``&``, ``|``, ``^=``, ``&=``, ``|=``, ``= with Heap``, ``[]``)
*   Matrix/2D Array (Covers ``() with multiple inputs``)
*   Iostream (Covers ``<<``, ``>>``)
|

Never Used
^^^^^^^^^^

| This is just ``,``, ``~``, ``!``, ``&&``, ``||``, ``->``, ``->*``, ``new``, ``delete``, ``new[]``, ``delete[]``, ``<<=``, and ``>>=``. These operators are used for such specific purposes that you gain practically nothing from overloading them. They're best left alone because you might compromise on the readability of your program. I put the "Never Used" stuff first to get it out of the way for the rest of the page. You can search documentation on using those operators if you want. The only practical I can even think of for some of them is making your own data type which holds larger values, such as a 128-bit integer Class called ``BigInt``, where you'll want to implement ``>>=``, ``<<=``, ``&&``, and ``||`` as Bitwise Operations for said Class. I can't even think of what to do for the others. Yes I did say you can have the operators carry out any function code but if you don't immediately know what the operator is doing, then it's better to have an actual function instead. If I do ``!var``, and ``var`` is a Class of Complex Number, what do I get from it? There's no such thing as ``NOT(Complex Number)``. If you want to check if the Complex Number's Imaginary Part is 0 then you're better off writing a function. ``if (var.isRealOnly())`` is far more readable than ``if (!var)``, because you immediately know what the function is doing. If you do end up having a Class where these operators make sense to implement then go for it, I'm just trying to emphasize on the readability, as it matters to both your future self and your colleagues later.
|
| Also, ``[][]`` isn't an operator, hence why I used ``()`` with multiple inputs instead. To use that you have to cascade it so that the first ``[]`` returns an object, and that object then calls ``[]`` to return a value. The only challenge with that is, if you're working with only one object which has a multi-dimensional array, such as a Matrix, then you need to use a Proxy. You can look it up if you're curious, I never ended up using it. Easier just to make a function ``grabElement(int row, int col)`` or to use the ``()`` operator.

Most Used
^^^^^^^^^

| I'll be doing the in-line declarations for all the operator functions here, then on the rest of the page doing the syntax for each operator. All will be explained in order, and if you want to run the code yourself you can download the file I've linked at the end of the page.
|
| Also I ditched the ``ComplexReal`` class because it was a carbon copy of the ``ComplexInt`` class except for not having the ``%`` operator, and also just using ``float`` instead of ``int``. It was easier to just cover the operators all within ``ComplexInt`` as it had the ``%`` operator as well.
|
| Last reminder that the current implementation is only *one* example of using the operators in this way. You can use them however you like, and however it benefits you. Just remember, readability is the priority. If you have to look at the code itself to see what the function is doing, you've messed up.

.. code-block:: c++
   :linenos:

    #include <iostream>
    #include <math.h>
    using namespace std;

    class ComplexInt {
    private:
      int real;
      int imag;
    public:
      ComplexInt(int real = 0, int imag = 0);
      ComplexInt(const ComplexInt& copy);
      int getReal() const;
      int getImag() const;
      void setReal(int real);
      void setImag(int imag);
      ComplexInt operator+(int r);
      ComplexInt operator+(const ComplexInt& obj);
      ComplexInt operator-(const ComplexInt& obj);
      ComplexInt operator*(const ComplexInt& obj);
      ComplexInt operator/(const ComplexInt& obj);
      ComplexInt operator%(const ComplexInt& obj);
      ComplexInt operator=(const ComplexInt& obj);
      ComplexInt& operator+=(const ComplexInt& obj);
      ComplexInt& operator-=(const ComplexInt& obj);
      ComplexInt& operator*=(const ComplexInt& obj);
      ComplexInt& operator/=(const ComplexInt& obj);
      ComplexInt& operator%=(const ComplexInt& obj);
      bool operator<(const ComplexInt& obj);
      bool operator>(const ComplexInt& obj);
      bool operator==(const ComplexInt& obj);
      bool operator!=(const ComplexInt& obj);
      bool operator<=(const ComplexInt& obj);
      bool operator>=(const ComplexInt& obj);
      ComplexInt& operator++();
      ComplexInt operator++(int dummy);
      ComplexInt& operator--();
      ComplexInt operator--(int dummy);
    };
    ComplexInt::ComplexInt(int real, int imag) {
      this->real = real;
      this->imag = imag;
    }
    ComplexInt::ComplexInt(const ComplexInt& copy) {
      cout << "COPY CONSTRUCTOR CALLED!" << endl;
      this->real = copy.getReal();
      this->imag = copy.getImag();
    }
    int ComplexInt::getReal() const {
      return real;
    }
    int ComplexInt::getImag() const {
      return imag;
    }
    void ComplexInt::setReal(int real) {
      this->real = real;
    }
    void ComplexInt::setImag(int imag) {
      this->imag = imag;
    }

operator+
"""""""""

| In :ref:`s2-oop-t15` you saw an implementation of Operator Overloading. Unfortunately, it was an example of a poorly implemented overload, as for ``operator+``, it affected the original class. It was doing what ``operator+=`` should have been doing instead. The only way to make an Operator Overload without affecting the original values, is to create a temporary Object, do the changes in that, and return that instead. Here's the proper implementation:

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator+(const ComplexInt& obj) {
      ComplexInt temp(*this); // Copy Constructor
      temp.setReal(this->getReal() + obj.getReal());
      temp.setImag(this->getImag() + obj.getImag());
      return temp;
    }

| This is what allows us to properly do something like ``c4 = c1 + c2 + c3`` without harming ``c1``, ``c2``, or ``c3`` in the process. And making a temporary Object is going to be a very recurring pattern throughout most of these definitions.
|
| Since this is a regular function, you can also overload it as such. In this case, you can make it accept ``int`` as an argument if you want to add a regular number to it.

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator+(int n) {
      ComplexInt temp(*this); // Copy Constructor
      temp.setReal(this->getReal() + n);
      temp.setImag(this->getImag());
      return temp;
    }

operator-
"""""""""

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator-(const ComplexInt& obj) {
      ComplexInt temp(*this);
      temp.setReal(this->getReal() - obj.getReal());
      temp.setImag(this->getImag() - obj.getImag());
      return temp;
    }

operator*
"""""""""

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator*(const ComplexInt& obj) {
      // General formula for multiplying two complex numbers is
      // (a+bi)(c+di) = (ac-bd) + i(ad+bc)
      ComplexInt temp;
      int a = this->getReal();
      int b = this->getImag();
      int c = obj.getReal();
      int d = obj.getImag();
      temp.setReal(a * c - b * d);
      temp.setImag(a * d - b * c);
      return temp;
    }

operator/
"""""""""

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator/(const ComplexInt& obj) {
      // General formula for dividing two complex numbers is
      // (a+bi)/(c+di) = ((ac+bd)/(cc+dd)) + i((bc-ad)/(cc+dd))
      ComplexInt temp;
      int a = this->getReal();
      int b = this->getImag();
      int c = obj.getReal();
      int d = obj.getImag();
      temp.setReal((a * c + b * d) / (c * c + d * d)); // ac+bd / cc + dd
      temp.setImag((b * c - a * d) / (c * c + d * d)); // bc-ad / cc + dd
      // Got these formulas off the internet.
      return temp;
    }

operator%
"""""""""

| The neat thing about a lot of Operator Overloading is, you only need to do half of it. In this case, ``%`` is by definition, ``a % b == a - ((a / b) * b)``. Since we've already implemented ``-``, ``/``, and ``*``, we can just re-use those.

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator%(const ComplexInt& obj) {
      return *this - ((*this / obj) * obj);
    }

| This also doesn't need a Copy to be made because we're not modifying ``*this`` in any way. Also, this is how you send an object into a function that involves using itself: with ``*this``. But you do have to be careful with it, you don't want to send the object into itself and cause an infinite recursion. That's what happens when you do a Copy Constructor by Value instead of by Reference.

operator= (Shallow Copy)
""""""""""""""""""""""""

| This operator is already overloaded by the Compiler. In :ref:`s2-oop-t13` I explained the Copy Constructor and how it works with the Heap. The part that I explained though, was ``obj c2 = c1;``, which calls the copy constructor. I didn't explain ``obj c2; c2 = c1;`` which are two separate lines. The Assignment Operator ``=`` is already overloaded, just like the Copy Constructor, but it makes a Shallow Copy. In the case of ``ComplexInt``, this is fine, but we'll come back to this later for a Deep Copy when dealing with ``Set``.
|
| This next bit of code isn't necessary but you can still write it if you want, or do whatever else you want with it. It's just what the compiler would make if you didn't overload it.

.. code-block:: c++
   :linenos:
   
    ComplexInt ComplexInt::operator=(const ComplexInt& obj) {
      this->real = obj.getReal();
      this->imag = obj.getImag();
      return *this;
    }

| https://en.cppreference.com/w/cpp/language/operator_assignment has more info about the Assignment Operator. As far as the Compiler's own version is concerned, it tries to make sure that if you do ``a = b``, then ``b`` is something that can be converted and applied to ``a``. For example, if you have a ComplexInt called ``c2``, and you do ``c2 = 20;``, then you'd think it doesn't work, but it does, because ``20`` can be converted into a ComplexInt, since we have a constructor for it. ``c2 = 20;`` is the same as doing ``c2 = ComplexInt(20);``, and since ``ComplexInt(20)`` is valid, the conversion works. If we do something like ``c2 = 'a'`` then it wouldn't work, but if we had a constructor for it, then it could. Play around with it.
    
operator+=
""""""""""

| This is where you DO want to affect the original class. So this time, you won't need a temporary object.

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator+=(const ComplexInt& obj) {
      this->real += obj.getReal();
      this->imag += obj.getImag();
      return *this;
    }

| There's one thing which is different about this: the Return Type is ``ComplexInt&``, and not ``ComplexInt``. Normally you're used to sending by reference, but *returning* by reference? That's new. But it's pretty simple, the logic is identical. In fact we already covered it at the end of the page in :ref:`s2-oop-t13`. Just like how we use a Reference so the Copy Constructor doesn't have to be called when passing an object to a function, we also use a Reference to return an object from it. There's two things that make it special, though. Unlike Copy Elision, which depends on the Compiler, this is *guaranteed* to not make a Copy. The only catch? It's only meant to be used when you know you're modifying the current Object *and* returning it. You can't use it on anything that returns ``*this`` without modifying it.
|
| I didn't mention this earlier but now seems a good time to mention it: If you do something like ``c3 = c1 + c2``, you'll have a Constructor called. Whether you made a Blank then set the values later, or used a copy, it doesn't matter. A Constructor was called because you used ``temp`` in ``operator+``. This is because you're using the values of ``c1`` but you don't want ``c1`` to be affected. You can't do anything about that, but what you *can* do is reduce further constructor calls. The next example of code calls a Constructor *three times*.

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator+=(const ComplexInt& obj) {
      *this = *this + obj;
      return *this;
    }

| The first one is called when evaluating ``*this + obj``, as there's a ``temp`` Object being created within that Function. The second one is called when the object is returning from that. This one's optional, and depends on the Compiler. In my testing with Visual Studio, it called the constructor, but for other compilers it might not. The third one is called when returning the object for ``operator+=``, which you might have known if you noticed that this time I removed the ``&`` in the Return Type. All of this, as opposed to the previous block of code, which calls the copy constructor a whopping *zero times*.
|
| The general rule of thumb is, if you're going to be modifying the object that's calling the function, then it's better to return by reference. This applies to both operator overloads and functions, I just didn't do it before because you're usually not returning an Object. That functionality really just exists for function cascading. That, and it's way more relevant and easier to understand here.

operator-=
""""""""""

| Same deal as ``operator+=``. Nothing extra here.

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator-=(const ComplexInt& obj) {
      this->real -= obj.getReal();
      this->imag -= obj.getImag();
      return *this;
    }

operator*=
""""""""""

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator*=(const ComplexInt& obj) {
      int a = this->getReal();
      int b = this->getImag();
      int c = obj.getReal();
      int d = obj.getImag();
      this->setReal(a * c - b * d);
      this->setImag(a * d - b * c);
      return *this;
    }

operator/=
""""""""""

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator/=(const ComplexInt& obj) {
      int a = this->getReal();
      int b = this->getImag();
      int c = obj.getReal();
      int d = obj.getImag();
      this->real = (a * c + b * d) / (c * c + d * d);
      this->imag = (b * c - a * d) / (c * c + d * d);
      return *this;
    }

operator%=
""""""""""

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator%=(const ComplexInt& obj) {
      *this = *this - (*this / obj) * obj;
      return *this;
    }

| This one is inefficient but realistically this isn't an implementation where you have to worry about optimizing it. It's more when dealing with larger objects, say a matrix of size 1000 by 1000, and you want to perform a modulo on every single element within that matrix individually. That's when you should be concerned about Constructors and Optimization. In that case you'd directly write code to modify, like shown above. It'll be more effort for you but way less effort for your computer. I just wrote it like this because I was feeling lazy, you're free to optimize it however you wish.

operator<
"""""""""

| That covers just about all the arithmetic operators. Now we'll be dealing with a different category. Notice how the return type for this is ``bool``. That's because this is frequently used in IF statements for comparisons. So for any comparison operators, such as ``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``, you'll be using ``bool`` to tell if it's either ``True`` or ``False``.

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator<(const ComplexInt& obj) {
      // This is the formula for the Modulo of a Complex Number.
      // It's just distance from origin on real/imaginary plane.
      float abs1 = pow(pow(this->real, 2) + pow(this->imag, 2), 0.5);
      float abs2 = pow(pow(obj.getReal(), 2) + pow(obj.getImag(), 2), 0.5);
      return abs1 < abs2;
    }

operator==
""""""""""

| Although from the code above, the next in line is ``operator>``, I want to implement ``operator==`` first because it lets us pull a neat trick for making things easier.

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator==(const ComplexInt& obj) {
      bool equal == true;
      if(this->real != obj.getReal())
        equal = false;
      if(this->imag != obj.getImag())
        equal = false;
      return equal;
    }
    
operator>
"""""""""

| Voila!

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator>(const ComplexInt& obj) {
      return !(*this < obj && *this == obj);
    }

| Since ``a > b`` (``a`` is Greater Than ``b``) is the same as writing ``!(a <= b)`` (``a`` is NOT Less Than Or Equal To ``b``), we used that to our advantage for not having to write separate code for ``>``. You still *can* write separate code, and honestly speaking I don't know if C++ practices say you *should* write separate code or re-use the operators, but it'll serve your purposes for now. Simply having ``==`` and ``>`` or ``<`` overloaded lets you overload all the other comparison operators. The neat thing here is that it's not un-optimized, since there's no Constructors or Copy Constructors being called within any of those operators.

operator>=
""""""""""

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator>=(const ComplexInt& obj) {
      return *this > obj || *this == obj;
    }
    
operator<=
""""""""""

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator<=(const ComplexInt& obj) {
      return *this < obj || *this == obj;
    }

operator!=
""""""""""

.. code-block:: c++
   :linenos:

    bool ComplexInt::operator!=(const ComplexInt& obj) {
      return !(*this == obj);
    }
    
operator++ (Pre-increment)
""""""""""""""""""""""""""

| Finally we get to Increment and Decrement. These are also pretty simple, and use previous concepts to be implemented. First we'll be looking into Pre-increment.

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator++() {
      this->real++;
      this->imag++;
      return *this;
    }

| Pretty simple. Just write ``++c1`` and it works. Returning by reference since we're modifying the original value. We'll repeat for Decrement too.

operator-- (Pre-decrement)
""""""""""""""""""""""""""

.. code-block:: c++
   :linenos:

    ComplexInt& ComplexInt::operator--() {
      this->real--;
      this->imag--;
      return *this;
    }

operator++ (Post-increment)
"""""""""""""""""""""""""""

| There's a small challenge with this, though. The compiler needs a way to differentiate between pre-increment and post-increment, but they're the same operator. So it just made it so the syntax for Post Increment and Decrement just has a Dummy Integer as an argument. The integer in question is never going to be used, and it *has* to be an integer. I tried using a ``char`` to save space but it gave an error instead. The integer just the syntax for it.
|
| Also, since it's a post increment, you have to use a Copy Constructor here to return the previous value. That's also the reason why we return by value instead of by reference, as compared to the code blocks above.

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator++(int dummy) {
      ComplexInt temp(*this);
      this->real++;
      this->imag++;
      return temp;
    }

| The logic is that whatever arithmetic shenanigans you're doing when it comes to *post-increment* (or decrement) will use the current value, and behind the scenes, the value increments. No, this doesn't have anything to do with multiple increments or decrements in one line. That still depends on the compiler, and you're still compromising readability with that and you shouldn't do so.

operator-- (Post-increment)
"""""""""""""""""""""""""""

.. code-block:: c++
   :linenos:

    ComplexInt ComplexInt::operator--(int dummy) {
      ComplexInt temp(*this);
      this->real++;
      this->imag++;
      return temp;
    }


Less Used
^^^^^^^^^

| The operators you see beyond this point use symbols that are specific. Other than a set and a custom numerical data type, I couldn't really think of any major examples for where they could practically be implemented. This was easier to do than a custom number.
|
| Another reminder that these operators can do absolutely anything since they're still functions in the end, but the purpose is readability. For that reason I chose SETs as an example class to implement.

.. code-block:: c++
   :linenos:

    #include <iostream>
    #include <math.h>
    using namespace std;
    
    class Set {
      // We'll keep things simple and keep it as a Set of Integers.
      // You'll figure out later how to actually make it so
      // it could be any data type without having to declare
      // SetInt, SetFloat, SetChar, and so on. That's with templates.
      // But that's Semester 3 content. Keep it simple for now.
    private:
      int* arr;
      int size;
      void swap(int& a, int& b);
      void removeDups();
    public:
      Set();
      Set(const Set& copy);
      int getSize() const;
      int* getArr() const;
      bool isSorted() const;
      void sortSet();
      void addElement(int n);
      void removeElement(int n);
      Set operator^(const Set& obj);
      Set operator&(const Set& obj);
      Set operator|(const Set& obj);
      Set& operator=(const Set& obj);
      Set& operator^=(const Set& obj);
      Set& operator&=(const Set& obj);
      Set& operator|=(const Set& obj);
      int operator[](int index) const;
      // int& operator[](int index);
      // Commented because it's not practical.
      // We'll get to this later.
    };

| Unlike before, I won't be going into the implementation details of the class. We're here for Operator Overloading, not sets. If you're still interested though, you can obtain the file with all the code from (INSERT LINK HERE).

operator|
"""""""""

| Normally, ``|`` acts as a BITWISE OR. In this case, we're using it in SET syntax, meaning this would be ``A v B``, which is A Union B. Even though I haven't showed the code for ``addElement``, you can probably already assume what's happening. I've made it so if you're trying to add an Element that's already there, it doesn't add it. So in this case you do get ``A v B``.

.. code-block:: c++
   :linenos:

    Set Set::operator|(const Set& obj) {
      Set temp;
      for (int i = 0; i < this->size; i++)
        temp.addElement(this->arr[i]);
      for (int i = 0; i < obj.getSize(); i++)
        temp.addElement(obj.getArr()[i]);
      return temp;
    }
    
operator&
"""""""""

| Normally, ``&`` acts as a BITWISE AND, or as an Address retriever. In this case, we're using it in SET syntax, meaning this would be ``A ^ B``, which is A Intersection B. It's implemented as such: For every element in A, check if it's also in B. If it is, then add it to ``A ^ B``, otherwise do nothing. Repeat for every element in A. 

.. code-block:: c++
   :linenos:

    Set Set::operator&(const Set& obj) {
      Set temp;
      for (int i = 0; i < this->size; i++)
        for (int j = 0; j < obj.getSize(); j++)
          if (this->arr[i] == obj.getArr()[j]) {
            temp.addElement(this->arr[i]);
            break;
          }
      return temp;
    }

operator^
"""""""""

| Normally, ``^`` acts as a BITWISE XOR. In this case, we're using it in SET syntax, meaning this would be ``(A v B) - (A ^ B)``. Unfortunately, since I didn't implement an operator overload for ``-`` out of laziness, I did all of the work here directly. It uses the previous overloads to find ``(A | B)`` and ``(A & B)``, then adds any elements that are in ``(A | B)`` but not in ``(A ^ B)`` to the answer set, and returns that.

.. code-block:: c++
   :linenos:

    Set Set::operator^(const Set& obj) {
      Set temp1 = *this | obj;
      Set temp2 = *this & obj;
      Set temp3;
      bool existsInIntersection = false;
      for (int i = 0; i < temp1.getSize(); i++) {
        existsInIntersection = false;
        for (int j = 0; j < temp2.getSize(); j++) {
          if (temp1.getArr()[i] == temp2.getArr()[j]) {
            existsInIntersection = true;
            break;
          }
        }
        if (!existsInIntersection) {
          temp3.addElement(temp1.getArr()[i]);
        }
      }
      return temp3;
    }

operator= (Deep Copy)
"""""""""""""""""""""

| This time we're using pointers, and for anything that uses pointers, you *have* to make a deep copy. That's what I've done here.

.. code-block:: c++
   :linenos:

    Set& Set::operator=(const Set& obj) {
      if (this->arr != nullptr)
        delete[] arr;
      this->size = obj.getSize();
      this->arr = new int[size];
      for (int i = 0; i < size; i++)
        this->arr[i] = obj.getArr()[i];
      return *this;
    }

| You might be wondering why I've wrote a ``delete[]`` command on Line 3. That's because the Assignment Operator, ``=``, can be called anywhere in the code. It may already have data. ``Set c2 = c1`` is NOT an assignment operator, it's a Copy Constructor. ``Set c2; c2 = c1;`` IS an assignment operator, it's NOT a copy constructor. In this case, I'm seeing if the object we're overwriting in question (meaning the object on the left side of ``c2 = c1``, meaning ``c2``) already has some data in it, and if so, then telling the compiler to free up that data since we won't be using it any longer. You *can* further optimize it by checking if both Sets are of equal size but in all honesty that's such a rare situation, and asking the compiler to free up the memory then declaring more isn't a very taxing thing anyways. It's the read and write operations that take so much time and effort.
|
| This has already been explained in detail in Deep Copies for Constructors back in :ref:`s2-oop-t13`, you can check it there as well. The only difference here is that the ``=`` operator can be called at any point in the code and can be called multiple times, which makes it different from copy constructors, which are only called once.

operator|=
""""""""""

| Just like before, since we're modifying ``*this``, we can return by reference. These operations, however, are rather expensive, as not only are you calling Constructors and adding values to them inside ``*(*this | obj)``, but after that you're also then assigning that into ``*this`` via a deep copy. So although I've written it this way just to clear concepts, you should either use this implementations for smaller pieces of data, or optimize it if dealing with larger pieces.

.. code-block:: c++
   :linenos:

    Set& Set::operator|=(const Set& obj) {
      *this = *this | obj;
      return *this;
    }
    
operator&=
""""""""""

.. code-block:: c++
   :linenos:

    Set& Set::operator&=(const Set& obj) {
      *this = *this & obj;
      return *this;
    }

operator^=
""""""""""

.. code-block:: c++
   :linenos:

    Set& Set::operator^=(const Set& obj) {
      *this = *this ^ obj;
      return *this;
    }
    
operator[] (By Value)
"""""""""""""""""""""

| We're approaching the end. This is by far the longest page I've had to work on.

.. code-block:: c++
   :linenos:

    int Set::operator[](int index) const {
      return arr[index];
    }
  
| This one's pretty simple. You just write the syntax, then find the appropriate position using ``c1[i]`` or something. But there's a ``const`` written there. This specific syntax is only meant to be used for read-only. We want to make another overload for writing the data as well, like doing ``c1[i] = value``. For that, we need to remove the ``const``, and also return by reference, as that's the only way it gives a modifiable location to the compiler to change the data.

operator[] (By Reference)
"""""""""""""""""""""""""

.. code-block:: c++
   :linenos:

      int& operator[](int index) {
        return arr[index];
      }
  
| It's not something to worry about too much. The compiler tells you (if it has something like intellisense or when compiling) that it should return by reference. That's the second usage of returning by reference: It lets the value be modified from outside. You do have to be careful about *not* setting a const if you want it to be modifiable though.

operator()
""""""""""

| Now, I'd put the code I wrote here for the Matrix Class, but I'm honestly just too tired to do so. So all you have to understand is the syntax. You can read the practical implementation from the file later if you're curious.

.. code-block:: c++
   :linenos:

      int Matrix::operator()(int row, int col) const {
        return arr[row][col];
      }

| You can make it have any amount of arguments. It's the only operator where you can do such a thing. In this case, we're dereferencing the value from the 2D array. We're doing it using ``()`` because ``[][]`` isn't an operator. There's other shenanigans involved with that. You could also just use ``int getElement(int row, int col);``. Just depends on you. You want to return by reference if you're dereferencing an array, though.

.. code-block:: c++
   :linenos:

      int& Matrix::operator()(int row, int col) {
        return arr[row][col];
      }

operator<<
""""""""""

| These would normally be categorized under ``Never Used`` except the fact that ``<iostream>`` uses it for input and output from the terminal. But since we can't just access ``<iostream>`` to make it compatible with our custom classes, we can implement it as an external overload instead.

.. code-block:: c++
   :linenos:

    ostream& operator<<(ostream& out, const ComplexInt& c)
    {
      out << c.getReal();
      out << " + " << c.getImag() << "i" << endl;
      return out;
    }

| The ``ostream`` object belongs to ``<iostream>``. It stands for "Output Stream". It's the magical thing that takes data from the Compiler and puts it on the terminal. We're not concerned with how it does that, all we're doing is asking it to output this specific object in this format for us whenever ``cout`` is called for that object. For the syntax, just do ``cout`` but replace the ``cout`` with the name of the ``ostream`` object, which in this case is ``out``. Now, whenever you do ``cout << c1`` (assuming that ``c1`` is a ``ComplexInt`` object), it'll call that function and output everything as written within that function. As always, since you're modifying the object in question, you're returning by reference.
|
| The confusing thing to you, however, might be the fact that it takes two arguments, when it's written as ``a << b``. And, big revelation, but every operator can actually do that. The only reason we didn't do so thus far was because it was just easier to manage, it gives you access to ``this``, and it gives access to private functions as well. For example, ``operator+``, although previously written as a Member Function ``Class operator+(Class2)``, can also be written as ``Class operator+(Class1, Class2)`` completely outside the class. This is how you actually overload the existing data types to be compatible with custom ones. You can do ``Class.operator+(float)``, but you can't do ``float.operator+(Class)``. You overcome this by doing ``ReturnType operator+(float, Class)``.

operator>>
""""""""""

| Here's the syntax for ``istream``. Now, whenever you do ``cin >> c1`` (assuming that ``c1`` is a ``ComplexInt`` object), it'll call that function and take inputs the same way it asks from within that function. Since you're modifying the ``istream``, you're returning by reference. In this case, though, remember to *not* write ``const``, as you *are* modifying the value.

.. code-block:: c++
   :linenos:

    istream& operator>>(istream& in, ComplexInt& c)
    {
      int temp = 0;
      cout << "Enter Real Part: ";
      in >> temp;
      c.setReal(temp);
      cout << "Enter Imaginary Part: ";
      in >> temp;
      c.setImag(temp);
      return in;
    }

Conclusion
^^^^^^^^^^

| I know that this page was long but I did it because I struggle with having internet a lot, so having it all be in one place without having to search and scroll makes things way easier to share and read and quote. Use this page as a reference for operator overloading. Whatever's left will be covered on the next page or two. After that, we move on to Class Relationships (Association, Aggregation, Composition).
