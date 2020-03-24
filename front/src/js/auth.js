function Auth() {}

Auth.prototype.ListenSigninEvent = function () {
    var username = $("#username");
    var password = $("#password");
    var remember = $("#remember");
    var submit = $("#submit");
    submit.click(function () {
        var username_val = username.val();
        var password_val = password.val();
        var remember_val = remember.prop("checked");

        xfzajax.post({
            url : "/auth/",
            data: {
                "username" : username_val,
                "password" : password_val,
                "remember" : remember_val?1:0
            },
            // 'success':function (result) {
            //     if(result['code']===200) {
            //         window.location.reload();
            //     }
            // },
        });
    })
};

Auth.prototype.run = function () {
    this.ListenSigninEvent();
};

//当html代码全部执行完后，执行此段代码
$(function () {
    var auth = new Auth();
    auth.run();
});