.. _s2-oop-t02:

2) Memory Leaks
---------------

| I mentioned in :ref:`s1-pf-t36` that Memory Leaks are what happen when you don't ``delete`` data you're no longer using.

.. code-block:: c++
   :linenos:

    int* ptr = new int;
    *ptr = 5;
    cout << *ptr << endl;
    ptr = NULL;

| What's happening here is that the memory location stored in ``ptr`` is being updated. First it was the heap location, and then it was the NULL location. But the location in the heap isn't properly addressed. The heap location is left occupied in the memory and the OS is never properly told that it's no longer needed. The pointer was used to access the heap, but now the thing remembering the address, the Pointer, no longer remembers it. So not only is the data lost, but the Heap still thinks that the data is useful.
|
| A Memory Leak is when data that's no longer being used isn't properly disposed of, and it takes up unnecessary space.
|
| As a shower thought this is what came to me way later when making these notes. Based on a video I saw about Team Fortress 2, by a guy named Shounic. The video mentioned a Memory Leak. I didn't know much about this at the time. I only randomly thought of this far far later: The whole point of the Heap, and Dynamic Memory, is being able to delete it. That's the one thing that separates it from the Stack. You can free up the Heap. And EVERYTHING runs off this logic. I mean, EVERYTHING.
| You're playing a game. You load a character. You have a gun. You shoot the gun. Every bullet isn't already shot, the player shoots it. When shot, the bullet is created, and where is it created? In the heap. ``bullet* ptr = new bullet``. And then when it lands it has to be deleted. ``delete bullet``. The map loads and then when the game ends, the map has to be removed from memory because you're no longer playing on it, and taken to the main menu.
| You open Google Chrome and browse the internet and read some stuff and watch some videos. Then you open another tab. And another. And another. And then you close some too. Then you close the browser. You don't wanna use it again for that time. Or you listen to some music and then you close it.
|
| EVERYTHING works on the Heap, because you don't ever know what's gonna be run at what time. You need to have the ability to close things and free up memory. It's all to make sure there's enough resources. It adapts.

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