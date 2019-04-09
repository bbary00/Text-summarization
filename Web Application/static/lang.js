arrLang={
	'en':{
		'input':"Enter your text",
		'sent':"Sentence",
		'required':"Required",
		'select':"Select the number of sentences",


	},
	'ua':{
		'input':"Введіть свій текст",
		'sent':"Речення",
		'required':"Обов'язково",
		'select':"Виберіть кількість речень",

	}
}

$(function(){
    $('.translate').click(function(){
        var lang=$(this).attr('id');
        $('.lang').each(function(index,element){
            if(arrLang[lang][$(this).attr('key')]!='Message' && arrLang[lang][$(this).attr('key')]!='Повідомлення'){
                $(this).text(arrLang[lang][$(this).attr('key')]);
            }
            $(this).attr('placeholder', arrLang[lang][$(this).attr('key')]);
        });
    });
});