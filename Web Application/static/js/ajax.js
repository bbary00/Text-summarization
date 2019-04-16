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
		.done(function(summary) {
		    document.getElementById("result").value = summary;
			$(".res").show();
			$(window).scrollTop($(".res").offset().top);

		});

		event.preventDefault();

	});

});
