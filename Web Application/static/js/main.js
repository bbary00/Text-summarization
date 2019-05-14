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
        $(window).on('load', function () {
	        $preloader = $('#preloader'),
	        $preloader.delay(3000).fadeOut('slow');
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

        // Phrases
        function getRandomInt(max) {
            return Math.floor(Math.random() * Math.floor(max));
        }
        var phrases = [
        "Якщо ви не здаєтеся, | це має значення. | Стівен Хокінг",
        "Все, що можна | уявити – реально. | Пабло Пікассо",
        "Навчання ніколи | не вичерпує розум. | Леонардо да Вінч",
        "Плани – ніщо, | планування – все. | Дуайт Д. Ейзенхауер",
        "Будь собою, | інші ролі зайняті. | Оскар Уайльд",
        "Прагніть не до успіху, | а до цінностей, які він дає. | Альберт Eнштeйн",
        "Найскладніше почати діяти, все | інше залежить тільки від наполегливості. | Амелія Ергарт",
        "Життя – це те, що з тобою | відбувається, поки ти будуєш плани. | Джон Леннон",
        "Логіка може привести вас від пункту А | до пункту Б, а уява – куди завгодно. | Альберт Енштейн.",
        "Неосмислене життя не | варте того, щоб його прожити. | Сократ",
        " 80% успіху — це з’явитися | в потрібному місці в потрібний час. | Вуді Аллен.",
        "Ваш час обмежений, не | витрачайте його, живучи чужим життям. | Стів Джобс.",
        "Перемога – це ще не все, | все – це постійне бажання перемагати. | Вінс Ломбарді.",
        " Наука – це організовані знання, | мудрість – це організоване життя. | Іммануїл Кант.",
        "У моєму словнику | немає слова неможливо. | Наполеон Бонапарт.",
        " Ви ніколи не перетнете океан, якщо | не наберетеся мужності втратити берег з виду. | Христофор Колумб.",
        "Свобода нічого не варта, якщо вона | не включає в себе свободу помилятися | Махатма Ганді.",
        "Або ви керуєте вашим | днем, або день управляє вами. | Джим Рон.",
        "Найкраща помста | величезний успіх | Френк Сінатра.",
        " Є тільки один спосіб уникнути критики: | нічого не робіть, нічого не говоріть і будьте ніким.  | Аристотель.",
        "Людина, якою вам судилося стати – це | тільки та людина, якою ви самі вирішите стати. | Ральф Голдо Емерсон.",
        " Краще бути впевненим в хорошому | результаті, ніж сподіватися на відмінний. | Воррен Баффетт.",
        "Варто тільки повірити, що ви | можете – і ви вже на півдороги до цілі | Теодор Рузвельт.",
        " Навчіться говорити Я | не знаю, і це вже буде прогрес. | Мойсей Маймонід.",
        "Почніть звідти, де ви зараз перебуваєте. | Використовуйте те, що у вас є і робіть все, що можете. | Артур Еш.",
        "Впади сім разів, | піднімися вісім | Японська приказка.",
        "У всьому є своя краса, | але не кожен може її побачити | Конфуцій.",
        " Коли я звільняюся від того, хто | я є, я стаю тим, ким я можу бути | Лао Цзи.",
        "Щастя – це не щось готове. | Щастя залежить тільки від ваших дій.  | Далай Лама.",
        "Якщо немає вітру, | беріться за весла. | Латинська приказка.",
        "Успіх – це здатність крокувати від однієї | невдачі до іншої, не втрачаючи ентузіазму. | Вінстон Черчилль.",
        "Єдиною межею наших завтрашніх | звершень стануть наші сьогоднішні сумніви. | Франклін Д. Рузвельт.",
        "Людина вмирає тоді, коли перестає | змінюватися, а похорон – просто формальність. | Генрі Форд.",
        "Любов і робота – це наріжні | камені нашої людяності. | Зигмунд Фрейд.",
        "Ваш добробут залежить | від ваших власних рішень. | Джон Д. Рокфеллер.",
        " Воістину той, хто не цінує | життя, той його не заслуговує | Леонардо да Вінчі.",
        "Визначеність мети — відправна | точка всіх досягнень. | Вільям Клемент Стоун.",
        "Ми стаємо тим, | про що ми думаємо. | Ерл Найтінгейл.",
        " Я не жертва обставин, | я – результат моїх рішень. | Стівен Кові.",
        "Будь собою, | інші ролі зайняті. | Оскар Уайльд.",
        "Невдача – це просто можливість | почати знову, але вже більш мудро. | Генрі Форд.",
        " Поразка – не поразка, якщо тільки | ви не визнаєте її такою у своїй свідомості. | Брюс Лі.",
        "Я краще помру від | пристрасті, ніж від нудьги. | Вінсент Ван Гог.",
        " Не важливо, як повільно ти | просуваєшся, головне, що ти не зупиняєшся | Конфуцій.",
        " Щоб вести людей | за собою, йди за ними. | Лао Цзи.",
        " Запам’ятайте, що не досягти | успіху – іноді теж велика удача. | Далай Лама.",
        "Завжди обирайте найважчий шлях – на | ньому ви не зустрінете конкурентів. | Шарль де Голль.",
        "Одне закінчене результативне | завдання вартує півсотні напівзакінчених | Стів Форбс.",
        "Біда не приходить | одна, але й удача теж. | Ромен Роллан.",
        " Роби все, що можеш, там, де ти | знаходишся, використовуючи все, що маєш. | Теодор Рузвельт",
        "Єдине щастя в житті – це | постійне прагнення вперед. | Еміль Золя.",
        "Виживає не найсильніший, а | найчутливіший до змін. | Чарльз Дарвін.",
        " Ми знаємо, хто ми є, але | не знаємо, ким ми можемо бути. | Вільям Шекспір.",
        "Кожен, хто живе в межах | свої можливостей, страждає нестачою уяви | Оскар Уальд",
        "Все популярне | неправильне | Оскар Уальд",
        "Життя занадто коротке, | щоб бути маленьким | Бенджамін Дізраелі",
        "Вершина ідеальності | в простоті. | Брюс Лі",
        "Є багато речей, на які | розумний чоловік не хотів би | звертати уваги. Ральф Вальдо Емерсон",
        "Якщо не | використовуєш, | значить втрачаєш",
        "Мисли | і | вдосконалюйся",
        "В світі не має обмежень | крім тих, яки ти сам | для себе встановлюєш",
        "Мисли самостійно. Будь | гравцем у шахи, а не фігурою. | Ральф Чарелл",
        "Найкращий захист | це атака. | Ден Кебл",
        "Розклад запобігає | хаосу і непотрібним захцянкам. | Анні Ділард",
        "Просто глянь | і забудь. | Рон Попейль",
        "На цій дорозі | враховуються лише кілька кроків | Жан Батіст Марі",
        ];
       var firstPiece = document.getElementById("one");
        var secondPiece = document.getElementById("two");
        var thirdPiece = document.getElementById("three");
        var random = getRandomInt(phrases.length-1);
        var pieces = phrases[random].split(" | ");
        firstPiece.innerHTML=pieces[0];
        secondPiece.innerHTML=pieces[1];
        thirdPiece.innerHTML=pieces[2];




}());
