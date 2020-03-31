from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)  # 创建一个文件加载器对象

# template = env.get_template('hello_world.txt')  # 获取一个模板文件
# print(template.render())

# template1 = env.get_template('lamb.txt')
# output = template1.render(name='linda')
# print(output)
# person = {}
# person['name'] = 'Frank'
# person['animal'] = 'dog'
# template2 = env.get_template('listdata.txt')
# output = template2.render(data=person)
# print(output)

# template3 = env.get_template('truth.txt')
# output = template3.render(truth=True)
# print(output)

# colors = ['red', 'green', 'blue']
# template4 = env.get_template('rainbow.txt')
# output = template4.render(colors=colors)
# print(output)

template5 = env.get_template('base.html')
output = template5.render(title='Baidu Title')
print(output)

template6 = env.get_template('child.html')
output = template6.render(title='Baidu Title',body='this is  test')
print(output)
