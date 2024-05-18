$(document).ready(function(){
	var add = document.getElementById('add_button');
	add.addEventListener('click',function (){
		const input = '<div class="fields"><input type="text" class="form-control" placeholder="Enter the url of the pdf" required name="url"></div><div class="submit"><button class="btn btn-success">Convert</button></div>';
		$('form').append(input);
	});
});