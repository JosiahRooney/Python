jQuery(function($){
    $(document).ready(function(){

        $('#pw_inp').on('input',function(){
            var inp = $(this).val();
            if (inp.length >= 8) {
                $('#eight_char').css('color','#0a0').css('font-weight','bold');
            } else {
                $('#eight_char').css('color','#999').css('font-weight','500');
            }
            var re = /[A-Z]/
            if ( inp.search(re) != -1 ) {
                $('#one_upper').css('color','#0a0').css('font-weight','bold');
            } else {
                $('#one_upper').css('color','#999').css('font-weight','500');
            }
            var re = /[\!\@\#\$\%\^\&\*\(\)\_\+\\\<\>\?\/]/
            if ( inp.search(re) != -1 ) {
                $('#one_spec').css('color','#0a0').css('font-weight','bold');
            } else {
                $('#one_spec').css('color','#999').css('font-weight','500');
            }
        });

        $('#pw_conf, #pw_inp').on('input',function(){
            var inp = $('#pw_conf').val();
            var pw = $('#pw_inp').val();
            if ( inp == pw ) {
                $('#matches').css('color','#0a0').css('font-weight','bold');
            } else {
                $('#matches').css('color','#999').css('font-weight','500');
            }
        });

    });
});