%# Template para fazer uma tabela HTML a partir de uma tupla result
% include('menu.tpl')

% p = pao[0]
<h1>{{p[0]}}</h1>
<h2>{{p[1]}}</h2>
{{p[2]}} <br><br>
Peso : {{p[3]}} g     <br> <br>
Preco: R$ {{p[4]}},00 <br> <br>
<table border="1">
%for p in pao:
    <tr>
    %for col in p:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>               <br>    

% include('pe.tpl')