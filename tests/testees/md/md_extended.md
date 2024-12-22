# Lorem ipsum

## Text Style

Strikethru: ~~The world is flat.~~ The world is round.

Highlight: Despite many reverses, ==freedom has won battles.==

### supercript & subscript

Lorem ~x~ dolor ^x^

amet ~12~ consectetur ^0^

adipiscing ~elit~ Nullam ^scelerisque^

This happened in 19 ^th^ C.

### Fenced Code Block

```
consectetur adipiscing elit
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam
```

Python language:

```python
def calculate_factorial(n):
    """
    compute the factorial of a given number

    :param n: the number to compute the factorial of
    :type n: int
    :return: factorial of param `n`
    :retype: int
    :raises ValueError: if `n` is negative
    """
    if n < 0:
        raise ValueError("negative value is not supported")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
```

C++ code:

```cpp
#include <iostream>
using namespace std;

// function to calculate the factorial of a number
int factorial(int n) {
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

int main() {
    int number;
    cout << "Enter a positive integer: ";
    cin >> number; // input a positive integer

    if (number < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
    } else {
        cout << "Factorial of " << number << " is " << factorial(number) << endl;
    }
    return 0;
}
```

JavaScript code:

```js
/**
 * Calculates the factorial of a given number
 * @param {Number} n - The number to calculate the factorial for
 * @returns {Number} The factorial of the provided number
 * @throws {Error} If the number is negative
 */
function factorial(n) {
    if (n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
    }
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Example usage
try {
    const num = 5; // replace with any positive integer
    console.log(`Factorial of ${num} is ${factorial(num)}`);
} catch (error) {
    console.error(error.message);
}
```

### Color Code

- `#FFCC00`
- `rgb(9, 105, 218)`
- `hsl(212, 92%, 45%)`

## Structures

### Table

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

### Task List

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

### List contains Footnote

- Lorem ipsum dolor
- Sed do eiusmod [^footnote-in-list]
- Ut enim veniam

## Technicals {#tech}

### Section Heading {#sec}

Section link to Chapter 2 [II](#technicals)

Q.v. [II.2.1](#section-heading)

### Footnote

Lorem ipsum [^1] dolor sit amet, [^2] consectetur [^third] [^fourth] Vivamus lacinia [^fourth] odio vitae vestibulum.

### Comment

Before Comment

<!-- Some Comment -->

After Comment

### Alert

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

<!-- Footnotes -->

[^footnote-in-list]: Some content of footnote in list

[^1]: *Social History of Alcohol Research* (older volumes) Social History of Alcohol & Drugs (newer volumes), Journal of the Alcohol & Temperance History Group.

[^2]: Contains **Bold** in Footnote

[^third]: Contains *Italics* in Footnote

[^fourth]: Contains `foo` in Footnote

