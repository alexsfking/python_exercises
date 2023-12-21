class Mobile:
    def __init__(self, number):
        self.number = number
        
    def turn_on(self):
        print(f'mobile phone {self.number} is turned on')
    
    def turn_off(self):
        print('mobile phone is turned off')
    
    def call(self, number):
        print(f'calling {number}')
        
        
mobile1 = Mobile("01632-960004")
mobile2 = Mobile("01632-960012")
mobile1.turn_on()
mobile2.turn_on()
mobile1.call("555-34343")
mobile1.turn_off()
mobile2.turn_off()