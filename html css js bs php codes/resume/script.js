$(document).ready(function(){
    //generate pdf
    $('.parent').each(function (i) {
      $(this).hide();
    });
    console.log('ready')
    $('#hide').click(function (){
      $('.parent').each(function (i) {
        $(this).hide();
      });
    });
    $("#print").click(function () {
        console.log('printing');
        $('.parent').each(function (i) {
          $(this).show();
        });
        var element = document.getElementsByClassName('parent');
        for (i=0;i<4;i++){
          var opt = {
            margin:       1,
            jsPDF: {
              format: 'a4'
            },
            filename:     'myfile.pdf',
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2 },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
            pagebreak: { mode: 'avoid-all' , before: '#page2el'  }
            };
            html2pdf().set(opt).from(element[i]).save();
          
        }
        /*$('.parent').each(function (i) {
          $(this).hide();
        });*/
    });
});