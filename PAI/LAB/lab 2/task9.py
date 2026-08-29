app_name = input("Enter your app name: ")
version = input("Enter your version: ")
supported_env = input("Enter your supported environment: ")
data_base_config = input("Enter your data base config: ")
app = (app_name, version, supported_env, data_base_config)
print(app)
#this is preferable because tuple is immutable hence data can not be changed added or removed after creation 