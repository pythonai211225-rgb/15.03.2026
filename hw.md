# Homework – Lists and Dictionaries

Solve the following exercises using **Python code**.

## Exercise 1 – Group words by length

```
["apple","banana","kiwi","grape","melon","pear"]

-> {
    5: ["apple","grape","melon"],
    6: ["banana"],
    4: ["kiwi","pear"]
}
```

Write a function that groups words by **number of letters**.

The **key** should be the length of the word, and the **value** should be a list of all words with that length.

```python
def group_words_by_length(words: list) -> dict:
    '''

    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    pass
```

## Exercise 2 – Average grade

```
grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

-> 82.5
```

Write a function that calculates the **average grade of all students**.

```python
def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    pass
```

## Exercise 3 – Group numbers by sign

```
[4, -2, 0, 7, -5, 3]

-> {
    "positive": [4,7,3],
    "negative": [-2,-5],
    "zero": [0]
}
```

Write a function that groups numbers based on their **sign**.

```python
def group_numbers(nums: list) -> dict:
    '''

    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    pass
```

**Submission email:** [pythonai211225+python18dict2@gmail.com](mailto:pythonai211225+python18dict2@gmail.com)
