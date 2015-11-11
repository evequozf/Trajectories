

var settings = {
	size: 20,
	random: false
}




$(document).ready(function() {
	$('#sidebar')
	.sidebar()	

	$("#divUpload2").on("click", function() {
	$('#new-file2').click()
	})

	$("#divUpload1").on("click", function() {
	$('#new-file1').click()
	})


    $('#hexagon').click(function() { settings.element = 'hexagon' })
    $('#square').click(function() { settings.element = 'square' })
    $('#line').click(function() { settings.element = 'line' })

    $('#inline').click(function() { settings.organization = 'inline' })
    $('#center').click(function() { settings.organization = 'center' })
    $('#border').click(function() { settings.organization = 'border' })

	$('#size').val(settings.size)

	$('#random').click(function() {
		( settings.random ) ? settings.random = false : settings.random = true
		console.log(settings)
	})
	
	$('#cast').click(function() {
		settings.size = parseInt($('#size').val())
		// settings.random = $('#random').val()
		console.log(settings)

		
		
	})
	

	$('#example_1').click(function() {
		settings.data = $.ajax('exemple.txt')
			.done(function(data) {
				var ids = [],
					sources = [],
					targets = [],
					weights = []
				var lines = data.split('\n')
				for ( var i = 0 in lines ) {
					var line = lines[i].split('\t')
					sources.push(line[0])
					targets.push(line[1])
					weights.push(line[2])
					if ( ids.indexOf(line[0]) < 0 ) ids.push(line[0])
					if ( ids.indexOf(line[1]) < 0 ) ids.push(line[1])
				}
				console.log([ids, sources, targets, weights])
				return([ids, sources, targets, weights])
				
			})
	})



})