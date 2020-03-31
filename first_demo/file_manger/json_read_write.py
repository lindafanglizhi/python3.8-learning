import json
# with open('data.json', 'r') as f:
#     mytxt = f.read()
#     print(mytxt)
#     txt_dict = json.loads(mytxt)
#     print(txt_dict)
#     print(type(txt_dict))
#     print(txt_dict['name'])
#     json_str = json.dumps(txt_dict)
#     print(json_str)

dict_new ={
    'name':'tom',
    'age':88
}
# with open('data.json', 'r') as f:
#     dict_1=json.load(f)
#     print(dict_1)
#     f.close()


with open('data.json', 'a') as fa:
    json.dump(dict_new,fa)
    fa.close()
