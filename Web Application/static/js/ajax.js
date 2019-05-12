$(document).ready(function() {

	$('#press').on('click', function(event) {
        var range;
	    var sent = $('#form').val();
	    var rangeValue = document.getElementById("rangeValue");
        if(rangeValue.innerHTML === undefined || rangeValue.innerHTML == ""){
            range = null;
        }else{
            range = $('#range').val();
            sent = null;
        }
		var isEnglish = function (text) {
            return /[a-z]/i.test(text);
        }
		$.ajax({
			data : {
				text : $('#area').val(),
				sentence : sent,
				percentage : range,
				lang : isEnglish($('#area').val())
			},
			type : 'POST',
			url : '/summarization'
		})
		.done(function(data) {
			$(".res").show();
			$(window).scrollTop($(".res").offset().top);
		    document.getElementById("result").value = data;

		});

		event.preventDefault();
	});

    $("#saved").on('click', function(event){
    		$.ajax({
			data : {
				summary : $('#result').val(),
				text : $('#area').val(),
			},
			type : 'POST',
			url : '/save'
		})
		.done(function(data) {
            var tooltip = document.getElementById('tooltip');
            $('.tooltiptext').html(data);
            tooltip.style.visibility = 'visible';
            tooltip.style.opacity = '1';
            setTimeout("tooltip.style.visibility = 'hidden';tooltip.style.opacity = '0';",2000);
		});

		event.preventDefault();
    });
});
