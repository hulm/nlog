$(function(){

	$('#changePwdensure').click(function(){
		if ($('#changePwdError'))
		{$('#changePwdError').remove();}
		pwd1=$('#changePwd1').val()
		pwd2=$('#changePwd2').val()
		if (pwd1=='' || pwd2=='')
		{
			alert("密码不能为空")
		}
		else
		{
			if  (pwd1 != pwd2)
			{
				$('#changePwd2').after('<span id="changePwdError" style="color:red">两次输入的密码不匹配</span>')
			}
			else
			{
				$('#changePwd1').val('')
				$('#changePwd2').val('')
			}
		}
	})

	$('#changePwdcancel').click(function(){

		
	})
})