jQuery(document).ready(function($) {
  
  $("#hidden").hide();
  //$('form').hide();
  $('#edit').hide();
  var witness_count=0 ;

  /*var i=1;
    var rentF_data = [] ;
    for(i  ;i<34;i++){
      rentF_data.push('RentF'+i);
    }
    console.log(rentF_data)*/
  //form data
  function getData()
  {
    event.preventDefault();
    let form_data = $("#form").serializeArray();
    console.log(form_data);
    /*$.each(form_data, function(i, field){
      c="#value"+i;
      let txt = field.value ;
      $(c).text(txt);
    });*/
  }

  //validation of form
  function validater_func(){
    
    var name = document.getElementById("RentF1").value;
        var email = document.getElementById("RentF2").value;
        if (!name || !email) {
            //alert("Please fill out all required fields.");
            //event.preventDefault(); // Prevent form submission
            console.log('validated');
            exit();
            //return;
        }
  }
  //1st dropdown type
  $('.dist1').change( function () 
  {
    var dropdown = $('.dist1').val();
    if(dropdown == "individual")
    {
      //console.log('ok');
      $('.comp1').each ( function ()
      {
        $(this).hide();
      });
      $('.ind1').each ( function ()
      {
        $(this).show();
      });
    }
    else 
    {
      //console.log('ok');
      $('.comp1').each ( function ()
      {
        $(this).show();
      });
      $('.ind1').each ( function ()
      {
        $(this).hide();
      });
    }
    
  });

  //2nd dropdown type
  $('.dist2').change( function () 
  {
    var dropdown = $('.dist2').val();
    if(dropdown == "individual")
    {
      //console.log('ok');
      $('.comp2').each ( function ()
      {
        $(this).hide();
      });
      $('.ind2').each ( function ()
      {
        $(this).show();
      });
    }
    else 
    {
      //console.log('ok');
      $('.comp2').each ( function ()
      {
        $(this).show();
      });
      $('.ind2').each ( function ()
      {
        $(this).hide();
      });
    }
    
  });

  $("#add_witness").click(function(){
  var form_data = $("#form").serializeArray();
  
  var input_tag = document.createElement('input');
  var br_tag = document.createElement('br');
  var button = document.getElementById('add_witness');
  button.before(input_tag);
  button.before(br_tag);
  input_tag.setAttribute("placeholder","Eg: enter the name of witness");
  input_tag.setAttribute("id","RentF"+eval(witness_count+form_data.length));
  input_tag.setAttribute("class","form-control");
  input_tag.classList.add("opacity-75");
  witness_count++;
  event.preventDefault();
  });


  $('form').submit (function (){
    validater_func();
    //$('form').validater();
    $('#edit').show();
    $('#hidden').show();
    $('form').hide();
    event.preventDefault();
    getData();
  });

  
  $('#add_condition').click(function (){

    var button = document.getElementById('add_condition');
    var input_tag = document.createElement('input');
    var br_tag = document.createElement('br');
    button.before(input_tag);

    var add_li = document.createElement('button');
    button.before(add_li);

    input_tag.setAttribute("id","new_li");
    input_tag.setAttribute("required",'');

    add_li.setAttribute("class","btn");
    add_li.setAttribute("id","add");
    add_li.classList.add("btn-primary");
    add_li.innerText = 'add';
    add_li.style.marginLeft = '10px' ;

    var remove_input = document.createElement('button');
    remove_input.setAttribute("class","btn");
    remove_input.setAttribute("id","remove_input");
    remove_input.classList.add("btn-primary");
    remove_input.innerText = 'remove input tag';
    remove_input.style.marginLeft = '10px' ;
    button.before(remove_input);

    br_tag.setAttribute("id","remove_br");
    button.before(br_tag);
    //console.log('condition added');
  });
  $("#edit").click(function(){
    var input_tag = document.getElementById('new_li');
    if (input_tag == null)
    {
    $('#edit').hide();
    $('#hidden').hide();
    $('form').show();
    event.preventDefault();
    }
    else if(!input_tag.value)
    {
      $('#warning').innerHTML = '<div class="alert alert-danger" role="alert">Either fill the input and add or remove the input field</div>';
      input_tag.focus();
      return;
    }
    /*var button = document.getElementById('add_condition');

    button.before(li_tag);
    
    $('#hidden').hide();
    $('form').show();
    event.preventDefault();*/
  });

  
  $(document).on("click", "#remove_input", function(){
    var input_tag = document.getElementById('new_li');
    var button_tag = document.getElementById('add');
    var button_remove_input_tag = document.getElementById('remove_input');
    var remove_br_tag = document.getElementById('remove_br');
    remove_br_tag.remove();
    button_remove_input_tag.remove();
    input_tag.remove();
    button_tag.remove();
    $('.alert').remove();
  });
  
  $(document).on("click", "#add", function(){
    var input_tag = document.getElementById('new_li');
    if(!input_tag.value)
    {
      document.getElementById('warning').innerHTML = '<div class="alert alert-danger" role="alert">Either fill the input and add or remove the input field</div>';
      input_tag.focus();
      return;
    }
    $('#warning').hide();
    var button_remove_input_tag = document.getElementById('remove_input');
    button_remove_input_tag.remove();
    var remove_br_tag = document.getElementById('remove_br');
    remove_br_tag.remove();
    //console.log('removing element');
    var li_tag = document.createElement('li');
    var input_tag = document.getElementById('new_li');
    var button_tag = document.getElementById('add');
    li_tag.innerHTML = input_tag.value ;
    input_tag.remove();
    button_tag.remove();
    var button = document.getElementById('add_condition');
    button.before(li_tag);
  });

  $("#print").click(function(){
    var input_tag = document.getElementById('new_li');
     if (input_tag == null)
    {
      $('#add_condition').hide();
    //$('#edit').hide();
    //$("#print").hide();
    var element = document.getElementById('hidden');
    var Openwindow ;
    var opt = {
    margin:  0.5,
    jsPDF: {
      format: 'a4'
    },
    filename:     'myfile.pdf',
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2 },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
    pagebreak: { mode: 'css' , before:'.page_break_before' }
    };
    html2pdf().set(opt).from(element).toPdf().get('pdf').then(function (pdf) {
      Openwindow = window.open(pdf.output('bloburl'), '_blank');
      if(!Openwindow.closed)
      {
        $('#add_condition').show();
      }
    });
    //$("#print").show();
    
    
    
    }
    else if(!input_tag.value)
    {
      document.getElementById('warning').innerHTML = '<div class="alert alert-danger" role="alert">Either fill the input and add or remove the input field</div>';
      input_tag.focus();
    }
    
    
  });
  
    
});