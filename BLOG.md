# Sort-Algorithm

In python, merge sort is defined as one of the sorting algorithms which is general-purpose, uses comparison based sorting by divide and conquer algorithm where the idea is to break down the list into sub-lists until each sub-list has max one element and merge all the sub-lists in reverse order to get the sorted sub-lists and finally a single list which is sorted is called merge sort. It is an efficient, general-purpose, and best sorting algorithm with the overall, average, and worst-case time complexity being O(nlogn).

# The logic behind Merge Sort in Python
***(Divide and Conquer)***
*Divide*
- divide the problem into multiple subproblems.
- solve the sub-problems by further dividing the sub-problems into atomic problems where they have an exact solution.
- combine all sub solutions to get the final solution to the given problem.
*Conquer*
- take two variables, “start” and “end”, where “start” will store the starting index, i.e. 0 in it, and the end will store the length of the list
- Using start and end variables,  find the middle of the list by using the formula as (start+end)/2 and store the result in variable mid, and divide the list into 2 sub-lists as a start to mid as one sub-list and mid+1 to end as another sub-list.
- divide the sub-lists into further sub-lists as atomic problems by following the process in step 2.
- merge all sub-lists with solutions to get the final list that will be in sorted order.

[White Board](Untitled%20(2).jpg)