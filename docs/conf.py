# Configuration file for the Sphinx documentation builder.

# -- Project information

from ast import arg
from datetime import datetime
import os
import sys
from sphinx_needs.api import add_dynamic_function

project = "CSJournal"
copyright = "2023, Woha"
author = "Woha"

release = "1.1"
version = "1.1"

# -- General configuration

extensions = [
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx_immaterial",
    "sphinx_design",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

# html_theme = "sphinx_rtd_theme"
html_theme = "sphinx_immaterial"

html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# html_logo = "s2b.png"

html_theme_options = {
    # "icon": {
    #     "repo": "fontawesome/brands/github-square",
    # },
    'logo_only': True,
    'display_version': False,
    "font": {
        "code": "JetBrains Mono"
    },
    "site_url": "https://csjournal.readthedocs.io/",
    "repo_url": "https://github.com/WilliamWoha/csjournal/",
    "repo_name": "CSJournal",
    "repo_type": "github",
    "edit_uri": "blob/main/docs",
    # "google_analytics": ["UA-XXXXX", "auto"],
    "globaltoc_collapse": True,
    "features": [
        # "navigation.sections",
        "navigation.top",
        "search.share",
        "navigation.tracking",
        "toc.follow"
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "yellow",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
    "toc_title": "CSJournal",
}

needs_id_regex = r'.*'
needs_types = [
    dict(directive="sw", title="Software", prefix="S_", color="#BFD8D2", style="card"),
    dict(directive="test", title="test", prefix="S_", color="#BFD8D2", style="card")
           ]

needs_extra_options = [
    'package_summary',
    'category',
    'sphinx_type',
    'license',
    'monthly',
    'overall',
    'code',
    'pypi',
    'website',
    'release_date',
    'release_name',
    'release_days',
    'download_points'
    'release_points',
    'points',
    'code_nice',
    'pypi_nice',
    'website_nice',
    'featured',
    'color',
    'deprecated',
    'stars',
    ]

needs_string_links = {
    # Links to the related github issue
    'links': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': '{{value}}',
        'options': ['code', 'pypi', 'website']
    },
    'links_nice': {
        'regex': r'^(?P<value>.*)$',
        'link_url': '{{value}}',
        'link_name': 'Link',
        'options': ['code_nice', 'pypi_nice', 'website_nice']
    }
}

# This automatically sets some values for all needs. Mostly dynamic functions
# calls to calucalte some value for needs.
# See https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-global-options
needs_global_options = {
   'collapse': 'True',
   'release_days': ("[[days_since_build('release_date')]]", "type == 'sw'"),
   'release_points': ("[[points('release')]]", "type == 'sw'"),
   'download_points': ("[[points('download')]]", "type == 'sw'"),
   'points': ("[[points('all')]]", "type == 'sw'"),
   'code_nice': ("[[copy('code')]]", "type == 'sw'"),
   'pypi_nice': ("[[copy('pypi')]]", "type == 'sw'"),
   'website_nice': ("[[copy('website')]]", "type == 'sw'"),
   'color': [
        ("blue", "sphinx_type=='extension'"),
        ("green", "sphinx_type=='theme'"),
        ("red", "sphinx_type=='other'"),
   ],
   'style': [
        ("awesome_[[copy('color')]]", "type=='sw'"),
   ],
   'template': [
        ("software", "type=='sw'"),
   ]
}

needs_variant_options = ["status"]  # Not needed, but workarund to avoid a bug and some warnings

needs_needextend_strict = False

def days_since_build(app, need, needs, *args, **kwargs):
    """
    Calculates the days from now to a given date, which is normally in the past.

    Usage::

        .. need:: My_need
           :date: 2020-09-08T11:05:55.2340Z
           :days: [[days_since_build('date')]]

    """
    date_option = args[0]
    date = need[date_option]
    
    date_obj = datetime.fromisoformat(date)
    delta = datetime.now() - date_obj

    return str(delta.days)

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    
    Source: https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    """
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
        app.connect("source-read", rstjinja, 50000)
        
        add_dynamic_function(app, days_since_build)
        add_dynamic_function(app, points)
