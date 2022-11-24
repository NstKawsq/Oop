from cont import *

def test_container_in():
    temp=cont()
    assert temp.input('in_1.txt')==5

def test_container_out():
    temp=cont()
    temp.input('in_1.txt')
    temp.out('test_out.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostOop\test_out.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostOop\standart_test_out.txt', encoding='utf-8').read()
    assert flag == True


def test_mark_count():
    temp = cont()
    temp.input('in_mark_count.txt')
    assert temp.mark_count()==2

def test_sort():
    temp = cont()
    temp.input('in_sort.txt')
    temp.sort()
    temp.out('test_sort.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostOop\test_sort.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostOop\standart_sort.txt', encoding='utf-8').read()
    assert flag == True


def test_filter():
    temp = cont()
    temp.input('in_filter.txt')
    temp.filtered_output_by_quotation('test_filter.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostOop\test_filter.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostOop\standart_filter.txt', encoding='utf-8').read()
    assert flag == True


def test_clear():
    temp = cont()
    temp.input('in_filter.txt')
    temp.clear()
    temp.out('test_clear.txt')
    flag = open(r'D:\pythonProject\timp\labMudrostOop\test_clear.txt', encoding='utf-8').read() == open(
        r'D:\pythonProject\timp\labMudrostOop\standart_clear.txt', encoding='utf-8').read()
    assert flag == True


