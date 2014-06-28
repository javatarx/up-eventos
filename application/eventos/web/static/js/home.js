require([
    'jquery',
//    'lib/youtube',
    'header',
    'form-hola'],
    function ($, header, hola) {
//        youtube.boot();
        hola.subscription();

});

require.config({
    urlArgs: "v=2.3"
});