$(document).ready(function() {
	$('#id_pay_to').width('70%');

	$('body').on('click', '#expense_submit', function(e){
		e.preventDefault();

		var description = $('#id_description').val();
		var cost = $('#id_cost').val();
		var pay_to = $('#id_pay_to').val();
		var month = $('#id_due_by_month').val();
		var day = $('#id_due_by_day').val();
		var year = $('#id_due_by_year').val();
		var date = month +'/' + day + '/' + year;

		if(!pay_to){
	        $('#div_id_pay_to').removeClass();
	        $('#id_pay_to').before('<label for="id_username" class="control-label  requiredField">This field is required</label>');
	        $('#div_id_pay_to').addClass('form-group has-error has-feedback');
	        return;
		}

		else{

		}
	})
});