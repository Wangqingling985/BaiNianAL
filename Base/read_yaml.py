import yaml,os

class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+'Data'+os.sep+filename
    def read_yaml(self):
        with open(self.filepath,'r',encoding='utf-8')as f:
            return yaml.load(f)
    def read_yaml02(self):
        with open('../Data/login.yaml','r',encoding='utf-8')as f:
            return yaml.load(f)

    def read_yaml03(self):
        with open('../Data/address.yaml', 'r', encoding='utf-8')as f:
            return yaml.load(f)


if __name__=='__main__':

# 登录数据
    datas=ReadYaml('login.yaml').read_yaml02()
    print(datas)
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect"), data.get("toast_expect")))
    print(arrs)


# 增加地址数据
    datas=ReadYaml("address.yaml").read_yaml03()
    data=datas.get("add_address").values()
    print(data)
    arrs=[]
    for data in datas.get('add_address').values():
        arrs.append((data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"), data.get("address"), data.get("postcode")))
    print(arrs)

# 修改地址数据
    datas = ReadYaml("address.yaml").read_yaml03()
    data=datas.get("updata_address").values()
    print(data)
    arrs1=[]
    for data in datas.get('updata_address').values():
        arrs.append((data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"), data.get("address"), data.get("postcode"), data.get("toast_expect")))
    print(arrs)





