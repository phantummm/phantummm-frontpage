var feed = document.getElementById("feedlist");
var feederror = document.getElementById("feederror");
var feedbutton = document.getElementById("loadmorebutton");
var pagenum = 1;

function feedGetter(page) {
	$.getJSON('/updates.json?page='+page, function(data) {
		var out = '';
		var i = 1;
		if(!data) {
			pagenum--;
			return;
		}
		$.each(data, function(key, val) {
			if( i++ % 2 ) {
				col = "bgwhite";
			} else {
				col = "bggray";
			}
			out += "\n\n<h3 class='" + col + "'><a href='#'><span class='updateproject'>[" + 
				val.project + "]</span>&nbsp;&nbsp;<span class='updatetitle'>" + 
				val.title + "</span><span class='updatetime'>" + val.timesince +
				" ago</span></a></h3>";
			out += "<div class='" + col + "'><p>" + val.description + "<br /><br />" +
				"<span class='updatelinks'><a href='" + val.url +
				"'>Link</a>";
			if(val.project_url) {
				out += "&nbsp;|&nbsp;<a href='" + val.project_url +
					"'>Project link</a>";
			}
			out += "</span></p></div>";
		});
		$('#feedlist').append(out);
		
		// There has to be a cleaner way to do this...
		if(page === 1) {
			$('#feedlist').accordion({
				collapsible: true,
				active: false,
				heightStyle: 'content',
			});
		} else {
			$('#feedlist').accordion('destroy')
				.accordion({
					collapsible: true,
					active: false,
					heightStyle: 'content',
				});
		}
	});
	return 0;
}

function loadUpdates() {
	feedGetter(pagenum);
	feedbutton.onclick = function () {
		feedGetter(++pagenum);
	};
}

window.onLoad = loadUpdates();