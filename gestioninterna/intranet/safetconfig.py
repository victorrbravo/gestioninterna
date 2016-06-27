#-*- coding: utf-8 -*-

# websafet
# archivo para normalizacion de directorios y rutas URL utilizadas en websafet


SERVER_URL        =  u"http://localhost/intranet"
LOGIN_URL         =  u"http://localhost//intranet/login"
TEMPLATES_PATH    =  u"/var/www/media/templates"
TEMPLATES_URL     =  u"http://localhost/media/templates/"
HOMESAFET_PATH    =  u"/home/debian"
MEDIA_PATH        =  u"/var/www/media"
MEDIA_URL         =  u"http://localhost/media"

TEMPLATES = (
	TEMPLATES_PATH + u'/' + u'index.html',
	TEMPLATES_PATH + u'/' + u'consoperations.html',
	TEMPLATES_PATH + u'/' + u'resultgeneration.html',
	TEMPLATES_PATH + u'/' + u'listgeneration.html',
	TEMPLATES_PATH + u'/' + u'safetsimple.html',
	TEMPLATES_PATH + u'/' + u'formoperations.html',
	TEMPLATES_PATH + u'/' + u'formgeneration.html',
	TEMPLATES_PATH + u'/' + u'consgeneration.html',
	TEMPLATES_PATH + u'/' + u'resultgeneration.html',
	TEMPLATES_PATH + u'/' + u'login.html',
	TEMPLATES_PATH + u'/' + u'credits.html',
	TEMPLATES_PATH + u'/' + u'menusimple.html', #11
	TEMPLATES_PATH + u'/' + u'listgenerationc.html',#12
	TEMPLATES_PATH + u'/' + u'plugintemplate.html', #13
	TEMPLATES_PATH + u'/' + u'register.html', #14
	TEMPLATES_PATH + u'/' + u'resultgenerationm.html', #15
	TEMPLATES_PATH + u'/' + u'listgenerationg.html', #16
)

JS_SAFETPROCESSCONSOLE_HEAD = u"""
<style type="text/css">
.svgdiv { border: 1px solid #3c8243; }
#svgintro { float: right; width: 150px; height: 150px; margin-right: 30px; background: #fff; border: 1px solid #3c8243; }
.svgsample { float: left; width: 46%; margin: 1%; overflow: scroll; border: 1px solid #3c8243; padding: 5px; }
.drawOpt { float: left; width: 25%; }
.row { clear: both; }
#showMods { padding: 0em 0.25em; background-color: #ddffe8; color: #000; border: 1px solid #3c8243; font-size: 80%; text-decoration: none; cursor: pointer; }
#domMods { display: none; padding: 0em 1em 0.5em; background-color: #ddffe8; border: 1px solid #3c8243; }
</style>
<script type="text/javascript" src="http://localhost/media/jquery-latest.js"></script> 
<!-- <script type="text/javascript" language="javascript" src="http://localhost/media/js/DataTables/media/js/jquery.js"></script> -->
<script type="text/javascript" language="javascript" src="http://localhost/media/js/DataTables/media/js/jquery.dataTables.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svg.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.debug.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svggraph.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgplot.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svganim.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgdom.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgfilter.js"></script>
<link type="text/css" href="http://localhost/media/jquery.svg.css" rel="Stylesheet" />
<!--		<style type="text/css" title="currentStyle">
			@import "http://localhost/media/js/DataTables/media/css/demo_page.css";
			@import "http://localhost/media/js/DataTables/media/css/demo_table.css";
		</style> -->

<script type="text/javascript">
var g = null;
var currheight = 100;
var currwidth = 100;
   $(document).ready(function() {
$.post('http://localhost/intranet/viewtable' ,{},
function(data) {
//alert(data);
var myjson = null;
myjson = eval("myjson = "+data);
//alert("Hola");
//			$('#dynamic').html( '<table cellpadding="0" cellspacing="0" border="0" class="display" name="example" id="example"></table>' );
		var oTable =	$('#example').dataTable( {
				"aaData": myjson.tasks,
				"aoColumns": myjson.columns,
				"bPaginate": false,
			        "fnFooterCallback": function ( nRow, aaData, iStart, iEnd, aiDisplay ) {
			            var totalp = 0.0;
				    var totalf = 0.0;
			//		alert(aaData[0].length);
				    if  ( aaData[0].length <= 6 ) {
						return;
					}
			            for ( var i=0 ; i<aaData.length ; i++ ) {
					var n = aaData[i][6];
					var f = aaData[i][7];
					if ( n.indexOf("%")>= 0 ) {
						n = n.substr(0,n.indexOf("%"));
        			        	totalp += parseFloat(n);
					}
					if ( f.indexOf("%")>= 0 ) {
						f = f.substr(0,f.indexOf("%"));
        			        	totalf += parseFloat(f);
					}

	            		     }
					 document.getElementById('tbfooter').innerHTML = "<p align=right>Porcentaje (Tareas realizadas): <b>"+totalp+"%</b><br/>"
						+"Porcentaje (Tareas faltantes):<b>"+totalf+"%</b></p>";
//					alert(totalp);
//					var nCells = nRow.getElementsByTagName('th');
//			                nCells[1].innerHTML = "Total:" + parseInt(totalp); 
			          }
                               });	
});


"""

JS_SAFETPROCESSCONSOLE_FUNCTIONS = u"""
    var svg = $('#svgload').svg('get');

    resetSize(svg,'100%','200%');

 $('#buttonwplus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonhplus').click(graphHPlus);

 $('#buttonwminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth - 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonwhminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth - 10;
        currheight = currheight - 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonwhplus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth + 10;
        currheight = currheight + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });

 $('#buttonhminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight - 10;
//        $(g).animate({svgViewBox: 
//    '        150, 87, 300, 175'}, 2000);
//        $(g).animate({svgWidth: 100, svgHeight: 100},2000);
//         var myrect = svg.rect(25, 25, 150, '25%', 10, 10, 
//          {fill: 'none', stroke: 'blue', strokeWidth: 3, 
//                   transform: 'rotate(0, 100, 75)'}); 
        resetSize(svg,currwidth+'%',currheight+'%');
//        $(g).animate({svgWidth: 100, svgHeight: 100},2000);
        });

function  graphHPlus () {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        }

function  graphHPlusFactor(factor) {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight + 10*factor;
        resetSize(svg,currwidth+'%',currheight+'%');
        }

function resetSize(svg, width, height) {
        svg.configure({width: width || $(svg._container).width(),
                height: height || $(svg._container).height()});
}



  });

function jsSaveGraph(myhosturl) {
var nombregrafo = prompt ("Nombre del grafo:","");
$.post(myhosturl+"/savegraph",{gname:nombregrafo},
function(data) {
        alert(data);

});

}

function jsViewTable(myhosturl) {

$.post(myhosturl ,{},
function(data) {
//alert(data);
var myjson = null;
myjson = eval("myjson = "+data);
//alert("Hola");
//			$('#dynamic').html( '<table cellpadding="0" cellspacing="0" border="0" class="display" name="example" id="example"></table>' );
		var oTable =	$('#example').dataTable( {
				"aaData": myjson.tasks,
				"aoColumns": myjson.columns,
				"bFilter": true,
				"bPaginate": false
			} );	
});

}


</script>
"""

JS_SAFETPROCESSCONSOLE_BOTTOM = u"""
<div id="svgload" class="svgdiv" style="overflow: scroll; width: 100%; height: 600px;"></div>
<div align="center">
<button type="button" id="buttonwplus">+Horizontal (zoom)</button>
<button type="button" id="buttonwminus">-Horizontal (zoom)</button>

<button type="button" id="buttonhplus">+Vertical (zoom)</button>
<button type="button" id="buttonhminus">-Vertical(Zoom) </button>

<button type="button" id="buttonwhplus">+Horz/Vert (zoom)</button>
<button type="button" id="buttonwhminus">-Horz/Vert (Zoom) </button>
</div>
"""

SAFETGOABOUT = u"""
<p align="center"> Desarrollado bajo Licencia <a href="http://www.gnu.org/licenses/gpl-2.0.html">GPL V 2.0</a><br/>
<b>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres <a href="http://www.cenditel.gob.ve">CENDITEL</a> 2011.
<b>Diseño y Programación:<br/></b> Víctor Bravo (vbravo at cenditel gob ve) <br/>
Antonio Araujo Brett aaraujo at cenditel gob ve <br/>
<b>Configuración: </b> Víctor Bravo y Pedro Buitrago (pbuitrago at cenditel gob ve) <br/>
</p>
"""

SAFETLOGIN = u"""
<form action="http://localhost/intranet/gologin" class="signin" method="post" enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">

<tr>
<th><label for="username_or_email">Nombre de usuario </label></th>
<td><input id="username" name="username" type="text" value="" /></td>
</tr>
<tr>
<th><label for="password">Contraseña</label></th>
<td><input id="password" name="password" type="password" value="" /> <small><a href="http://localhost/intranet/goresendpassword">¿Lo has olvidado?</a></small></td>
</tr>
<tr>
<th><label for="remember_me"></label></th>
<td><input id="remember_me" name="remember_me" type="checkbox" value="1" /> <label for="remember_me" class="inline">Recordar mis datos</label></td>
</tr>
<tr>
<th><label for="signin_submit"></label></th>
<td><input class="btn btn-m" id="signin_submit" name="commit" type="submit" value="Iniciar Sesión" /></td>
</tr>
</table>
</fieldset>
</form>
<form action="http://localhost/intranet/goregister" class="signin" method="post" enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tr>
<td><input class="btn btn-m" id="register_submit" name="register_commit"   type="submit" value="Registrarse" /></td>
</tr>
<tr>
<td>
<p> Sistema Automatizado para la Firma y Estampillado de Tiempo SAFET,
</p>
</td>
</tr>
</table>
</fieldset>
</form>

"""

SAFETREGISTER = u"""
<form action="http://localhost/intranet/register" class="signin" method="post" enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tr>
<th><label for="fullname">Nombre Completo</label></th>
<td><input id="fullname" name="fullname" type="text" value="" /></td>
</tr>
<tr>
<tr>
<th><label for="account">Nombre de cuenta </label></th>
<td><input id="account" name="account" type="text" value="" /></td>
</tr>
<tr>
<th><label for="email">Correo electrónico</label></th>
<td><input id="email" name="email" type="text" value="" /></td>
</tr>
<tr>
<th><label for="passwordone">Contraseña</label></th>
<td><input id="passwordone" name="passwordone" type="password" value="" /></td>
</tr>
<tr>
<tr>
<th><label for="passwordtwo">Repita Contraseña</label></th>
<td><input id="passwordtwo" name="passwordtwo" type="password" value="" /> </td>
</tr>
<tr>
<th><label for="passwordtwo">Escriba Texto de la imagen</label></th>
<td>
 <script type="text/javascript"
       src="http://www.google.com/recaptcha/api/challenge?k=6LcoN9gSAAAAABCQBM6PH8yJhj-YHy1fpvrYtHia">
    </script>
    <noscript>
       <iframe src="http://www.google.com/recaptcha/api/noscript?k=6LcoN9gSAAAAABCQBM6PH8yJhj-YHy1fpvrYtHia"
           height="300" width="500" frameborder="0"></iframe><br>
       <textarea name="recaptcha_challenge_field" rows="3" cols="40">
       </textarea>
       <input type="hidden" name="recaptcha_response_field"
           value="manual_challenge">
    </noscript>
</td>
</tr>
<tr>
<th></th>
<td><input class="btn btn-m" id="register_submit" name="commit"  type="submit" value="Registrarse" /></td>
</tr>
<tr>
<th></th>
<td>
<p> Sistema Automatizado para la Firma y Estampillado de Tiempo SAFET,
</p>
</td>

</tr>
</table>
</fieldset>

</form>
"""
SAFETCHANGEPASSWORD = u"""
<form action="http://localhost/intranet/changepassword" class="signin" method="post" enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tr>
<th><label for="passwordone">Contraseña</label></th>
<td><input id="passwordone" name="passwordone" type="password" value="" /></td>
</tr>
<tr>
<tr>
<th><label for="passwordtwo">Repita Contraseña</label></th>
<td><input id="passwordtwo" name="passwordtwo" type="password" value="" />
<input id="account" name="account" type="hidden" value="%s" />
 </td>
</tr>	
<tr>
<th></th>
<td><input class="btn btn-m" id="register_submit" name="commit"  type="submit" value="Cambiar contraseña" /></td>
</tr>
<tr>
<th></th>
<td>
<p> Sistema Automatizado para la Firma y Estampillado de Tiempo SAFET,
</p>
</td>

</tr>
</table>
</fieldset>
</form>
"""

SAFETRESENDPASSWORD = u"""
<form action="http://localhost/intranet/resendpassword" class="signin" method="post" enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tr>
<th><label for="passwordone">Nombre de su usuario</label></th>
<td><input id="account" name="account" type="text" value="" /></td>
</tr>
<tr>
<tr>
<th></th>
<td><input class="btn btn-m" id="register_submit" name="commit"  type="submit" value="Enviar" /></td>
</tr>
<tr>
<th></th>
<td>
<p> Sistema Automatizado para la Firma y Estampillado de Tiempo SAFET,
</p>
</td>

</tr>
</table>
</fieldset>
</form>
"""



PRINTLINKS = u"""
<font size=3><b>Sistema Automatizado para la Firma Electrónica y el Estampillado de tiempo SAFET</b><br/>
Usted desea realizar una de las siguientes opciones:</font>
<br/><br/>
<a href="/intranet/goinputform">Ingreso o modificación de información</a><br/><br/>
<a href="/intranet/goinputconsole">Generar reportes o gráficos de consulta</b></a><br/><br/><br/>
<a href="/intranet/logout"> Cerrar Sesión</b></a><br/>
"""

SAFETGOLOGIN = u"""
     <b>Usuario</b> o <b>Contraseña</b> inválida<br/>
     <a href="http://localhost/intranet/login">
     Haga click aquí para intentar de nuevo
     </a><br/><br/><br/><p></p><p></p><p></p>
"""

HTML_SAFETGOINPUTFORM = u"""
<html>
<head>
  <script src="http://localhost/media/jquery-latest.js"></script>
  <link rel="stylesheet" href="http://localhost/media/main.css" type="text/css" />
  <link rel="stylesheet" href="http://localhost/media/jquery.autocomplete.css" type="text/css" />
  <link rel="stylesheet" href="http://localhost/media/main.css" type="text/css" />
  <link rel="stylesheet" href="http://localhost/media/css/ui-lightness/jquery-ui-1.8.8.custom.css" type="text/css" />

  <script type="text/javascript" src="http://localhost/media/jquery.bgiframe.min.js"></script>
  <script type="text/javascript" src="http://localhost/media/jquery.autocomplete.js"></script>
  <script>

  $(document).ready(function(){
        function formatItem(row) {
                return "<strong>"+row[0]+"</strong>" ;
        }
        function formatResult(row) {
                return row[1];
        }

    var data = "Core Selectors Attributes Traversing Manipulation CSS Events Effects Ajax Utilities".split(" ");
  $("#inputform").autocomplete('http://localhost/intranet/formcomplete', {
                width: 400,
                multiple: true,
                multipleSeparator: " ",
                formatItem: formatItem,
                formatResult: formatResult
        });

$("#inputform").result(function(event, data, formatted) {
                var hidden = $(this).parent().next().find(">:input");
                hidden.val( (hidden.val() ? hidden.val() + ";" : hidden.val()) + data[1]);

  });

});

  </script>
  
</head>
<body>
<div >Formulario </div>
<br/>
<form action="http://localhost/intranet/1"
class="signin" method="post"  enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tbody>
<tr>
<th>Escriba su Formulario: <br>
</th>
<td><textarea cols="60" rows="12" name="inputform" id="inputform"></textarea><br>
</td>
</tr>
<tr>
<th><br>
</th>
<td><input class="btn btn-m" id="signin_submit" name="commit"
value="Enviar" type="submit"></td>
</tr>
<tr>
<th><br>
</th>
<td>
<p> Sistema Automatizado para la Firma y Estampillado de Tiempo
SAFET, </p>
        """+"""
</td>
</tr>
</tbody>
</table>
</fieldset>
</form>
</body>
</html>
"""

JS_SAFETGOINPUTCONSOLE = u"""
<script>
  $(document).ready(function(){
        function formatItem(row) {
                return "<strong>"+ row[0] + "</strong>";
        }
        function formatResult(row) {
                $("#inputform").val("");
                return row[1];
        }

    var data = "Core Selectors Attributes Traversing Manipulation CSS Events Effects Ajax Utilities".split(" ");
  $("#inputform").autocomplete('http://localhost/intranet/conscomplete', {
                width: 400,
                multiple: true,
                multipleSeparator: " ",
                formatItem: formatItem,
                formatResult: formatResult
        });

$("#inputform").result(function(event, data, formatted) {
                var hidden = $(this).parent().next().find(">:input");
                hidden.val( (hidden.val() ? hidden.val() + ";" : hidden.val()) + data[1]);

  });

  });
</script>
<form action="http://localhost/intranet/2"
class="signin" method="post"  enctype="multipart/form-data">
<fieldset class="common-form standard-form">
<table cellspacing="0">
<tr>
<th>Escriba su consulta: <br>
</th>
<td><textarea cols="60" rows="12" name="inputform" id="inputform"></textarea><br>
</td>
</tr>
<tr>
<th><br>
</th>
<td><input class="btn btn-m" id="signin_submit" name="commit"
value="Enviar" type="submit"></td>
</tr>
<tr>
<th><br>
</th>
<td>
        """+ """
</td>
</tr>
</table>
</fieldset>
</form>

"""

JS_SAFETCONSOLE = u"""
<style type="text/css">
.svgdiv { border: 1px solid #3c8243; }
#svgintro { float: right; width: 150px; height: 150px; margin-right: 30px; background: #fff; border: 1px solid #3c8243; }
.svgsample { float: left; width: 46%; margin: 1%; overflow: scroll; border: 1px solid #3c8243; padding: 5px; }
.drawOpt { float: left; width: 25%; }
.row { clear: both; }
#showMods { padding: 0em 0.25em; background-color: #ddffe8; color: #000; border: 1px solid #3c8243; font-size: 80%; text-decoration: none; cursor: pointer; }
#domMods { display: none; padding: 0em 1em 0.5em; background-color: #ddffe8; border: 1px solid #3c8243; }
</style>
<script type="text/javascript" src="http://localhost/media/jquery-latest.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svg.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.debug.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svggraph.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgplot.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svganim.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgdom.js"></script>
<script type="text/javascript" src="http://localhost/media/jquery.svgfilter.js"></script>
<link type="text/css" href="http://localhost/media/jquery.svg.css" rel="Stylesheet" />
<script type="text/javascript">
var g = null;
var currheight = 100;
var currwidth = 100;
   $(document).ready(function() {
"""


JS_SAFETCONSOLE_FUNCTIONS = u"""
    var svg = $('#svgload').svg('get');

    resetSize(svg,'100%','200%');

 $('#buttonwplus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonhplus').click(graphHPlus);

 $('#buttonwminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth - 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonwhminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth - 10;
        currheight = currheight - 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });
 $('#buttonwhplus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currwidth = currwidth + 10;
        currheight = currheight + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        });

 $('#buttonhminus').click(function() {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight - 10;
//        $(g).animate({svgViewBox: 
//    '        150, 87, 300, 175'}, 2000);
//        $(g).animate({svgWidth: 100, svgHeight: 100},2000);
//         var myrect = svg.rect(25, 25, 150, '25%', 10, 10, 
//          {fill: 'none', stroke: 'blue', strokeWidth: 3, 
//                   transform: 'rotate(0, 100, 75)'}); 
        resetSize(svg,currwidth+'%',currheight+'%');
//        $(g).animate({svgWidth: 100, svgHeight: 100},2000);
        });

function  graphHPlus () {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight + 10;
        resetSize(svg,currwidth+'%',currheight+'%');
        }

function  graphHPlusFactor(factor) {
        var svg = $('#svgload').svg('get');
        g = svg.getElementById('graph0');
        currheight = currheight + 10*factor;
        resetSize(svg,currwidth+'%',currheight+'%');
        }

function resetSize(svg, width, height) {
        svg.configure({width: width || $(svg._container).width(),
                height: height || $(svg._container).height()});
}

  });

function jsSaveGraph(myhosturl) {
var nombregrafo = prompt ("Nombre del grafo:","");
$.post(myhosturl+"/savegraph",{gname:nombregrafo},
function(data) {
        alert(data);

});

}

}

</script>
"""

JS_SAFETCONSOLE_BOTTOM = u"""
<div id="svgload" class="svgdiv" style="overflow: scroll; width: 100%; height: 600px;"></div>
<div align="center">
<button type="button" id="buttonwplus">+Horizontal (zoom)</button>
<button type="button" id="buttonwminus">-Horizontal (zoom)</button>

<button type="button" id="buttonhplus">+Vertical (zoom)</button>
<button type="button" id="buttonhminus">-Vertical(Zoom) </button>

<button type="button" id="buttonwhplus">+Horz/Vert (zoom)</button>
<button type="button" id="buttonwhminus">-Horz/Vert (Zoom) </button>
</div>
"""
