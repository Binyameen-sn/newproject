$(document).ready(function()
{	
$('#login').click(function()
	{
	var name=$("#email").val();
	var paswd=$("#password").val();
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
	$.ajax(
	{
		'url':'http://services.trainees.baabtra.com/LoginService/login.php',
		'DataType':'jsonp',
		'data':{email:name,password:paswd},
		success:function(data)
		{
			console.log(data);
			var json = $.parseJSON(data);
			console.log(json[0].Msg)
			if(json[0].ResponseCode=="200")
			{
				window.location.href="/facebooklog/success?email="+json[0].vchr_first_name+"&&name="+json[0].vchr_first_name;
			}
			else if(json[0].ResponseCode=="500")
			{
				window.location.href="/facebooklog/fberror?email="+json[0].vchr_user_name+"&&name="+json[0].vchr_first_name;
			}
			else
			{
				window.location.href="/facebooklog/fberror2";
			}
			console.log(json[0].ResponseCode)
			$("#contact").html(data);
		},
		error:function()
		{
			alert("error");
		}
	});
});

});