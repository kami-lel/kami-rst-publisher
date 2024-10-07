=========================
kami-rst-publisher README
=========================

.. default-role:: smart

.. contents::

``kami-rst-publisher`` is a personalized tool based on ``docutils`` and *reStructuredText*.

This README have four parts:

1. **usage** § `I`_: how to use kami-rst-publisher

#. **rST** part § `II`_, `III`_,  & `IV`_: i.e. reStructuredText. This part is a study note of *rST* standard. It will also define *preference* in expression varieties

#. **native** part § `V`_ & § `VI`_: *roles* and *directives* implemented by ``kami-rst-publisher``

#. **style guide** § `VII`_: the less-technical specifications of documentation

Docutils Project Documentation [#docutil]_ (abbr. *docutil*) and Python Developler's Guide [#python]_ (abbr. *doc python*) are heavily referenced.
































.. _I:

`I` usage
#########
Use ``kami-rst-publisher`` as Python package or by a CLI, v.i.













`1` Python package
==================
Use ``kami-rst-publisher`` as Python code::

    from docutils.core import publish_file
    from kami-rst-publisher import init_publisher

    init_publisher()

    publish_file(...)













`2` API
=======
An API (defined in ``./kami_rst_publisher/rst2html_file.py``) can be used for publish raw rST plain text into html 5 file(s).

One can use in Python::

    from kami_rst_publisher import init_publisher
    from kami_rst_publisher import Rst2htmlFile, Rst2htmlFileBatch, Rst2htmlFileRecursive

    init_publisher()

    Rst2htmlFile(src, dest)

Check *docstring* for each classes.












`3` Python CLI
==============
One could use a CLI defined in ``./kami_rst_publisher/cli.py``

Run with python::

    python3 -m kami_rst_publisher.cli ...

And its *help* file::

    usage: (kami rST publisher)publisher-cli.py [-h] [-b] [-r] [-c [WAIT]] [-l] [-v] [-s [SUFFIX]] [-f FILTER]
                                                SOURCE [DESTINATION]

    personalized rST publisher based on docutils but with extra roles & directives

    positional arguments:
      SOURCE                SOURCE of rST text, file or directory path
      DESTINATION           DESTINATION of rendered .html file(s), file or directory path. Rendered file will be saved
                            alongside with SOURCE if not given

    options:
      -h, --help            show this help message and exit
      -b, --batch           render any file with name fullmatching (regex) FILTER in a directory SOURCE. SOURCE &
                            DESTINATION should be directory path. FILTER default to ".+\.rst", but can be set by -f
      -r, --recursive       like -b, but recursively into each sub-folder of SOURCE. This flag overwrites -b. DESTINATION
                            is not used when -r
      -c [WAIT], --continuous [WAIT]
                            render all changed files once every WAIT seconds. WAIT default to 5.0.
      -l, --light           render in light mode
      -v, --verbose
      -s [SUFFIX], --suffix [SUFFIX]
                            SUFFIX for rendered file. Default to ".R"
      -f FILTER, --filter FILTER
                            with -b or -r, set FILTER for file matching. Default to ".+\.rst"












`4` stylesheets
===============
There are two render styles:

- light mode: apply stylesheet ``responsive.css`` & ``kami_html5.css``
- dark mode: apply stylesheet ``responsive.css``, ``kami_html5.css``, & ``kami_html5_dark.css``

These stylesheets will utilize these typefaces for desired looking;

- ``Literata 12pt``
- ``Atkinson Hyperlegible``
- ``Raleway``
- ``Cormorant Garamond Medium``
- ``Fira Code Kami``
- ``Playfair Display``
































.. _II:

`II` rST
########
`1` paragraph
=============
**Paragraph** is the basic element for text. Paragraphs consist of blocks of left-aligned text with no markup indicating any other body element.

Blank lines are used to separate paragraphs from each other and from other elements. Multiple blank lines are functionally equivalent to single blank line.

::

    a single line paragraph

    second paragraph
    with multiple lines



    Another paragraph with multiple blank lines before it

※ *doc python*, “The maximum line length is 80 characters for normal text”. However ``kami-rst-publisher`` prefers **not** to follow such convention. I.e. one should put text of the same paragraph formatted in a single line. 













`2` indentation
===============
Space character is used for indentation rather than tabs. It is used to provoke certain functions of rST such as lists, block quotes, etc. ``kami-rst-publisher`` uses **4 spaces** for indentation.

This is an example of list, which requires indentation to provoke::

    - first item

      - sub-level item in first iem

    - second item

Several elements (e.g. lists, footnotes, etc.) require both a marker and indentation, therefore intentation might varies (※ *docutil*.) E.g.::

    - a bullet list's second line
      start aligned with text

          and additional indentation within should be additional 4 spaces, therefore 2+4=6 in total

    .. [1] and elements such as footnote's second line
       aligned left with the bracket (i.e. 3 spaces)

As shown in these examples, number of spaces used for indentation might not be multiple of 4.

※ *doc python*, “All reST files use an indentation of 3 spaces”, but ``kami-rst-publisher`` prefers to use 4 spaces as the default.

※ *docutil*, tab, form feeds, and vertical tabs would be automatically converted, but ``kami-rst-publisher`` prefers to not use these functions. I.e. only space character shall be used.













`3` text style
==============
`3.1` italics
-------------
*Italics* is for texts that should be understood literally. It is also used for book, movie, magazine titles etc.

*example text in italics*

※ *docutil*, a interpreted text role ``:title-reference:`` is used for titles of materials. But ``kami-rst-publisher`` simpliy use italics for such function.





`3.2` bold
----------
**Bold** is for emphasizing the meaning of the text.

**example text in bold**





`3.3` subscript & superscript
-----------------------------
Subscript and superscript are possible by::

    normal text :subscript:`subscript text` :superscript:'superscript text' 

    or as normal :sub:`subs` :sup:`sups`

rendered as:

    normal text :subscript:`subscript text` :superscript:`superscript text`

    or as normal :sub:`subs` :sup:`sups`





`3.4` math
----------
Express mathematical notation in *LaTeX math syntax* without math delimiters ``$ $``.

E.g.::

    :math:`f(x)=ax^2+bx+c`

Rendered as:

    :math:`f(x)=ax^2+bx+c`












`4` heading
===========
`4.1` title
-----------
The title of the entire document should be formatted as::

    ==========
    Main Title
    ==========





`4.2` section heading
---------------------
Six levels of section headings are available in ``kami-rst-publisher``::

    primary heading
    ###############
    content could be placed after heading w/o any blank line

    secondary heading
    =================

    tertiary heading
    ----------------

    quaternary heading
    ~~~~~~~~~~~~~~~~~~

    quinary heading
    ***************

    senary heading
    ^^^^^^^^^^^^^^

There does not exist an universal standard for order of symbols among rST realizations. ``kami-rst-publisher`` has decide to use the symbol order shown above for section headings. (The order of symbols used by ``kami-rst-publisher`` is different with *docutil*.) Likely, there does not exist any standard on whether a overline is required. ``kami-rst-publisher`` require overline for title, but prohibit overline usage for headings.

Optionally, blank lines might be added before headings if the document is relative long. Number of lines are defined in § `I.4.4`_. This provide a visual clearity of the document structure.

※ *docutil*, “A blank line after a title is optional.” ``kami-rst-publisher`` prefers to not having blank line after the heading. 



.. _I.4.3:

`4.3` section heading reference
-------------------------------
In rST, section headings themselves are already *anonymous hyperlink targets*, but it is a good practice to make *named hyperlink target* (※ § `I.11.2.1`_) e.g.::

    .. _I:

    `I` primary heading
    ###################

    .. _I.1:

    secondary heading
    =================

    .. _I.1.1:

    tertiary heading
    ----------------

And these can be referenced by::

    please see `I`_, `I.1`_, and `I.1.1`_

This is only required if the section is referenced in the document. Do not create unnessary hyperlink target if the section is never referenced in the document.

These explicit hyperlink target should be considered *blank lines* regarding blank lines before headings.



.. _I.4.4:

`4.4` blank lines before heading
--------------------------------
=========== ======= ======= =====
heading     symbol  medium  long
=========== ======= ======= =====
primary     ###     13      34
secondary   ===     5       13
tertiary    ---     3       5
quaternary  ~~~     2       3
quinary     \***    1       2
senary      ^^^     1       1
=========== ======= ======= =====

One should pick the *medium* or *long* sequence to use regarding the textual length of the document.

*Rubric* should be considered as a level in the heading, the number of blank lines before a rubric should be: that of same level heading minus 1.

These numbers are selected from the Fibonacci sequence: **1**, **1**, **2**, **3**, **5**, 8, **13**, 21, **34**, ~













`5` list
========
`5.1` bullet list
-----------------
The syntax of the bullet list is::

    this is a bullet list:

    - 1st item (after a blank line)
    - 2nd item

      - sub item (after a blank line)
    - 3rd item (blank line not required)
    
    continuing paragraph

In ``kami-rst-publisher``, it is preferable to use ``-`` for all levels of nested list.

※ *docutil*, blank line before first item is required. Blank line between items (between ``1st item`` and ``2nd item``.) Blank line for return to last level list (between ``sub item`` and ``3rd item``) are optional, they are also optional in ``kami-rst-publisher``.





`5.2` enumerated list
---------------------
There are two sets of preferred syntax of enumerated list by ``kami-rst-publisher``. By using Arabic numerals::

    preceding paragraph

    1. first item
    2. second item
    3. third item

    continuing paragraph

Or by using lower-case Roman numerals::

    preceding paragraph

    (i) first item
    (ii) second item
    (iii) third item

    continuing paragraph

Or by using lower-case letters::

    preceding paragraph

    (a) first item
    (b) second item
    (c) third item

    continuing paragraph

Auto-enumerator can be evoked to automatically generate next entry::

    2. second item
    #. third item
    #. fourth item

And **nested** enumerated list is also possible::

    1. first item
    2. second item

        (a) a item
        (b) b item
        (c) c item
      
    3. third item













`6` table
=========
A table might be drawn as a simple table::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    =====  =====  ======

    =====  =====
    col 1  col 2
    =====  =====
    1      Second column of row 1.
    2      - Second column of row 2.
           - Second item in bullet
             list
    \      Row 3; column 1 will be empty.
    =====  =====

rendered as:

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    =====  =====  ======

    =====  =====
    col 1  col 2
    =====  =====
    1      Second column of row 1.
    2      - Second column of row 2.
           - Second item in bullet
             list
    \      Row 3; column 1 will be empty.
    =====  =====

Or grid tables::

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

rendered as

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














.. _I.7.1:

`7` footnote
============
`7.1` numerical footnote
------------------------
Numerical footnote is consistent through the entire document.
::

    There are 300 of them [1]_ , but none of them is male [2]_. Thirdly [#]_. 

    Another research showed that. [#labelled_footnote]_

    continuing paragraph

    .. Footnote

    .. [1] footnote content 1

    .. [2] footnote content 2

    .. [#] footnote content 3

    .. [#labelled_footnote] footnote labelled

Labelled footnote is prefereable when the document is lengthy. Labelled footnote shall have a simple reference name (※ § `I.11.1.1`_,) and it is suggested to use `KS.Syb.MinUdr` to concatenate multiple words.

Despite footnote could be placed anywhere in the document, ``kami-rst-publisher`` prefers numerical footnote always placed at the end of the document, after main content. Placing a comment ``.. Footnote`` before the list of footnote contents::

    main content of document

    .. Footnote

    .. [1] footnote content 1

    .. [2] footnote content 2





`7.2` symbolic footnote
-----------------------
Symbolic footnote is used mostly as local footnote.
::

    First [*]_, second [*]_, and third [*]_

    .. [*] footnote content 1

    .. [*] footnote content 2

    .. [*] footnote content 3

    continuing paragraph

For symbolic footnote, it is suggested to put the footnote content as close to the footnote symbol as possible. Be careful each time use footnote, number of reference and targets (footnote content) should be matched.













`8` transition
==============
Transition is used to mark a subtle separation between paragraph or between paragraphs. Syntax of transition is 4 or more repeated ``-``. It is suggested to use 4 of them in most cases.

::

    first pargraph(s)

    ----
    
    second paragraph(s)

    ---------------

    third pargraph(s)

※ *docutil*, a transition should not begin or end a section or document, nor should two transitions be immediately adjacent.













`9` comment
===========
**Comment** is the invisible content after render.

::

    .. this is a comment

    ..
       this is also a comment












`10` escaping
=============
``\`` is used to override the special meaning of markup characters. E.g. 
::

    \*escape* vs. *escape*

    \``with`` vs. ``with``

    \\ vs. \

The previous code will be rendered as:

    \*escape* vs. *escape*

    \``with`` vs. ``with``

    \\ vs. \

``\`` is also used to place inline literals within a single word::

    **KS**\ *Mark*\ ``up``

Which will be rendred as:

    **KS**\ *LML*\ ``KS``













`11` hyperlink
==============
Despite used extensively in most rST realizations, ``kami-rst-publisher`` prefers to minimize the usage of hyperlink for **comprehensiblility** (※ § `VII.1`_). Heavily relying on hyperlink will result confusion when the document is viewed in forms (e.g. printed paper) those do not support hyperlink. Documents are suggested to explicitly write the reference in text, and using hyperlink only as gimmick and tool.

The function of hyperlink is used in ``kami-rst-publisher`` only in cases of:

- section heading reference (※ § `I.4.3`_)
- footnote (※ § `I.7.1`_)





`11.1` reference name
---------------------
*Reference name* is not an element, but rather a technical identification for cross-referencing elements.

“Reference names are whitespace-neutral and case-insensitive.”※*docutil*, which means:

- multiple whitespace characters(e.g. space, tab, newline, etc.) become single space character
- majuscule letter get converted to miniscule

.. _I.11.1.1:

`11.1.1` simple reference name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
“Simple reference names are single words consisting of alphanumerics plus isolated (no two adjacent) internal hyphens, underscores, periods, colons and plus signs; no whitespace or other characters are allowed.”※*docutil* In regex::
    
    [A-Za-z0-9-_.:+]*

(but no adjacent “-”, and case is not significant)


`11.1.2` phrase-reference
~~~~~~~~~~~~~~~~~~~~~~~~~
“Reference names using punctuation or whose names are phrases (two or more space-separated words) are called "phrase-references".” ※*docutil*
::

    Want to learn about `my favorite programming language`_?

    .. __: http://www.python.org





`11.2` hyperlink syntax
-----------------------
Hyperlink reference & target should not be used carelessly in ``kami-rst-publisher`` documents. There are only serveral special cases where hyperlinks are used. This section merely records the syntax of such functionality, therefore it can be used in those special cases.

.. _I.11.2.1:

`11.2.1` named hyperlink reference & target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    please see link1_ or see `this link`_ (phrase reference)

    .. _link1:
    .. _this link:

    para1 or other elements


`11.2.2` anonymous hyperlink reference & target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    please see this section__ or see `this section`__

    .. __: anonymous-hyperlink-target-link-block
    .. or alternative syntax
    __ anonymous-hyperlink-target-link-block    

“the first anonymous reference will link to the first anonymous target” and “it is recommended that targets be kept close to references.” ※*docutil*
































.. _III:

`III` rST directives
####################
[#rst_directives]_











.. _III.1:

`1` table of content
====================
::

    .. contents::

Or with alterantive title::

    .. contents:: Table of Content












`2` admonitions
===============
There are different types of admonitions:

- ``attention``
- ``caution``
- ``danger``
- ``error``
- ``hint``
- ``important``
- ``note``
- ``tip``
- ``warning``

E.g. for ``note``::

    .. note::

        content of note

Rendered as:

.. note::

    cotent of note

----

There are also a *generic* admonitions::

    .. admonition:: title of admonition

        content of it

Rendered as:

.. admonition:: title of admonition

    content of it













`3` rubric
==========
Rubric work as a heading yet it is not part of the document structure::

    .. rubric:: subtitle for this part

Rendered as:

.. rubric:: subtitle for this part













`4` sidebar
===========
::

    .. sidebar:: sidebar heading (ad lib)

        content 1st line
        content 1st line continue

        content 2nd line

Rendered as:

.. sidebar:: sidebar heading (ad lib)

    content 1st line
    content 1st line continue

    content 2nd line
































.. _IV:

`IV` literal & quotation
#########################
`1` inline literal
==================
``Literals`` is used for “code samples” (※ *doc python*), link, etc. It is a even-more-literal text style than italics, for its content should not be interpreted nor changed at all.

E.g. ::

    The function ``foo`` is defined as ...

Rendered as:

    The function ``foo`` is defined as ...

※ *docutil*, all white space character (including line breaks) is preserved in literal. Also, blank lines are required before and after a literal block.

A ``code`` role is available in some rST realizations, but using literal text style is preferable in ``kami-rst-publisher``.












`2` literal block
=================
It is similar to inline literals (v.s.):: 

    the example code is shown as following
    ::

        a blank line is required before the content

        1 + 1 = 2

    or with '::' placed at the end of the line::

        1 + 1 = 2

    continuing paragraph













`3` block quote
===============
::

    preceding paragraph

        "It is my business to **know** things.  That is my trade."

    continuing paragraph

※ *docutil*, All markup processing (for body elements and inline markup) continues within the block quote.













`4` epigraph
============
It is similar to block quote, but could attribute to author.::

    .. epigraph::

        "Ignorance, the root and stem of every evil."

        -- Plato

Rendered as:

.. epigraph::

    "Ignorance, the root and stem of every evil."

    -- Plato













`5` line block
==============
Line block will keep line structure of the quote, useful for poetry, lyrics, etc.

::

    | Lend us a couple of bob till Thursday.
    | I'm absolutely skint.
    | But I'm expecting a postal order and I can pay you back
      as soon as it comes.
    | Love, Ewan

Rendered as:

| Lend us a couple of bob till Thursday.
| I'm absolutely skint.
| But I'm expecting a postal order and I can pay you back
  as soon as it comes.
| Love, Ewan
































.. _V:

`V` native role
###############
`1` smart role
==============
The *smart role* could be used by::

    :smart:`smart content`

But it is often convenient to set the default role to it at the begining of each document::

    .. default-role:: smart

    `smart content`

It has various functions:

- KScode: start with ``KS.`` or the text is ``KS``, render as KScode
- KSproxy: start with ``.``, render as KSproxy
- number: v.i., render with number-specific typeface
- fallback: render like bold

The criteria of *number* is to start with:

- Arabic number 0~9,
- Roman numeral component: ``OIVXL``, or
- lower case of them

(For Roman numeral, the possible range for it is 0~89, i.e. `O` to `LXXXIX`)

----

E.g.::

    KScode e.g. `KS.abc.def`

    KSproxy e.g. `.abc.def`

    number e.g. `3`, `3.2`, `III`, `iv`

    fallback e.g. `abc`

render as:

    KScode e.g. `KS.abc.def`

    KSproxy e.g. `.abc.def`

    number e.g. `3`, `3.2`, `III`, `iv`

    fallback e.g. `abc`












`2` tag role
============
::

    :tag:`example_tag`

render as:

    :tag:`example_tag`
































.. _VI:

`VI` native directive
#####################
`1` tag directive
=================
The tag directive could be used by::

    .. tag:: example_tag

    .. tag:: example_proper{
        content_of_proper_tag
        }

    .. tag:: 
        example_proper{
            content_of_proper_tag
        }

Rendered as:

.. tag:: example_tag

.. tag:: example_proper{
        content_of_proper_tag
    }

.. tag:: 
    example_proper{
        content_of_proper_tag
    }











.. _VI.2:

`2` subtitle directive
======================
Give the subtitle of the article, e.g.::

    =====
    title
    =====

    .. subtitle:: The Subtitle

or multiple lines::

    .. subtitle:: The 1st Line Subtitle

        2nd Line
        3rd Line
































.. _VII:

`VII` style guide
#################

.. _VII.1:

`1` comprehensibility principle
===============================
Considering two **viewing** scenarios:

- preferable method of viewing content is in their *fancy form* after rendering
- in *raw form*, when one could both edit **and** view the content

Therefore, raw content should also be **comprehensible**. In order to achieve this, deisgn choices shall be made to maximize raw text readibility when they would not interfere the functionalities. Implict, murky, or complex structure and design logic should be avoided.













`2` document structure
======================
A common document structure:

1. title
#. subtitle (ad lib): by using *subtitle directive*, ※ § `VI.2`_
#. introduction (ad lib): one or more paragraphs introducing the rest of content
#. table of contents (ad lib): ※ § `III.1`_
#. content managed by headings
#. enclosure: signature, release date, location, etc.
#. appendix (ad lib)
#. bibliography (ad lib)
#. change (ad lib): a list of changes in this version of document
#. designatable (ad lib): a nested list of designatables declared in this document
#. footnote (ad lib): content of footnotes












`3` heading numbering
=====================
One could use `KS.Num.Rm.M` (Roman numeral in upper case) enclosed in *smart role* for *primary heading* numbering::

    `O` general
    ###########

    `I` first chapter
    #################

    `II` second chapter
    ###################

----

Use `KS.Num.Dec` separated by ``.`` for lower level heading numbering::

    `I` first chapter
    #################
    `1` section 1
    =============
    `1.1` low section 1
    -------------------

    `1.2` low section 2
    -------------------

    `1.3` low section 3
    -------------------
    `1.3.1` lower section
    ~~~~~~~~~~~~~~~~~~~~~

----

Use letter for appendix, etc.::

    `A` appendix
    ############

    `B` bibliography
    ################

    `C` change
    ##########

    `D` designatable
    ################
































.. Footnote

.. [#docutil] Q.v. https://docutils.sourceforge.io/docs/index.html

.. [#python] Q.v. https://devguide.python.org/documenting/

.. [#rst_directives] Q.v. https://docutils.sourceforge.io/docs/ref/rst/directives.html
