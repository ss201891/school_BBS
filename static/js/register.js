function bindEmailCaptchaClick(){
    $('#captcha-btn').click(function (event){
        $this = $(this);
        event.preventDefault();
        var email = $("input[name='email']").val();
        $.ajax({
            url: '/auth/captcha/email?email='+email,
            method: 'GET',
            success: function (result){
                var code = result['code'];
                if (code == 200){
                    var countdown = 60
                    $this.off('click')
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown <= 0){
                            clearInterval(timer);
                            $this.text('获取验证码')
                            bindEmailCaptchaClick()
                        }
                    }, 1000);
                    alert('验证码发送成功');
                }else {
                    alert(result['message']);
                }
            },
            fail: function (error){
                console.log(error)
            }
        })
    });
}


//整个网页都加载完后再执行
$(function (){
    bindEmailCaptchaClick()
});