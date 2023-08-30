.. _s2-oop-t02:

2) Memory Leaks
---------------

| I mentioned in :ref:`s1-pf-t36` that Memory Leaks are what happen when you don't ``delete`` data you're no longer using.

.. code-block:: c++
   :linenos:

    int* ptr = new int;
    *ptr = 5;
    cout << "Value: " << *ptr << endl;
    cout << "Address: " << ptr << endl;
    ptr = new int;
    *ptr = 10;
    cout << "Value: " << *ptr << endl;
    cout << "Address: " << ptr << endl;

| What's happening here is that the memory location stored in ``ptr`` is being updated. Not the Not the value, the address itself. First it gains a free space from the Heap and stores 5 in there, then it gains another free space from the Heap and stores 10 in there. If you run that code, you'll notice that the two Address: outputs are different. Although it's one pointer, it uses two different heap locations in the memory, because we called a ``new int`` in Line 5. But if you were able to actually look at the memory (some compilers and IDEs let you do this), you'll notice that at the first address, the value 5 is still stored. It's still there, and forever will be there until the program ends. Remember back in :ref:`s1-pf-37` how I said that Tom wants you to remember the warehouses, or else he can't help you when you forget where it is? This is what's happening. On the original paper you wrote the warehouse address, you've written a new warehouse address. The old one is lost and now you have no idea where that warehouse is, and now have no way to access what's inside of it. That memory will just sit there with that value, and you won't be able to access it or use it. This is what's known as a Memory Leak.
|
| A Memory Leak is when data that's no longer being used isn't properly disposed of, and it takes up unnecessary space.

.. code-block:: c++
   :linenos:

    int* ptr = new int;
    *ptr = 5;
    ptr = new int;
    *ptr = 7;
    delete ptr;


.. code-block:: c++
   :linenos:

    void fun()
    {
        int* ptr = new int;
    }

    int main()
    {
        fun();
    }

| These are two more examples of Memory Leaks. In the first one, the address of the first location in the heap is overridden when another place is looked for. In the second one, the pointer is made and it's not overrided. But since it's part of a function, it ends up being destroyed when the function ends.
|
| The correct way to avoid a Memory Leak in both of these situations is:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 4,8

    int* ptr = new int;
    *ptr = 5;
    delete ptr;
    ptr = NULL;
    ptr = new int;
    *ptr = 7;
    delete ptr;
    ptr = NULL;

| I highlighted lines 4 and 8 because I wanted to bring up that, in this specific code, they're unnecessary. You're setting it to ``NULL`` and then immediately setting it to ``new int`` in the next line. But this is only for example. In realistic scenarios, you'd end up not using the pointer for multiple lines or even pages before you need it again, which is why it's good practice to set to ``NULL``.
| The ``NULL`` in Line 8 is unnecessary because that's where the entire code ends for this specific scenario. For real world scenarios that means ``int main()`` has reached its end. At that point, everything becomes destroyed anyways.
.. code-block:: c++
   :linenos:

    int* fun()
    {
        int* ptr = new int;
        return ptr;
    }

    int main()
    {
        int* ptr = fun();
    }

| This is how you avoid a Memory Leak in the second code. You make sure there's a place to remember it when the function is called. If however you made a function that uses Dynamic Memory and you don't need it anymore, then just do ``delete ptr`` and then ``ptr = NULL`` within that function and you're good to go. Just make sure the pointer to do that before the function ends. You can just delete it the normal way if you do ``return`` the pointer.
