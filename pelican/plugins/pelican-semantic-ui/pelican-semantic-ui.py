from pelican import signals
from jinja2 import ChoiceLoader, FileSystemLoader

def add_loader(pelican):
    '''
    https://stackoverflow.com/questions/30109097/trying-to-override-jinja-choicereloader-in-a-pelican-plugin
    '''

    pelican.env.loader = ChoiceLoader([
        pelican.env.loader,
        #PackageLoader('Semantic-UI-Jinja2', 'templates'),
        FileSystemLoader('/home/niels/Projects/public/Semantic-UI-Jinja2/semantic_ui_jinja2/templates'),
    ])

def register():
    signals.generator_init.connect(add_loader)