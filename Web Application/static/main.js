(function(){
	
	$('#area').on('input', function (event) {
	 	var text = event.target.value;
	 	var sentences = text.replace(/([.?!])\s*(?=[A-Z])/g, "$1|").split("|");
	 	var form = document.getElementById("form");
	 	console.log(sentences);

	 	while (form.firstChild) {
    		form.removeChild(form.firstChild);
		}
		option = document.createElement('option');
		option.setAttribute('value','');
		option.setAttribute('disabled',"");
		var sent = document.getElementById("sent");
		if(sent.innerHTML=="Речення"){
			option.innerHTML ="Виберіть кількість речень";
		}else{
			option.innerHTML = "Select the number of sentences";
		}
		option.setAttribute('selected',"");
		option.className= "lang";
		option.setAttribute('key',"select");
		form.appendChild(option);

		for(var i = 1;i<=sentences.length;i++){
			var option = document.createElement('option');
			option.setAttribute('value',i);
			option.innerHTML=i;
			form.appendChild(option);
		}
		if(sentences==0){
			form.removeChild(form.firstChild);
			form.removeChild(form.firstChild);
			option = document.createElement('option');
			option.setAttribute('value','');
			option.setAttribute('disabled',"");
			if(sent.innerHTML=="Речення"){
				option.innerHTML ="Виберіть кількість речень";
			}else{
				option.innerHTML = "Select the number of sentences";
			}
			option.setAttribute('selected',"");
			option.className= "lang";
			option.setAttribute('key',"select");
			form.appendChild(option);
			
		}
	
		var btn = document.getElementById('press');
		btn.disabled=true;
		form.addEventListener('change',function(){
			if(!isNaN(form.value)){
				btn.disabled=false;
			}
		})
		
		

	})
}());
