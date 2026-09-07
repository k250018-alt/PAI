class Vault:
    def __init__(self,username:str,vault_status:str,password:str):
        self.username = username
        self._vault_status = vault_status
        self.__password = password
    def change_password(self,password:str):
        if password != self.__password:
            self.__password = password
        else:
            print("same password")
    def verify(self,password:str):
        if self.__password == password:
            print("Access granted")
            return True
        else:
            print("Access denied")
            return False
    def check_vault(self,password:str):
        if self.verify(password):
            print("Vault status : ",self._vault_status)
vlt = Vault("Vault Username","Vault Password","")
vlt.change_password("<PASSWORD>")
vlt.check_vault("<PASSWORD>")