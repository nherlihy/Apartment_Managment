$(document).ready(function()){

	$("body").on("click", "expenseButton", function(e)){
		e.preventDefault();
		var cost = $("#id_expense_cost").val();
		var payTo = $("#id_expense_pay_to").val();
	}
}