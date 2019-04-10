$(document).ready(function() {

	$('#press').on('click', function(event) {

		$.ajax({
			data : {
				text : $('#area').val(),
				sentence : $('#form').val()
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