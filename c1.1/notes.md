# C1.1 — Python Basics: Notes

Summary of concepts covered by [p1.py](p1.py), [p2.py](p2.py), [p3.py](p3.py), and [p4.py](p4.py).

## 1. Variables, Types & Literals ([p1.py](p1.py))

- Variables are created by assignment — no explicit type declaration needed (dynamic typing).
- `print()` accepts multiple comma-separated arguments and joins them with a space.
- f-strings (`f"..."`) let you embed expressions directly inside string literals: `f"{name}"`.
- `type(x)` returns the runtime type of `x`.
- Python has **four** ways to write string literals, all equivalent to `str`:
  - `"double quotes"`
  - `'single quotes'`
  - `"""triple double quotes"""` (also used for multi-line strings/docstrings)
  - `'''triple single quotes'''`
- Special singleton/boolean values:
  - `None` → type `NoneType` (absence of a value)
  - `True` / `False` → type `bool`

## 2. Operators ([p2.py](p2.py))

| Category | Operators | Notes |
|---|---|---|
| Arithmetic | `+ - * / // % **` | `/` always returns `float`; `//` is floor division; `%` is remainder |
| Comparison | `== != > < >= <=` | Return `bool` |
| Logical | `and or not` | Short-circuit evaluation |
| Bitwise | `& \| ^ ~` | Operate on integer bit patterns; `~a` = `-a - 1` |
| Shift | `<< >>` | Multiply/divide by powers of 2 |
| Assignment (compound) | `+= -= *= /= //= %=` | Shorthand for `x = x <op> y` |

**Gotchas worth remembering:**
- `/` (true division) always yields a `float`, even `10 / 5 == 2.0`.
- Once you use `/=` or `//=` on an int, the variable can become a `float` (e.g. `c //= 2` after a prior `/=` gives `3.0`, not `3`).
- `~a` is bitwise NOT: computed as `-(a + 1)`.

## 3. Type Conversion ([p3.py](p3.py))

- **Implicit conversion** (coercion): Python automatically widens a "smaller" type to a "larger" one in mixed-type expressions — e.g. `int + float → float`.
- **Explicit conversion** (casting): the programmer converts manually with built-ins:
  - `int(x)`, `float(x)`, `str(x)`, `bool(x)`, etc.
  - Needed when combining incompatible types, e.g. a numeric `str` with a number: `float("20") + 30`.

## 4. Reading User Input ([p4.py](p4.py))

- `input(prompt)` always returns a **string**, regardless of what the user types.
- To use input as a number, cast it explicitly: `int(input(...))` or `float(input(...))`.
- `str.isdigit()` is a safe way to check whether a string contains only digits before converting it with `int()` — avoids a `ValueError` crash on non-numeric input.
- String concatenation with `+` requires all operands to be strings — non-strings must be cast with `str()` first (e.g. `"You are " + str(age) + " years old."`).
- Casting straight from `input()` (`int(input(...))`) is concise but will crash with `ValueError` if the user enters non-numeric text — no validation happens.

## Key Takeaways

- Python is dynamically typed; use `type()` to inspect a variable's runtime type at any point.
- Division (`/`) always produces a float; use `//` when you need an integer/whole-number result.
- `input()` output is always `str` — validate (`isdigit()`) or `try/except` before casting to avoid crashes.
- Prefer f-strings over `+` concatenation when mixing types — no manual `str()` calls needed.