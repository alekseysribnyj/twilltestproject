{%if CustomErrors%}{%for error in CustomErrors%}<font color="red">{{error}}</font><br>{%endfor%}{%endif%}
<form name="LoginForm" method="POST" action="{{abslturl}}/login/">
{{ form.as_p }}
<input type="submit" value="Login"/>
</form>

