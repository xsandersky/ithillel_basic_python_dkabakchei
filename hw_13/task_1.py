class Godzilla:
    def __init__(self, stomach_volume):
        self.stomach_volume = stomach_volume
        self.stomach_contain = 0


    def eat(self, volume_human):
        if  self.stomach_contain + volume_human <= self.stomach_volume:
            self.stomach_contain += volume_human

            print(f'Годзилла с объемом желудка {self.stomach_volume} съела человека объемом {volume_human}')
            if self.stomach_contain > self.stomach_volume * 0.9:
                print('Годзилла наелся и больше не может есть людей')

        else:
            print('Годзилла не может съесть данного человека из-за недостатка места в желудке')


if __name__=='__main__':
    a = Godzilla(1000)
    a.eat(950)
    b = Godzilla(1500)
    b.eat(1450)

