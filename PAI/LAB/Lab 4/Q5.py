import abc
class Agent(abc.ABC):
    @abc.abstractmethod
    def perform_task(self):
        pass
class SecurityAgent(Agent):
    def perform_task(self):
        print("Detecting cyber threat\n")
class MonitoringAgent(Agent):
    def perform_task(self):
        print("Monitoring security alert\n")
class RecoveryAgent(Agent):
    def perform_task(self):
        print("Recoverin system service\n")
Sagent = SecurityAgent()
Magent = MonitoringAgent()
Ragent = RecoveryAgent()
Sagent.perform_task()
Magent.perform_task()
Ragent.perform_task()