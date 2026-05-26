## WEEK02: BIG MISUNDERSTANDING AND MISUSE: build-max-heap vs max-heapify
- build-max-heap is to get the largest/smallest element in the whole array
- max-heapify is to get the largest/smaless element to a specific index in a limited number of elements in an array only (we can call this a heap). that's why we have heap_end. we don't want to max-heapify the whole array
<<<<<<< HEAD
- the build-max-heap here makes use of the max-heapify to find the largest from the middle upwards (read build-max-heap algo to recall)
=======
- the HEAPSORT is basically a sort in-place. We find the largest element, swap it to the end. And repeat the procedure to find the largest in the remainaing heap and keep swapping for n - 1 times to get n - 1 elements sorted. The remaining element will be sorted automatically (since we sort in place). first use build-max-heap to find largest in the whole array. from that onward, use max-heapify to find largest in the remaining heap (which is 0 to the heap_end)

>>>>>>> 797eacf (week02: add lesson leant in week02)
