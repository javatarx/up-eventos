define([
    'jquery',
    'vendor/jquery.form',
    'vendor/jquery.validate',
    ], function ($) {
    return{
        subscription : function(callbackFocus){
            var $formulario     = $('#subscription'),
                $confirmacion   = $(".subscription .msg"),
                $email          = $(".subscription .email"),
                $name           = $('.subscription .name'),
                $submit         = $('.subscription .submit');

            $email.focus(function(){
                $name.parent().removeClass('hidden');
                $formulario.parent().addClass('displayed');
                if(callbackFocus){
                    callbackFocus();
                }
            });
            
            $formulario.validate();

            var email_gmail,
                dominio,
                form_content;
            $formulario.ajaxForm({
                clearForm: true,
                beforeSubmit: function (arr, $form, options)
                {
                    $confirmacion.text("Inscribiendote...").fadeOut().fadeIn();
                    email_gmail  = arr[0].value;
                    dominio      = email_gmail.split('@')[1];
                    form_content = $form;
                },
                success: function (datos)
                {
                    datos = JSON.parse(datos);
                    if(dominio === "gmail.com"){
                        $('.bird').hide();
                        form_content.parent().slideUp();
                        $('.user-mail').text(email_gmail);
                        $('.gmail-message').slideDown();
                    }
                    if(datos.code == "214")
                    {
                        $('.bird').hide();
                        $confirmacion.text("Ya eras parte de nuestra comunidad, sigue compatiendo").fadeOut().fadeIn();
                    }
                    else if(datos.error)
                    {
                        $confirmacion.text("A ocurrido un error. intentalo nuevamente").fadeOut().fadeIn();
                        $email.focus();
                    }
                    else
                    {
                        $confirmacion.text("Ya eres parte de nuestra comunidad, muchas gracias").fadeOut().fadeIn();
                    }
                }
            });
        }
    };

});

