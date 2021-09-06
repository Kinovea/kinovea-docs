# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
project = 'Kinovea'
copyright = '2021, Kinovea documentation authors (CC0 1.0)'
author = 'Kinovea documentation authors'

# The full version, including alpha/beta/rc tags
release = '0.9.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['css/kinovea.css']
html_logo = 'images/logo/kinovea.svg'
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'style_external_links': True,
    'style_nav_header_background': "#404040",
    # Collapse navigation (False makes it tree-like)
    #'collapse_navigation': False,
}

html_context = {
  'display_github': False,
}

pdf_documents = [('index', u'kinoveadoc', u'Kinovea documentation', u'Kinovea community'),]


# -- Options for Epub output ----------------------------------------------

# EPUB Output
epub_theme = "sphinx_rtd_theme"
#epub_theme = 'epub'

# Bibliographic Dublin Core info.

epub_description = "Kinovea reference manual"
epub_publisher = "Kinovea"
epub_title = project
epub_author = author
epub_copyright = copyright

# The cover page information. This is a tuple containing the filenames of
# the cover image and the html template.
#epub_cover = ('_static/cover.png', 'epub-cover.html')
epub_css_files = ['css/kinovea.css']

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in the file toc.ncx.
epub_tocdepth = 2

# Control whether to display URL addresses.
epub_show_urls = 'no'


