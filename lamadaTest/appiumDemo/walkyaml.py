import yaml
import os

# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath = os.path.join(basepath, "pageelement")


def parseyaml():
    '''

    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements


if __name__ == "__main__":
    a = parseyaml()
    print(a)
    for i in a["HomePage"]['locators']:
        print(i)