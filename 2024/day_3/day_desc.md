# --- Day 3: Mull It Over ---

"Our computers are having issues, so I have no idea if we have any Chief Historiansin stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at theNorth Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) iscorrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just tomultiply some numbers. It does that with instructions likemul(X,Y), whereXandYare each 1-3 digit numbers. For instance,mul(44,46)multiplies44by46to get a result of2024. Similarly,mul(123,4)would multiply123by4.

However, because the program's memory has been corrupted, there are also many invalid characters that should beignored, even if they look like part of amulinstruction. Sequences likemul(4*,mul(6,9!,?(12,34), ormul ( 2 , 4 )donothing.

For example, consider the following section of corrupted memory:

```shell
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```
Only the four highlighted sections are realmulinstructions. Adding up the result of each instruction produces161(2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorruptedmulinstructions.What do you get if you add up all of the results of the multiplications?

