jQuery(function($){
    $(document).ready(function(){
        var gold = $('#gold').data('gold');

        if (gold < 50) {
            $('#casino').attr('disabled','disabled');
        } else {
            $('#casino').removeAttr('disabled')
        }
    });
});