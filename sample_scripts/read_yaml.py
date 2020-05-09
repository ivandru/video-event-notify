# pip3 install pyyaml
import yaml

yaml_file_path = './example.yaml'

with open(yaml_file_path, 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)