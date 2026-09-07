import abc
class Robot(abc.ABC):
    def __init__(self,name,battery):
        self._name = name
        self._battery = battery
    def charge(self):
        print("Charging Robot "+self._name)
        self._battery = 100
    @abc.abstractmethod
    def move(self):
        pass
class DeliveryRobot(Robot):
    def move(self):
        if self._battery >20:
            print("Moving Robot to delivery location "+self._name)
            self._battery -= 30
        else:
            print("cannot move not enough battery")
class SecurityRobot(Robot):
    def move(self):
        if self._battery >20:
            print("Moving Robot to security location "+self._name)
            self._battery -= 30
        else:
            print("cannot move not enough battery")
class RescueRobot(Robot):
    def move(self):
        if self._battery >20:
            print("Moving Robot to rescue location "+self._name)
            self._battery -=30
        else:
            print("cannot move not enough battery")
devrobot = DeliveryRobot("devrobot" , 30)
devrobot.move()
secrobot = SecurityRobot("secrobot" , 10)
secrobot.move()
rescuerobot = RescueRobot("rescuerobot" , 20)
rescuerobot.move()
devrobot.charge()
secrobot.charge()
rescuerobot.charge()
devrobot.move()
secrobot.move()
rescuerobot.move()