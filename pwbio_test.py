from pywebio.input import input,TEXT,NUMBER
from pywebio.output import put_text
from pywebio import start_server

def test():
    a=input('Формативки через пробел', type=TEXT)
    b=input('СОРы через пробел', type=TEXT)
    cc=input('Максимальные баллы за СОРы через пробел', type=TEXT)
    d=input('Максимальный балл по СОЧ', type=NUMBER)
    x=list(map(int,a.split()))
    y=list(map(int,b.split()))
    z=list(map(int,cc.split()))
    ans=(sum(x)+sum(y))/(sum(z)+len(x)*10)*100
    put_text('У вас '+str(ans)+'%')
    put_text('Для 5 вам нужно набрать '+str(round((0.845-ans/200)*2*d,1)))
    put_text('Для 4 вам нужно набрать '+str(round((0.645-ans/200)*2*d,1)))
    
    
if __name__=='__main__':
    start_server(test, port=80)
    
