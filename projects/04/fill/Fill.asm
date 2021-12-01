// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(BLACK)
    @KBD
    D=M
    @WHITE
    D;JEQ   // goto WHITE if no key pressed

    @color
    M=1

    @8191
    D=A
    @iterator   // reset iterator to 8191
    M=D

    @FILLSCREEN
    0;JMP   // fill screen with black pixels

(WHITE)
    @KBD
    D=M
    @BLACK
    D;JNE   // goto BLACK if key pressed

    @color
    M=0

    @8191
    D=A
    @iterator   // reset iterator to 8191
    M=D

    @FILLSCREEN
    0;JMP   // fill screen with white pixels

(FILLSCREEN)
    // iterate over all the pixels -> fill with color
    @iterator
    D=M
    @SCREEN
    D=A+D
    @currentpixel
    M=D

    @color
    D=M
    @currentpixel
    A=M
    M=D

    @iterator
    M=M-1

    // check if iterator has reached end of screen -> go back to check keyboard input
    @iterator
    D=M
    @BLACK
    D;JEQ

    @FILLSCREEN
    0;JMP