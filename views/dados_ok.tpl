% include('menu.tpl')

%nome, celular, endereco, complemento, referencia, obs = result[0:6]
%print(nome, celular, endereco, complemento, referencia, obs)

<h1>Meus dados</h1>

<p> *** Seja bem-vindo {{nome.split()[0]}} ***</p>

Nome : {{nome}} <br>
Celular :  {{celular}} <br>

<br>

Endereco :  {{endereco}} <br>
Complemento :  {{complemento}} <br>
Pontos de referencia :  {{referencia}} <br>
Observacoes :  {{obs}} <br>

 <br>   

% include('pe.tpl')
