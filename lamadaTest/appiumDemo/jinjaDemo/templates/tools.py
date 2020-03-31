import os
import jinja2
from appiumDemo.jinjaDemo.templates import tools1


basepath = '/Users/lindafang/PycharmProjects/lamadaTest/appiumDemo/jinjaDemo/templates'
# yamlpage = tools1.parseyaml()
page_list = {'LoginPage': ['微信登录', '手机号登录', '其它登录', 'QQ', '微博', '账号密码', '输入账号', '输入密码', '登录按钮'], 'MyPage': ['我的', '请点击登录'], 'HomePage': ['城市选择', '首页搜索']
}

#
# def get_page_list(yamlpage):
#     page_object = {}
#     for page, names in yamlpage.items():
#         loc_names = []
#         locs = names['locators']
#         for loc in locs:
#             loc_names.append(loc['name'])
#         page_object[page] = loc_names
#     print(page_object)
#     return page_object


def create_pages_py(page_list):
    print(os.path.join(basepath, "templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath, "pages.py"), 'w') as f:
        f.write(template.render(page_list))


if __name__ == '__main__':
    create_pages_py(page_list)




