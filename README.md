# FRUIT NINJA PROJECT

This was a project I did in 2021 for a program called Schulich Ignite from the University of Calgary. For our last project in our class, we were given free reign to create any game we desired through Pygame. The README file was last modified December 8, 2021 and reads as follows:

This is my final project, a scuffed version of Fruit Ninja in Pygame!

In order to play the game, you must first press SPACE. As of now, the only indication that the game has started or ended is in the terminal, so have that open alongside the game. If the game ends, press SPACE again to play again. The objective is to slice as many fruit as you can, without hitting any of the rockets!

The bulk of the code and the main loop for the game is located in the main.py file. Here's where you can edit the resolution (not recommended, didn't accomodate for that) and framerate. More importantly, key mechanics like the spawn mechanic and the stages of the game can be edited here.

The items.py file outlines what the Item() class or object is. Item() is a sprite object, so an image is loaded in this class. Also located here is the update method, essential to the movement of the item, and the launch method, which launches the item upward (and also dictates what's affected by gravity or not).

The cursor.py file outlines what the Cursor() class or object is. It's a simpler sprite object that is used to slice the fruits and rockets (the Item() objects). The tp method is used to update the location of the in-game cursor to the cursor of your system.

More details lie in the comments of each file, and attempts to describe each section of the code and what it does.