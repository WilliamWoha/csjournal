.. _s3-dsa-req0:

Requirements
------------

| Same as the last two Semesters. You just need a Compiler and a Pen and Paper. Though this time we'll also be utilizing a Visualization program called ``Graphviz``. You can obtain it at https://graphviz.org/. This is a program that takes anything written in the ``DOT`` language and converts it into a ``.png`` or ``.svg`` for viewing. Here's an example to showcase its behaviour:

.. code-block:: DOT
   :linenos:

    graph {
        a -- b;
        b -- c;
        a -- c;
        d -- c;
        e -- c;
        e -- a;
    }

| Produces this:
|
.. raw:: html
    :file: images/inheritance_3.svg
|
|
| https://graphs.grevian.org/example has more examples of it in action. So you can see how much power it has. The only challenge is that unlike ``pythontutor`` which shows how the data is actually arranged in memory, GraphViz and DOT require you to manually code the functionality, and that's going to depend on your specific Data Structure. I'll provide functions for how to print out the full set of data using Graphviz, but if your Data Structure is implemented in a different way, your GraphViz function will also have to be done differently. All it does is visualize what you wrote in it, you still have to be careful about what you write into it.
