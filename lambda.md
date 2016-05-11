## Sorted

`sorted` is a function that takes in a list and returns a new, sorted list.

```python
nums = [3,2,6,1,5]
sorted(nums) # [1,2,3,5,6]
```

It also works on words!

```python
animals = ['monkey', 'eagle', 'giraffe', 'emu', 'seal']
sorted(animals) # ['eagle', 'emu', 'giraffe', 'monkey', 'seal']
```

Makes sense, right?  "Ea" comes before "em" comes before "g" and so forth.  But what if I wanted to sort based on where the first "e" is in the word?

```python
sorted(animals, key=lambda x: x.find("e")) # ['eagle', 'emu', 'seal', 'monkey', 'giraffe']
```

Woah, woah, woah--What just happened?  What's `lambda`?

##Lambda

The term "lambda" comes from an attempt to formally define mathematics from the 1930s.  You can read about it on [Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus), and if you understand it, maybe you can explain it to me.  I like another name for the same concept, "anonymous functions".  As that suggests, a lambda function is just a function that doesn't have a specific name.  Why would we want that?  Because it's a function we'll only use in one place.

##Anatomy of an Anonymous Function

There are three pieces to a lambda function:

1. The keyword `lambda`.  Duh.
2. The parameters that your anonymous function takes.  In a traditional function, these would go in the parentheses after the function name (the `x` in `def func(x):`).
3. A single expression that your function will return.  In a traditional function, this would be, unsurprisingly, anything after the `return` keyword.

This anonymous function takes a single parameter, num, and returns that number times 2:

```python
lambda num: num*2
```

And here's a lambda that takes multiple parameters:

```python
lambda a,b: a*a + b*b
```

It's not too useful on its own, but we can assign it to a variable.

```python
f = lambda a,b: a*a + b*b
f(3,4) # 25
```

Of course, anything you can write as a lambda can also be written as a named function.

```python
def f(a,b):
	return a*a + b*b
```

The lambda version is shorter, but more importantly, it's more convenient to use as a callback.

##Callback?

A callback is a function that's passed into another function as a parameter.  Let's take another look at the `sorted` example from earlier:

```python
sorted(animals, key=lambda x: x.find("e")) # ['eagle', 'emu', 'seal', 'monkey', 'giraffe']
```

`sorted` takes an optional parameter, `key`, that's a callback function, and sorts the list based on the results of that function.  `'eagle'.find('e')` = 1, so it's first, `'giraffe'.find('e')` = 7, so it's last, and so forth.  (I believe when the key returns the same value for two entries, as with 'eagle' and 'emu' here, it defaults to the normal order.)  As before, we can accomplish the same thing with a named function:

```python
def find_first_e(word):
	return word.find("e")

sorted(animals, key=find_first_e) # ['eagle', 'emu', 'seal', 'monkey', 'giraffe']
```

This code is perfectly fine, but if we know that there's no other place we'll need to use the `find_first_e` function, there's no reason to save it to memory.  Lambda functions are perfect for this type of one-time-use situation.

Here are some sorts with other possible keys:
```python
# By length
sorted(animals, key=lambda x: len(x)) # ['emu', 'seal', 'eagle', 'monkey', 'giraffe']

# By third letter
sorted(data, key=lambda x: x[2]) # ['seal', 'eagle', 'monkey', 'giraffe', 'emu']

# By the sine of the ASCII code of the last letter
import math
sorted(animals, key=lambda x: math.sin(ord(x[-1]))) # ['emu', 'eagle', 'giraffe', 'seal', 'monkey']
```

As that last example shows, lambdas can get pretty complicated while still a single line, and they have something of a reputation in the Python community for being ugly.  In real code, you may want to consider making that into a named function just for readability.

You can also add a `key` parameter to `max` and `min`.  One common task is to find the key in a dictionary with the highest or lowest associated value.  Lambdas make that a snap.

```python
data = {"alpha": 4, "bravo": 2, "charlie": 7, "delta": 1, "echo": 5, "foxtrot": 3}
max(data, key=lambda x: data[x]) # 'charlie'
min(data, key=lambda x: data[x]) # 'delta'
```  

##Other Uses

Beginning programmers can have trouble thinking about callback functions.  When would a function ever take another function as an argument?  Here are some examples that the platform presents under the umbrella of the Underscore.js library:

####Map

Takes in a function and an iterable (a list, dictionary, or anything else you can loop through) and outputs the results of applying that function to every element of the iterable.

```python
nums = [2,3,4,5]
list(map(lambda x: x*(x+1), nums)) # [6, 12, 20, 30]
```

####Filter

Takes in a function that returns a boolean (true/false) value and an iterable and outputs an iterable with the items were the function would return true.

```python
nums = [2,3,4,5]
list(filter(lambda x: x%2==0, nums)) # [2,4]
```

####Reject

The opposite of filter.  Returns the items in an iterable where the given function returns false.

```python
nums = [2,3,4,5]
list(reject(lambda x: x%2==0, nums)) # [1,3]
# (This won't actually work, as Python doesn't have a built-in reject function, though you'll write one in the underscore assignment.)
```

####Reduce

Changes an iterable into a single value by repeatedly applying a given function to each element in turn.

```python
from functools import reduce # In Python 3, reduce was moved from the standard library to the functools module
reduce(lambda a,b: a+b, nums) # 14 = 2 + 3 + 4 + 5
reduce(lambda a,b: a*b, nums) # 120 = 2 * 3 * 4 * 5
reduce(lambda a,b: b**(a%b), nums) # 625 (left as an exercise for the reader)
```

##A Word Of Warning

Anonymous functions can be powerful and callbacks more generally are quite important (and even moreso in other languages such as JavaScript).  However, as I mentioned, they're held in somewhat low esteem in Python.  That's because Python has its own syntax that frequently renders them unnecessary.  The underscore library functions mentioned above can all be replicated with a combination of *list comprehension* and *generator expressions*.  (Those terms don't mean much on their own, I know, but they'll make it easier for you to look up answers if something breaks.)

```python
nums = [2,3,4,5]

# map
[i**i for i in nums] # [4,27,256,3125]

# filter
[i for i in nums if i%2==0] # [2,4]

# reject
[i for i in nums if i%2!=0] # [3,5]
[i for i in nums if not i%2==0] # [3,5] alternate syntax

#reduce
sum(i for i in nums) # 14; you can also just do sum(nums)
```
