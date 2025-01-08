Задача "Потоки гостей в кафе":
import random
from threading import Thread
from time import sleep
from queue import Queue


class Table():
    '''Класс столов для помещений'''
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    '''Класс гостя имитирующее действие'''
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # sleep(random.randint(3, 10))
        pause =  random.randint(3, 10)
        sleep(pause)

class Cafe:
    ''' Класс кафе с гостями и столами '''
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        '''Функция заполняет пустые столы и создает очередь из гостей'''
        for i in range(0,len(self.tables)):
            if self.tables[i].guest==None:
               self.tables[i].guest=guests[i]
               thread = guests[i]
               thread.start()
               print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')

        for i in range(len(self.tables), len(guests)):
            self.queue.put(guests[i])
            print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        '''Функция симулирует процесс обслуживания гостей'''
        while not (self.queue.empty()) or not all_table_empty:
            all_table_empty = True

            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread = table.guest
                    thread.start()

                if table.guest is not None:
                    all_table_empty = False

def main():
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

if __name__ == '__main__':
    main()
