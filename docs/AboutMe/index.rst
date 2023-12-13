.. _aboutme:

========
About Me
========

| Hello! My name is Muhammad Ibrahim Awais. I was born on 6th December, 2003, and have been super fond of anything digital and related to tech since I first had a computer with Windows XP when I was four years old. The first ever game I played with it was Need For Speed: Underground, and I frequently used to open things to try to find out what was going on inside them.
|
| Today I can assemble and disassemble any regular Computer system and assist anyone with what kind of parts to choose and how everything works. I'm also a massive fan of Animation and VFX, which is the reason I learnt to use Blender, as I wish to make my own animations and show my own ideas and stories. I've been programming since I was 15, but I never truly enhanced my skill in it until I took admission into a university, as motivation was enough to get started, but discipline is required to take you to the end. During COVID, with plentiful free time, I learnt a plethora of skills, of which I have mastered none but I do hold a passion and newfound respect for people who do it professionally, such as Cardistry, Baking, Cooking, Carpentry, Sketching, Painting, Pottery, Pixel Art, Video Editing, Animating, and learnt Chess. I also worked with a team of people to create a Meme Mod for NFS: Most Wanted called the Pepega Mod.
|
| I'm a fan of anything and everything where human passion and creativity shows itself. I enjoy learning all things, be it scientific or philosophical. I enjoy all content except horror. Really, the only part of life I don't enjoy, is the inhumane things that happen to innocent people, and politics. It just feels like everyone yells at each other and has no desire to make improvements. I just want people to be happy. Every person has a soul, and one person isn't more important than another.
|
| My purpose in life is to make proud the people I respect, and be happy doing the things I love doing with the people I love doing it with. And along the way, if I can do something that truly helps someone the same way I was helped in my darkest times, so they too can lead a fulfilling life, I'll know I've won.

University Projects
-------------------

| Although most of the Projects here are related to university, I still put my heart and soul into them to try and make the best versions. The Data Structures project isn't fully complete yet so I can't comment on it but everything else (PF, OOP, COAL) required you to make games, and for *every* subject, in *every* semester, I've consistently scored the highest marks and won the "Best Project" award. Each Project was solo and had hundreds of submissions.
|
| That's not to say I'm some kind of prodigy or have a lot of talent. I experienced *plenty* of struggle with every single one of them and many, many sleepless nights were spent on them. I was just committed to making something my teachers could be proud of, and to prove to myself that I can make a great product.
|
| The works are written in descending order, from most recent to least recent.

PacManASM
^^^^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 2%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="1149" height="718" src="https://www.youtube.com/embed/B0cpoWkWj4A" title="PacManASM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>

| My task was to create Pac-Man via Assembly Language, specifically via MASM syntax by enabling the Microsoft Macro Assembler under Build Dependencies of a Visual Studio C++ Empty Project. Normally the university course teaches Assembly on DOS-Box but since this time it was done on Visual Studio, it was supposed to be done on the Terminal instead.
|
| I wasn't a fan of this, as the game in question wouldn't look or feel smooth. I asked my teacher if WinAPI functions were allowed, and he was ok with it, but told me to be careful as I'd be doing it at my own risk.
|
| I needed three things:
*  How to draw things
*  How to move things
*  How to time things
| If I got that much, I was able to make a game.
|
| I spent the next 2 days uncovering old archives and forums as it turns out, Microsoft had replaced the WinAPI Assembly Documentation in favor of WinAPI C and C++ Documentation. I guess those languages got optimized enough and computers got powerful enough that the need for Assembly Documentation was no longer required. The WinAPI libraries had to be installed from a site called www.masm32.com which, surprisingly, was just an executable Installer which automatically assembled and linked the files you needed, regardless of the OS you use.
|
| Then I spent the next 6 days in stress and pain as I was able to get a window open and I was able to load one Bitmap Image on it, but not two. It would flicker, glitch, load duplicates, do many, many things I didn't want. Until at some point in my lack of sleep thought that making it in C and converting it might be my only hope, at which point I thought...why make it in C at all? Just do that part in my head. And finally, after 8 days of immense struggle, I was able to understand Double Buffering and draw a Graphics Window with multiple Bitmap Images, through pure MASM Assembly.
|
| From this point onwards it was just a matter of implementing the game, and I spent 5 sleep deprived days and nights on it trying to make it the best version it could be because finding the motivation to do a game in Assembly again will be an impossible task. It's now or never. And after the deadline passed, the attached video was the result.
|
| The code is in the video description.

Vulcan
^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 2%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="1233" height="694" src="https://www.youtube.com/embed/mpPYtAB94s4" title="Vulcan" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>

| The task was to make another game, but this time incorporate OOP Concepts. I had a reputation to uphold so I spent 130 hours on it and multiple sleepless nights to try and finish it before the deadline, and it turned out amazing. The same thing as Semester 1, but going even more above and beyond to try and see just what I can do.
|
| The code is in the video description.

Tetris
^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 2%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="1149" height="718" src="https://www.youtube.com/embed/sw7ajcEk27M" title="Tetris" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>

| Just this semester I learnt how to write "Hello World!" and in this same semester there's so much to do. Tetris was such an intense project for someone just starting out to programming. I only got 40% in my Mid-Exam and I was fearing failing the subject. I spent so much time and effort learning C++ and making the project to try and get muscle memory for the language. I did it so vigorously that instead of doing the smart thing and looking up the proper ways of doing things, I just did what made sense. I spent 800 lines on the rotations for the tetrominoes. Instead of *rotating* the pieces, that code *restructures* them. Each *individual piece* obtains new coordinates to go to, for *each rotation*. Instead of using a timer to trigger between different frames, I did 50 IF statements checking "If time is between 0 and 0.1", "If time is between 0.1 and 0.2", and so on. It's one of the *worst programmed* things I've done but it was so important to my learning and it ended up being so well made (despite that bad programming) that in terms of visual quality and gameplay it won the "Best Project" award, and I got so much muscle memory for C++ and Programming in general that I got 89.5% on my Final Exam.
|
| The code is in the video description.

Personal Projects
-----------------

| Also written in descending order, from most recent to least recent

CSJournal
^^^^^^^^^

| This is a site made with the help of readthedocs.org, a service specifically meant for documentation. Originally started as a way to get payback at my university for, at the time of creation, what looked like failing students on purpose, which I later realized was a misunderstanding but we're not gonna get into that. This was a site I made where I would upload my notes and understanding of programming concepts with the sole purpose of helping students who are struggling. I also wanted to use this site for fulfilling two other objectives: Revision of my own concepts, and Documentation of my Degree.
| 
| At first I uploaded notes for everything, such as Applied Physics and Calculus, but the work required would be too much for one person to handle, which is why I reduced it to Programming specifically, which is what most students were struggling with anyways. It's not popular enough to get on search results at the moment but it's still a very useful collection of information I can give to anyone struggling with programming, and anyone willing to know what I've learnt in my degree. It's a lot of things to document and is all being done solo because I have a specific style of English I write in and I try to personalize it here and there. For that reason, it's not always up-to-date. But eventually, it will be, and I hope that by 2026 I have a full documentation of my journey with the hopes that it helped someone somewhere along the way.

NFS Most Wanted: Pepega Mod
^^^^^^^^^^^^^^^^^^^^^^^^^^^

| [WARNING: This Creative Work features content which may not be suitable for all audiences. This is specifically mentioned as a way to present a public project I did but viewer discretion is advised.]
|
| I have a passion for gaming, and Need For Speed: Most Wanted (2005) is one of the best games I've ever had the pleasure of experiencing. I found a Speedrunning channel for the game called KuruHS and noticed some mods for the game, one of which was called the Pepega Mod. I was learning Blender at the time so I thought it was a good opportunity to put that skill to good use. I got in touch with the team that was working on it, presented my skillset and creative ideas, and eventually we worked together to build one of the most downloaded mods for NFS Most Wanted 2005 that exists today, and then mastering that further in an Anniversary Update (or as Eden, our Group Head titled it, Anniver.2ary update, as a creative way to say Version 2 of the mod).
|
| It now sits at more than 150,000 downloads and millions of views spread across multiple YouTube videos. The humor in it can be very specific, and often misunderstood, but the ten of us in the team still put in as much effort as possible to modify the game and provide a new, refreshing, and fun experience on a classic game. It also got a version made for NFS: ProStreet, but I had left the team by then.
|
| Extensive work was done in Blender which primarily included Modelling, Texturing, UV Editing, Scripting, and so on. Basically everything except Animation but even that was done sometimes for specific cutscenes. Community created tools were used for modifying the game's contents to adjust for changes such as new races, cars, events, cutscenes, gameplay elements, and really anything we could. It was an overhaul, and people loved it. It was responsible for teaching me the most important thing about being a game developer:
|
| You sacrifice the feeling of experiencing something for the first time, so that you can make that experience possible for everyone else. But the feeling you get in return? There is nothing more fulfilling than knowing your work is the reason why someone else can feel joy and fun.

Old School Projects
-------------------

| These were from my previous school. They aren't linked to Programming but they're linked to the creative passion I have. They're both from my Media Studies tasks from the previous school.
|
| The videos themselves are *terrible*. They aren't well made, they're rushed, but the important thing is how much I've learnt since then and during then. These bad works are the practice and foundation that served to pave the way towards good ones. You live and learn.
|
| I got an A grade on both projects.

The World Will Know Your Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| https://theibrahimawais.blogspot.com/

The Ripper
^^^^^^^^^^

| https://iawaisproductions.blogspot.com/
