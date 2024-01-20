.. _s3-dsa-t09:

9) Queues
---------

| The reason we dived so deep into how a List works, both via an Array and a Linked List is because we want to modify them to implement other Data Structures, such as Queues, Stacks, and Trees. These three in particular are going to use Nodes and pointers to next Nodes *religiously*. You can implement them using Arrays as well but it's very unconventional to do so. It's still useful to do for specific purposes such as fixed size circular buffers, though, which is why we study it.
|
| A Queue is a Data Structure that works on the ideology of ``FIFO``, which stands for ``First-In-First-Out``. This is another way of writing ``First Come First Serve``. As the name ``queue`` implies, you can imagine it to be like a line at a ticket counter, and the first person being addressed in the queue will be the person that entered the queue first, and once that person is addressed, they'll be the first to leave. Then the second person that entered the queue will be addressed, then the third, and so on until the queue is empty.
|
| As far as their implementation is concerned, as stated earlier, it'll be a modified version of a List, where Items will be inserted in one end (rear) and deleted at the other end (front). We call them the rear at the front because just like a line at a ticket counter, you enter the line from the rear, and you leave the front of the line when you're done. 
|
| You'll use a queue for many applications...probably. I haven't used it in any major systems or applications but I probably will in next semester, as https://www.geeksforgeeks.org/applications-of-queue-data-structure/ lists many uses such as Task Scheduling, Message Buffering, Event Handling, Printer Queues, Network Protocols, and so on, and the first four are all related to OS development.
|
| For our ADT we want to define these operations:
*   Create the Queue
*   Destroy the Queue
*   Find the size of the Queue
*   Check if the Queue is empty
*   Check if the Queue is full (Array based implementation only)
*   Insert an item into the Queue (also called an Enqueue or Push operation)
*   Remove an item from the Queue (also called a Dequeue or Pop operation)
*   Return the item at the front of the Queue (also called a Peek operation)
*   Clear the Queue
| If you compare these operations to what we wrote for the List, you'll notice a lot of similarities and a few differences. Until the Insert operation, it's basically identical, but the Insert and Remove operations will NOT let the programmer control the position. All the programmer can do is Enqueue and Dequeue, otherwise they risk violating the rules of the Data Structure. A queue won't work the way it's designed to if the second item in line suddenly gets priority and is addressed over the first one. The rules must be followed. And yes there can be situations where the thing you're enqueueing *is* more important than what's already in the queue, but that's a different Data Structure called a Priority Queue. We're not dealing with that right now.
|
| So now that the ADT operations are written down, lets define the class for it to write it in C++.

.. code-block:: c++
   :linenos:

    template <typename T>
    class Queue {
    public:
        Queue();
        ~Queue();
        int size() const;
        bool isEmpty() const;
        bool isFull() const;
        void enqueue(const T& item);
        T dequeue();
        T peek();
        void clear();
    };

| And just as before, we need to write the functionality of it. There's two approaches: Array based, and Linked List based. One method of using an Array can look like this:
*   Start:      ``- - - - -``
*   Enqueue(3): ``3 - - - -`` 3 is Added
*   Enqueue(4): ``3 4 - - -`` 4 is Added
*   Enqueue(5): ``3 4 5 - -`` 5 is Added
*   Dequeue():  ``4 5 - - -`` 3 is Released
*   Enqueue(2): ``4 5 2 - -`` 2 is Added
*   Enqueue(8): ``4 5 2 8 -`` 8 is Added
*   Dequeue():  ``5 2 8 - -`` 4 is Released
*   Dequeue():  ``2 8 - - -`` 5 is Released
*   Dequeue():  ``8 - - - -`` 2 is Released
*   Dequeue():  ``- - - - -`` 8 is Released
| However, you might have noticed a small problem with this approach: I've (theoretically) implemented it so that for ``enqueue`` it starts at the first location and does a linear search until it finds a free space. Although functional, it makes the complexity of ``enqueue`` O(n), which is extremely slow. On top of that, the ``dequeue`` operation also has a complexity of O(n) because of the shifting of elements when a value is dequeued.
|
| Both of these challenges can be overcome by keeping two additional variables to keep track of the Front and the Rear. It's very simple: just make it so Front remembers the index of the next value to dequeue, and Rear holds the index for the end of the line. The same array above would then have contents as follows:
*   Start:      ``- - - - -``, Front == -1, Rear == -1
*   Enqueue(3): ``3 - - - -``, Front == 0, Rear == 0, 3 is Added
*   Enqueue(4): ``3 4 - - -``, Front == 0, Rear == 1, 4 is Added
*   Enqueue(5): ``3 4 5 - -``, Front == 0, Rear == 2, 5 is Added
*   Dequeue():  ``- 4 5 - -``, Front == 1, Rear == 2, 3 is Released
*   Enqueue(2): ``- 4 5 2 -``, Front == 1, Rear == 3, 2 is Added
*   Enqueue(8): ``- 4 5 2 8``, Front == 1, Rear == 4, 8 is Added
*   Dequeue():  ``- - 5 2 8``, Front == 2, Rear == 4, 4 is Released
*   Dequeue():  ``- - - 2 8``, Front == 3, Rear == 4, 5 is Released
*   Dequeue():  ``- - - - 8``, Front == 4, Rear == 4, 2 is Released
*   Dequeue():  ``- - - - -``, Front == -1, Rear == -1, 8 is Released 
*   Enqueue(1): ``1 - - - -``, Front == 0, Rear == 0, 1 is Added
*   Enqueue(2): ``1 2 - - -``, Front == 0, Rear == 1, 2 is Added
*   Enqueue(3): ``1 2 3 - -``, Front == 0, Rear == 2, 3 is Added
*   Enqueue(4): ``1 2 3 4 -``, Front == 0, Rear == 3, 4 is Added
*   Enqueue(5): ``1 2 3 4 5``, Front == 0, Rear == 4, 5 is Added
| Adding these two integers reduces the complexity of ``enqueue`` and ``dequeue`` down to O(1), as the Array immediately knows which place to add a value to, and return a value from.
|
| The only catch with this is that there's a size limit. If Rear reaches a value of 5 then it won't work anymore as the array has a size of 5 and the index ranges from 0 to 4. One way around this is to implement a circular functionality. You can see this being useful in a situation like ``front == 4, rear == 4, programmer uses enqueue()``. There are free values in the queue, at indexes ``0, 1, 2, 3``, but if you *didn't* make your queue circular then you might be returning an error statement instead. Making your queue circular means moving the ``rear`` back to index 0 by keeping track of free spaces. Doing this will increase the amount of IF statements you have to write but effectively lets you have an infinite amount of ``enqueue`` and ``dequeue`` operations as long as there aren't more than ``n`` items in the queue at once.
|
| That's the major problem though. You can't have more than ``n`` items in the queue at once, since it's an array. In space saving measures this is fine behaviour but if we want a general purpose Queue, we want to be able to grow it as much as possible. That's where the Linked List implementation comes in. It's effectively the same logic, and it keeps the O(1) complexity of the ``enqueue``` and ``dequeue`` operations (by keeping pointers for Front and Rear, similar to how you remembered indexes in the Array version), but with the added advantage that it can grow infinitely. Here's how it would look (Front and Rear are pointers, when I've written Front == 3 it means Front is pointing to a Node in a Linked List, and the data in that node is 3. Front itself is NOT equal to 3!):
*   Start:      ``NULL``,       Front == ``nullptr``, Rear == ``nullptr``
*   Enqueue(3): ``3``,          Front == 3, Rear == 3
*   Enqueue(4): ``3 -> 4``,       Front == 3, Rear == 4
*   Enqueue(5): ``3 -> 4 -> 5``,    Front == 3, Rear == 5
*   Dequeue():  ``4 -> 5``,       Front == 4, Rear == 5, 3 is Released
*   Enqueue(2): ``4 -> 5 -> 2``,    Front == 4, Rear == 2
*   Enqueue(8): ``4 -> 5 -> 2 -> 8``, Front == 4, Rear == 8
*   Dequeue():  ``5 -> 2 -> 8``,    Front == 5, Rear == 8, 4 is Released
*   Dequeue():  ``2 -> 8``,       Front == 2, Rear == 8, 5 is Released
*   Dequeue():  ``8``,          Front == 8, Rear == 8, 2 is Released
*   Dequeue():  ``NULL``,       Front == ``nullptr``, Rear == ``nullptr``, 8 is Released
| This time, using the class definition written near the start of the page, try to implement both the Array based implementation and the Linked List based implementation yourself. It's going to be a modified version of a List in both the Array form and the Linked List form. I've already given the codes for making a List via an Array and a Linked List on the previous page, I won't be giving the code for newer things unless it's something super important or useful. In Semester 1 and Semester 2 I did that for reference purposes and examples but now you need to learn the two most important skills a programmer can have:
*   Being able to write an answer using a set of rules or requirements
*   Being able to find an answer using a set of rules or requirements
| Try to make it yourself, use the existing code for the List and modify it to make it. If you have trouble, see if someone else already made it by googling it or checking GitHub (this is something a lot of people miss out, SERIOUSLY check GitHub!). Don't copy paste, don't plagiarize. See what they did, try to understand what they did and why they did it, then write your own code.
|
| Here's a hint for the Private Data Members:
|
| Array based:
*   ``T* arr``
*   ``int size``
*   ``int front``
*   ``int rear``
|
| Linked List based:
*   ``Node<T>* front``
*   ``Node<T>* rear``
| If you have trouble, I'm always willing to answer questions and help out via Discord @ ``williamwoha``. It's the easiest way to contact me (without revealing my real life identity or phone number) which is why I use it. Good luck!