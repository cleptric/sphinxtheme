"""
CakePHP Git branch extension.

A simple sphinx extension for adding
the GitHub branch name of the docs' version.
"""


def setup(app):
    app.connect('html-page-context', append_template_ctx)
    app.add_config_value('branch', '', True)
    app.add_config_value('version_name', '', True)
    app.add_config_value('version_list', [], True)
    app.add_config_value('search_version', '', True)


def append_template_ctx(app, pagename, templatename, ctx, event_arg):
    ctx['branch'] = app.config.branch
    ctx['version_name'] = app.config.version_name
    ctx['version_list'] = app.config.version_list
    ctx['search_version'] = app.config.search_version
