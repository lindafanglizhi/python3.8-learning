import yaml

with open("data.yaml","r") as f:
    data_yaml =f.read()
    data =yaml.load(data_yaml)
    print(data[0])

