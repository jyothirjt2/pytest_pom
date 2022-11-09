import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getapplicationURL():
        url = config.get("common info" , "baseURL")
        return url

    @staticmethod
    def getusername():
        useremail = config.get("common info","username")
        return useremail

    @staticmethod
    def getpassword():
        password = config.get("common info","password")
        return password

