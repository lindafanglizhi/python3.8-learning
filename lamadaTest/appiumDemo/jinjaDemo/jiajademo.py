from jinja2 import Template


templa = Template('hello {{name}}!')
print(templa.render(name='linda 房'))

basehtml ='<html><head><title>{{}title}</title></head><body><h1>{{header}}</h1><p>{{body}}</p></body></html>'
htmlte =Template(basehtml)