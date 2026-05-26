## WEEK02: BIG MISUNDERSTANDING AND MISUSE: build-max-heap vs max-heapify
- build-max-heap is to get the largest/smallest element in the whole array
- max-heapify is to get the largest/smaless element to a specific index in a limited number of elements in an array only (we can call this a heap). that's why we have heap_end. we don't want to max-heapify the whole array
- the build-max-heap here makes use of the max-heapify to find the largest from the middle upwards (read build-max-heap algo to recall)
