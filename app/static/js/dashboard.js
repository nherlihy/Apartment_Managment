$(document).ready(function() {
	$('#id_pay_to').width('70%');

	$('body').on('click', '#expense_submit', function(e){
		e.preventDefault();

		var description = $('#id_description').val();
		var total_cost = $('#id_total_cost').val();
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
		    	data: {'description' : description, 'total_cost': total_cost, 'pay_to' : pay_to, 'due_by' : date},
		    	success: function(response){
		    		if(response.success){
		    			var expense = JSON.parse(response.data.expense)[0];
		    			var due_date_split = expense.fields.due_by.split('-');
		    			var create_date_split = expense.fields.date_added.split('-');
		    			var due_date = due_date_split[1] + '-' + due_date_split[2] + '-' + due_date_split[0];
		    			var create_date = create_date_split[1] + '-' + create_date_split[2] + '-' + create_date_split[0];

		    			if(response.data.pay_to == response.data.request_user){
		    				var button = '<button type="button" id="' + expense.pk + '" class="btn btn-danger btn-sm">Clear Payment</button>' 
		    			}
		    			else{
		    				var button = 'Pending'
		    			}

			    		$('#expenses_table tr:first').after('<tr><td id="expense_number">' + button + '</td><td id="expense_name"> ' + expense.fields.description + ' </td> \
                    										  <td id="expense_created">' + create_date + ' <td id="expense_due"> ' + due_date + ' </td><td id="expense_cost">$' + expense.fields.total_cost + '</td> \
                    										  <td>$' + expense.fields.split_cost + '</td><td id="pay_to">' + response.data.pay_to + ' </td></tr>');
			    		$('#expense_modal').modal('hide');
		    		}
		    		else{
		    			var errors = JSON.parse(response.data.errors);
		    			if(errors.description){
		    				$('#description_error').remove();
	        				$('#div_id_description').removeClass();
		    				$('#id_description').before('<label for="id_description" id="description_error" class="control-label  requiredField">' + errors.description[0].message + '</label>');
                   	 		$('#div_id_description').addClass('form-group has-error has-feedback');
		    			}
		    			else{
		    				$('#div_id_description').removeClass();
		    				$('#description_error').remove();
		    			}
		    			if(errors.total_cost){
		    				$('#total_cost_error').remove();
	        				$('#div_id_total_cost').removeClass();
		    				$('#id_total_cost').before('<label for="id_total_cost" id="total_cost_error" class="control-label  requiredField">' + errors.total_cost[0].message + '</label>');
                   	 		$('#div_id_total_cost').addClass('form-group has-error has-feedback');
		    			}
		    			else{
		    				$('#div_id_total_cost').removeClass();
		    				$('#total_cost_error').remove();
		    			}
		    		}
		    	}
			})
		}
	})

	$('body').on('click', '.btn.btn-danger', function(e){
		e.preventDefault();
		var id = $(this).attr('id');
		$(this).hide();

		var td = $(this).parent();
		td.append('Confirm:<button type="button" class="btn btn-link" id="yes">Yes</button><button type="button" id="no" class="btn btn-link">No</button>');
	})

	$('body').on('click', '.btn.btn-link', function(e){
		e.preventDefault();
		if($(this).attr('id') == 'no'){
			var button = $(this).prev().prev().show();
			var td = button.parent();
			td.empty();
			td.append(button);
		}
		else{
			var id = $(this).prev().attr('id');
			var csrftoken = getCookie('csrftoken');

			$.ajax({
				headers: { 'X-CSRFToken': csrftoken },
		    	url: 'ajax/clear-expense',
		    	type: 'PUT',
		    	data: {'id' : id},
		    	success: function(response){
		    		var expense = JSON.parse(response.data.expense)[0];
		    		$('#' + id).parent().parent().remove();

		    		var due_date_split = expense.fields.due_by.split('-');
		    		var create_date_split = expense.fields.date_added.split('-');
		    		var due_date = due_date_split[1] + '-' + due_date_split[2] + '-' + due_date_split[0];
		    		var create_date = create_date_split[1] + '-' + create_date_split[2] + '-' + create_date_split[0];

			    		$('#expenses_table tr:first').after('<tr><td id="expense_number">Payed</td><td id="expense_name"> ' + expense.fields.description + ' </td> \
                    										  <td id="expense_created">' + create_date + ' <td id="expense_due"> ' + due_date + ' </td><td id="expense_cost">$' + expense.fields.total_cost + '</td> \
                    										  <td>$' + expense.fields.split_cost + '</td><td id="pay_to">' + response.data.pay_to + ' </td></tr>');
		    	}
		});

	}
	});

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