"""
update the file ``./kami_rst_publisher/assets/publisher_version_appendix.html`` with version extraccted from ``./setup.cfg``
"""


PUBLISHER_VERSION_APPENDIX_TEMPLATE = """
<!-- PUBLISHED BY kami_rst_publisher.#{} -->
"""


from pathlib import Path
import configparser


if __name__ == '__main__':
    setup_cfg_path = (Path(__file__).parent.parent / 'setup.cfg').resolve()
    appendix_file_path = (Path(__file__).parent.parent / 
            'kami_rst_publisher' / 'assets' /
            'publisher_version_appendix.html').resolve()

    with open(appendix_file_path, 'w') as appendix_file:
        config = configparser.ConfigParser()
        config.read(setup_cfg_path)

        version = config['metadata']['version']
        ver_hf = version.replace('.', '-')  # change e.g. '3.1' -> '3-1
        content = PUBLISHER_VERSION_APPENDIX_TEMPLATE.format(ver_hf)

        appendix_file.write(content)
