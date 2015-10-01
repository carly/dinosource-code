$(document).ready(function () {
  $('.element').on('click', function() {
    

    var elementTag = 'trex-' + this.innerHTML;
    $('.' + elementTag).toggleClass('highlight');

    // Toggle entire table rows 
    $(this).toggleClass('highlight');
    $(this).next().toggleClass('highlight');

  });

});
