$(document).ready(function() {

    $('.nav-tabs > li a').click(function(){
        $('.nav-tabs > li').removeClass('active');
        $(this).parent().addClass('active');
        $('.tab-content > div').removeClass('active');
        $($(this).attr('href')).addClass('active');
        return false;
    });
});
