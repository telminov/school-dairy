#! /usr/bin/python
# encoding: utf-8
import random
while True:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        result = raw_input("%s x %s = " % (a, b))
        result = int(result)

        rigth_result = a * b
        if rigth_result == result:
            print 'Верно!'
        else:
            print 'Не верно... :( Правильный ответ "%s"' % rigth_result
        
    except ValueError:
        print u'Не правильное значение "%s". Ожидается число.' % result
