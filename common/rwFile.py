import json
import configparser
import yaml
from config import configPath


class ReadConfig:
    def __init__(self):
        self.config_path = configPath.CONFIGDATA_PATH
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, encoding='utf-8')

    # QQ邮箱配置
    @classmethod
    def get_email(cls, value):
        value = ReadConfig().config.get('email', value)
        return value

    # Mysql配置
    @classmethod
    def get_db(cls, value):
        value = ReadConfig().config.get('mysql', value)
        return value


class ReadYaml:
    def __init__(self):
        self.file_data = configPath.YAML_PATH

    # 读取 yaml文件
    def readYaml(self):
        file = self.file_data
        with open(file, mode='r', encoding='utf-8') as f:
            yamlData = yaml.safe_load(f)  # 单文件读取
            # yamlData = list(yaml.load_all(f,Loader=yaml.FullLoader))  # 多文件读取 返回生成器
            return yamlData

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
        with open(file, mode='w', encoding='utf-8') as f:
            yaml.dump(desired_caps, f, Dumper=yaml.RoundTripDumper)

class ReadJson:
    def __init__(self):
        self.file_data = configPath.JSON_PATH

    # 读取json文件
    def readJson(self):
        file = self.file_data
        with open(file, mode='r') as f:
            jsonData = f.read()
            dictData = json.loads(jsonData)
            return dictData

