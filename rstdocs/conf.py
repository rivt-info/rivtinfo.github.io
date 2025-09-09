import sys
import os
from pathlib import Path
sys.path.append(str(Path(".").resolve()))
from sphinx.locale import get_translation

project = 'rivt.info'
copyright = '2023 StructureLabs LLC'
author = 'rholland'
release = '0.3.0'

extensions = ['sphinx.ext.githubpages','sphinx_togglebutton',
              "sphinxcontrib.jquery", 'sphinx_copybutton',
              'sphinx_favicon', 'sphinx.ext.duration',
              'sphinx.ext.doctest', 'sphinx.ext.autodoc',
              'sphinx_design']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']
master_doc = 'index'
templates_path = ['_templates']
locale_dirs = ['_locale'] 



html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_context = {"default_mode": "dark"}
html_sidebars = {"**": ["sidebar-nav-bs.html"]}
html_static_path = ['_static', '_static/img']
html_css_files = ['css/custom.css',]
html_theme_options = {
    "pygments_light_style": "tango",  
    "pygments_dark_style": "github-dark",   
    "navbar_start": ["navbar-logo", "index_link"],
    "collapse_navigation": True ,
    "header_links_before_dropdown": 6,
    "navbar_align": "left",
    "show_toc_level": 1,
    "navigation_depth": 1,
    "footer_start": ["copyright"],
    "footer_end": [],
    "logo": {
        "text": "Home",
        "image_dark": "rivhome11c.png",
        "image_light": "rivhome11c.png",
    }
}



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
