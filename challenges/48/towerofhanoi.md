# Challenge #48 - Towers of Hanoi

The Towers of Hanoi is a mathematical game consisting of 3 rods (A, B, and C) and N disks. Initially, all of th edisks are stacked in decreasing value of diameter, where the smallest disk is placed on the top and they are on rod A. The objective is to move the entire stack to another rod, in this case either B or C, obeying these 3 rules:
- Only one disk can be moved at a time
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
- No disk can be placed on top of a smaller disk


The minimal number of moves required to solve a Tower of Hanoi puzzle is 2<sup>n</sup>-1, which is what we can use to verify our algorithm is correct.

### NOTE: You may find that the puzzle will be incomplete, this is most likely due to recursion depth limit your compiler has. I probably won't make the iterative version of this