=========================
kami-rst-publisher README
=========================

.. default-role:: smart

.. contents::

``kami-rst-publisher`` is a personalized tool based on ``docutils``

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
One could use a CLI defined in ``./kami_rst_publisher/__main__.py``

Run with python::

    python3 -m kami_rst_publisher ...

And its *help* file::

    usage: (kami rST publisher)publisher-cli.py [-h] [-b] [-r] [-c [WAIT]] [-l] [-v] [-s [SUFFIX]] [-e EXPRESSION] SOURCE [DESTINATION]

    personalized rST publisher based on docutils but with extra roles & directives

    positional arguments:
      SOURCE                SOURCE of rST text, file or directory path
      DESTINATION           DESTINATION of rendered .html file(s), file or directory path. Rendered file will be saved alongside with SOURCE if not given

    options:
      -h, --help            show this help message and exit
      -b, --batch           render any file with name fullmatching (regex) EXPRESSION in a directory SOURCE. SOURCE & DESTINATION should be directory path. EXPRESSION default to ".+\.rst", but can be set by -f
      -r, --recursive       like -b, but recursively into each sub-folder of SOURCE. This flag overwrites -b. DESTINATION is not used when -r
      -c [WAIT], --continuous [WAIT] render all changed files once every WAIT seconds. WAIT default to 5.0.
      -l, --light           render in light mode
      -v, --verbose
      -s [SUFFIX], --suffix [SUFFIX] SUFFIX for rendered file. Default to ".R"
      -e EXPRESSION, --expression EXPRESSION with -b or -r, set EXPRESSION for file matching. Default to ".+\.rst"












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


































`II` rST customization
######################
``kami-rst-publisher`` allow customization of *rST* by utilizing **customized roles and directives**.













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













`3` tag role
============
::

    :tag:`example_tag`

render as:

    :tag:`example_tag`













`4` tag directive
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
































.. Footnote

.. [#docutil] Q.v. https://docutils.sourceforge.io/docs/index.html

.. [#python] Q.v. https://devguide.python.org/documenting/

