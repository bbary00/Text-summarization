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
			alert(data);
			// if (data.error) {
			// 	$('#errorAlert').text(data.error).show();
			// 	$('#successAlert').hide();
			// }
			// else {
			// 	$('#successAlert').text(data.name).show();
			// 	$('#errorAlert').hide();
			// }

		});

		event.preventDefault();

	});

});