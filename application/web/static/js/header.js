define([
    'jquery'],
    function ($) {
        var  $openMenu = $('.display-menu'),
        $cerrar    = $('.close-editar'),
        $menu = $('.menu');
        
        var base = {
            subMenu : function(){
                var self = this;
                $('.tab[data-display]').on('click',function(e){
                    e.preventDefault();
                    if(!$(this).hasClass('active')){
                        self.subMenu.prototype.open(this);
                    }else{
                        self.subMenu.prototype.close(this.getAttribute('data-display'));
                    }
                });
                this.subMenu.prototype.open = function(elemento) {
                    var data = $(elemento).data('display');
                    $('.'+data).slideDown();
                    $(elemento).addClass('active');
                };
                
                this.subMenu.prototype.close = function(elemento) {
                    $('.'+elemento).slideUp();
                    $('[data-display='+elemento+']').removeClass('active');
                };

            },
            abrir : function(){
                var self = this;
                $openMenu.on('click',function(){
                    if(!$(this).hasClass('active')){
                       $menu.slideDown();
                       $(this).addClass('active');
                    }else{
                       $menu.slideUp();
                       $(this).removeClass('active');
                       self.subMenu.prototype.close('social-login');
                    }
                });
            },
            boot: function () {
                this.abrir();
                this.subMenu();
            },
        };
        base.boot();

});
