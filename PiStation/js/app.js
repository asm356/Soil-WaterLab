$(document).ready(function(){
	$.ajax({
		url: "http://localhost/PiStation/php/station_1.php",
		method: "GET",
		success: function(data) {
			var ts = [];
			var ct = [];

			for(var i in data) {
				ts.push(data[i].timestamp);
				ct.push(data[i].count * 0.1);
			}

			var chartdata = {
				labels: ts,
				datasets : [
					{
						label: 'Rainfall (mm)',
						backgroundColor: 'rgba(25, 25, 112, 0.5)',
						borderColor: 'rgba(25, 25, 112, 0.5)',
						hoverBackgroundColor: 'midnightblue',
						hoverBorderColor: 'midnightblue',
						data: ct
					}
				]
			};

			var ctx = $(".mycanvas");
			
			var options = {
				scales: {
					yAxes: [{
						display: true,
						ticks: {
							suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
							// OR //
							beginAtZero: true   // minimum value will be 0.
						}
					}]
				}
			};

				var barGraph = new Chart(ctx, {
				type: 'bar',
				data: chartdata, options
			});
		},
		error: function(data) {
			console.log(data);
		}
	});
});