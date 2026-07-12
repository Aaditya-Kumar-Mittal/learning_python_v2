# C1.2 — Strings in Python: Notes

Summary of concepts covered by [p5.py](p5.py), [p6.py](p6.py), [p7.py](p7.py), [p8.py](p8.py), and [p9.py](p9.py).

## 1. String Basics & Escape Sequences ([p5.py](p5.py))

- Strings are concatenated with `+`; joining two strings does **not** add a space automatically — add `" "` explicitly if needed.
- Escape sequences let you embed special characters inside string literals:
  - `\n` — newline
  - `\t` — tab
  - `\b` — backspace (deletes the character before it when printed to a terminal)
- `len(str)` returns the number of characters in a string, as an `int`.
- `type(x)` still works on the result of `len()` to confirm it's an `int`.

## 2. Indexing & Slicing ([p6.py](p6.py))

- Strings are indexable sequences; `name[i]` gives the character at position `i` (0-based).
- `range(len(name))` combined with a `for` loop lets you iterate over every index in a string.
- **Slicing** syntax: `name[start:stop]` — extracts characters from `start` up to (not including) `stop`.
  - `name[:7]` — omit `start` to slice from the beginning.
  - `name[14:]` — omit `stop` to slice to the end.
  - `name[-6:]` — negative indices count from the end of the string (`-1` is the last character).
  - `name[:-13]` — mix positive/negative and omitted bounds freely.
- Slicing never raises an error for out-of-range indices — it just clips to the available characters.

## 3. Built-in String Methods ([p7.py](p7.py))

| Method | Purpose |
|---|---|
| `.upper()` / `.lower()` | Convert entire string to upper/lower case |
| `.capitalize()` | Capitalize only the first character of the string |
| `.title()` | Capitalize the first character of **every** word |
| `.swapcase()` | Invert the case of every character |
| `.startswith(x)` / `.endswith(x)` | Return `bool` — whether string starts/ends with `x` |
| `.replace(old, new)` | Return a copy with all occurrences of `old` replaced by `new` |
| `.find(x)` | Return the lowest index of `x`, or `-1` if not found (does **not** raise an error) |
| `.count(x)` | Return the number of non-overlapping occurrences of `x` |

- All these methods return a **new** string/value — strings are immutable, so the original is never modified in place.

## 4. Combining `input()` with String Membership ([p8.py](p8.py))

- The `in` operator checks substring/character membership: `char in someString` returns `bool`.
- Practical pattern: take user input, check membership with `in`, then use `.count()` to report how many times it occurs.
- Useful for building simple interactive validators or search utilities.

## 5. Iterating a List with `if`/`elif`/`else` ([p9.py](p9.py))

- Not string-specific, but a good example of using a `for` loop over a `list` combined with `if/elif/else` branching to map values (traffic light colors) to actions.
- `elif` chains are evaluated top-to-bottom; the first matching condition wins, and `else` is the fallback for anything unhandled.

## Key Takeaways

- Strings support both **indexing** (`str[i]`) and **slicing** (`str[start:stop]`), and slicing is forgiving of out-of-range bounds.
- Negative indices/slices count from the end of the string — handy for grabbing suffixes without knowing the exact length.
- String methods (`.upper()`, `.find()`, `.count()`, etc.) always return new values; strings themselves are immutable.
- `.find()` returns `-1` on failure instead of raising, while the `in` operator gives a quick boolean membership check — pick whichever fits the situation.