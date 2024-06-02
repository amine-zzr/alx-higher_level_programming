$(document).ready(function() {
  $('#btn_translate').click(function() {
    let languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
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
});
