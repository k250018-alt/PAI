class SecuritySystem:
    def respond(self):
        pass
class Firewall(SecuritySystem):
    def respond(self):
        print("Block suspicious network traffic")
class Antivirus(SecuritySystem):
    def respond(self):
        print("Isolate malicious Files")
class IntrusionDetection(SecuritySystem):
    def respond(self):
        print("Generate security alert")
firewall = Firewall()
antivirus = Antivirus()
intrusion_detection = IntrusionDetection()
firewall.respond()
antivirus.respond()
intrusion_detection.respond()