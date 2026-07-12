# C1.4 — Dictionaries & Sets in Python: Notes

Summary of concepts covered by [p16.py](p16.py) and [p17.py](p17.py).

## 1. Dictionary Basics ([p16.py](p16.py))

- A `dict` stores data as **key-value pairs**, written with curly braces: `{"name": "John Doe", "age": 20, ...}`.
- Each key must be **unique**; keys aren't limited to strings — `1` and `12.99` are valid keys alongside string keys in the same dict.
- Dictionaries are **mutable** — contents can be changed after creation.
- Dictionaries can be **nested** — a value can itself be a dict (`"address": {"street": ..., "city": ...}`) or a list (`"subjects": ["Math", "Science", "History"]`).
- Accessing values:
  - `student["name"]` — direct key lookup; raises `KeyError` if the key doesn't exist.
  - `student["address"]["city"]` — chained lookup to reach a nested dict's value.
  - `student.get("name")` — safe lookup; returns `None` (or a supplied default) instead of raising if the key is missing: `student.get("phone", "Not Found")`.

### Dictionary Methods

| Method | Purpose |
|---|---|
| `.keys()` | Returns a `dict_keys` view of all keys |
| `.values()` | Returns a `dict_values` view of all values |
| `.items()` | Returns a `dict_items` view of `(key, value)` tuples |
| `.get(key, default)` | Safe lookup — returns `default` (or `None`) instead of raising `KeyError` |
| `.update(other_dict)` | Merges `other_dict` into the dictionary, adding new keys / overwriting existing ones |

- `len(student)` returns the number of key-value pairs (top-level keys only — nested dict/list entries don't add to the count).

## 2. Set Basics ([p17.py](p17.py))

- A `set` is an **unordered collection of unique elements**, written with curly braces: `{1, 2, 3, 2, 3}` → duplicates are automatically dropped.
- `type(x)` confirms it's `set`; `len(x)` gives the number of unique elements.
- **Gotcha:** `{}` creates an empty **dict**, not an empty set — use `set()` to create an empty set.
- Sets require **hashable** elements: numbers, strings, and tuples work; `9` and `9.0` are treated as the *same* element (equal hash), but `9` and `'9.0'` are different (different types). Tuples can be set elements as long as they're hashable.

### Set Methods — Mutating

| Method | Effect |
|---|---|
| `.add(x)` | Adds a single element `x` |
| `.update(iterable)` | Adds multiple elements at once, from a set, list, etc. |
| `.remove(x)` | Removes `x`; raises `KeyError` if `x` isn't present |
| `.discard(x)` | Removes `x` if present; does **nothing** (no error) if absent |
| `.pop()` | Removes and returns an **arbitrary** element (sets are unordered, so which one is unpredictable); raises `KeyError` on an empty set |
| `.clear()` | Empties the set, leaving `set()` |

### Set Methods — Comparisons Between Sets (Set Algebra)

Given `ASet = {1,2,3,4,5}` and `BSet = {4,5,6,7,8}`:

| Method | Meaning | Example Result |
|---|---|---|
| `.union(other)` | All elements from both sets | `{1,2,3,4,5,6,7,8}` |
| `.intersection(other)` | Elements common to both | `{4,5}` |
| `.difference(other)` | Elements in this set but not `other` | `ASet.difference(BSet)` → `{1,2,3}` |
| `.symmetric_difference(other)` | Elements in either set, but not both | `{1,2,3,6,7,8}` |
| `.issubset(other)` | `True` if this set's elements are all in `other` | `BSet.issubset(ASet)` → `False` |
| `.issuperset(other)` | `True` if this set contains all of `other`'s elements | `ASet.issuperset(BSet)` → `False` |
| `.isdisjoint(other)` | `True` if the two sets share no elements | `ASet.isdisjoint(BSet)` → `False` |

- `.difference()` is **not symmetric** — `ASet.difference(BSet)` and `BSet.difference(ASet)` give different results (each removes the *other* set's elements from itself).

## Key Takeaways

- Use a **dict** when you need to look values up by a meaningful key; use a **set** when you need a collection of unique, unordered values with fast membership tests.
- `dict.get(key, default)` and `set.discard(x)` are the "safe" variants that avoid exceptions — prefer them over `dict[key]` / `set.remove(x)` when the key/element might not exist.
- Both dicts and sets require their keys/elements to be **hashable** — this is why `9` and `9.0` collapse to one set element (same hash) but `9` and `'9.0'` don't (different types/hashes).
- `{}` is a dict literal, not an empty set — always use `set()` to create an empty set.
- Sets support full set-algebra operations (`union`, `intersection`, `difference`, `symmetric_difference`) plus relationship checks (`issubset`, `issuperset`, `isdisjoint`) — useful for comparing collections without writing manual loops.
