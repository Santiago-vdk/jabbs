$(window).scroll(function() {

    if ($(this).scrollTop() > 20) {
        $('.menu').fadeOut();
    } else {
        $('.menu').fadeIn();
    }
});




$(function() {
    $("#keywords").autocomplete({
        source: "../get_jobs",
        minLength: 2,
    });
});



$(document).ready(function() {
    $("#keywords").on("keyup click input", function() {
        if (this.value.length > 0) {

            $(".row").show().filter(function() {
                return $(this).find('.ui_name').text().toLowerCase().indexOf($("#keywords").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });



    $("#location").on("keyup click input", function() {
        if (this.value.length > 0) {

            $(".row").show().filter(function() {
                return $(this).find('.ui_location').text().toLowerCase().indexOf($("#location").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });

    $("#option_freelance").click(function() {
        if (!($("#option_freelance").is(':checked'))) {
            $(".row").show().filter(function() {
                return $(this).find('.ui_type').text().toLowerCase().indexOf($("#option_freelance").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });

    $("#option_fulltime").click(function() {
        if (!($("#option_fulltime").is(':checked'))) {
          console.log($("#option_fulltime").val())
          
            $(".row").show().filter(function() {
                return $(this).find('.ui_type').text().toLowerCase().indexOf($("#option_fulltime").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });

    $("#option_temporary").click(function() {
        if (!($("#option_temporary").is(':checked'))) {
            $(".row").show().filter(function() {
                return $(this).find('.ui_type').text().toLowerCase().indexOf($("#option_temporary").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });

    $("#option_internship").click(function() {
        if (!($("#option_internship").is(':checked'))) {
            $(".row").show().filter(function() {
                return $(this).find('.ui_type').text().toLowerCase().indexOf($("#option_internship").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });

    $("#option_parttime").click(function() {
        if (!($("#option_parttime").is(':checked'))) {
            $(".row").show().filter(function() {
                return $(this).find('.ui_type').text().toLowerCase().indexOf($("#option_parttime").val().toLowerCase()) == -1;
            }).hide();
        } else {
            $(".row").show();
        }
    });


});

$(document).on('click', '.main-content', function() {
    $('#keywords').val('');
    $('#keywords').select();
    $("#keywords").blur();
});