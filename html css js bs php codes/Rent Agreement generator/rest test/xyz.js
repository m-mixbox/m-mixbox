$(document).ready(function(){
    //generate pdf
  $("#print").click(function(){
      
  var element = document.getElementById('results');
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
  html2pdf().set(opt).from(element).save();
  });
  });