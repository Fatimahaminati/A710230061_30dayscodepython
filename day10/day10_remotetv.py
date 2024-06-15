class RemoteTv():
    def __init__(self):
        self.switchIsOn = False
        self.volume = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def volumeUp(self):
        if self.volume < 10:
            self.volume = self.volume + 1

    def volumeDown(self):
        if self.volume > 0:
            self.volume = self.volume - 1

    def show(self):
        print('Switch is on ?', self.switchIsOn)
        print('volume is:', self.volume)

remoteSatu = RemoteTv()
remoteSatu.turnOn()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.show()
remoteSatu.volumeDown()
remoteSatu.volumeDown()
remoteSatu.turnOff()
remoteSatu.show()