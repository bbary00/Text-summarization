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
	    })
        $(window).on('load', function () {
	        $preloader = $('#preloader'),
	        $preloader.delay(2000).fadeOut('slow');
        });
        $('.count').each(function () {
            $(this).prop('Counter',0).animate({
                Counter: $(this).text()
            }, {
                duration: 2100,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
        // slider
        var btn = document.getElementById('press');
        var range = document.getElementById("range");
        var rangeValue = document.getElementById("rangeValue");
        range.addEventListener('change',function(){
            rangeValue.innerHTML=range.value;
            btn.disabled = false;

        })

        var slideIndex = 1;
        showDivs(slideIndex);

        function plusDivs(n) {
            showDivs(slideIndex += n);
        }

        function showDivs(n) {
          var i;
          var x = document.getElementsByClassName("block");
          if (n > x.length) {slideIndex = 1}
          if (n < 1) {slideIndex = x.length}
          for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
          }
          x[slideIndex-1].style.display = "inline-block";
        }

        var slideLeft = document.getElementById("left");
        var slideRight = document.getElementById("right");
        slideLeft.addEventListener('click',function(){
            plusDivs(-1);
            btn.disabled=true;
            rangeValue.innerHTML = "";
        })
        slideRight.addEventListener('click',function(){
            plusDivs(1);
            btn.disabled=true;
        })
}());
