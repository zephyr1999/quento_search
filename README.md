# quento_search
This is a simple python 3 scipt which can solve any quento board.

Quento is a fun little iOS game developed by Q42 (https://www.q42.nl/) which involves finding sequences of numbers which sum to a particular value.
For more information on quento, see: http://quento.com/ 

Usage is as follows:
run the script in interactive mode (i like to use ipython): 

```ipython -i quento_search2.py```

the board is arranged with values:

```
a1 + a2

- a3 -

a4 + a5
```

So using the above notation, initialize a new board like:

`>>>b = Board(a1,a2,a3,a4,a5)`

Where the a's are the values found on the board.

Then simply solve the board like so:

```
>>>b.depth_value_search(depth,value)
```

And the algorithm will search the constructed tree and return the first found solution sequence. 

Here's an example. For the board:

```
8 + 5
- 4 -
3 + 1
```

you can do:

```
>>> b = Board(8,5,4,3,1)
>>> b.depth_value_search(5,13)
8 + 5 - 1 + 4 - 3 
```

The paths.txt file is all possible paths through the 3x3 square:
```
0 1 2
3 4 5
6 7 8
```
