#Regex challenges:

###Part 1: Searching a wordlist

Python code:

```python
words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

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
13. Find all words that contain an "b", any number of characters *including zero*, then another "b"



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
Benelux |`['belgium', 'the netherlands', 'luxembourg']` | `['denmark', 'norway', 'sweden']`
Great Lakes | `['superior', 'ontario', 'michigan', 'huron', 'erie']` | `['atlantic', 'pacific', 'indian', 'arctic', 'southern']`
Best Actors | `['jean dujardin', 'daniel day-lewis', 'matthew mcconaughey', 'eddie redmayne', 'leonardo dicaprio']` | `['meryl streep', 'jennifer lawrence', 'cate blanchett', 'julianne moore', 'brie larson']` 
Superheroes | `['superman', 'batman', 'wonder woman', 'green lantern', 'martian manhunter', 'aquaman', 'flash']` | `['clark kent', 'bruce wayne', 'diana prince', 'hal jordan', 'john jones', 'arthur curry', 'barry allen']`
Superheroes 2 | `['superman', 'batman', 'wonder woman', 'green lantern', 'martian manhunter', 'aquaman', 'flash']` | `['iron man', 'thor', 'ant-man', 'wasp', 'hulk', 'captain america', 'hawkeye', 'vision', 'black widow']`
Python modules | `['__future__', 'array', 'base64', 'collections', 'datetime', 'fractions', 'functools', 'hashlib', 'http', 'itertools', 'json', 'operator', 'pickle', 'random', 're', 'string', 'subprocess', 'tkinter', 'turtle', 'unittest']` | `['beautifulsoup4', 'Django', 'Flask', 'itsdangerous', 'Jinja2', 'pep8', 'Pillow', 'pip', 'psycopg2', 'pytz', 'requests', 'selenium', 'setuptools', 'simplejson', 'six', 'SQLAlchemy', 'virtualenv', 'wheel']`
Shakespearean tragedies | `['antony and cleopatra', 'coriolanus', 'hamlet', 'julius caesar', 'king lear', 'macbeth', 'othello', 'the tragedy of romeo and juliet', 'timon of athens', 'titus andronicus', 'troilus and cressida', 'the tempest']` | `["all's well that ends well", "a midsummer night's dream", 'as you like it', 'the comedy of errors', "love's labour's lost", 'measure for measure', 'the merchant of venice', 'merry wives of windsor', 'much ado about nothing', 'the taming of the shrew', 'the two gentlemen of verona', 'twelfth night']`
Grab bag | `['baptize', 'ember', 'gauntlet', 'head start', 'herb', 'polysyllabic', 'sandy', 'sword']` | `['barbarian', 'embark', 'rhubarb', 'sandbar', 'scabbard', 'threadbare', 'wheelbarrow', 'zanzibar']`
Grab bag 2 | `['acidic', 'activity', 'agitation', 'agonizing', 'aligning', 'authenticity', 'authoritative', 'awkward']` | `['absolve', 'activating', 'agony', 'alpha', 'ant', 'argumentative', 'authentic', 'author']`

When you're done, read Google's Peter Norvig describe writing a regex golf solver, which includes a fascinating look at how a very good programmer codes and, particularly in the second part, thinks about algorithms.
* Part 1: http://nbviewer.jupyter.org/url/norvig.com/ipython/xkcd1313.ipynb
* Part 2: http://nbviewer.jupyter.org/url/norvig.com/ipython/xkcd1313-part2.ipynb?create=1