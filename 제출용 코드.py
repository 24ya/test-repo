#5-3
import random

class Player():
    def __init__(self,name):
        self.name=name
        self.balance=3000
        self.area=0

    def move(self,dice):
        self.area+=dice
        if self.area>9:
            self.area-=10

    def pay_money(self):
        self.balance-=600

    def buy(self):
        self.balance-=300

    def earn_money(self):
        self.balance+=600
    def check_balance(self):
        return self.balance
    def check_area(self):
        return self.area
    def check_name(self):
        return self.name
    def __str__(self):
        return str(self.name)


class City():
    def __init__(self,n,name):
        self.name=name
        self.status=0
        self.area=n
        self.owner_name='empty'
    def owner(self,player):
        self.owner_name='%s'%player
        self.name=self.name+'(%s)'%player
        self.status=1
    def check_owner_name(self):
        return self.owner_name
    def check_area(self):
        return str(self.area)
    def check_status(self):
        return self.status
    def __str__(self):
        return str(self.name)

p1=Player('Saya')
p2=Player('Python')
c1=City(1,'Seoul')
c2=City(2,'Tokyo')
c3=City(3,'Sydney')
c4=City(4,'LA')
c5=City(5,'Cairo')
c6=City(6,'Phuket')
c7=City(7,'New delhi')
c8=City(8,'Hanoi')
c9=City(9,'Paris')

turn=0
winner=''

def Game(p1,p2):
    global winner
    dice = random.randint(1, 6)
    p1.move(dice)
    p_position = str(p1.check_area())
    print(p1, ':', dice)
    if p_position=='0':
        print('Start Point')
    else:
        for i in range(1, 10):
            if p_position == eval('c' + '%d' % i).check_area():
                if eval('c' + '%d' % i).check_status() == 0:
                    print(eval('c' + '%d' % i),'(empty)',sep='')
                    if p1.check_balance() < 300:
                        print('Can\'t buy %s'%eval('c' + '%d' % i))
                        break
                    else:
                        eval('c' + '%d' % i).owner(p1)
                        p1.buy()
                        break
                elif eval('c' + '%d' % i).check_owner_name() == p1.check_name():
                    print(eval('c' + '%d' % i))
                    break
                elif eval('c' + '%d' % i).check_owner_name() == p2.check_name():
                    print(eval('c' + '%d' % i))
                    if p1.check_balance() < 600:
                        p1.pay_money()
                        p2.earn_money()
                        winner = '%s' % p2
                        break
                    else:
                        p1.pay_money()
                        p2.earn_money()
                        break
    print('%s\'s balance is %d'%(p1,p1.check_balance()))

def BoardPrint():
    print('=' * 300)
    for i in range(0, 10):
        if i == 0:
            print('Start Point', end='        ')
        else:
            print(eval('c' + '%s' % i), end='        ')
    print()
    for i in range(0, 10):
        if i == 0:
            if p1.check_area() == i or p2.check_area() == i:
                space = len('Start Point')
                if p1.check_area() == i:
                    print(p1.check_name(), end='')
                    space -= len(p1.check_name())
                if p2.check_area() == i:
                    print(p2.check_name(), end='')
                    space -= len(p2.check_name())
                if space > 0:
                    print(' ' * space, end='')
            else:
                print(' ' * len('Start point'), end='')

        else:
            if p1.check_area() == i or p2.check_area() == i:
                space = len(str(eval('c' + '%s' % i)))
                if p1.check_area() == i:
                    print(p1.check_name(), end='')
                    space -= len(p1.check_name())
                if p2.check_area() == i:
                    print(p2.check_name(), end='')
                    space -= len(p2.check_name())
                if space > 0:
                    print(' ' * space, end='')
            else:
                print(' ' * len(str(eval('c' + '%s' % i))), end='')
        print('        ', end='')
    print()
    print('='*300)

while turn<30 and winner=='':
    turn+=1
    print('Turn %d'%turn)
    Game(p1,p2)
    print('...........................')
    Game(p2,p1)
    print('\n\n')
    BoardPrint()
    print('\n\n')

print('Final Result\n%s\'s balance is %d\n%s\'s balance is %d\n'%(p1,p1.check_balance(),p2,p2.check_balance()))

if winner=='':
    if p1.check_balance()>p2.check_balance():
        winner = '%s' % p1
        print('The winner is %s!' % winner)
    elif p1.check_balance()<p2.check_balance():
        winner = '%s' % p2
        print('The winner is %s!' % winner)
    else:
        print('WOW! Draw!')
else:
    print('The winner is %s!'%winner)