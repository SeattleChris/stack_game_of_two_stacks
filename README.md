# stack_game_of_two_stacks

Alexa has two stacks of non-negative integers, stack `a[n]` and stack `b[m]` where index `0` denotes the top of the stack. Alexa challenges Nick to play the following game:

* In each move, Nick can remove one integer from the top of either stack `a` or stack `b`.
* Nick keeps a running sum of the integers he removes from the two stacks.
* Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer `maxSum` given at the beginning of the game.
* Nick's final score is the total number of integers he has removed from the two stacks.

Given `a`, `b`, and `maxSum` for `g` games, find the maximum possible score Nick can achieve.

## Function Description

Complete the twoStacks function in the editor below.

twoStacks has the following parameters:

* int maxSum: the maximum allowed sum
* int a[n]: the first stack
* int b[m]: the second stack

Returns

* int: the maximum number of selections Nick can make

## Constraints

* 1 <= g <= 50
* 1 <= n,m <= 10^5
* 0 <= a[i],b[i] <= 10^6
* 1 <= maxSum <= 10^9

Subtasks:

* 1 <= n,m <= 100 for 50% of the maximum score.
