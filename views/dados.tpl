% include('menu.tpl')
<h1>Meus dados</h1>
<h2>No momento, somente clientes previamente cadastrados podem por produtos na sua cesta pelo site </h2>

<form action="/checa_login" method="post">
    Celular :   <br> <input name="id" type="text" /> <br><br>
    Senha :     <br> <input name="senha" type="password" />  <br>
                <br> <input value="ok" type="submit" />  
</form>          
 
<p>{{msg}}</p>

% include('pe.tpl')