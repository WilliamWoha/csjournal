.. _s3-dsa-t01:

1) Intro to Data Structures
---------------------------

| We study Data Structures because it provides a way for organizing data. A Data Structure is any representation that is used for storing information. Each one is a useful tool to deal with different things with a different Time and Space Complexity. You'll learn what those are later. An integer, a struct, a class, an array, a linked list, and so on. Anything that deals with storing data in a unique way counts as a Data Structure.
|
| You'll learn throughout the semester many ways to store data, and might be wondering why so many forms exist, such as a Arrays, Linked Lists, and then further uses of these to store and access data in a unique way such as with Queues, Stacks, Binary Trees, Graphs, and so on. All of these exist to tackle different problems in different ways. Realistically, when you're dealing with a lot of data, and I mean a *lot* of data, like millions of records, you have to consider the situation. A Linked List, compared to an Array, can grow infinitely (or at least as long as there exists any memory), and it's very very easy to insert and delete data into it. The challenge for it comes with a way slower access to data compared to something like an Array. On the other hand, an Array has a fixed size, even when using the Heap. When you want to change the size of it, you have to copy over all the values to a new Array of a bigger size, which is a very computationally expensive task if you're copying thousands of values. But accessing data from an array is nearly instant.
|
| Each Data Structure requires Space for storing data, and Time to perform each task. There's some efforts from the programmer for Optimization as well. The cost of a Data Structure is the measure of how much Time and Space in resources it uses, and the choice of which Data Structure to use depends on the Frequency with which various Data Operations are applied. There is no "one size fits all". It depends on what you're trying to do. We'll be learning how each Data Structure works, how to make our own version of it, understand the costs, and scenarios in which we can use them.
|
| Using one Data Structure over another can make the difference between a program running for a few seconds, or for a few days. So let's get started!
