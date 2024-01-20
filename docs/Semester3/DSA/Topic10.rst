.. _s3-dsa-t10:

10) Stacks
----------

| My hands are cold from winter. *Really* should've written these things earlier because it's coming to bite me now.
|
| The next Data Structure we'll be dealing with is the Stack. It works on the ideology of ``LIFO``, which stands for ``Last-In-First-Out``. As the name ``stack`` implies, you can imagine it to be like a Stack of plates or books. You keep adding on to the pile, and whenever you need something, you take it from the top of the pile. You *can* take it from the middle as well in the real world, but it's harder, and as far as the Data Structure is concerned, it's impossible.
|
| This time, unlike a Queue which had both a Front and a Rear, we'll only be dealing with one end: The Front. This is both where Data will be inserted from, and data will exit from. You can imagine it to be like one of those plate dispencers at weddings. You put in a plate from the top, and you take one from the top. You can't put in a plate from the bottom, and you can't take one from the bottom.
|
| There's many major uses of Stack, and the biggest one is for Function Calling. Calling a function adds it to a Stack, and when that function is complete, that function is removed from the stack. It allows the computer to back track to the original place where the function was called. This back tracking also allows it to be used for maze-finding algorithms (in case it finds a dead end), and for the ``undo`` function in many programs. It's also used in compilers to check for completeness of brackets, and in html for checking for completeness of tags. You can find more uses of it with a quick google search.
|
| For our ADT we want to define these operations:
*   Create the Stack
*   Destroy the Stack
*   Find the size of the Stack
*   Check if the Stack is empty
*   Check if the Stack is full (Array based implementation only)
*   Insert an item into the Stack (also called Push)
*   Remove an item from the Stack (also called Pop)
*   Peek at the top of the Stack (also called Top)
*   Clear the Stack
| So now that the ADT operations are written down, lets define the class for it to write it in C++.

.. code-block:: c++
   :linenos:

    template <typename T>
    class Stack {
    public:
        Stack();
        ~Stack();
        int size() const;
        bool isEmpty() const;
        bool isFull() const;
        void push(const T& item);
        T pop();
        T peek();
        void clear();
    };

| And just as before, we need to write the functionality of it. The same way we did the Queue, we can do this via an Array based implementation or via a Linked List based implementation. It's remarkably similar to the Queue.
|
| In the Array based implementation you can either have the entire array shift itself, having a complexity of O(n) for both Push and Pop operations. Another thing you can do, however, is have a variable to keep track of the Top of the stack. This way, you can have a complexity of O(1) for both Push and Pop operations. The only downside to this is that the Stack will have a fixed size.
|
| O(n) version:
*   Start:      ``- - - - -``
*   Push(3):    ``3 - - - -``
*   Push(4):    ``4 3 - - -``
*   Push(5):    ``5 4 3 - -``
*   Push(6):    ``6 5 4 3 -``
*   Pop():      ``5 4 3 - -``
*   Pop():      ``4 3 - - -``
*   Push(7):    ``7 4 3 - -``
*   Pop():      ``4 3 - - -``
*   Pop():      ``3 - - - -``
| Although it's slow, try to implement it for practice anyways.
|
| For the O(1) version, just like how we kept Front and Rear in the Queue, we'll be keeping track of the top of the Stack. This allows us to have the same functionality without having to shift the entire array. The only downside to this is that the Stack will have a fixed size.
|
| O(1) version:
*   Start:      ``- - - - -``, Top == -1
*   Push(3):    ``3 - - - -``, Top == 0
*   Push(4):    ``3 4 - - -``, Top == 1
*   Push(5):    ``3 4 5 - -``, Top == 2
*   Push(6):    ``3 4 5 6 -``, Top == 3
*   Pop():      ``3 4 5 - -``, Top == 2
*   Pop():      ``3 4 - - -``, Top == 1
*   Push(7):    ``3 4 7 - -``, Top == 2
*   Pop():      ``3 4 - - -``, Top == 1
*   Pop():      ``3 - - - -``, Top == 0
| And to solve that Fixed Size problem, we can use a Linked List based implementation. Here's how the functionality of that will look like:
*   Start:      ``NULL``, Top == NULL
*   Push(3):    ``3 -> NULL``, Top == 3
*   Push(4):    ``4 -> 3 -> NULL``, Top == 4
*   Push(5):    ``5 -> 4 -> 3 -> NULL``, Top == 5
*   Push(6):    ``6 -> 5 -> 4 -> 3 -> NULL``, Top == 6
*   Pop():      ``5 -> 4 -> 3 -> NULL``, Top == 5
*   Pop():      ``4 -> 3 -> NULL``, Top == 4
*   Push(7):    ``7 -> 4 -> 3 -> NULL``, Top == 7
*   Pop():      ``4 -> 3 -> NULL``, Top == 4
*   Pop():      ``3 -> NULL``, Top == 3
| If your understanding of Linked Lists is good then you won't see anything wrong here, but just in case you're confused as to how it's able to shift the entire list, we're not. What we're doing is adding a new node, making that the head, and that new node is pointing to the previous head. We're not shifting the entire list, we're just adding a new node to the top of it, which is exactly how a Stack works. The key difference here, however, is that not only is the size dynamic, but the complexity is also O(1) because we're *always* adding and removing from the top of the list.
|
| Try to implement it on your own again. The Class definition is available by scrolling up. Here's a hint for the Private data members (yes this is all you need, Stack is unbelievably simple):
|
| Array based (O(1)):
*   ``T* arr``
*   ``int size``
*   ``int top``
|
| Linked List based (O(1)):
*   ``Node<T>* top``
