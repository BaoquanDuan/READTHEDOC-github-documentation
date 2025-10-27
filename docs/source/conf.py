# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'CHESS'
copyright = '2026, Duan'
author = 'd'

release = '1.0.0'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',       # 支持 .md 文件
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
