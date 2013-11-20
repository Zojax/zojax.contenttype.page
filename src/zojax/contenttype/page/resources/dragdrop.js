$(document).ready(function() {

    // Sort
    $(".z-form-field .multi-widget").children().each(function(index) {
        if ($(this).attr('id') == 'form-widgets-tabs-'+index+'-row') {
            $('#form-widgets-tabs-'+index+'-widgets-position').val(index);
        }
    });

    $( ".z-form-field .multi-widget" ).sortable({
        connectWith: ".z-form-field .multi-widget",
        axis: "y",
        update: function(event, ui) {
            parent = ui.item.parent();
            parent.children().each(function(index) {
                var Id = $(this).attr('id');
                Id = Id.replace('form-widgets-tabs-', '');
                Id = Id.replace('-row', '');
                $('#form-widgets-tabs-'+Id+'-widgets-position').val(index);
            });
        }
    }).disableSelection();

    // Expand-collapse
    $(".z-form-field .multi-widget .row > div.widget").hide();

    $(".z-form-field .multi-widget .row > div.label").addClass("closed");

    var toggleItem = function() {
        var $glideElement = $(this);
	    if ($glideElement.next().is(":hidden")) {
		    // show it
		    $glideElement.removeClass("closed");
		    $glideElement.addClass("open");
		    $glideElement.next().slideDown();
	    } else {
		    // hidde it
		    $glideElement.removeClass("open");
		    $glideElement.addClass("closed");
		    $glideElement.next().slideUp();
	    }
	    return false;
    }

    $(".z-form-field .multi-widget .row > div.label").click(toggleItem);
});
