# Super Mario Stairs

Super Mario Bros. (1985) is among the most iconic videogames of all time.

Even though the game has 32 levels, many speedrunners can beat the entire thing in under five minutes.

However, even the most accomplished speedrunners can have their runs foiled by a run in with the dreaded stairs:

![SMB1 Stairs](smbstairs.png)

One wrong move on these steps, and your momentum is gone, and with it, any chance of a world-record time.

## The Goal

We're going to write three functions: one to build downward stairs, one to build upward stairs, and one to build pyramid stairs (they go up and then back down).

Here's what your code should ultimately be able to do:

#### Code for descending stairs:

```python
downstairs(4)
```

The code above should print a descending staircase of four steps to the console like this:

```bash
#
##
###
####
```

#### Code for ascending stairs:

```python
upstairs(6)
```

The code above should print an ascending staircase of six steps to the console like this:

```bash
     #
    ##
   ###
  ####
 #####
######
```

#### Code for pyramid stairs:

```python
pyramid(4)
```

The code above should print an ascending staircase of 4 steps and it's mirror descending staircase to the console like this:

```bash
   # #
  ## ##
 ### ###
#### ####
```

## Skills You May Need

### Printing Without Newlines

In Python, it's important to notice that when we use the print() function, the computer automatically adds a newline character (a press of the enter key) after the string you tell it to print.

Sometimes, though, you may want to use the print() function multiple times and have all the text show up on the same line. You can do that by specifying a second parameter in the print() function called end and setting it to an empty string.

Here are some examples:

```python
print("Welcome user!")
print("This is a standard print statement.")

print("This is a print statement without a newline.", end = "")
print("This is another print statement.", end = "")
```

The code above will print to the console like this:

```
Welcome user!
This is a standard print statement.
This is a print statement without a newline.This is another print statement.
```

### For-in loops

Doing this will be a little repetitive. You may want a way to loop through code.

One of the most precise ways of doing this is with a for-in loop. Feel free to catch a refresher of that concept from our <a href="https://github.com/upperlinecode/leap-year-python-methods">leap year lab</a>.
