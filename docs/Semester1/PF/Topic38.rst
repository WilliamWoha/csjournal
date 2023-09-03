.. _s1-pf-t38:

38) Why DMA is so important
---------------------------

Dynamic Memory's Significance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Although I did just type "Congrats on finishing this semester" on the last line of the previous page, I'm making this page later because I figured it out near the end of Semester 2 when I actually got to work on my End Of Semester Project.
|
| Dynamic Memory Allocation is so important because it's the only way to create and destroy memory in C++.
|
| Sounds obvious, I know. But let's take a more practical example. Take a video game, like Minecraft. When you're roaming around the open world, you encounter a lot of mobs such as Cows, Chickens, and Creepers. But the thing is, the game doesn't know the exact amount of mobs to spawn. It's completely random and it depends on where you are on the map. It spawns them when you're close and when you're far away, it despawns them to save on memory and performance. Anything that despawns in any game means it gets removed from memory. GTA 5 takes up 115 GB of space on the hard drive but can be run on 8 GB of RAM. It doesn't load up everything at once, it loads things in chunks based on different calculations and what you're looking at. Every car is created when spawned in, and destroyed when it either despawns or it actually gets destroyed in game. With Tekken, you have dozens of characters to choose from and dozens of maps to play on. It doesn't load every single map and every single character at the same time, it sees what the player chooses and then based on that it creates specific variables in the Heap. In FIFA, with hundreds of teams and playable characters, it loads specific voice lines and 3d models and prepares specific values in the Heap. With tabs in Google Chrome or Mozilla Firefox, you're creating a new instance which has its own specific data, and when the tab is closed, it's destroyed. With Windows, you can open MS Word, Excel, Firefox, and many other apps at the same time. They're taking up new memory in the Heap. And when they're closed, that memory is then freed up. This is why being able to create and destroy memory is important. So you only load up the things you need, and when you don't need them, they're no longer there. This control over memory is why Pointers and specifically working with the Heap is so important, because you don't actually know the exact specifics of how much to allocate what. The Dynamic aspect is what makes it so powerful.
|
| Good luck in Semester 2!