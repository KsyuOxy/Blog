$(document).ready(function () {
    console.log('ready works');

    let valid_login = false;
    let valid_email = false;
    let valid_passwd = false;
    let valid_passwd_confirm = false;

    let loginExp = /^[a-zA-Z0-9][a-zA-Z0-9_]{4,14}$/;
    let regExp_email = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    let regExp_passwd = /(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z*]{8,}/

    //----------------------------------------------------------------
    $('#login_field').change(function () {
        let _login = $(this).val()

        if (!loginExp.test(_login)){
            $('#login_icon').attr('src', '../../static/img/remove.png')
            $('#login_error').text('Длина должна быть 5-15 и состоять из букв и цифр')
            valid_login = false;
        }else{
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login_field=' + _login,
                success: function(result){
                    if (result.message_login === 'занят'){
                        $('#login_icon').attr('src', '../../static/img/remove.png')
                        $('#login_error').text('Логин уже занят')
                        valid_login = false;
                    }else{
                        $('#login_icon').attr('src', '../../static/img/check.png')
                        $('#login_error').text('')
                        valid_login = true;
                    }
                }
            })
        }
    })
    $('#login_field').focus(function () {
        $('#login_icon').attr('src', '../../static/img/question.png')
        $('#login_error').text('')
    })
    //----------------------------------------------------------------
    $('#email_field').blur(function () {
        let _email = $(this).val()
        if (regExp_email.test(_email)){
            $('#email_icon').attr('src', '../../static/img/check.png')
            $('#email_error').text('')
            valid_email = true;
        }else{
            $('#email_icon').attr('src', '../../static/img/remove.png')
            $('#email_error').text('Не валидный email')
            valid_email = false;
        }
    })
    $('#email_field').focus(function () {
        $('#email_icon').attr('src', '../../static/img/question.png')
        $('#email_error').text('')
    })

    //----------------------------------------------------------------
    $('#password_field').blur(function () {
        let _password = $(this).val()

        if (regExp_passwd.test(_password)){
            $('#password_icon').attr('src', '../../static/img/check.png')
            $('#password_error').text('')
            valid_passwd = true;
        }else{
            $('#password_icon').attr('src', '../../static/img/remove.png')
            $('#password_error').text('Должно быть не менее 8 символов, цифра, буква в верхнем и нижнем регистре')
            valid_passwd = false;
        }
    })
    $('#password_field').focus(function () {
        $('#password_icon').attr('src', '../../static/img/question.png')
        $('#password_error').text('')
    })

    //----------------------------------------------------------------
    $('#password_confirmation_field').blur(function () {
        let _password_confirm = $(this).val()

        if (_password_confirm === $('#password_field').val()){
            $('#password_confirm_icon').attr('src', '../../static/img/check.png')
            $('#password_confirm_error').text('')
            valid_passwd_confirm = true;
        }else{
            $('#password_confirm_icon').attr('src', '../../static/img/remove.png')
            $('#password_confirm_error').text('Должен соответствовать паролю, введённому в предыдущем поле')
            valid_passwd_confirm = false;
        }
    })
    $('#password_confirmation_field').focus(function () {
        $('#password_confirm_icon').attr('src', '../../static/img/question.png')
        $('#password_confirm_error').text('')
    })

    //----------------------------------------------------------------

    $('#submit').click(function () {
        if (
            valid_login === true &&
            valid_email === true &&
            valid_passwd === true &&
            valid_passwd_confirm === true
        ){
            $('.form-group').attr( 'onsubmit', 'return true')
        }
    })
    //----------------------------------------------------------------
})
