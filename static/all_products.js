	
function doSafetDelete( currid ) {
	console.log("(1)..doSafetDelete...."); 
	bootbox.confirm("¿Está seguro de  eliminar esta publicación?", 
	function(result) {			
	  console.log(currid);
	  if (result) {
		  myname = "thesafetrow_" + currid
		  console.log("myname: " + myname);						    
		  //$('#' + myname).html("Hola");
		  $.post('/ajaxforma_borrar_publicación',{ id: currid }, 
		  function(data) { 
		    console.log("(2)..data:......myname:"); 
		    console.log(data); 
		    mydata = eval('(' + data + ')');
		    if (mydata["result"] == "true" ) {
			      $('#' + myname).hide();						       
		    }
		    else {
			console.log("error, no deleted"); 
		      
		    }
		  
		  console.log("(3)...data:......"); 
	    
	    });
	 }
    
	console.log("pass");			
			
	});					
}


function doSafetFavorite(myobj, mypubid ) {
      console.log("(1)..doSafetFavorite....mypubid:" + mypubid); 					      					      
      $.post('/ajaxforma_hacer_favorito', { pubid: mypubid }, 
	    function(data) { 
	    	console.log("(2)..data:......myname:"); 
	    	console.log(data); 
	    	myresult = eval("(" + data + ")" );
	    	console.log("result:" + myresult["result"]); 
	    	if (myresult["result"] == "true") {
	    	mynewbutton = "<button class=\"btn btn-warning\" onclick=\"doSafetUnFavorite(this.parentNode,"+
	    	mypubid+")\"  data-toggle=\"tooltip\" data-placement=\"left\" title=\"Colocar como no favorito\" >" +
                "<i class=\"glyphicon glyphicon-star\"></i></button>";
	    	  
		  $(myobj).html(mynewbutton);
	    	}
	    	
	    });
      
}
function doSafetUnFavorite(myobj, mypubid ) {
      console.log("(1)..doSafetFavorite....mypubid:" + mypubid); 					      					      
      $.post('/ajaxforma_no_hacer_favorito', { pubid: mypubid }, 
	    function(data) { 
	    	console.log("(2)..data:......myname:"); 
	    	console.log(data); 
	    	myresult = eval("(" + data + ")" );
	    	console.log("result:" + myresult["result"]); 
	    	if (myresult["result"] == "true") {
	    	mynewbutton = "<button class=\"btn btn-primary\" onclick=\"doSafetFavorite(this.parentNode,"+
	    	 mypubid+")\"  data-toggle=\"tooltip\" data-placement=\"left\" title=\"Colocar como favorito\" >" +
                "<i class=\"glyphicon glyphicon-star\"></i></button>";
	    	  
		  $(myobj).html(mynewbutton);
	    	}
	    	
	    });
      
}

var lastcommentobj = "";

function doSafetShow(summary, photo1, photo2, photo3, price, description ) {
  $( "#dialogshow" ).dialog({  resizable: true });
  myhtml = "<div class=\"row\">\n"
          "<div class=\"col-md-6\">\n"
  //myhtml= "<p>";
  myhtml = myhtml + "<img src=\"" + photo1 +"\"></img>"
  if ( photo2.length > 0 ) {
  myhtml = myhtml + " <img src=\"" + photo2 +"\"></img>"
  }
  
  if ( photo3.length > 0 ) {
  myhtml = myhtml + " <img src=\"" + photo3 +"\"></img>"					  
  }
  
  
  myhtml = myhtml + "</div>\n";
  myhtml = myhtml + "</div>\n";
  
  mydata = "<div class=\"row\">\n"
          "<div class=\"col-md-12\">\n";
  mydata += " "+ summary;
  if (description.length > 0 ) {
  
    currlen = description.length;					    
    mydata = mydata + description.substring(0,currlen);
    
  }
  mydata += "</div>\n";
  mydata += "</div>\n";
  
  myprice = "</button><button class=\"btn btn-primary\">Precio:" + price +"</button>";
  
  myhtml = myhtml + mydata + myprice;
  
  $( "#dialogshow" ).html(myhtml);
  

}



function doSafetEdit( currid ) {
	      console.log("(1)..doSafetEdit....currid" + currid); 
	      myurl = 
"/goform/gomodify/modificar_publicación/" +currid;	
						 

	      
	      window.location = myurl;


      
}

function doSafetComments(myobj, currid ) {

console.log("doSafetAddComment");
mycurrobj = "#currboxcomment_" + currid;
if (mycurrobj == lastcommentobj ) {
	$(lastcommentobj).html("");					      
	lastcommentobj = "";
	return;
}
myoperation = "operacion:Listar_datos Cargar_archivo_flujo: /home/usuario/.safet/flowfiles/comentarios.xml Variable: vPorPublicacion" +
" parameters.ByPublication: " + currid; 

$("#divForLoading").show();
$.post('/ajaxconsole',{ operation: myoperation
	}, 
	    function(data) { 
	      $("#divForLoading").hide();
	      if ( lastcommentobj.length > 0 ) {
		      $(lastcommentobj).html("");					      
	      }
	      console.log("(1)..data:......ajaxconsole:|" + data + "|"); 
	     
	      	 
	      myresult = eval("(" + data + ")" );
	      mylist = myresult["safetlist"];
	      
	      console.log("(2)..data:......ajaxconsole:" +  mylist.length); 
	      mynewtable = "";
	      mynewtable += "<div class=\"panel-footer\" id=\"commenttable\" name=\"commenttable\" >\n";
	      mynewtable += "<ul class=\"list-group\">\n";
	        
	      if (mylist.length > 0){
	      	for(i = 0; i < mylist.length; i++) {
				console.log("comment:" + mylist[i]["comment"] + " owner:" + mylist[i]["owner"]);
				mynewitem = "<li class=\"list-group-item text-capitalize\">" + mylist[i]["comment"] + "<div class=\"text-right\"><font size=\"1\">Por <b> $" +mylist[i]["owner"] 
				+"</b> hace "+
				mylist[i]["commenttime"].substring(18) +"</font></div></li>\n";
				mynewtable += mynewitem;							
	      	}
	      }else{
	      		mynewitem = "<li class=\"list-group-item first-coment\">Sea el primero en comentar sobre este producto <b>Weetup</b><div class=\"text-right\"><font size=\"1\">Weetup</font></div></li>";
				mynewtable += mynewitem;	
	      }
	      

	      mynewtable += "</ul>";

	      console.log("(3)..data:......ajaxconsole"); 						      						      
	     

	      mynewcomment = "";
	      
	     if (curruserinfo[0].cuenta != "comprador" ) {
		      
		      mynewcomment += "<hr/><form action=\"javascript:void(0);\" class=\"form-inline\" role=\"form\"><div class=\"row\"><div class=\"form-group col-md-12\"><input style=\"width:100%\" maxlenght=\"320\" class=\"currcomment form-control\" type=\"text\" placeholder=\"Escribe tu comentario aquí...\" id=\"currcomment\" name=\"currcomment\" /></div><div class=\"text-right col-md-12\"><br/><button class=\"btn btn-default\" onclick=\"doSafetAddComment("+ currid +")\" >Agregar</button></div></div></form>";

		      mynewcomment += "</div>";
		}	
		      mynewobj = "#currboxcomment_" + currid;
	 	     console.log("(1)..doSafetComments.newobj:" + mynewobj);
		      $(mynewobj).html(mynewcomment);
		      lastcommentobj = mynewobj;						      
		      mynewobj = "#currboxcomment_" + currid;
		      $(mynewobj).html(mynewtable + mynewcomment);
	      
	    });


// ****************
      
      
      
}


function doSafetGetComment( currid ) {

}

function doSafetAddComment( currid ) {
    mycomment = $("#currcomment").val();

    if(mycomment.length < 10){
		bootbox.alert("Su comentario debe tener al menos diez (10) caracteres", function(result) {
        if (result) {
            // currentForm.submit();
            return;
        }
    });

    	return false;
    }


    $("#divForLoading").show();
    $.post('/ajaxforma_agregar_comentario',{ Publicacion_id: currid,
	  Comentario: mycomment
	    }, 
		function(data) { 
		$("#divForLoading").hide();
		    //if ( lastcommentobj.length > 0 ) {
			//    $(lastcommentobj).html("");					      
		    //}
		    console.log("(2)..data:......myname:"); 
		    console.log(data); 
		    myresult = eval("(" + data + ")" );
		    console.log("result:" + myresult["result"]);

		    if (myresult["result"] == "true") {
		       myid = myresult["id"];
		       myoperation = "operacion:Listar_datos Cargar_archivo_flujo: /home/usuario/.safet/flowfiles/comentarios.xml Variable: vPorId parameters.ById:" + myid
		       console.log("myoperation: " + myoperation);

		       $("#divForLoading").show(); 	      
		       $.post('/ajaxconsole',{ operation: myoperation
	    	       },  
		           function(data) { 
		           	$(".first-coment").remove();
					$("#divForLoading").hide();    
		           		console.log("....data new comment:");
		           		myresult = eval("(" + data + ")" );							           		
		           		console.log(data);
		           		console.log("**comment table...1");

		           		mycomment = myresult["safetlist"][0]["comment"];
		           		mytime = myresult["safetlist"][0]["commenttime"];
		           		myowner = myresult["safetlist"][0]["owner"];
		           		mynewitem = "<li class=\"list-group-item text-capitalize\">"+ mycomment+ "<div class=\"text-right\"> <font size=\"1\">Por " +myowner +" hace "+mytime.substring(18) +"</font></div></li>\n";
		           		$("#commenttable ul").append(mynewitem);
		           		console.log("***comment table...2..newitem:" + mynewitem);
		           		$("#currcomment").val("");

			  			//$("#currboxcomment").html("");
			  		  
		    	   }													
	           );
		   }
		   
		});

}



function doSafetPublish(myobj, currid ) {
console.log("(1)..doSafetBuy...."); 
     bootbox.confirm("¿Está seguro de publicar este producto?", 
    function(result) {			
    
    console.log(currid);
    if (result) {
	    
	    $.post('/processbuy/'+currid+"/Published/-1/",
                            { id: currid }, 
	    function(data) { 						    
	      console.log("(2)..processbuy:......myname:"); 
	      myresult = eval("(" + data + ")" );
	      console.log("result:" + myresult["result"]); 
	      if (myresult["result"] == "true") {
	    	  mynewbutton = "<button title=\"Publicado\" class=\"btn btn-success\"><i class=\"glyphicon glyphicon-check\"></i></button>"
		  $(myobj).html(mynewbutton);


	      }						      
	    })					
	    
    }
    
    console.log("pass buy");		
	    });					
}


function doSafetRate(myobj, currid ) {
console.log("(1)..doSafetRate..."); 
	content = $(myobj).html();
	selectedPositiva = content.indexOf("btn-success") > -1 ? 'checked="checked"' : '';
	selectedNeutra = content.indexOf("btn-info") > -1 ? 'checked="checked"' : '';
	selectedNegativa = content.indexOf("btn-danger") > -1 ? 'checked="checked"' : '';
	bootbox.dialog({
	title: "Calificar publicación",
	message: '<div class="row"> ' +
	'<div class="col-md-12"> ' +
	'<form class="form-horizontal"> ' +
	'<div class="form-group"> ' +
	'<label class="col-md-6 control-label" for="awesomeness">Como lo califica la venta?</label> ' +
	'<div class="col-md-6"> <div class="radio"> <label for="awesomeness-0"> ' +
	'<input type="radio" ' + selectedPositiva + ' name="awesomeness" id="awesomeness-0" value="2" checked="checked"> ' +
	'Positiva </label> ' +
	'</div>' +
                        '<div class="radio"> <label for="awesomeness-1"> ' +
	'<input type="radio" ' + selectedNeutra + ' name="awesomeness" id="awesomeness-1" value="1"> Neutra </label> ' +
	'</div> ' +
	'<div class="radio"> <label for="awesomeness-2"> ' +
	'<input type="radio" ' + selectedNegativa + ' name="awesomeness" id="awesomeness-2" value="0"> Negativa </label> ' +
	'</div> ' +

	'</div> </div>' +
	'</form> </div> </div>',
	buttons: {
	success: {
		label: "Guardar",
	className: "btn-success",
		callback: function () {
		
			console.log("doSafetRate");
			var answer = $("input[name='awesomeness']:checked").val()
			var mystr ="Se eligió <b>" + answer + "</b>";
			console.log(mystr);
			var options = {};
			options["0"] = "Negativa";
			options["1"] = "Neutra";
			options["2"] = "Positiva";

	 $.post('/processbuy/'+currid+"/Scored/"+answer+"/",
                            { id: currid }, 
                            function(data) {                                                
                              console.log("(2)..processbuy:......myname:"); 
                              myresult = eval("(" + data + ")" );
                              console.log("result:" + myresult["result"]); 
                              if (myresult["result"] == "true") {
                              	  
                              	  scoreIcon = "glyphicon-ok-sign";
									  scoreStatus = "btn-info";

                              	  if(options[answer] == options["0"]){
                          	  		scoreIcon = "glyphicon-thumbs-down";
									  	scoreStatus = "btn-danger";
                              	  }else if(options[answer] == options["2"]){
                          	  		scoreIcon = "glyphicon-thumbs-up";
									  	scoreStatus = "btn-success";
                              	  }

                              	  mynewbutton = '<button title="Publicación calificada como: ('+options[answer]+')" class=\"btn '+ scoreStatus +'\" onclick=\"doSafetRate(this.parentNode, '+ currid +')\"><i class=\"glyphicon '+ scoreIcon +'\"</i></button>';
                              	  console.log(mynewbutton);

                                  $(myobj).html(mynewbutton);
                              }                                               
                            });    							

			   Example.show(mystr);
			    }
		  	  }
			}
			}
	); 
    				
}




function doSafetBuy(myobj, currid ) {

if (curruserinfo[0].cuenta == "comprador" ) {
bootbox.alert("Inicie sesión o regístrese para poder realizar la compra", function(result) {
	      if (result) {
		  // currentForm.submit();
		  return;
	      }
	  });
	  return;
      
}
console.log("(1)..doSafetBuy...."); 
     bootbox.confirm("¿Está seguro de comprar este producto?", 
    function(result) {			
    
    console.log(currid);
    if (result) {
	    
	    $.post('/processbuy/'+currid+"/Sold/-1/",
                            { id: currid }, 
	    function(data) { 						    
	      console.log("(2)..processbuy:......myname:"); 
	      myresult = eval("(" + data + ")" );
	      console.log("result:" + myresult["result"]); 
	      if (myresult["result"] == "true") {
	    	  mynewbutton = "<button class=\"btn btn-success\"><i class=\"glyphicon glyphicon-log-in\"></i> Comprado</button>"
		  $(myobj).html(mynewbutton);
		  myurl = "/makepurchase/none/"+currid;
		  console.log("compra realizada url:" + myurl);

		  window.location = myurl;
	      }						      
	    })					
	    
    }
    
    console.log("pass buy");		
	    });					
}


