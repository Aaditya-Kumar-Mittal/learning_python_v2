# C1.1 — Practice Questions

Based on the concepts in [notes.md](notes.md) (variables & types, operators, type conversion, user input).
Try to solve each without running the code first, then verify in Python.

---

## Section A — Variables & Types (Warm-up)

**A1.** What will `type()` return for each of these? Predict before checking.
```python
x = 7
y = 7.0
z = "7"
w = 7 == 7.0
v = None
```

**A2.** What is the difference (if any) between these four assignments? Do they all produce the same type?
```python
s1 = "hello"
s2 = 'hello'
s3 = """hello"""
s4 = '''hello'''
```

**A3.** Write a program that stores your name, age, and height (as a float) in variables, then prints all three in a single f-string sentence.

---

## Section B — Operators (Predict the Output)

**B1.** Without running it, predict the output of each line:
```python
a = 17
b = 4
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**B2.** What does `~10` evaluate to? Explain why using the formula `~a = -(a + 1)`.

**B3.** Predict the final value and type of `c` after running this sequence:
```python
c = 20
c += 10
c -= 5
c *= 2
c /= 5
c //= 2
```

**B4.** What is the output of `5 > 3 and 2 > 4`? What about `5 > 3 or 2 > 4`? What about `not(5 > 3)`?

**B5.** Explain, in your own words, what `a << 2` and `a >> 2` do to the integer `a`. What is `8 << 2`? What is `8 >> 2`?

---

## Section C — Type Conversion

**C1.** What happens (result and type) when you run each of these? Which ones raise an error?
```python
print("5" + "5")
print(int("5") + 5)
print("5" + 5)
print(float("5") + 5)
```

**C2.** Predict the type of `result` in this implicit-conversion example, and explain *why* Python chose that type:
```python
result = 10 + 3.5
```

**C3.** Convert the string `"3.14"` to a float, then to an int. What value do you get after the int conversion, and why?

**C4.** `bool()` can convert other types too. Predict the output of:
```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))
```

---

## Section D — Working with `input()`

**D1.** Write a program that asks the user for two numbers (as strings via `input()`), converts them to `int`, and prints their sum, difference, and product.

**D2.** The following code crashes if the user types a non-numeric age. Rewrite it using `.isdigit()` (like [p4.py](p4.py)) to avoid the crash, and print a friendly error message instead.
```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

**D3.** Write a program that asks the user for a number and prints whether it is even or odd, using the modulus operator `%`.

**D4.** Write a "mini calculator": ask the user for two numbers and an operator (`+`, `-`, `*`, `/`) as input, then print the result of applying that operator. (Hint: use `if`/`elif` to check which operator was entered.)

---

## Section E — Mixed / Challenge

**E1.** A user enters their birth year as a string via `input()`. Write code that computes and prints their age in the current year (use a fixed current year like `2026` for simplicity).

**E2.** Given `principal = 1000`, `rate = 5` (percent), and `time = 3` (years), calculate simple interest using the formula `SI = (principal * rate * time) / 100`. Print the result with an f-string, formatted to 2 decimal places (hint: `f"{value:.2f}"`).

**E3.** Ask the user to enter a temperature in Celsius (as input) and convert it to Fahrenheit using `F = C * 9/5 + 32`. Validate that the input can be converted to a float before doing the math — if it can't, print an error instead of crashing.

**E4.** Without running Python, work out by hand what `7 & 3`, `7 | 3`, and `7 ^ 3` evaluate to (write out the binary first). Then verify your answer by running the code.

---

### Answer key note
Try every question yourself first. If you want, ask me to check your answers or walk through any question step by step.
