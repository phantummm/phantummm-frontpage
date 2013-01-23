function loadUpdates(project) {
	$.getJSON("/updates.json?page=all&project="+project, function(data) {
		var out = '';
		var i = 1;
		$.each(data, function(key, val) {
			if( i++ % 2 ) {
				var col = "bgwhite";
			} else {
				var col = "bggray";
			}
			out += "\n\n<h3 class='" + col + "'><a href='#'><span class='updateproject'>[" + 
				val.project + "]</span>&nbsp;&nbsp;<span class='updatetitle'>" + 
				val.title + "</span><span class='updatetime'>" + val.timesince +
				" ago</span></a></h3>";
			out += "<div class='" + col + "'><p>" + val.description + "<br /><br />" +
				"<span class='updatelinks'><a href='" + val.url +
				"'>Link</a>";
			out += "</span></p></div>";
		});
		$("#projectfeed").append(out);
		$('#projectfeed').accordion({
			collapsible: true,
			active: false,
			heightStyle: 'content',
		});
	});
}