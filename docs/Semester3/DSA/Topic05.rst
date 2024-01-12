.. _s3-dsa-t05:

5) Why We Study Data Structures
-------------------------------

| The rest of the semester is just tackling different Data Structures and how they work, what they specialize in, and so on. The theoretical part was easy, but since we were doing it in C++ the programmed part was a major hassle because of all the debugging, and more importantly, not knowing whether we did it correctly or not. This is where Graphviz comes into play because it lets you visualize these Data Structures.
|
| From here till the end this is the total list of Data Structures we had to implement:
*   Array
*   List
*   Queues
*   Stacks
*   Trees
*   Heap
*   Hash Table
*   B-Trees
*   Graphs
| We also covered Red Black Trees as our last assignment, and I wasn't able to finish that on time because I got sick. Some advice if you happen to go to the same university as me, don't ever skip assignments because they WILL get asked about in your exams. Even though I got marked 0 in that assignment, I still scored marks in my Final Exam because I covered the theoretical aspect of how to do Red Black Trees. Don't skip assignments.
|
| I do have to write one last thing before we continue with the subject: ADT's and Data Structures. ADT means Abstract Data Type and it is a way of describing a Data Structure and its operations but without the implementation. It tells *what* a Data Structure is supposed to do, but not *how* it does it, the same way a function prototype works. For example, a Stack ADT is a Data Structure that has the following operations:
*   Push
*   Pop
*   Peek
*   isEmpty
*   isFull
*   etc.
| We'll get into detail when we're actually learning Stacks. In C++ we typically bring the ADT's to life through the use of Classes, and that's also why we templatize them. Other languages probably do this through other techniques as well. 
|
| You might be wondering why we're bothering to go into detail about *how* the Data Structure works, instead of just showing the Data Structure and showing how to use it. I'd like to introduce you to https://github.com/codecrafters-io/build-your-own-x, and specifically the part on that page that says ``"What I cannot create, I do not understand" - Richard Feynman``. I don't actually know who that is, and a quick Google Search shows an American Physicist known for his work in quantum mechanics, quantum electrodynamics, particle physics, and the physics of the superfluidity of supercooled liquid helium. He's got a point though. The purpose of learning the *how* of something also lets you use the thing more effectively, and down the line make advancements to add on or improve. That's why the GitHub link above shows things like making your own 3D Engine, even though hundreds of game engines and physics simulation engines exist already. It also shows how to make your own OS, how to make your own programming language, your own Search Engine, your own Virtual Machine, your own Bot, your own Database, and so on. It's a great resource to learn how to make your own things, and I highly recommend checking it out. We're learning Data Structures and the theoretical knowledge behind all of these different implementations to further understand what each Data Structure does, how it does it, what features and compromises it has to deal with, and either implement it or modify it to tackle with a different solution. Neural Networks? That's a Data Structure for dealing with Machine Learning and Artifical Intelligence. Arrays? That's a Data Structure for dealing with storing data and fast accesses. Hash Tables? That's a Data Structure for dealing with storing data in a non-contiguous memory block. Trees? That's a Data Structure for dealing with storing data in a hierarchical manner. Graphs? That's a Data Structure for dealing with storing data in a network manner. And so on. Even Operating Systems use Data Structures to manage their memory, their processes, their threads, their files, and so on. It's all about understanding how to use the right tool for the right job, and if the tool doesn't exist, then you make your own, and that's why we're learning Data Structures.