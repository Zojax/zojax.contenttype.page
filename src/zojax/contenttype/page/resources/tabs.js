$(document).ready(function() {

    $('.page-nav-tabs > li a').click(function(){
        $('.page-nav-tabs > li').removeClass('active');
        $(this).parent().addClass('active');
        $('.tab-content > div').hide('slow');
        $($(this).attr('href')).show('slow');
        return false;
    });
});
