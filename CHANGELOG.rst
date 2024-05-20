============================
kami-rst-publisher CHANGELOG
============================

.. default-role:: smart

.. contents::













version checklist
#################
Finalize *code*:

1. check **todo** within code

Update *documentation*:

1. ``CHANGELOG.rst``: record changes of this version
2. ``README.rst``: update with new feature
3. ``README.R.html``: render (with ``-s`` arg)
4. ``CHANGELOG.rst``: finalize *version message*

Update versions in *package management*:

1. ``setup.cfg``:

   - update ``metadata/version``
   - include non-``.py`` files in ``options.package_data``

2. update version line (1st line) in stylesheet ``kami_html5.css``

.. rubric:: commit process

Stash aways most recent changes::

    git checkout dev
    git stash push

Squash merge ``main`` from ``dev``::

    git checkout main
    git merge --squash dev
    git stash pop

Inspect changes of this version::

    git status [-s]
    git diff --cached . [PATH]

Make the version commit with *version message* in ``main``::

    git commit -m "..."

Catch up ``dev`` branch with the version::

    git checkout dev
    git merge main













future feature
##############

- add ``-d`` option to append date in resulting filename. E.g. ``-d 13`` means add ``.#[02022-03-05]`` as suffix
- eliminate the need write ``.. default-role:: smart`` for each file













3-0
###
version message::

    3-0: pack as package & fix format

changes:

- to release the project as a *Python* **package**, modify the structure of the project and change/add related files
- change how **light/dark mode** is implemented. Eliminate the need of ``.conf`` files, and stylesheet directories are generated and passed-in programmatically
- remove ``./src/kami-rst-publisher/publisher_cli.bat``, because it no longer work with current project structure
- **stylesheet** changes of ``kami_html5.css`` and ``kami_html5_dark.css`` in ``./kami_rst_publisher/asssets/kami_html5.css``:

  - *rubric* was not distinguishable enough from normal headings, now it has a different *hue*
  - different levels of *headings* were not distinguishable when placed with some distance in between, thus:

    - relative font sizes of heading levels are changed
    - in *darkmode*, different heading levels have different *shades* of color













2-6
###
commit message::

    #2-6: create publisher_cli.bat

- add ``publisher_cli.bat``

  - and respective documentation in ``README.rst``

- change format of version indicating line in ``kami_htmla5.css``, now it is::

      /* PUBLISHED BY kami-rst-publisher.#2-6 */

.. rubric:: 02023-10-27












2-5
###
commit message::

    #2-5: improve continuous mode, fix format, etc.

- change related to *continuous mode*:

  - change each renderers to improve continuous mode (in ``/src/kami_rst_publisher/rst2html_file.py``)
  - rename to ``publisher_cli.py`` (from ``cli.py``)
  - change in ``publisher_cli.py`` to accommodate changes of continuous mode

- change stylesheets: (in ``stylesheet/``)

  - ``kami_html5.css``

    - embedded kami-rst-publisher version, at 1st line as comment
    - improve regards lists (``ol``, ``ul``)
    - allow for nested *ordered list* ``ol`` now

  - ``kami_html5_dark.css``: add color to headings

- change in ``CHANGELOG.rst``:

  - revert order of each entry. Now later is at top
  - add *release checklist* used before each release
  - add *todo feature* recording features to be implemented in the future

- minor correction and change in ``README.rst``

.. rubric:: 02023-10-26













2-4
###
commit message::

    #2-4: stylesheet rewrite & light mode switch

**stylesheet** related:

- rewrite ``kami_html5.css`` & ``kami_html5_dark.css`` for better eligibility & comment
- make in-text reference different color (cf. normal text)
- improve format of lists including smaller line height, light font, etc.
- create ``stylesheet_test.rst`` (and its rendered form - ``stylesheet_test.R.html``) for testing stylesheet

re ``cli.py``:

- add ``-l`` to enable rendering with light mode

.. rubric:: 02023-06-29













2-3
###
commit message::

    #2-3: fix recursive mode message

Change in ``rst2html_file.py``: in recursive mode, it used to print all traversed folders in the str() messages.
Now it only includes folders those have at least one file is rendered.

.. rubric:: 02023-05-26













2-2
###
commit message::

    #2-2: add recursive mode, etc.

- in ``~/stylesheet/kami_html5.css``: decrease line spacing for lists
- in ``~/src/kami_rst_publisher/role.py``: fix *smart_role* not recognizing ``KS`` as KScode (also make relevant update in ``README.rst``)
- split features of ``~/src/kami_rst_publisher/cli.py`` into ``cli.py`` (as **CLI**) and ``rst2html_file.py`` (as **API**.)

  - make it possible to **recursively** render
  - make the rendering **verbose**
  - rename *repeat mode* to **continuous**
  - update ``README.rst`` to explain these usages

.. rubric:: 02023-05-25













2-1
###
.. rubric:: increase dark theme legibility, etc.

- change in ``kami_html5_dark.css`` regarding dark theme:

  - **bold** was not enough contrast from normal. It is now added with accent color
  - brighten type color for literals & literal blocks

- use *css* classes in smart role, tag role, & tag directive to implement KScode, KSproxy, & `KS.Tag`
- change in ``kami_html5.css`` regarding ``ol`` to use different typefaces for marker & content
- minor correction in ``README.rst``

.. rubric:: 02023-04-27













2-0
###
.. rubric:: version 2.0

- change in stylesheet ``kami_html5.css``: list use typeface *Atkinson Hyperlegible*
- update *smart role* by using HTML classes ``kami-ArabicNumber`` & ``kami-RomanNumeral``
- implement ``~/src/kami_rst_publisher/cli.py``













1-2
###
.. rubric:: dark & light render

Split stylesheets into ``kami_html5.css`` & ``kami_dark_green.css``, viz.:

- light render: use both ``responsive.css`` and ``kami_html5.css``
- dark render: use all of ``responsive.css``, ``kami_html5.css`` & ``kami_dark_green.css``













1-1
###
- add stylesheets













1-0
###
1st version
