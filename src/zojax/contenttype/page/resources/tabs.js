$(document).ready(function() {
    $('.page-nav-tabs > li a').click(function(){
        if ($(this).parent().hasClass('active'))
            return false;
        $('.page-nav-tabs > li').removeClass('active');
        $(this).parent().addClass('active');
        var self = this;
        $('.tab-content > div:visible').hide("slide", { direction: "left" },  200, function(){
            $($(self).attr('href')).show("slide", { direction: "left" }, 200);
        });
        return false;
    });
});
