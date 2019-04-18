$(document).ready(function() {

	$('#press').on('click', function(event) {
        var range;
	    var sent = $('#form').val();
	    var rangeValue = document.getElementById("rangeValue");
        if(rangeValue.innerHTML === undefined || rangeValue.innerHTML == ""){
            range = null
        }else{
            range = $('#range').val();
            sent = null;
        }
		$.ajax({
			data : {
				text : $('#area').val(),
				sentence : sent,
				percentage : perc
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

});
