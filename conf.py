# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any, Dict

import pydata_sphinx_theme
from sphinx.application import Sphinx

sys.path.append(str(Path(".").resolve()))

# -- Project information -----------------------------------------------------

project = 'rivt'
copyright = '2023 StructureLabs'
author = 'rholland'
release = '0.1'


# -- General configuration ---------------------------------------------------

myst_heading_anchors = 3

myst_enable_extensions = ['substitution', 'deflist',
                          'html_image', 'amsmath']

extensions = ['myst_parser', 'sphinx.ext.githubpages',
              "sphinxcontrib.jquery", 'sphinx_copybutton']

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static', ]
html_logo = "_static/img/rivt01a.png"
html_theme_options = {
    "show_nav_level": 2,
    "navbar_align": "content",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navigation_depth": 3,
    "logo": {
        "text": "rivt",
        "image_dark": "_static/img/riv-dark8.png",
    },
}

html_sidebars = {
    "**": ["sidebar-nav-bs"]
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
