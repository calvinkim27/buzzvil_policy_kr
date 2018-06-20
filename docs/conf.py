# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import logging
import os.path
import re
import subprocess


logger = logging.getLogger('rtd-samples')


def get_git_branch():
    """Get the git branch this repository is currently on"""
    path_to_here = os.path.abspath(os.path.dirname(__file__))

    # Invoke git to get the current branch which we use to get the theme
    try:
        p = subprocess.Popen(['git', 'branch'], stdout=subprocess.PIPE, cwd=path_to_here)

        # This will contain something like "* (HEAD detached at origin/MYBRANCH)"
        # or something like "* MYBRANCH"
        branch_output = p.communicate()[0]

        # This is if git is in a normal branch state
        match = re.search(r'\* (?P<branch_name>[^\(\)\n ]+)', branch_output)
        if match:
            return match.groupdict()['branch_name']

        # git is in a detached HEAD state
        match = re.search(r'\(HEAD detached at origin/(?P<branch_name>[^\)]+)\)', branch_output)
        if match:
            return match.groupdict()['branch_name']
    except Exception:
        logger.exception(u'Could not get the branch')

    # Couldn't figure out the branch probably due to an error
    return None


# -- Project information -----------------------------------------------------

project = u'버즈빌 정책센터'
copyright = u'© 2018 Buzzvil. All Rights Reserved.'
author = u'Buzzvil'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

