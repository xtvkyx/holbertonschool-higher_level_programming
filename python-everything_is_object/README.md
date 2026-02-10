# Python – Everything is Object

## Introduction

In this project, I learned that in Python everything is considered an object. This means numbers, strings, lists, functions, and even classes are stored in memory as objects. Understanding this idea helps programmers know how Python works internally and helps avoid mistakes when working with variables.

---

## id and type

Python gives us two functions to learn more about objects: `type()` and `id()`.

`type()` tells us what kind of object we are working with.

```python
a = 10
print(type(a))
```

Output:

```
<class 'int'>
```

`id()` shows the memory address of the object.

```python
a = 10
print(id(a))
```

If two variables have the same `id`, it means they are pointing to the same object in memory.

---

## Mutable Objects

Mutable objects are objects that can be changed after they are created. Examples include lists, dictionaries, and sets.

Example:

```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)
print(l2)
```

Output:

```
[1, 2, 3, 4]
```

The list changed in both variables because they refer to the same object.

---

## Immutable Objects

Immutable objects cannot be changed after they are created. Examples include integers, strings, and tuples.

Example:

```python
a = 5
a += 1
```

When we change `a`, Python actually creates a new object instead of modifying the original one.

---

## Why Does It Matter?

Knowing the difference between mutable and immutable objects helps prevent bugs. Sometimes changing one variable might affect another variable if they reference the same object.

For example:

```python
l1 = [1, 2, 3]
l2 = l1
l1 += [4]
print(l2)
```

Output:

```
[1, 2, 3, 4]
```

But:

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

Output:

```
[1, 2, 3]
```

---

## How Arguments Are Passed to Functions

Python passes objects by reference.

Example with immutable objects:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

Output:

```
1
```

The value does not change.

---

Example with mutable objects:

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

Output:

```
[1, 2, 3, 4]
```

The list changes because lists are mutable.

---

## Conclusion

This project helped me understand how Python handles objects in memory. Learning about mutability, identity, and references is very important because it affects how variables behave in programs. This knowledge will help me write better and more efficient Python code in the future.

