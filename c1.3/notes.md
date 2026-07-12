# C1.3 — Lists & Tuples in Python: Notes

Summary of concepts covered by [p10.py](p10.py), [py11.py](py11.py), [p12.py](p12.py), [p13.py](p13.py), [p14.py](p14.py), and [p15.py](p15.py).

## 1. List Basics, Mutability & Slicing ([p10.py](p10.py))

- A `list` is written with square brackets: `[50, 60, 70, 80, 90]`; `type(x)` confirms it's `list`.
- Lists can hold mixed types in one literal (`["John", 20, "Male", 122101]`) — no type constraint per element.
- Two ways to iterate a list with a `for` loop:
  - `for item in list:` — iterate directly over values.
  - `for i in range(len(list)):` — iterate over indices when you also need the position (`list[i]`).
- **Strings are immutable, but lists are mutable** — `student1[0] = "John Doe"` reassigns an element in place; the same operation on a string would raise a `TypeError`.
- List slicing mirrors string slicing (`list[start:stop:step]`):
  - `charList[0:4]` — elements at index 0–3.
  - `charList[0:]` / `charList[:]` — full shallow copy of the list.
  - `charList[-1]` — last element (negative indexing).
  - `charList[-4:-1]` — slice using negative bounds on both ends.
  - `charList[::2]` — every second element (step = 2).
  - `charList[3::4]` — start at index 3, then step by 4.

## 2. Common List Methods — Mutating in Place ([py11.py](py11.py))

| Method | Effect |
|---|---|
| `.append(x)` | Adds `x` to the end of the list |
| `.sort()` | Sorts the list ascending, in place |
| `.sort(reverse=True)` | Sorts descending, in place |
| `.reverse()` | Reverses the current order of elements, in place |
| `.insert(i, x)` | Inserts `x` at index `i`, shifting later elements right |
| `.remove(x)` | Removes the **first** occurrence of value `x` (raises `ValueError` if not found) |
| `.pop(i)` | Removes and returns the element at index `i` |
| `.pop()` | Removes and returns the **last** element (no index needed) |
| `.clear()` | Empties the list in place, leaving `[]` |

- All of these methods mutate the list **in place** and return `None` (except `.pop()`, which returns the removed item) — this is the key contrast with string methods, which always return a new value.

## 3. Tuple Basics — Immutable Sequences ([p12.py](p12.py))

- A `tuple` is written with parentheses: `(1, 2, 3, ..., 10)`; `type(x)` confirms it's `tuple`.
- **Tuples are immutable, but lists are mutable** — a tuple has no `.append()`, `.sort()`, `.remove()`, etc.; once created, its contents can't change.
- Tuples support the same read-only operations as lists/strings:
  - Indexing: `tup1[0]`, `tup1[-1]`.
  - `len(tup1)` — number of elements.
  - Slicing: `tup1[0:4]`, `tup1[0:]`, `tup1[:]`, `tup1[-4:-1]`, `tup1[::2]`, `tup1[3::4]` — identical slicing rules to lists and strings.
- Tuple-specific query methods (both work on any tuple, no mutation involved):
  - `.count(x)` — how many times `x` appears.
  - `.index(x)` — index of the first occurrence of `x`.

## 4. Building a List Interactively ([p13.py](p13.py))

- `int(input(...))` reads how many items to collect, then a `for i in range(num):` loop prompts once per item and `.append()`s each to a starting `[]`.
- `f"Enter the name of movie {i+1}: "` — `i+1` converts a 0-based loop index into a human-friendly 1-based prompt.
- Pattern: **start with an empty list, grow it with `.append()` inside a loop** — the standard way to collect a variable number of inputs.

## 5. Checking for a Palindrome with Slicing ([p14.py](p14.py))

- `palindromeList[::-1]` — step `-1` reverses a list (or string/tuple) without a named method, by slicing over the whole sequence backwards.
- A palindrome check is just an equality comparison: `original == original[::-1]`.
- `==` on lists compares **element-by-element**, not by identity — two separately-built lists with the same values and order are equal.

## 6. Converting a Tuple to a List ([p15.py](p15.py))

- `.count(x)` on a tuple works the same as on a list (see [p12.py](p12.py)) — counts occurrences of `x`.
- To convert a tuple into a list manually: start with `emptyList = []`, then loop `for i in range(len(tup1)): emptyList.append(tup1[i])`.
- (Note: Python also provides `list(tup1)` as a direct built-in conversion — the manual loop shown here achieves the same result "by hand" for practice.)

## Key Takeaways

- **Lists are mutable** (`.append`, `.sort`, `.insert`, `.remove`, `.pop`, `.clear` all modify in place); **tuples are immutable** (read-only: indexing, slicing, `.count()`, `.index()`).
- Indexing, slicing (`[start:stop:step]`), and negative indices work identically across `str`, `list`, and `tuple` — they're all sequence types.
- `seq[::-1]` reverses any sequence via slicing — a common idiom for reversal and palindrome checks.
- To collect a variable number of inputs, start with an empty list and `.append()` inside a loop (`p13.py`); the same index-loop pattern can copy a tuple's elements into a list (`p15.py`).
- `list.remove(x)` and `tuple.index(x)` both operate on the **first matching value**, and both raise an error if the value isn't present — check membership with `in` first if that's a concern.
