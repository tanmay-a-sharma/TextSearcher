
## Overview



```
searcher = TextSearcher()
searcher.load("some_file.txt")
results = searcher.search("fox", 2)
```

In addition to finding matches the Search function should return the given number of words (2, in the example above) as context around the matched word.

For example given a file containing,
> The quick brown fox jumped over the lazy dog.

running `searcher.Search("fox", 2)` would return.
> quick brown fox jumped over





### python
Provided a `Pipfile` for usage with `pipenv`, but any recent version of python and pytest should be sufficient for running the tests.

### Files


**files/Siddhartha.txt**
A larger text file which is used by some of the tests to validate your solution.

**files/Siddhartha.opening.txt**
A smaller text file which is used by some of the tests to validate your solution.


### Requirements and assumptions
* A word consists of any sequence of the characters a-z, A-Z, 0-9, apostrophe, and dash. Therefore, “animal’s” is a single word, as are “1844” and “xxxxx10x”.
* Any non-word character is regarded as punctuation and will be ignored by the search (but included in the results).
* Search should be case-insensitive, so "fox" and "Fox" should return the same set of results.
* You don't have to worry about matching plural words: "river" does not have to find occurrences of "rivers".
* Strings should be returned in document order.
* Strings should be returned exactly as they appear in the document, including original punctuation and capitalization.
* The exception to the previous rule is white space. Strings should be return with extraneous whitespace removed.
* Overlapping hits require no special treatment; each should be returned as a separate hit.
* If no hits are found it should return an empty array.
* It is safe to assume that the contents of the underlying file can be held in memory.
* The assumption is that a single file with be read into the `TextSearcher` once and then the searched multiple times. Your implementation should be most efficient at searching.
