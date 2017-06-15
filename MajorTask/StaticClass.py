import jinja2

class StaticFiles:
    def __init__(self, loc_list, template_file=None):
        self.loc_list = loc_list
        if template_file == None:
            self.template_file = "templates/env.html"
        else:
            self.template_file = template_file

    def template_env_file(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template(self.template_file)
        return template.render(list=self.loc_list)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{}'.format(self.loc_list)
