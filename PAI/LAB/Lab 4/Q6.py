class Computer_resource_manager():
    def __init__(self,CPU_usage:int,Ram_usage:int,Battery:int):
        self.CPU_usage = CPU_usage
        self.Ram_usage = Ram_usage
        self.Battery = Battery
    def Check_status(self):
        if(self.CPU_usage > 80):
            print("Heavy CPU load\n")
        if(self.Ram_usage > 85):
            print("High memory usage\n")
        if(self.Battery <20):
            print("Low Battery\n")
comp1 = Computer_resource_manager(85,24,15)
comp2 = Computer_resource_manager(25,90,15)
print("First comp")
comp1.Check_status()
print("Second comp")
comp2.Check_status()