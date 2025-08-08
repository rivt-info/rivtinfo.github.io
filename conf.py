import sys
from pathlib import Path
sys.path.append(str(Path(".").resolve()))

project = 'rivt.info'
copyright = '2023 StructureLabs LLC'
author = 'rholland'
release = '0.1'

extensions = ['sphinx.ext.githubpages',
              "sphinxcontrib.jquery", 'sphinx_copybutton',
              'sphinx_favicon', 'sphinx.ext.duration',
              'sphinx.ext.doctest', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']

html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_context = {"default_mode": "light"}
html_sidebars = {"**": ["search-field.html", "sidebar-nav-bs.html"]}
html_static_path = ['_static', '_static/img']
html_css_files = ['css/custom.css',]
html_theme_options = {
    "navbar_align": "left",
    "show_nav_level": 2,
    "show_toc_level": 2,
    "navigation_depth": 2,
    "footer_start": ["copyright"],
    "footer_end": [],
    "logo": {
        "image_dark": "_static/img/rivhome11c.png",
        "image_light": "_static/img/rivhome11c.png",
    }
}

favicons = [
    {"href": "favicon-32x32.png"},
    {"href": "favicon-16x16.png"},
]
