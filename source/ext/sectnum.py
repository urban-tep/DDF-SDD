import sys

def setup(app):
    app.add_config_value('number_section', False, 'html')
    app.add_config_value('number_section_prefix', '', 'html')
    app.add_config_value('number_section_suffix', '', 'html')
    app.add_config_value('number_section_start', 1, 'html')
    app.add_config_value('number_section_maxdepth', sys.maxint, 'html')

    app.connect('env-updated', add_number_section)

    return {'version': '0.1'}   # identifies the version of our extension



from docutils import nodes
from docutils.nodes import section
from docutils.nodes import title
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


def add_number_section(app, env):
    """
    Automatically assigns numbers to the titles of document sections.
    It is possible to limit the maximum section level for which the numbers
    are added.  For those sections that are auto-numbered, the "autonum"
    attribute is set, informing the contents table generator that a different
    form of the TOC should be used.
    """

    if app.config.number_section:
      return env.assign_section_numbers()