class WashingMachineMode:
    def __init__(self, powder_supply, drum_speed, powder_amount, temprature):
        self.powder_supply = powder_supply
        self.drum_speed = drum_speed
        self.powder_amount = powder_amount
        self.temprature = temprature

    def washing_time(self):
        return self.powder_amount // self.powder_supply

class RegularMode(WashingMachineMode):
    def __init__(self):
        return super().__init__(2, 1000, 200, 40)
    def washing_time(self):
        return super().washing_time()

class IntensiveMode(WashingMachineMode):
    def __init__(self):
        return super().__init__(5, 2000, 200, 50)
    def washing_time(self):
        return super().washing_time()

class SensitiveMode(WashingMachineMode):
    def __init__(self):
        return super().__init__(1, 800, 150, 30)
    def washing_time(self):
        return super().washing_time()


def avarage_temperature():
    return (RegularMode().temprature + IntensiveMode().temprature + SensitiveMode().temprature) // 3


print('Время обычной стирки', RegularMode().washing_time(), 'минут')
print('Время интенсивной стирки', IntensiveMode().washing_time(), 'минут')
print('Время деликатной стирки', SensitiveMode().washing_time(), 'минут')
print('Средняя температура трёх стирок', avarage_temperature(), 'градусов по Цельсию')
