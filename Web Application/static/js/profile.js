$(window).ready(function() {
    $.ajax({
            data: {},
            type: 'POST',
            url: '/db_info'
        })
        .done(function(data) {
            var list = document.getElementById('list');
            var listSaved = document.getElementById('list-saved');
            var username = document.getElementById("username");
            var time = document.getElementById("time");
            var words = document.getElementById("words");

           var pageData = data["page_data"];
           var savedData = data["saved_data"];
           var last10 = data["last_10"];

           for(var key in last10){
               var icon1 = document.createElement('i');
               icon1.setAttribute('class', "far fa-copy fas copy");
               icon1.addEventListener('click', function(event) {
                   this.previousElementSibling.select();
                   document.execCommand('copy');
               })
               var textarea = document.createElement('textarea');
               textarea.setAttribute('class', 'form-control');
               textarea.setAttribute('readonly', 'readonly');
               textarea.value = last10[key];
               var li = document.createElement('li');
               li.appendChild(textarea);
               li.appendChild(icon1);
    //           list.insertBefore(li, list.firstChild);
               list.appendChild(li);
           }

           username.innerHTML =pageData["user_name"];
           time.innerHTML = "Saved time<br/>" + pageData["saved_time"];
           words.innerHTML = "Saved words<br/>" + pageData["saved_words"];


           for(let [key, value] of Object.entries(savedData)){
                var icon1 = document.createElement('i');
                icon1.setAttribute('class', "far fa-copy fas copy");
                icon1.addEventListener('click', function(event) {
                    this.previousElementSibling.select();
                    document.execCommand('copy');
                });
                var icon2 = document.createElement('i');
                icon2.setAttribute("class", "fas fa-angle-right angle");


                var text = document.createElement('textarea');
                text.setAttribute('class', 'form-control falling');
                text.setAttribute('readonly', 'readonly');
                text.value = Object.values(value)[0];
                text.style.display = "none";
                icon2.addEventListener('click', function(event) {
                    var trigger = this.classList.contains("fa-angle-right");
                    if (trigger) {
                        this.removeAttribute("class");
                        this.setAttribute("class", "fas fa-angle-down angle");
                        this.parentElement.nextElementSibling.style.display = "block";
                    } else {
                        this.removeAttribute("class");
                        this.setAttribute("class", "fas fa-angle-right angle");
                        this.parentElement.nextElementSibling.style.display = "none";
                    }
                });
                var textarea = document.createElement('textarea');
                textarea.setAttribute('class', 'form-control');
                textarea.setAttribute('readonly', 'readonly');
                textarea.value = Object.keys(value)[0];
                var li = document.createElement('li');
                var span = document.createElement('span');
                span.setAttribute("class","tooltiptext");
                span.innerHTML = "To see full text";
                icon2.appendChild(span);
                li.appendChild(textarea);
                li.appendChild(icon1);
                li.appendChild(icon2);
                listSaved.appendChild(li);
                listSaved.insertBefore(text, li.nextElementSibling);
           }
        });

    var slideIndex = 1;
    showDivs(slideIndex);

    function plusDivs(n) {
        showDivs(slideIndex += n);
    }

    function showDivs(n) {
        var i;
        var x = document.getElementsByClassName("block");
        if (n > x.length) {
            slideIndex = 1
        }
        if (n < 1) {
            slideIndex = x.length
        }
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        x[slideIndex - 1].style.display = "block";
    }

    var slideLeft = document.getElementById("left");
    var slideRight = document.getElementById("right");
    slideLeft.addEventListener('click', function() {
        plusDivs(-1);
    })
    slideRight.addEventListener('click', function() {
        plusDivs(1);
    })


    $(window).on('load', function () {
	        $preloader = $('#preloader'),
	        $preloader.delay(2500).fadeOut('slow');
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



})