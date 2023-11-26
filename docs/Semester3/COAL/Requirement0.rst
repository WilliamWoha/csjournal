.. _s3-coal-req0:

Requirements
------------

| We'll be doing our Assembly work on Visual Studio, via MASM, and the code will be 32-bit x86 code. There's no additional libraries to install, it can all be done via the ``C++ Empty Project`` template, but I'd recommend setting up a Custom Template for assembly from the help of this video https://youtu.be/-MgEzUbGhq0. Also, we won't be dealing with the terminal for most of our code. Now we'll just be working with the Debugger, and using Breakpoints and the Watch to see what happens.

.. code-block:: nasm
   :linenos:

    .386
    .model flat,stdcall
    .stack 4096
    ExitProcess proto,dwExitCode:dword

    .code
    main PROC
        ; Move the values into the registers
        mov ax, 2
        mov bx, 3
        mov cx, 1
        mov dx, 5
        add ax, bx    ; 5
        add cx, dx    ; 6
        sub ax, cx    ; The result is FFFFFFFF

        INVOKE ExitProcess,0
    main ENDP
    END main

| Once your template is all set, we'll be ready to do some actual Assembly work.