from time import time
import csv
import os.path
import pandas as pd

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class Llist:
    def __init__(self, capacity = None): # None потому что clean придется переделывать, а я не хочу))))
        '''Инициализация круговоро буфера. Принимает значение capacity как максимальное и текущее.'''
        self.capacity = self.oldcapacity = capacity
        self.front = None
        self.back = None
    #@timer_func
    def resize(self, newsize):
        '''Изменение размеров кругового буфера. Принимает значение newsize как новое максимальное значение'''
        if newsize > self.oldcapacity:
            diff = newsize - self.oldcapacity # разница между старым и новым размером
            self.capacity += diff # расширение размера до нового
            self.oldcapacity = newsize

        if newsize < self.oldcapacity:
            if self.capacity == 0: # если массив полон - удалить столько значений, насколько новое значение меньше старого
                diff = self.oldcapacity - newsize
                for i in range(diff):
                    Llist.delete(self)
                self.capacity = 0 # места нет
                self.oldcapacity = newsize

            if self.capacity == self.oldcapacity: # массив пуст
                self.oldcapacity = newsize
                self.capacity = self.oldcapacity

            if newsize < self.oldcapacity - self.capacity:
                diff = self.oldcapacity - newsize - self.capacity
                for i in range(diff):
                    Llist.delete(self)
                self.oldcapacity = newsize
                self.capacity = 0

            if newsize == self.oldcapacity - self.capacity:
                self.oldcapacity = newsize
                self.capacity = 0


            if newsize > self.oldcapacity - self.capacity:
                self.capacity = self.capacity - self.oldcapacity + newsize
                self.oldcapacity = newsize
    #@timer_func
    def add(self, node):
        '''Добавление нового элемента кругового буфера. Класс Node принимает значение node и задает стандартные параметры'''
        if self.capacity == 0:
            self.front = self.front.next
            curnode = Node(node, None)
            self.back.next = curnode
            self.back = curnode

        else:
            if self.front == None:
                self.front = Node(node, None)
                self.back = self.front

            elif self.back == self.front:
                self.back = Node(node, None)
                self.front.next = self.back

            else:
                curnode = Node(node, None)
                self.back.next = curnode
                self.back = curnode

            self.capacity -= 1 # заполняем конечный массив

        self.back.next = self.front # связь мужду первым и последним элементом
        #print(self.back.next.value)
    #@timer_func
    def delete(self):
        '''Удаление элемента кругового буфера. Удаляется самый старый элемент буфера.'''
        if self.front != self.back:
            self.front = self.front.next
            self.back.next = self.front
            self.capacity += 1
        else:
            self.capacity += 1
            self.clean()

    #@timer_func
    def get(self, index):
        '''Получение значения элемента кругово буфера по индексу (index).'''
        if index == -1:
            return self.back.value
        if self.front != None:
            counter = 0
            curnode = self.front
            while counter != index:
                curnode = curnode.next
                counter += 1
            return curnode.value
    #@timer_func
    def set(self, index, value):
        '''Изменение значения элемента кругового буфера по индексу (index) и значению (value).'''
        if index == -1:
            self.back.value = value
            return
        if self.front != None:
            counter = 0
            curnode = self.front
            while counter != index:
                curnode = curnode.next
                counter += 1
            curnode.value = value

    def __str__(self):
        '''Вывод массива в терминал в понятном виде.'''
        if self.front != None:
            curnode = self.front
            answer = str(curnode.value) + ' '
            while curnode.next != self.front:
                curnode = curnode.next
                answer += str(curnode.value) + ' '
            return answer
        return 'Массив пуст'

    def clean(self):
        '''Полная очистка буфера.'''
        self.__init__(self.oldcapacity)

@timer_func
def addfunc(dataset):
    with open(dataset, 'r', newline='') as csvfile:
        list_ = Llist(len(pd.read_csv(dataset)))
        for i in csvfile:
            list_.add(i)
    return list_

@timer_func
def getfunc(dataset):
    with open(dataset, 'r', newline='') as csvfile:
        for i in csvfile:
            list_.get(int(i))

@timer_func
def setfunc(dataset):
    with open(dataset, 'r', newline='') as csvfile:
        for i in csvfile:
            list_.set(int(i), int(i))

@timer_func
def resizefunc(dataset):
    with open(dataset, 'r', newline='') as csvfile:
        for i in csvfile:
            list_.resize(int(i))

@timer_func
def deletefunc(dataset):
    with open(dataset, 'r', newline='') as csvfile:
        for i in csvfile:
            list_.delete()



if __name__ == '__main__':
    list_ = addfunc('add/dataset.csv')
    for i in range(10):
        pass
        #list_ = addfunc('data/add/dataset5_step.csv')
        #getfunc('get/dataset_step.csv')
        #setfunc('set/dataset_step.csv')
        #resizefunc('resize/dataset_step.csv')
        #deletefunc('add/dataset_step.csv')
    
