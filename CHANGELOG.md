# kami-rst-publisher CHANGELOG

[^format]













## [Unreleased]

### Added

- hooks-utility as Git Submodule

### Changed

- formalize `CHANGELOG.md` format

### Deprecated
### Removed
### Fixed















## [4.1.0] - 2024-12-26

version message

```
4-1: fix critical bug in web server mode
```













## [4.0.0] - 2024-12-26

version message

```
4-0: add Markdown support
```

changes in stylesheets:

- use relative fontsize for literal, such that it may appears in title, headings, & list
- make hyperlink to footnote superscripts

change re **CLI**:

- fix bug in CLI regarding options `-p` and `-D`
- add support for render **Markdown** as source:

    - utilize 3-rd party parser `myst-docutils`
    - reorganize `tests/` for new tests and tests for md
    - add MLOs `--rst` and `--md`
    - function of  `-e` is changed to make it possible for rst & md render

- change publisher version appending logic, content of file `./kami_rst_publisher/assets/publisher_version_appendix.html` is added after render as HTML comment














## [3.4.0] - 2024-12-19

version message

```
3-4:modularize CLI function to 3 modes
```

- `CHANGELOG.md`: renamed & translated from `CHANGELOG.rst`
- `README.rst`: update content structure, clarify usage instructions
- `kami_rst_publisher`:

    - `__main__.py`: modularized CLI with single and recursive modes
    - `cli_single.py`: implements single mode for CLI
    - `cli_recursive.py`: implements recursive mode for CLI
    - `cli_web_server.py`: placeholder for future web server implementation
    - `cli_utils.py`: contains common utility functions for CLI operations

- `tests/`: extensive addition of test cases for the CLI functionalities, covering various scenarios including permissions and output checks.













## [3.3.0] - 2024-12-11

version message:

```
3-3:update module structure and CLI options
```

**reorganize Python module structure:**

- in `__init__.py`, expose content of and remove function `init_publisher`, user now initialize publisher by performing an `import` of the module.
- utilize `__all__` in scripts.

**change to CLI:**

- rename option to `--expression` (from `--filter`)
- CLI is implemented in `./kami_rst_publisher/__main__.py`, renamed from `cli.py`.

**remove useless files:**

- test render result `./tests/test_render.R.html`
- `./kami_rst_publisher/docutils.conf`

---

- add color and font setting for subscript and superscript in *stylesheets*.
- use a standalone `publisher_version.css` to include publisher version in every rendered `.html` file.













## [3.2.0] - 2024-10-07

version message:

```
3-2:extract stylesheet_note as a separate file.
```













## [3.1.0] - 2024-10-07

version message:

```
3-1:remove certain TAG in stylesheet, record issues.
```

- kami_rst_publisher/assets/stylesheets/kami_html5.css: remove certain TAG word.
- record issues and future features in their most related files.













## [3.0.0] - 2024-05-09

version message:

```
3-0: pack as package & fix format.
```

**changes:**

- to release the project as a *Python* **package**, modify the structure of the project and change/add related files.
- change how **light/dark mode** is implemented. Eliminate the need for `.conf` files, and stylesheet directories are generated and passed-in programmatically.
- remove `./src/kami-rst-publisher/publisher_cli.bat`, because it no longer works with the current project structure.
- **stylesheet** changes of `kami_html5.css` and `kami_html5_dark.css` in `./kami_rst_publisher/assets/kami_html5.css`:

  - *rubric* was not distinguishable enough from normal headings, now it has a different *hue*.
  - different levels of *headings* were not distinguishable when placed with some distance in between, thus:

    - relative font sizes of heading levels are changed.
    - in *dark mode*, different heading levels have different *shades* of color.













## 2-6

commit message:

```
#2-6: create publisher_cli.bat
```

- add `publisher_cli.bat`

  - and respective documentation in `README.rst`.

- change format of version indicating line in `kami_html5.css`, now it is::

      /* PUBLISHED BY kami-rst-publisher.#2-6 */

> 02023-10-27













## 2-5

commit message:

```
#2-5: improve continuous mode, fix format, etc.
```

- change related to *continuous mode*:

  - change each renderer to improve continuous mode (in `/src/kami_rst_publisher/rst2html_file.py`).
  - rename to `publisher_cli.py` (from `cli.py`).
  - change in `publisher_cli.py` to accommodate changes of continuous mode.

- change stylesheets: (in `stylesheet/`)

  - `kami_html5.css`

    - embedded kami-rst-publisher version, at 1st line as comment.
    - improved regards lists (`ol`, `ul`).
    - allow for nested *ordered list* `ol` now.

  - `kami_html5_dark.css`: add color to headings.

- change in `CHANGELOG.rst`:

  - revert order of each entry. Now later is at top.
  - add *release checklist* used before each release.
  - add *todo feature* recording features to be implemented in the future.

- minor correction and change in `README.rst`.

> 02023-10-26













## 2-4

commit message:

```
#2-4: stylesheet rewrite & light mode switch
```

**stylesheet** related:

- rewrite `kami_html5.css` & `kami_html5_dark.css` for better eligibility & comment.
- make in-text reference different color (cf. normal text).
- improve format of lists including smaller line height, light font, etc.
- create `stylesheet_test.rst` (and its rendered form - `stylesheet_test.R.html`) for testing stylesheet.

re `cli.py`:

- add `-l` to enable rendering with light mode.

> 02023-06-29













## 2-3

commit message:

```
#2-3: fix recursive mode message.
```

Change in `rst2html_file.py`: in recursive mode, it used to print all traversed folders in the str() messages. Now it only includes folders that have at least one file rendered.

> 02023-05-26













## 2-2

commit message:

```
#2-2: add recursive mode, etc.
```

- in `~/stylesheet/kami_html5.css`: decrease line spacing for lists.
- in `~/src/kami_rst_publisher/role.py`: fix *smart_role* not recognizing `KS` as KScode (also make relevant update in `README.rst`).
- split features of `~/src/kami_rst_publisher/cli.py` into `cli.py` (as **CLI**) and `rst2html_file.py` (as **API**):

  - make it possible to **recursively** render.
  - make the rendering **verbose**.
  - rename *repeat mode* to **continuous**.
  - update `README.rst` to explain these usages.

> 02023-05-25













## 2-1

increase dark theme legibility, etc.

- change in `kami_html5_dark.css` regarding dark theme:

  - **bold** was not enough contrast from normal. It is now added with accent color.
  - brighten type color for literals & literal blocks.

- use *css* classes in smart role, tag role, & tag directive to implement KScode, KSproxy, & `KS.Tag`.
- change in `kami_html5.css` regarding `ol` to use different typefaces for marker & content.
- minor correction in `README.rst`.

> 02023-04-27













## 2-0

version 2.0.

- change in stylesheet `kami_html5.css`: list use typeface *Atkinson Hyperlegible*.
- update *smart role* by using HTML classes `kami-ArabicNumber` & `kami-RomanNumeral`.
- implement `~/src/kami_rst_publisher/cli.py`.













## 1-2

dark & light render.

Split stylesheets into `kami_html5.css` & `kami_dark_green.css`, viz.:

- light render: use both `responsive.css` and `kami_html5.css`.
- dark render: use all of `responsive.css`, `kami_html5.css` & `kami_dark_green.css`.













## 1-1

- add stylesheets.













## 1-0

1st version.














[unreleased]: https://github.com/kami-lel/kami-rst-publisher/compare/v4.1.0...dev
[4.1.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v4.0.0...v4.1.0
[4.0.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v3.4.0...v4.0.0
[3.4.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v3.2.0...v3.3.0
[3.2.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/kami-lel/kami-rst-publisher/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/kami-lel/kami-rst-publisher/releases/tag/v3.0.0













[^format]: CHANGELOG format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); Version scheme adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).