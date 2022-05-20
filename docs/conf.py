# -*- coding: utf-8 -*-

# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import shutil
import warnings
from distutils.dir_util import copy_tree

import mthree as m3

"""
Sphinx documentation builder
"""

# The short X.Y version
version = m3.__version__
# The full version, including alpha/beta/rc tags
release = m3.__version__


rst_prolog = """
.. |version| replace:: {0}
""".format(m3.version.short_version)

# -- Project information -----------------------------------------------------
project = 'Mthree {}'.format(version)
copyright = '2021, Mthree Team'  # pylint: disable=redefined-builtin
author = 'Mthree Development Team'
# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'nbsphinx',
    'jupyter_sphinx'
]
html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = ['gallery.css']
nbsphinx_timeout = 300
nbsphinx_execute = 'always'

exclude_patterns = ['_build', '**.ipynb_checkpoints']

jupyter_execute_kwargs = dict(allow_errors=False)

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------
autosummary_generate = True

# -----------------------------------------------------------------------------
# Autodoc
# -----------------------------------------------------------------------------

autoclass_content = 'init'

# If true, figures, tables and code-blocks are automatically numbered if they
# have a caption.
numfig = True

# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to
# strings that are used for format of figure numbers. As a special character,
# %s will be replaced to figure number.
numfig_format = {
    'table': 'Table %s'
}
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ['mthree.']

# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "qiskit_sphinx_theme"


#html_sidebars = {'**': ['globaltoc.html']}
html_last_updated_fmt = '%Y/%m/%d'


def load_tutorials(app):
    dest_dir = os.path.join(app.srcdir, 'tutorials')
    source_dir = os.path.dirname(app.srcdir)+'/tutorials'

    try:
        copy_tree(source_dir, dest_dir)
    except FileNotFoundError:
        warnings.warn('Copy tutorials failed.', RuntimeWarning)

def clean_tutorials(app, exc):
    tutorials_dir = os.path.join(app.srcdir, 'tutorials')
    shutil.rmtree(tutorials_dir)

def setup(app):
    load_tutorials(app)
    app.connect('build-finished', clean_tutorials)