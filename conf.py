# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rivt'
copyright = '2023 StructureLabs'
author = 'rholland'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

myst_heading_anchors = 3

myst_enable_extensions = ['substitution', 'deflist',
                          'html_image', 'amsmath']

extensions = ['myst_parser', 'sphinx.ext.githubpages',
              "sphinxcontrib.jquery", 'sphinx_copybutton']

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'insegel'
html_static_path = ['_static', ]
html_logo = "riv02.png"
html_theme_options = {
    'navigation_depth': 2
}
