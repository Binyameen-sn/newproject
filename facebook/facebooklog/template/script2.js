$(document).ready(function()
{	
$('#login').click(function()
	{
	var name=$("#email").val();
	var paswd=$("#password").val();
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
				window.location.href="facebook2.html?email="+json[0].vchr_first_name;
			}
			else if(json[0].ResponseCode=="500")
			{
				window.location.href="fberror.html?email="+json[0].vchr_first_name;
			}
			else
			{
				window.location.href="fberror2.html";
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