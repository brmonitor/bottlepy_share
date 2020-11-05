%# Template para fazer uma tabela HTML a partir de uma tupla result
<h1>Pães</h1>
<table border="1">
%for p in paes:
    <tr>
    %for col in p:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
