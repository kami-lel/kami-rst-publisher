===========
Lorem ipsum
===========

.. default-role:: smart

.. subtitle:: Nullam condimentum

.. contents:: Table of Contents

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Nulla eu nulla quis ligula sollicitudin feugiat.
Vestibulum pulvinar, mauris sed commodo blandit,
sem ligula lacinia risus,
a faucibus sem magna quis libero.

Tristique eget urna in, posuere tristique tellus. Donec ante dolor, laoreet laoreet leo a, consequat tincidunt mauris.


Text Style
##########

.. rubric:: Bold

Lorem **ipsum** dolor sit **amet consectetur adipiscing** elit.

**Nulla eu nulla quis ligula sollicitudin feugiat.**

.. rubric:: Italics

Lorem *ipsum* dolor sit *amet consectetur adipiscing* elit.

*Nulla eu nulla quis ligula sollicitudin feugiat.*

.. rubric:: superscript & subscript

Lorem :sub:`x` dolor :sup:`x`

amet :sub:`12` consectetur :sup:`0`

adipiscing :sub:`elit` Nullam :sup:`scelerisque`

This happened in 19 :sup:`th` C.

----

**This is Bold** and *This is Italics* and :sub:`subscript` and :sup:`superscript`

.. rubric:: math

:math:`f(x)=ax^2+bx+c`

The equation for the quadratic formula is given by :math:`x = \frac{{-b \pm \sqrt{{b^2 - 4ac}}}}{{2a}}`, where :math:`a`, :math:`b`, and :math:`c` are coefficients of the quadratic equation.

:math:`V = \int_0^{2\pi} d\theta \int_0^{1} r \sqrt{1 - r^2} dr`

.. _II:

`II` **Bold** in Heading
########################
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

`II.2` ``Code`` in Heading
==========================
Nulla eu nulla quis ligula sollicitudin feugiat.  Vestibulum pulvinar, mauris sed commodo blandit, sem ligula lacinia risus, a faucibus sem magna quis libero.

.. _`II.2.1`:

`II.2.1` *Italics* in Heaindg
-----------------------------
Etiam mauris lectus

`II.2.1.4` Superscript, 12 :sup:`th` Century
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tristique eget urna in, posuere tristique tellus. Donec ante dolor, laoreet laoreet leo a, consequat tincidunt mauris.

`II.2.1.4.5` Heading 5
^^^^^^^^^^^^^^^^^^^^^^
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

`II.2.2` Supscript, H\ :sub:`2`\ O
----------------------------------
Etiam mauris lectus

List
====

.. rubric:: unordered list

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

.. rubric:: ordered list

Arabic number:

1. Quisque porttitor ex turpis
2. vitae ullamcorper est fermentum eget
3. cras rutrum elit sit amet commodo blandit

Arabic number with auto:

1. Quisque porttitor ex turpis
#. vitae ullamcorper est fermentum eget
#. cras rutrum elit sit amet commodo blandit

Roman numeral:

(i) Quisque porttitor ex turpis
(ii) vitae ullamcorper est fermentum eget.
(iii) Cras rutrum elit sit amet commodo blandit. Nulla tincidunt dui neque, sit amet congue magna mollis quis. Vivamus velit nunc, volutpat et risus et, dictum tempus elit. Quisque venenatis neque lobortis turpis ullamcorper posuere.

Letter:

(a) Lorem ipsum dolor sit amet, consectetur adipiscing elit.
(b) Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
(c) Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

.. rubric:: nested list

- Lorem ipsum dolor
- Sed do eiusmod

  - Ut enim veniam
  - Duis aute irure

- Excepteur sint occaecat

----

1. Quisque porttitor ex turpis
2. vitae ullamcorper est fermentum eget.

   (a) a item
   (b) b item
   (c) c item

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
  #. b item
  #. c item

- cras rutrum elit sit amet commodo blandit

  (a) a item
  (b) b item
  (c) c item

- cras rutrum elit sit amet commodo blandit. nulla tincidunt dui neque

  - test

    - test

      1. test1
      #. test1
      #. test1

- cras rutrum elit sit amet commodo

.. rubric:: elements in list

- Lorem ipsum **dolor** sit amet, *consectetur* ``adipiscing`` elit.
- Sed do eiusmod **tempor incididunt ut labore et** dolore magna aliqua.
- Ut enim ad minim veniam, *quis nostrud exercitation* ullamco laboris nisi ut aliquip
- ``ex ea commodo consequat duis aute irure dolor in reprehenderit in`` voluptate velit esse
- cillum :sub:`dolore` eu fugiat :sup:`nulla` pariatur
- Excepteur sint occaecat cupidatat [#in-list]_ non proident

Table
=====

.. rubric:: simple table

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
=====  =====  ======

Another table:

=====  =====
col 1  col 2
=====  =====
1      Second column of row 1.
2      - Second column of row 2.
       - Second item in bullet
         list
\      Row 3; column 1 will be empty.
=====  =====

.. rubric:: grid table

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+

.. rubric:: element in table

=====  =====
col 1  col 2
=====  =====
1      ``Second`` column of row 1.
2      Second **column** of row 2. *Second item in bullet* list
\      Row 3 column 1 will be empty. [#in-table]_
=====  =====

Transition
==========
Text Body Quisque gravida tempor mauris eget fermentum. Nullam scelerisque lobortis mauris sed laoreet. Sed eleifend, lacus nec elementum condimentum, magna lectus mattis nulla, sed porttitor quam orci sit amet arcu. Maecenas nec dolor nunc.

----

Proin et quam nulla. Vivamus maximus a felis a interdum. Curabitur sit amet condimentum tortor, vitae mollis tortor. Nam porta tempus tempor. Sed velit orci, tempus vel venenatis a, maximus ut tellus. Aenean eget tincidunt eros. Cras nec semper magna, vel facilisis erat. Donec eget massa varius, vehicula erat vitae, varius odio. Donec in hendrerit sem.

Literal & Quotations
####################
Literals
========
Lorem ipsum ``dolor`` sit amet

::

    consectetur adipiscing elit
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam

Code::

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

block quote
===========
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam

    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Curabitur pretium tincidunt lacus.

    Nulla gravida orci a odio

Et vulputate enim erat vestibulum.

epigraph
========

.. epigraph::

    "Ignorance, the root and stem of every evil."

    -- Plato

line block
==========

| Lend us a couple of bob till Thursday.
| I'm absolutely skint.
| But I'm expecting a postal order and I can pay you back
  as soon as it comes.
| Love, Ewan

Technicals
##########
Footnote
========
Lorem ipsum [*]_ dolor sit amet, [*]_ consectetur [*]_ adipiscing elit. [*]_ Vivamus lacinia [*]_ odio vitae vestibulum.

Sed tristique [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_ [*]_

.. [*] Phasellus orci lectus

.. [*] lacinia ut neque in, dignissim malesuada lacus

.. [*] *Social History of Alcohol Research* (older volumes) Social History of Alcohol & Drugs (newer volumes), Journal of the Alcohol & Temperance History Group.

.. [*] Contains **Bold** in Footnote

.. [*] Contains *Italics* in Footnote

.. [*] Contains ``foo`` in Footnote

.. [*] Contains math formula :math:`f(x)=ax^2+bx+c` in Footnote

.. [*] Superscript & Subscript in notes: adipiscing :sub:`elit` Nullam :sup:`scelerisque`

.. [*] The 9th note

.. [*] The 10th note

.. [*] The 11th note

.. [*] The 12th note

.. [*] The 13th note

.. [*] The 14th note

.. [*] The 15th note

.. [*] The 16th note

.. [*] The 17th note

.. [*] The 18th note

.. [*] The 19th note

.. [*] The 20th note

Lorem ipsum [#]_ dolor sit amet, [#]_ consectetur [#third]_ [#fourth]_ Vivamus lacinia [#fourth]_ odio vitae vestibulum.

Comment
=======

Before Comment

.. Some Comment Content

After Comment

Section Link
============

Section link to Chapter 2 `II`_

Q.v. `II.2.1`_

Directives & Sidebar
####################

.. sidebar:: sidebar heading (ad lib)

    content 1st line
    content 1st line continue

    content 2nd line


.. admonition:: title of admonition

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Vivamus lacinia odio vitae vestibulum. Sed tristique libero ac sapien facilisis, non interdum risus viverra.
    Ut venenatis lorem at metus fermentum, nec tincidunt nisi auctor.

.. attention::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. caution::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. danger::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. error::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. hint::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. important::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. note::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. tip::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. warning::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. Footnotes

.. [#] The 1st Footnote

.. [#] The 1st Footnote

.. [#third] The 3rd Footnote

.. [#fourth] The 4th Footnote

.. [#in-list] Footnote in List

.. [#in-table] Footnote in Table

