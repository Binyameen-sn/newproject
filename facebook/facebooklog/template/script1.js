$(document).ready(function(){
	
$("#login").click(function(){
	
	var name= $("#email").val();
	var password=$("#password").val();
	if(name=="")
	{
		$("#demo").text("please enter email");
	}
	else if(password=="")
	{
		$("#demo").text("");
		$("#demo1").text("plese enter password");
	}
	else
	{
		$("#demo1").text("");
		alert("login successful")
	}
})

});