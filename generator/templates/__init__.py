from jinja2 import Template
from utils.common import get_config
import os

def generate_template(template_name):
    template_dir = os.path.join(get_config()['templates_path'], f'{template_name}.html')
    print(template_dir)
    with open(template_dir, mode='r') as f:
        return Template(f.read())

def custom_render_template(template: Template, *args, **kwargs):
    return template.render(*args, **kwargs)