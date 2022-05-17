# Problem 

Write a function called repeatStr which repeats the given string string exactly n times.
```python
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
```

# Answer 

```python

def repeat_str(repeat, string):
    return string * repeat

```
NOTE :
The repetition operator is denoted by a '*' symbol and is useful for repeating strings to a certain length. 


# Advanced Answer

```python 

from operator import mul as repeat_str

```

NOTE :
The  ***mul*** function takes 2 arguments at a time and returns their product. 
