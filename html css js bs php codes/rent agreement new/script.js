$(document).ready(function(){
    $('form').hide();
    $('#print').click(function ()
    {
        var pdf = new jsPDF('p', 'pt', 'letter');
        
        source = $('#hidden').get(0);
        
        specialElementHandlers = {
            
            '#bypassme': function (element, renderer) {
                
                return true
            }
        };
        margins = {
            top: 80,
            bottom: 60,
            left: 40,
            width: 522
        };

        pdf.fromHTML(
        source, 
        margins.left, 
        margins.top, { 
            'width': margins.width,
            align : "justify",
            'elementHandlers': specialElementHandlers
        },

        function (dispose) {

        }, margins);
        pdf.output("dataurlnewwindow");
        
            /*const data = document.getElementById('hidden');
            // console.log(data);
    
            html2canvas(data).then((canvas) => {
                // Few necessary setting options
                const imgWidth = 208;
                const pageHeight = 295;
                const imgHeight = canvas.height * imgWidth / canvas.width;
                const heightLeft = imgHeight;
    
                const contentDataURL = canvas.toDataURL('image/png');
                const pdf = new jsPDF('p', 'mm', 'a4'); // A4 size page of PDF
                const position = 0;
                pdf.addImage(contentDataURL, 'PNG', 0, position, imgWidth, imgHeight);
                pdf.save('ikismail.pdf'); // Generated PDF
            });*/
        
    
    });
  });