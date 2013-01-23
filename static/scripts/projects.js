$("#projectdialog").dialog({ autoOpen: false });
$("#opener").click( function() {
	$("#projectdialog").dialog("open");
});

function accordionize() {
	$('#projectlist').accordion({
		collapsible: true,
		active: false,
		heightStyle: 'content',
	});
}

window.onLoad = accordionize();