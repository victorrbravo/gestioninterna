function doSafetUnFollow(myobj, account, fromMainProfile ) {
      console.log("(1)..doSafetUnFollow....account:|" + account + "|"); 					      					      
      $.post('http://localhost:8080/ajaxforma_no_seguir_usuario',{  cuenta2: account }, 
	    function(data) { 
	    	console.log("(2)..data:......myname:"); 
	    	console.log(data); 						
	    	myresult = eval("(" + data + ")" );
	    	console.log("result:" + myresult["result"]); 
	    	if (myresult["result"] == "true") {
				
				fromMainProfileParam = "false";
				if(fromMainProfile == true){
					section = '.profile-followers > b';
					fromMainProfileParam = "true";
				}else{
					section = '.profile-followers-' + account +' > b';
					minusTo('.profile-followings > b');
				}
				
				minusTo(section);

				mynewbutton = "<button class=\"btn btn-primary\" onclick=\"doSafetFollow(this.parentNode, '"+account +"', " + fromMainProfileParam  +" )\"><i class=\"glyphicon glyphicon-hand-right\"></i> Seguir</button>"
				$(myobj).html(mynewbutton);

	    	}

	    });
}

function doSafetFollow(myobj, account, fromMainProfile ) {
	console.log("(1)..doSafetFollow....account:" + account); 					      					      
	$.post('http://localhost:8080/ajaxforma_seguir_usuario',{ cuenta2: account }, 
	function(data) { 
		console.log("(2)..data:......myname:"); 
		console.log(data); 
		myresult = eval("(" + data + ")" );
		console.log("result:" + myresult["result"]); 
		if (myresult["result"] == "true") {
			
			fromMainProfileParam = "false";
			if(fromMainProfile == true){
				section = '.profile-followers > b';
				fromMainProfileParam = "true";
			}else{
				section = '.profile-followers-' + account +' > b';
				addTo('.profile-followings > b');
			}
			
			addTo(section);

			mynewbutton = "<button class=\"btn btn-primary\" onclick=\"doSafetUnFollow(this.parentNode, '"+ account +"', " + fromMainProfileParam  +" )\"><i class=\"glyphicon glyphicon-thumbs-down\"></i> Dejar de seguir</button>"
			$(myobj).html(mynewbutton);

		}
	});
      
}

function addTo(section){
	section = $(section);
	count = section.html();
	count = (count.trim() == "") ? 0 : count;
	section.html(parseInt(count) + 1);
}

function minusTo(section){
	section = $(section);
	count = section.html();
	count = (count.trim() == "") ? 0 : count;
	if(count > 0){
		section.html(parseInt(count) - 1);
	}
}
