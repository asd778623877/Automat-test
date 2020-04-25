import os
import yaml
def ret_yaml_date(file_name):
    file_path=os.getcwd() + os.sep + "Data" + os.sep + file_name + ".yml"
    with open(file_path,"r",encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    data = ret_yaml_date("search_date").get("search_date")
    set_data_list = []
    for i in data.keys():
        set_data_list.append((i, data.get(i).get("test")))
    print(set_data_list)