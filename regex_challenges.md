#Regex challenges:

###Part 1: Searching a wordlist

Python code:

```python
words = ["list", "of", "words", "goes", "here"]

prob1answer = [word for word in words if re.search(r"regex goes here", word)]
```

1. Find all words that start with a vowel
2. Find all words that end with two vowels
3. Find all words that include all five vowels in order
4. Find all words that contain a five-letter palindromic substring
5. Find all words that contain a double letter
6. Find all words that contain two double letters
7. Find all words that contain the same double letter twice
8. Find all words that contain two double letters OR a five-letter palindromic substring
9. Find all words that only use the letters in "regular expression" (each letter can appear any number of times)
10. Find all words that only use letters that AREN'T in "regex"
11. Find all words that contain an "b", any character, then another "b"
12. Find all words that contain an "b", any number of characters, then another "b"
13. Find all words that contain an "b", any number of characters *including zero*, then another "b".



##Part 2: Capture groups

Given the string: `text = "Jack Nicholson, 12 Oscar nominations, Jack Nicklaus, 18 major championships, Ivory Soap, 99.4% pure, Jack Sprat, 0.0% fat, Kurtwood Smith, That '70s Show, Jack Benny, age 39, Jack London, author"`

Using `re.findall(r"regex goes here", text)`...
1. Make a list of the last names of everyone named "Jack"
2. Make a list of all of the percentages

##Extra credit: Regex golf

![xkcd](http://imgs.xkcd.com/comics/regex_golf.png)

Write the shortest regex that will match all members from one group and no members from another group.  (Assume we're using re.search, not re.match)

Category | Match all of... | ...and none of... 
--- | --- | ---
Benelux |`["Belgium", "the Netherlands", "Luxembourg"]` | `["Denmark", "Norway", "Sweden"]`
Great Lakes | `["Superior", "Ontario", "Michigan", "Huron", "Erie"]` | `["Atlantic", "Pacific", "Indian", "Arctic", "Southern"]`
Best Actors | `["Jean Dujardin", "Daniel Day-Lewis", "Matthew McConaughey", "Eddie Redmayne", "Leonardo DiCaprio"]` | `["Meryl Streep", "Jennifer Lawrence", "Cate Blanchett", "Julianne Moore", "Brie Larson"]` 
Superheroes | `["Superman", "Batman", "Wonder Woman", "Green Lantern", "Martian Manhunter", "Aquaman", "Flash"]` | `["Clark Kent", "Bruce Wayne", "Diana Prince", "Hal Jordan", "John Jones", "Arthur Curry", "Barry Allen"]`
Superheroes 2 | `["Superman", "Batman", "Wonder Woman", "Green Lantern", "Martian Manhunter", "Aquaman", "Flash"]` | `["Iron Man", "Thor", "Ant-Man", "Wasp", "Hulk", "Captain America", "Hawkeye", "Vision", "Black Widow"]`
Shakespearean tragedies | `["Antony and Cleopatra", "Coriolanus", "Hamlet", "Julius Caesar", "King Lear", "Macbeth", "Othello", "The Tragedy of Romeo and Juliet", "Timon of Athens", "Titus Andronicus", "Troilus and Cressida", "The Tempest"]` | `["All's Well That Ends Well", "A Midsummer Night's Dream", As You Like It", "The Comedy of Errors", "Love's Labour's Lost", "Measure for Measure", "The Merchant of Venice", "Merry Wives of Windsor", "Much Ado about Nothing", "The Taming of the Shrew", "The Two Gentlemen of Verona", "Twelfth Night",]`
Grab bag | `["baptize", "ember", "gauntlet", "head start", "herb", "polysyllabic", "sandy", "sword"]` | `["barbarian", "embark", "rhubarb", "sandbar", "scabbard", "threadbare", "wheelbarrow", "zanzibar"]`
Grab bag 2 | `["acidic", "activity", "agitation", "agonizing", "aligning", "authenticity", "authoritative", "awkward"]` | `["absolve", "activating", "agony", "alpha", "ant", "argumentative", "authentic", "author"]`

When you're done, read Google's Peter Norvig describe writing a regex golf solver, which includes a fascinating look at how a very good programmer codes and, particularly in the second part, thinks about algorithms.
* Part 1: http://nbviewer.jupyter.org/url/norvig.com/ipython/xkcd1313.ipynb
* Part 2: http://nbviewer.jupyter.org/url/norvig.com/ipython/xkcd1313-part2.ipynb?create=1