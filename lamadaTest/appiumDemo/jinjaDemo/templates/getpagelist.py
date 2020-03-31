from appiumDemo.jinjaDemo.templates import tools1

# yamlpage = tools1.parseyaml()


def get_page_list(yamlpage):
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        locs = names['locators']
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object



