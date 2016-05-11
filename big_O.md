## Time Complexity

One of the common questions in programming is: "How long will this take?"  It's a hard question to answer!  Let's say I'm testing my bubble sort code:

```python
def bubble(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                done = False
```

One idea would be to generate a random list and see how long it takes to run:

```python
from time import time
from random import randint

start = time()

randomlist = [randint(0,10000) for x in range(100)]

bubble(randomlist)
print(randomlist)

print("All done in {} seconds!".format(time()-start))
```

This gives the message `All done in 0.015505075454711914 seconds!`  It's nice to know, but it's heavily dependent on my machine, and there's always a chance that the random list was already nearly in order, so the bubble sort function didn't have to do any work.  Clearly, we need a more rigorous definition.

## Big O Notation

Computer scientists describe time complexity in Big O notation.  There's a mathematical definition (as well as related terms such as Big Omega and Big Tau), but for our purposes, it's how long it takes to perform a function on an input of size n.

Several operations are considered constant time (`O(1)`).  No matter how large the input is, it always takes the same amount of time for the computer to perform the operation.

* Checking if an integer is odd or even (`%2`)
* Checking if one number is larger than another (`>`)
* Most arithmatic (`+`, `-`, `*`, `/`)
* Setting a variable (`foo = 12`)
* Reading the value in a given position in an array (`arr[4]`)
* Finding a key in a dictionary (`dict["bar"]` or `"bar" in dict`)

Similarly, there are some algorithms that require doing a constant-time operation once for each item in your data.  There are considered linear time (`O(n)`).  One simple example if finding the maximum value in an unsorted array.  You should have written this as part of the Basic 13 algorithms; your code probably looks something like this:

```python
def max_val(arr):
	max_so_far = arr[0]
	for val in arr[1:]:
		if val > max_val: max_val = val
	return max_val
```

As you can see, if your array has n items, the `max_val` function does n constant-time operations (setting or comparing variables).  If you think of the constant operations as taking 1 time-unit, then this must take 1*n time-units.

"But wait!" you might be saying.  "Consider the array `[1,2,3,4]`!  You claim that will take 4 time-units, but since both comparing and setting a variable take 1, this will really take 7!  This should be `O(2n-1)`!"  First, pat yourself on the back, that's a very astute point.  Second, it turns out it doesn't really matter.  When we talk about time complexity, we're generally a) just comparing to other functions as also measured in Big O notation, and b) thinking about arbitarily large input.  Once n gets big, really really big, that "-1" won't make a difference, so we can say `O(2n)`.  Similarly, once n is large enough, a*n will be larger than b, and less than c*n^2 no matter what (positive) values of a, b, and c you choose, so we can just say `O(n)`.

Some other linear-time operations:

* Checking if a value is in an unsorted array (`"foo" in arr`)
* Finding all even numbers in an array (`[i for i in arr if i%2==0]`)
* Creating a dictionary based on an array, with keys the unique answers in the array and values how many times they appear.
* Checking if a string is a palindrome
* Finding a value in a singly-linked list

Continuing from above, if your function does a linear-time operation once for every item in your input, or a constant-time operation n times for every item, it takes `O(n^2)`, or quadratic, time.  For bubble sort, each loop through the list comparing and potentially swapping adjacent elements takes linear time, and it could take up to n times through the list before everything's in order.  Other `O(n^2)` algorithms include:

* Finding a value in a 2-dimensional array (an array of arrays)
* Selection sort
* Insertion sort
* Pretty much any other sort easy enough that you might think to implement it by hand

The naive, first-guess approach to solving a problem is usually `O(n^2)` or worse.  As a rule of thumb, you can guess a program's time complexity by counting the number of nested loops.  One loop is linear, two is quadratic, three is cubic, and so forth.  (This class of algorithms, with time complexity `O(n^a)` or better, are known as "polynomial time.")  This approximation breaks down for more complicated or clever code (it's possible to write something with a nested for-loop that's still in linear time, for example), but generally you should be wary if you have a loop inside of a loop.

##And Beyond

Consider this function:

```python
def binary_search(arr, num):
    """Uses a binary search to check if a value is in a sorted array"""
    low, high = 0, len(arr)-1
    while high > low+1:
        mid = int((high+low)/2)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            low = mid
        else:
            high = mid
    if arr[high] == num or arr[low] == num:
        return True
    else:
        return False
```

What's the time complexity?  If you're using the rule of thumb, you might say `O(n)` because there's one loop.  However, look more closely.  The binary search eliminates half of the potential search space each time, so the while loop runs at most log-2 times.  (Need a refresher on logarithms?  Try this [University of Utah site](http://www.math.utah.edu/~pa/math/log.html) from 1997, ideally on the newest version of Netscape.)  `O(log n)` is fantastic: If you double the length of your array, worst-case it will only take one additional pass of the loop!  Unfortunately, most problems don't have a log time solution.

More common is `O(n log n)`.  It's hard to conceptualize or recognize off-hand, but this would be algorithms that do a linear number of operations a logarithmic number of times.  Clever sort algorithms, like quicksort or mergesort, fall into this camp, as they involve recursively cutting a list in half, based on a function that looks at every element in each sublist once.  In fact, it's been proven that comparison-based sorting can't be any better than `O(n log n)`.

On the other hand, consider this program to calculate the nth Fibonacci number:

```python
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-2) + fib(n-1)
```

What's the time complexity?  Well, the first level calls the function twice, so the second level involves four function calls, then eight, then sixteen... In fact, this is `O(2^n)`!  Ay-yi-yi!  (This is why I say that recursive Fibonacci is a trap.)  Listing all of the possible subsets of a set is likely also 2^n time.

Even worse than that is `O(n!)`.  When time complexity gets that bad, it's hard to find simple examples, but this would include a brute-force solution to the [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), or any other function that looks at every possible permutation of a given set.

`O(2^n)` and `O(n!)` aren't good, obviously, but sometimes they're unavoidable.  In fact, it's generally believed (though not yet proven) that many interesting problems, ranging from how to efficiently pack a knapsack to factoring the product of two large primes to solving a sudoku puzzle, can't be solved better than `O(2^n)`.  (It's always been proved, somewhat surprisingly, that these problems are equally hard, computationally speaking; one problem can be transformed into another in polynomial time.  This means that if you come up with a very clever sudoku solver, you might at the same time be undermining all modern cryptography.)

##Further Thoughts

* __Average case__: Though all of this, we've been looking at worst-case time complexity.  There's an argument that it would make more sense to focus on average-case instead; after all, that's what the performance will be most of time, whereas the worst case could be very rare.  (Indeed, the preferred method for maximizing a linear system, [Dantzig's simplex algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm), is used because of its polynomial average case, although it's been shown to have worst-cast `O(2^n)`.)  It's worth keeping in mind, but programmers are a pessimistic lot, so the standard in the field is to look at worst-case.
* __Best case__: Similarly, you might be wondering about best-case time complexity.  This is usually only a curiousity, but understanding what type of input would lead to your best-case performance can be very helpful, as if you know your data will look a certain way you can tailor your algorithm to fit it.  For example, if you don't know anything about the data that will be fed in, you'd never choose bubble sort over quicksort.  However, if you know your data will already be almost entirely sorted, with maybe a few elements slightly out of place, then bubble sort will be very close to its `O(n)` best-case, whereas quicksort will still take `O(n log n)`.
* __Space complexity__: We can also measure space complexity, how much memory a program will need, in terms of Big O notation.  It's generally less important than time complexity in modern environments--it's easier to add memory to your system than add hours to the day--but it's an important consideration if you're working in a system with tight limits on memory, such as a wristwatch or a Mars lander, or if you're trapped decades in the past.  There's generally a trade off between time and space, with fast algorithms requiring more memory, but it's not definitive; you can write something that both takes a long time *and* uses all of your memory (like, say, recursive Fibonacci).
* __`O(∞)`__: Just for fun, here's an example of an algorithm with the worst possible performance.  Behold the bogosort:  
```python
import random
def is_sorted(arr):
	if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
		return True
	else:
		return False
	# You can write a more efficient is_sorted function, but as we'll see, it won't matter
def bogosort(arr):
	while not is_sorted(arr):
		random.shuffle(arr)
	return arr
```
This is average-case factorial time, worst-case infinite time.

##Futher Reading

* [Big O cheat sheet](http://bigocheatsheet.com/)
* Dionysis Zindros's [Gentle Introduct to Algorithm Complexity Analysis](http://discrete.gr/complexity/) is very good and a little more technical than I was aiming for here