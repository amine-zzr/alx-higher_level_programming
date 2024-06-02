$(document).ready(function() {
  $('#btn_translate').click(function() {
    let languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'GET',
      dataType: 'json',
      data: { lang: languageCode },
      success: function(response) {
        $('#hello').text(response.hello);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        $('#hello').text('Error fetching translation.');
        console.error('Error:', textStatus, errorThrown);
      }
    });
  });

  $("#language_code").keypress(function(event) {
        if (event.which == 13) { // this is the Enter key event code
            $("#btn_translate").click();
        }
    });
});
