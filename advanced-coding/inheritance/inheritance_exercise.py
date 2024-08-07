class MobilePhone:
    def __init__(self, screentype, networktype, dualsim, fcamera, rcamera, ram, storage):
        self.screenType = screentype
        self.networkType = networktype
        self.dualSim = dualsim
        self.frontCamera = fcamera
        self.rearCamera = rcamera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print(f"Making a call using my {self.__class__.__name__} with {self.networkType} network")

    def receive_call(self):
        print(f"Receiving a call using my {self.__class__.__name__} with {self.networkType} network")

    def take_pic(self):
        print(f"Taking a selfie with my {self.__class__.__name__} using the {self.frontCamera} front camera")


class Apple(MobilePhone):
    def __init__(self, screentype, networktype, dualsim, fcamera, rcamera, ram, storage, facetime, faceunlock):
        MobilePhone.__init__(self, screentype, networktype, dualsim, fcamera, rcamera, ram, storage)
        self.facetime = facetime
        self.faceunlock = faceunlock


class Samsung(MobilePhone):
    def __init__(self, screentype, networktype, dualsim, fcamera, rcamera, ram, storage, backlight):
        MobilePhone.__init__(self, screentype, networktype, dualsim, fcamera, rcamera, ram, storage)
        self.backlight = backlight


apple = Apple('Touch Screen', '5G', "No", '12MP', '48MP', '4GB', '64GB', 'Yes', 'Yes')
samsung = Samsung('Touch Screen', '4G', "Yes", '8MP', '32MP', '3GB', '32GB', 'Yes')

apple.make_call()
samsung.receive_call()
apple.take_pic()
samsung.take_pic()
