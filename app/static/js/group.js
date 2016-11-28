$(document).ready(function() {
	$("body").on("click", "#create_group_button", function(e){
		e.preventDefault();
		var csrftoken = getCookie('csrftoken');
		var name = $("#id_group_name").val();

		$.ajax({
			headers: { 'X-CSRFToken': csrftoken },
		    url: '/create-group',
		    type: 'POST',
		    data: {'group_name' : name},
		    success: function(response) {
		    	if(response.success){
		    		window.location.href = response.data.url;
		    	}
		    	else{
		    		var errors = JSON.parse(response.data.errors);
		    		$('.control-label').remove();
		    		if(errors.group_name){
			    		$('#id_group_name').before('<label for="id_group_name" class="control-label  requiredField">' + errors.group_name[0].message + '</label>');
			    	}
		    	}
		    }
		})
	});

	$("body").on("click", "#join_group_button", function(e){
		e.preventDefault();
		var csrftoken = getCookie('csrftoken');
		var code = $("#add_group_name").val();

		$.ajax({
			headers: {'X-CSRFToken' : csrftoken},
			url: '/add-group',
			type: 'POST',
			data: {'group_code' : code},
			success: function(response){
				if(response.success){
					window.location.href = response.data.url
				}
				else{
					$('.control-label').remove();
					$('#add_group_name').before('<label for="add_group_name" class="control-label  requiredField">' + response.data.errors[0]+ '</label>');
				}
			}
		})
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