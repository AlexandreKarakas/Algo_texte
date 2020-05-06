$(document).ready(function() {
	$('#mode').on('click', function() {
		var isChecked = $('#mode').is(':checked');
		if(isChecked == true) {
			$('body').css('background-color','#2a2d31');
			$('body').css('color','#fdf6f3');
		} else {
			$('body').css('background-color','white');
			$('body').css('color','black');
		}
	});
	$('#lang').on('click', function() {
		var lang = $('#lang').attr('src');
		if(lang == './Images/france.png') {
			lang = './Images/uk.png';
			$('#lang').attr('src',lang);

			$('#searchGEP').attr('value','GoogleEco+ Search');
			$('label[for="textToSearch"]').html('Write the text to search');
		} else {
			lang = './Images/france.png';
			$('#lang').attr('src',lang);
			
			$('#searchGEP').attr('value','Rechercher via Google-Eco+');
			$('label[for="textToSearch"]').html('Ecrivez le texte à rechercher');
		}
	});
});