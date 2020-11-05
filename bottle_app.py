# A very simple Bottle Hello World app for you to get started with...
from bottle import route, run, template, static_file, get, post, request
from sqlite3 import connect
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "josi.db")


@route('/')
def static_page2():
    #print('panfleto2 :')
    return template('panfleto2')

    
@route('/Ola/<name>')
def greet(name='Stranger'):
    print('name :', name)
    return template('Ola {{name}}, como vai voce?', name=name)    
    
    
def DB_Select(sel):
    conn = connect(db_path)
    c = conn.cursor()
    c.execute(sel)
    result = c.fetchall()
    c.close()
    return result 
    
@route('/ecobio')
def ecobio():    
    result = DB_Select("SELECT * from ELinha")
    for t in result:
        print(t)
    if result:
        return str(result)
    return HTTPError(404, "Pagina nao encontrada")
    
@route('/delicias')
def delicias():    
    result = DB_Select("SELECT * from tipo_comida")
    for i in result:
        print(i)
    if result:
        return str(result)
    return HTTPError(404, "Pagina nao encontrada") 
    
@route('/paes')
def paes():
    result = DB_Select("SELECT nome,destaque,peso,preco from FOODs where tipo ='P'")
    output = template('tabela_paes', paes=result)
    return output

@route('/paes/<cod>')
def pao(cod):
    result = DB_Select(f"SELECT nome,destaque,ingredientes,peso,preco from FOODs where cod_item ='{cod}'")
    for i in result:
        print('oi ', i)
        print(f'R$ {i}')
    output = template('pao', pao=result)
    return output	


@route('/sobre')
def sobre():
    return template('sobre')

#static

# seguindo este video : Serving Static Files in Bottle Py     https://www.youtube.com/watch?v=sb346d3iKBk
@route('/static/<filepath:path>')
def server_static(filepath):
    static_raiz = os.path.join(BASE_DIR, "static")
    #print(filepath)
    #print(static_raiz)
    return static_file(filepath, root=static_raiz)
    
@route('/i/<filename>')
def static_image(filename):
    #print(filename)
    return static_file(filename, root='static/images')

@route('/panfleto')
def static_page():
    #print('panfleto :')
    return template('panfleto')

@get('/dados')
def login():
    return template('dados',msg='')

@post('/checa_login')
def checa_login():
    id = request.forms.get('id')
    senha = request.forms.get('senha')
    #print('forms : ', request.forms)
    #print('id : ', id)
    #print('senha : ', senha)
    result = DB_Select(f"SELECT nome,celular, endereco, complemento, referencia, obs from Clientes where celular = {id} and pass ='{senha}'")
    #print('result : ', result)
    if result == []:    # nao encontrou
        m = '*** Infelizmente celular errado ou senha errada ou cliente ainda nao cadastrado ***'
        return template('dados',msg=m)
    else:
        return template('dados_ok', result=result[0])
   

run(host='localhost', port=8080, debug=True, reloader=True)
