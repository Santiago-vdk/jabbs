$(window).scroll(function() {

    if ($(this).scrollTop()>20)
     {
        $('.menu').fadeOut();
     }
    else
     {
      $('.menu').fadeIn();
     }
 });




$(function() {
  $("#keywords").autocomplete({
    source: "../get_jobs",
    minLength: 2,
  });
});



$(document).ready(function () {



$("#keywords").on("keyup click input", function () {
if (this.value.length > 0) {

  $(".row").show().filter(function () {
    return $(this).find('.ui_name').text().toLowerCase().indexOf($("#keywords").val().toLowerCase()) == -1;
  }).hide();
}
else {
  $(".row").show();
}
});



$("#location").on("keyup click input", function () {
if (this.value.length > 0) {

  $(".row").show().filter(function () {
    return $(this).find('.ui_location').text().toLowerCase().indexOf($("#location").val().toLowerCase()) == -1;
  }).hide();
}
else {
  $(".row").show();
}
});




});

$(document).on('click','.main-content',function(){

	$('#keywords').val('');
	$('#keywords').select();
		$("#keywords").blur();
});