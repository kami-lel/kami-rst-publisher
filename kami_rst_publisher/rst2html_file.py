
import os
from os.path import dirname, abspath, join
import re

from docutils.core import publish_file

STYLESHEET_DIR = "./assets/stylesheets/"  # relative to this file

# stylesheets in STYLESHEET_DIR
LIGHTMODE  = ['responsive.css', "kami_html5.css"]
DARKMODE = ['responsive.css', "kami_html5.css", "kami_html5_dark.css"]

def create_settings_overrides(light_mode=False):
    opt = {}
    stylesheet_dir = abspath(join(dirname(__file__), STYLESHEET_DIR))
    opt["stylesheet_dirs"] = [stylesheet_dir]
    opt["stylesheet_path"] = LIGHTMODE if light_mode else DARKMODE
    return opt


class Rst2htmlFile(object):
    """
    render a single raw rST file, and saved as a html 5 file::

        render_obj = Rst2htmlFile(...)  # 1st render done during initialization

    Then if one want render more than 1 time::

        render_obj.render()

    One can get *message* regards the render by::

        print(render_obj.render())  // or
        print(render_obj.render_msg)  // get message after render


    :param src_path: source path of raw rST file. Can be any plain text files e.g. .rst, .txt, etc.
    :type src_path: io.PathLike
    :param dest_path: path to create new html 5 file. if ``None``, save alongside with *src_path*
    :type dest_path: io.PathLike or NoneType
    :param suffix: Suffix for the generated html 5 file in regard to the old file name.
            Only used when *dest_path* is ``None``. Default to ".R"
    :type suffix: string
    :raise ValueError: src_path is not an accessible file
    :raise docutils.io.OutputError: fail to generate/save html 5 file
    """

    def __init__(self, src_path, dest_path=None, suffix=None, light_mode=False):
        # normalize source path
        self.src = os.path.abspath(src_path)  # make source path absolute
        if not os.path.isfile(self.src):
            raise ValueError('src_path "{}"({}) is not an existing file'.format(src_path, self.src))

        # normalize destination path
        if dest_path:
            # destination path provided by user
            self.dest = os.path.abspath(dest_path)  # make destination path absolute
        else:
            # save (rendered) alongside with source
            suffix = ".R" if suffix is None else suffix  # default value
            folder, full_filename = os.path.split(self.src)
            filename, _ = os.path.splitext(full_filename)  # split filename & extension
            self.dest = os.path.join(folder, (filename + suffix + '.html'))

        self.last_src_mod = None  # save source file modification time during last render
        self.render_msg = None  # save message of last render

        # gen *destination abbr* for message
        common_path = os.path.commonpath([self.src, self.dest])
        self._dest_abbr = self.dest.replace(common_path, "~")

        # make settings_overrides
        self.settings_overrides = create_settings_overrides(light_mode)

        self.render()  # do 1st render

    def render(self):
        """
        :return: ``self.render_msg`` if rendered successfully,
                thus "" if render does not occur because the source file is not modified from last render
        :rtype: str
        :raise docutils.io.OutputError: fail to generate/save html 5 file
        """
        if (not self.last_src_mod) or (os.path.getmtime(self.src) != self.last_src_mod):
            # actual render by docutils
            publish_file(source_path=self.src,
                    destination_path=self.dest,
                    writer_name='html5',
                    settings_overrides=self.settings_overrides)

            self.last_src_mod = os.path.getmtime(self.src)
            # gen message
            self.render_msg = "{}\t\t-> {}".format(self.src, self._dest_abbr)
        else:
            # for there is no actual render happening
            self.render_msg = ""

        return self.render_msg

    def __str__(self):
        return self.render_msg


class Rst2htmlFileBatch(object):
    """
    render any file with name fullmatching (regex) *filter* in a **directory** *src_dir*::

        batch_render_obj = Rst2htmlFileBatch(...)  # 1st render done during init

    Then if one want to render more than 1 time::

        batch_render_obj.render()

    One can get *message* regards the render by::

        print(batch_render_obj.render())  // or
        print(str(batch_render_obj)  // get message after render


    :param src_dir: a directory path
    :type src_dir: os.PathLike
    :param dest_dir: directory path to save the rendered html 5 files. If ``None``, save within *src_dir*
    :type dest_dir: os.PathLike or NoneType
    :param mask:filter (a regex pattern) to recognize plain text files to be rendered. Default to ``.+\.rst``
    :type mask: str
    :param suffix: Suffix for the generated html 5 files in regard to the old file names. Default to ".R"
    :type suffix: string
    :raise ValueError: src_dir is not an accessible directory
    :raise docutils.io.OutputError: fail to generate/save html 5 file
    """

    def __init__(self, src_dir, dest_dir=None, mask=None, suffix=None, lightmode=False):
        # set default value for param
        mask = mask or r'.+\.rst'
        suffix = ".R" if suffix is None else suffix

        # normalize src dir path
        self.src = os.path.abspath(src_dir)  # make source dir path absolute
        if not os.path.isdir(self.src):
            raise ValueError('src_dir "{}"({}) is not an existing directory'.format(src_dir, self.src))

        # normalize dest path
        self.dest = dest_dir and os.path.abspath(dest_dir)  # kept as None if not provided

        self.file_objs = []
        for full_filename in os.listdir(self.src):
            src_file = os.path.join(self.src, full_filename)
            if os.path.isfile(src_file) and re.fullmatch(mask, full_filename):
                # select only file with filename match FILTER in self.src
                # generate destination file path
                if self.dest:
                    filename, _ = os.path.splitext(full_filename)  # source name w/o extension
                    dest_file = os.path.join(self.dest, (filename + suffix + '.html'))
                else:
                    dest_file = None

                obj = Rst2htmlFile(src_file, dest_file, suffix, lightmode)
                self.file_objs.append(obj)

    def render(self):
        """
        render the 2nd time (after render during init) or more


        :return: ``str(self)`` for message regards this render
        :raise docutils.io.OutputError: fail to generate/save html 5 file
        """
        for obj in self.file_objs:
            obj.render()

        return self.__str__()

    def __str__(self):
        if not any(v.render_msg for v in self.file_objs):
            # none of file objs actually rendered
            return ""

        first_line = "{} -> {}".format(self.src, self.dest) if self.dest else self.src
        lines = [first_line]

        for obj in self.file_objs:
            if not obj.render_msg:
                continue  # skip non-rendered obj

            file_src = obj.src.replace(self.src, "~")  # abbr file_src in respect to self.src
            # abbr file_dest in respect to self.dest or self.src
            file_dest = obj.dest.replace(self.dest, "*") if self.dest else obj.dest.replace(self.src, "~")
            lines.append("\t{}\t\t-> {}".format(file_src, file_dest))

        return "\n".join(lines)


class Rst2htmlFileRecursive(object):
    """
    recursively render any files fullmatching (regex) *filter* in *root_dir* and its sub-folders::

        recursive_obj = Rst2htmlFileRecursive(...)  # 1st render done during initialization

    Then if one want render more than 1 time::

        recursive_obj.render()

    One can get *message* regards the render by::

        print(recursive_obj.render())  // or
        print(str(recursive_obj))  // get message after render


    :param root_dir: the base directory path
    :type root_dir: os.PathLike
    :param suffix: Suffix for the generated html 5 files in regard to the old file names. Default to ".R"
    :type suffix: string
    :raise ValueError: root_dir is not an accessible directory
    :raise docutils.io.OutputError: fail to generate/save html 5 file
    """

    def __init__(self, root_dir, mask=None, suffix=None, lightmode=False):
        root = os.path.abspath(root_dir)  # make source dir path absolute
        if not os.path.isdir(root):
            raise ValueError('root_dir "{}"({}) is not an existing directory'.format(root_dir, root))

        self.batch_objs = []
        for dirpath, _, _ in os.walk(root):
            batch_obj = Rst2htmlFileBatch(dirpath, mask=mask, suffix=suffix, lightmode=lightmode)
            self.batch_objs.append(batch_obj)

    def render(self):
        for batch_obj in self.batch_objs:
            batch_obj.render()

        return self.__str__()

    def __str__(self):
        batch_obj_msg = [str(v) for v in self.batch_objs if str(v)]
        if batch_obj_msg:
            return "\n".join(batch_obj_msg)
        else:
            # none of batch obj rendered
            return ""
