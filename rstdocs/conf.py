import sys
import os
from pathlib import Path
sys.path.append(str(Path(".").resolve()))
from sphinx.locale import get_translation

project = 'rivt.info'
copyright = '2023 StructureLabs LLC'
author = 'rholland'
release = '0.1'

extensions = ['sphinx.ext.githubpages',
              "sphinxcontrib.jquery", 'sphinx_copybutton',
              'sphinx_favicon', 'sphinx.ext.duration',
              'sphinx.ext.doctest', 'sphinx.ext.autodoc']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']
master_doc = 'index'
templates_path = ['_templates']
language = 'en'
locale_dirs = ['_staticsrc/locale/'] 
gettext_compact = False # Important for themes to pick up translations

html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_context = {"default_mode": "dark"}
html_sidebars = {"**": ["sidebar-nav-bs.html"]}
html_static_path = ['_staticsrc', '_staticsrc/img']
html_css_files = ['css/custom.css',]
html_theme_options = {
    "collapse_navigation": True ,
    "header_links_before_dropdown": 6,
    "navbar_align": "left",
    "show_toc_level": 2,
    "navigation_depth": 2,
    "footer_start": ["copyright"],
    "footer_end": [],
    "logo": {
        "image_dark": "rivhome11c.png",
        "image_light": "rivhome11c.png",
    }
}

# Specify the message catalog name
catalog = "messages"

# Get the translation object
_ = get_translation(catalog)

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "href": "favicon-16x16.png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "href": "favicon-32x32.png",
    },

]
