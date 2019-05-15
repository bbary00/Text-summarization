(function(){

		$('#area').on('change', function (event) {
            var text = event.target.value;
            var sentences = text.replace(/([.?!])\s*(?=[A-ZА-Я])/g, "$1|").split("|");
            var amountOfSentences = sentences.length;
            var lastLetter;
            for(var i = 0; i<sentences.length; i++){
                if(sentences[i].length <=1){
                    continue;
                }
                lastLetter = sentences[i][sentences[i].length-2];
                if(lastLetter==lastLetter.toUpperCase() && sentences[i].length<3){
                    amountOfSentences-=1;
                }
            }
            $('#area').on('keydown', function (event){
                if(event.keyCode == 8){
                    range.disabled=true;
                    rangeValue.innerHTML = "";
                    btn.disabled=true;
                }

            })
            var form = document.getElementById("form");
            var range = document.getElementById("range");
            range.disabled=true;
            var rangeValue = document.getElementById("rangeValue");
            rangeValue.innerHTML = "";
            if(sentences.length >=2){
                range.disabled=false;
            }
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

        //Check if limit
              var isLimited = !!($('#area').attr('maxLength'));
              var area = document.getElementById('area');
              var maxLength = 2000;
              if(isLimited){
                if(area.value.length >= maxLength){
                  Swal.fire({
                    html: 'The limit of 2000 characters is exceeded.<br/></br><strong>Please register to use all advantages:</strong><br/><ul><li>Unlimited text</li><li>See your previous summaries</li><li>Custom your environment</li></ul><button type="button" class="swal2-confirm swal2-styled" aria-label style="display: inline-block; border-left-color: rgb(48, 133, 214); border-right-color: rgb(48, 133, 214);"><a href="signup" style="color:white;text-decoration:none">Sign up</a></button>',
                    type: 'warning',
                    showCancelButton: true,
                    showConfirmButton:false,
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Sign up',
                   })
                }
              }
	    })

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

        // clear
        var clear = document.getElementById("clear");
        clear.addEventListener('click',function(event){
            document.getElementById("area").value="";
            range.disabled=true;
            rangeValue.innerHTML = "";
            btn.disabled=true;
            while (form.firstChild) {
                form.removeChild(form.firstChild);
            }
            option = document.createElement('option');
            option.setAttribute('value','');
            option.setAttribute('disabled',"");
            option.setAttribute('selected',"");
            option.innerHTML = "Select the number of sentences";
            form.appendChild(option);
        })

        // copy
        var copy = document.getElementById("tip");
        copy.addEventListener('click',function(event){
            var text = document.getElementById("result");
            text.select();
            document.execCommand('copy');
        })

        // day/night mode
        $('.toggle').click(function(){
            $('.toggle').toggleClass('active');
            $('body').toggleClass('night');
            $('.badge').toggleClass('night');
            $('#profile').toggleClass('night');
        })

        function changeClass(){
            $(this).prev().toggleClass('active')
        }
        $(function(){
            $('#more-info h3').click(function(){
                $(this).next().slideToggle();
                $(this).toggleClass('active');
            })
        })
}());
