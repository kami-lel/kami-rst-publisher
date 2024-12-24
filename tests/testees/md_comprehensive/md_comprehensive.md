# Lorem ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Nulla eu nulla quis ligula sollicitudin feugiat.
Vestibulum pulvinar, mauris sed commodo blandit,
sem ligula lacinia risus,
a faucibus sem magna quis libero.

Tristique eget urna in, posuere tristique tellus. Donec ante dolor, laoreet laoreet leo a, consequat tincidunt mauris.

----

Line break (not paragraph break)

Lorem ipsum dolor sit amet,  consectetur adipiscing elit

Sed do eiusmod tempor  
incididunt ut labore et  
dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## Text Style

### Bold

Lorem **ipsum** dolor sit **amet consectetur adipiscing** elit.

**Nulla eu nulla quis ligula sollicitudin feugiat.**

### Italics

Lorem *ipsum* dolor sit *amet consectetur adipiscing* elit.

*Nulla eu nulla quis ligula sollicitudin feugiat.*

Bold & Italics: Lorem ***ipsum*** dolor

### by html tags

Underline: <ins>text</ins>

#### supercript & subscript

Lorem <sub>x</sub> dolor <sup>x</sup>

amet <sub>12</sub> consectetur <sup>0</sup>

adipiscing <sub>elit</sub> Nullam <sup>scelerisque</sup>

This happened in 19 <sup>th</sup> C.


## Heading Tests

### **Bold** in Heading

#### `Code` in Heading

##### *Italics* in Heading

###### Lowest Heading

## Structures

### List

#### unordered list

Bullet point list short:

- Lorem ipsum dolor
- Sed do eiusmod
- Ut enim veniam
- Duis aute irure
- Excepteur sint occaecat

Bullet point list long:

- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
- Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
- Lorem ipsum dolor

#### ordered list

Arabic number:

1. Quisque porttitor ex turpis
2. vitae ullamcorper est fermentum eget
3. cras rutrum elit sit amet commodo blandit

Arabic number with wrong numbering in raw:

1. Quisque porttitor ex turpis
3. vitae ullamcorper est fermentum eget
5. cras rutrum elit sit amet commodo blandit

#### nested list

- Lorem ipsum dolor
- Sed do eiusmod

    - Ut enim veniam
    - Duis aute irure

- Excepteur sint occaecat

----

1. Quisque porttitor ex turpis
2. vitae ullamcorper est fermentum eget.

    1. a item
    2. b item
    3. c item

3. cras rutrum

----


1. Quisque porttitor ex turpis
2. vitae ullamcorper est fermentum eget.

    - a item
    - b item
    - c item

3. cras rutrum elit sit

----

- Quisque porttitor ex turpis
- vitae ullamcorper est fermentum eget.

    1. a item
    2. b item
    3. c item

- cras rutrum elit sit amet commodo blandit
- cras rutrum elit sit amet commodo blandit. nulla tincidunt dui neque

    - test

        - test

            1. test1
            2. test1
            3. test1

- cras rutrum elit sit amet commodo

#### elements in list

- Lorem ipsum **dolor** sit amet, *consectetur* `adipiscing` elit.
- Sed do eiusmod **tempor incididunt ut labore et** dolore magna aliqua.
- Ut enim ad minim veniam, *quis nostrud exercitation* ullamco laboris nisi ut aliquip
- `ex ea commodo consequat duis aute irure dolor in reprehenderit in` voluptate velit esse

### Horizontal Rules
Text Body Quisque gravida tempor mauris eget fermentum. Nullam scelerisque lobortis mauris sed laoreet. Sed eleifend, lacus nec elementum condimentum, magna lectus mattis nulla, sed porttitor quam orci sit amet arcu. Maecenas nec dolor nunc.

----

Proin et quam nulla. Vivamus maximus a felis a interdum. Curabitur sit amet condimentum tortor, vitae mollis tortor. Nam porta tempus tempor. Sed velit orci, tempus vel venenatis a, maximus ut tellus. Aenean eget tincidunt eros. Cras nec semper magna, vel facilisis erat. Donec eget massa varius, vehicula erat vitae, varius odio. Donec in hendrerit sem.

## Code

Lorem ipsum `dolor` sit amet

A pair: Lorem ipsum ``dolor`` sit amet

Block literal

    consectetur adipiscing elit
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam

Code:

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

## Blockquote

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam

>quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
>
>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Curabitur pretium tincidunt lacus.
>
>Nulla gravida orci a odio

Et vulputate enim erat vestibulum.

## Technicals

### Link

[DuckDuckGo](https://duckduckgo.com)

[DuckDuckGo](https://duckduckgo.com "The Private Search Engine")

<https://www.duckduckgo.comd>

<fake@example.com>

### HTML tags

Center text:

<center>Duis aute irure dolor in reprehenderit in voluptate</center>

Change Color to *Red*:

<font color="red">Sed ut perspiciatis unde omnis iste natus error</font>

<strong>Bold</strong> by `<strong>`

Make <small>Text Small</small>

