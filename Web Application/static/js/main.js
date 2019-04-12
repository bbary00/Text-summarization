(function(){
	
	$('#area').on('input', function (event) {
	 	var text = event.target.value;
	 	var sentences = text.replace(/([.?!])\s*(?=[A-Z])/g, "$1|").split("|");
	 	var amountOfSentences = sentences.length;
	 	var lastLetter;
	 	for(var i = 0;i<sentences.length;i++){
	 		lastLetter = sentences[i][sentences[i].length-2];
	 		if(lastLetter==lastLetter.toUpperCase() && sentences[i].length<3){
	 			amountOfSentences-=1;
	 		}
	 	}
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

		for(var i = 1;i<=amountOfSentences;i++){
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

		//ajax
		$('#press').on('click', function(event) {
			$(".res").show();
			$(window).scrollTop($(".res").offset().top);
			var data = $('#area').val();
			document.getElementById("result").value = data;
		});
	})

}());
// дивитися речення і якшо там 1 символ то сплітити його до наступного