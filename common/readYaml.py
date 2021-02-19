# pip install ruamel.yaml
# pip install pyyaml
import yaml
from common import configpath
file_data = configpath.yaml_path


class ReadYaml:
    def __init__(self):
        self.file_data = file_data

    # 读取 yaml文件
    def readYaml(self):
        file = self.file_data
        yamldata=[]
        with open(file,mode='r',encoding='utf-8') as f:
            yamlData = yaml.load_all(f,Loader=yaml.FullLoader)
            for i in yamlData:
                print(i)
                yamldata.append(i)
            return yamldata

    # 写入 yaml文件
    def writeYaml(self):
        from ruamel import yaml
        file = self.file_data
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'A5RNW18316011440',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'automationName': 'UiAutomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }
        with open(file,mode='w',encoding='utf-8') as f:
            yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)

if __name__ == '__main__':
    y = ReadYaml()
    yamldata = y.readYaml()
    print(yamldata[0][1]['test2'])


