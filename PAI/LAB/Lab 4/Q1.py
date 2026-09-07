class System:
    name: str
    ipaddress: str
    threat: str
    def __init__(self,name:str, ipaddress:str, threat:str):
        self.name = name
        self.ipaddress = ipaddress
        self.threat = threat
    def scan(self):
        if self.threat.lower() == 'low':
            print("System Safe")
        elif self.threat.lower() == 'medium':
            print("Suspicious Activity")
        elif self.threat.lower() == 'high':
            print("Critical threat Detected")
        else:
            print("Invalid")
sys1 = System('python', '127.0.0.1', 'low')
sys2 = System('python', '127.0.0.1', 'medium')
sys3 = System('python', '127.0.0.1', 'high')
sys1.scan()
sys2.scan()
sys3.scan()