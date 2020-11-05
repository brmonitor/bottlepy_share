% include('menu.tpl')

<form action="/checa_login" method="post">
Nome : <input name="nome" type="text" /> <br>
Celular : <input name="celular" type="text" />  
Whatsapp : <input name="Whatsapp" type="checkbox" /> 

<br>

Endereco : <input name="endereco" type="text" />  <br>
Complemento : <input name="complemento" type="text" />  <br>
Pontos de referencia : <input name="referencia" type="text" />  <br>
Observacoes : <input name="observacoes" type="text" /> 

<input value="Login" type="submit" />
</form>            <br>   
 
<p>{{msg}}</p>

% include('pe.tpl')
