import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'CHESS'
author = 'Duan'
release = '1.0.0'
version = '0.1.0'

extensions = [
    'myst_parser',         # 支持 Markdown
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
html_theme = 'sphinx_rtd_theme'
source_suffix = ['.rst', '.md']
