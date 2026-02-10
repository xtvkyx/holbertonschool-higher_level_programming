# Python – Everything is Object

*(Suggested picture at top: diagram showing variables pointing to objects in memory)*

---

## Introduction

One of Python’s most important concepts is that **everything is an object**. Unlike some programming languages that separate primitive data types from objects, Python treats all data as objects. Numbers, strings, lists, functions, and even classes themselves are objects stored somewhere in memory.

Understanding this concept helps developers write better, more predictable code and avoid common mistakes related to memory, references, and function behavior.

---

## `id` and `type`

Every object in Python has:

* **Type** → What kind of object it is
* **Identity** → Where it is stored in memory

Python provides two built-in functions to check these:

### `type()`

This function tells us the object’s type.

```python
a = 10
print(type(a))
```

Output:

```
<class 'int'>
```

---

### `id()`

This function returns the object’s memory address (identifier).

```python
a = 10
print(id(a))
```

Example output:

```
140715658018640
```

Two variables that point to the same object will have the same `id`.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

Output:

```
Same number for both
```

This shows that `a` and `b` reference the same object.

---

## Mutable Objects

Mutable objects are objects whose values can be changed **after creation**.

### Common mutable types:

* Lists
* Dictionaries
* Sets

### Example:

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

The change appears in both variables because they reference the same list object.

Another example showing identity staying the same:

```python
l = [1, 2, 3]
print(id(l))

l.append(4)
print(id(l))
```

The memory address does **not change** because the object itself was modified.

---

## Immutable Objects

Immutable objects cannot be changed after they are created. Any modification creates a **new object** instead.

### Common immutable types:

* Integers
* Floats
* Strings
* Tuples

### Example with integers:

```python
a = 5
print(id(a))

a += 1
print(id(a))
```

The memory address changes because Python creates a new integer object.

---

### Example with strings:

```python
s = "Hello"
s2 = s

print(s is s2)
```

Output:

```
True
```

But if we modify the string:

```python
s = s + " World"
```

Python creates a new object instead of modifying the original string.

---

## Why Does It Matter?

Understanding mutable vs immutable objects helps avoid unexpected bugs.

### Example:

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

Here, `l1 + [4]` creates a **new list**, so `l2` still references the old list.

However:

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

`+=` modifies the list in place.

This difference is critical when working with shared references.

---

## How Python Treats Mutable and Immutable Objects

Python handles objects using references rather than copying values automatically.

### Immutable objects:

* Safe to share between variables
* Python may reuse objects for performance

Example:

```python
a = 89
b = 89

print(a is b)
```

Often outputs:

```
True
```

---

### Mutable objects:

* Changes affect all references
* Python avoids automatically copying them

Example:

```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 == l2)
print(l1 is l2)
```

Output:

```
True
False
```

They have equal values but are different objects.

---

## How Arguments Are Passed to Functions

Python uses **pass-by-object-reference**. This means functions receive references to objects, not copies.

### Immutable example:

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

The integer does not change because integers are immutable.

---

### Mutable example:

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

The list changes because it is mutable.

---

### Assignment inside functions:

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]

assign_value(l1, l2)
print(l1)
```

Output:

```
[1, 2, 3]
```

Reassigning the variable inside the function does not affect the original reference.

---

## Additional Learning From Advanced Tasks

While working on this project, I also learned:

* How list copying works using slicing:

```python
def copy_list(a_list):
    return a_list[:]
```

* The difference between tuple syntax:

```python
a = (1)      # Not a tuple
a = (1,)     # Tuple
```

* How Python may reuse empty or small immutable objects for optimization.

---

## Conclusion

The concept that **everything in Python is an object** is fundamental to understanding how the language works. Learning about object identity, mutability, and reference behavior allows developers to write cleaner, safer, and more efficient code.

Understanding these concepts is especially important when working with functions, data structures, and performance optimization. Mastering them helps prevent unexpected behavior and strengthens overall programming skills in Python.

