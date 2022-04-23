import configparser
import os

config = configparser.RawConfigParser()
project_file = os.path.abspath(os.path.join(__file__,'..','..'))
config_file = os.path.join(project_file,'Configurasions','config.ini')
config.read(config_file)

class ReadConfig:

    @staticmethod
    def URL():
        url = config.get('common data','baseURL')
        return url

    @staticmethod
    def Login_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def Login_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def Excel_file_path():
        file = os.path.abspath(os.path.join(__file__, '..', '..'))
        excel_file= os.path.join(file,'TestData','LoginData.xlsx')
        return excel_file



