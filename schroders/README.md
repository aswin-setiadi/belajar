# Find My Number

## Setup (Tested on Windows 11 Python 3.11.5)

1. In terminal, go to schroders directory 
2. Run ```$python main.py```
3. For testing, run ```$python test.py```

## Discussion

There are a potentially maximum 8 candidates of knight move from each cell. We first build adjacency list for all the keys based on those 8 moves. At first I tried with naive dfs. The code will loop each key and traverse down until node depth of 10. Each traversal will track the node depth in a variable. If current node is a vowel, the ```vowel_count``` will keep track so it will avoid traversing down through another vowel once maximum vowel allowed reached. If the recursion reach node depth of 10, it will add to total valid 10 key sequence variable traversed so far. 

In first iteration, the program will traverse down the tree finding valid 10 key sequences, and append the 10 key sequence string to instance ```naive_results``` list. Each recursion keeps track of the current node traversed sequence and it has to copy current node seq list before passing it down as they are mutable. This significantly grow memory usage in the scenario the requested **key sequences length** increases. The program then return length of ```naive_results``` as the total number of valid 10 key sequences.

First improvement, I changed the ```seq``` parameter to ```int``` so every down traversal just +1 instead of list copy and appending node key to the list, improving memory usage.

Second improvement, I applied **memoization** by tracking the total downstream valid 10 key sequences given current node conditions. The tracker marks the current node conditions as ```{vowel_count}_{node}_{depth}``` where ```vowel_count``` is the current node total traversed vowels, ```node``` is the current node key, and ```depth``` is the current node depth in the current traversal. These 3 conditions combination affect the total outcome of the downstream valid 10 key sequences. By tracking and pruning the already visited traversal from the recursions, the program is able to run significantly faster. The recursion will accumulate the total traversed valid 10 key sequences and then log it on a single line to standard out.

## Runtime

First successful run using time.time_ns()

- naive dfs= 801.8434047698975 ms
- replace seq ```list[str]``` to depth ```int```= 228.40213775634766 ms
- use memoization to keep track of traversed path= 9.593500 ms

Using time.perf_counter()

- naive dfs= 3.387205 ms
- replace seq ```list[str]``` to depth ```int```= 1.746320 ms
- use memoization to keep track of traversed path= 0.002575 ms

## Repository

Link: https://github.com/aswin-setiadi/belajar/tree/master

Folder: schroders