=========================
kami-rst-publisher README
=========================

.. default-role:: smart

.. contents::

``kami-rst-publisher`` is a personalized tool based on ``docutils``
































.. _I:

`I` usage
#########
Use ``kami-rst-publisher`` as Python package or by a CLI, v.i.













`1` Python package
==================
Use ``kami-rst-publisher`` as Python code::

    from docutils.core import publish_file
    from kami_rst_publisher import *

    publish_file(...)













`2` API
=======
An API (defined in ``./kami_rst_publisher/rst2html_file.py``) can be used for publish raw rST plain text into html 5 file(s).

One can use in Python::

    from kami_rst_publisher import Rst2htmlFile, Rst2htmlFileBatch, Rst2htmlFileRecursive

    Rst2htmlFile(src, dest)

Check *docstring* for each classes.












`3` Python CLI
==============
One could use a CLI defined in ``./kami_rst_publisher/__main__.py``

Run with python::

    python3 -m kami_rst_publisher ...

And its *help* file::

    usage: kami_rst_publisher [-h] [-r] [-e FILTER] [-w [PORT]] [-s [SUFFIX]] [-p {dark,light}] [-D] [-v] [-q] SOURCE [DESTINATION]

    personalized rST publisher based on docutils but with extra roles & directives

    - single mode: given a SOURCE file, publish a HTML file
    - recursive mode: recusrively publish all files in SOURCE folder
    - web server mode: to be implemented

    positional arguments:
      SOURCE                SOURCE of raw text, as file/directory path
      DESTINATION           DESTINATION for rendered files, as file/directory path
                            if absent, rendered files will be saved alongside SOURCE

    options:
      -h, --help            show this help message and exit
      -r, --recursive       enable recursive mode, v.s.
      -e FILTER, --expression FILTER
                            with --recursive, use FILTER to select files to be rendered
                            default to ".+\.rst"
      -w [PORT], --web-server [PORT]
                            enable web server mode, v.s.
      -s [SUFFIX], --suffix [SUFFIX]
                            append SUFFIX to rendered files
                            default to ".R"
                            ignored in single mode and DESTINATION is given
      -p {dark,light}, --render-preset {dark,light}
                            set rendering presets
      -D, --dark            equivalent to --preset dark
      -v, --verbose
      -q, --quiet












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


