$(document).ready(function() {

    $('.nav-tabs > li a').click(function(){
        $('.nav-tabs > li').removeClass('active');
        $(this).parent().addClass('active');
        $('.tab-content > div').hide('fast');
        $($(this).attr('href')).show('fast');
        return false;
    });
});
