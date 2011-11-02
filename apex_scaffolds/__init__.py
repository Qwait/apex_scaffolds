from paste.util.template import paste_script_template_renderer

from pyramid.scaffolds import PyramidTemplate

class JinjaPyramidTemplate(PyramidTemplate):
    def pre(self, command, output_dir, vars):
        vars['jinja_start'] = '{{'
        vars['jinja_end'] = '}}'

        super(JinjaPyramidTemplate, self).pre(command, output_dir, vars)

class RajaTemplate(JinjaPyramidTemplate):
    _template_dir = 'raja_template'
    summary = 'Routes, Alchemy, Jinja2, Apex'
    template_renderer = staticmethod(paste_script_template_renderer)