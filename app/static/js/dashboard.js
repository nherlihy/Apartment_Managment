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
			$('#pay_to_error').remove();
	        $('#div_id_pay_to').removeClass();
	        $('#id_pay_to').before('<label for="id_username" id="pay_to_error" class="control-label  requiredField">This field is required</label>');
	        $('#div_id_pay_to').addClass('form-group has-error has-feedback');
	        return;
		}

		else{
			$('#pay_to_error').remove();
			$('#div_id_pay_to').removeClass();

			var csrftoken = getCookie('csrftoken');
			$.ajax({
				headers: { 'X-CSRFToken': csrftoken },
		    	url: 'ajax/add-expense',
		    	type: 'POST',
		    	data: {'description' : description, 'cost': cost, 'pay_to' : pay_to, 'due_by' : date},
		    	success: function(response){
		    		if(response.success){
		    			var expense = JSON.parse(response.data.expense)[0];
		    			var date_split = expense.fields.due_by.split('-');
		    			var date = date_split[1] + '-' + date_split[2] + '-' + date_split[0];
			    		$('#expenses_table tr:first').after('<tr><td id="expense_number"> ' + expense.pk +'</td><td id="expense_name"> ' + expense.fields.description + ' </td> \
                    										  <td id="expense_due"> ' + date + ' </td><td id="expense_cost"> ' + expense.fields.cost + '</td><td>NA</td></tr>');
		    		}
		    		else{
		    			var errors = JSON.parse(response.data.errors);
		    			if(errors.description){
		    				$('#description_error').remove();
	        				$('#div_id_description').removeClass();
		    				$('#id_description').before('<label for="id_username" id="description_error" class="control-label  requiredField">' + errors.description[0].message + '</label>');
                   	 		$('#div_id_description').addClass('form-group has-error has-feedback');
		    			}
		    			else{
		    				$('#div_id_description').removeClass();
		    				$('#description_error').remove();
		    			}
		    			if(errors.cost){
		    				$('#cost_error').remove();
	        				$('#div_id_cost').removeClass();
		    				$('#id_cost').before('<label for="id_username" id="cost_error" class="control-label  requiredField">' + errors.cost[0].message + '</label>');
                   	 		$('#div_id_cost').addClass('form-group has-error has-feedback');
		    			}
		    			else{
		    				$('#div_id_cost').removeClass();
		    				$('#cost_error').remove();
		    			}
		    		}
		    	}
			})
		}
	})

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});