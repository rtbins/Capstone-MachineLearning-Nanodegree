myApp.controller('lineChartCtrl', function ($scope, $http) {

    google.charts.load('current', {
        'packages': ['line', 'corechart']
    });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

        var chartDiv = document.getElementById('chart_div');
        var materialOptions = {
            chart: {
                title: 'Average Temperatures and Daylight in Iceland Throughout the Year'
            },
            series: {
                // Gives each series an axis name that matches the Y-axis below.
                0: {
                    axis: 'Temps'
                },
                1: {
                    axis: 'Daylight'
                }
            },
            axes: {
                // Adds labels to each axis; they don't have to match the axis names.
                y: {
                    Temps: {
                        label: 'Temps (Celsius)'
                    },
                    Daylight: {
                        label: 'Daylight'
                    }
                }
            }
        };

        $http.get('http://localhost:5000/stockData/rohit').
        then(function (data, status, headers, config) {
                var d = _.pairs(data["data"]["AAPL"]).slice(1, 100);
                var _data = [];
                for(var key in d){
                    if (d.hasOwnProperty(key)) {
                        _data.push([Date.parse(key), d[key]])
                    }
                }

                var data = google.visualization.arrayToDataTable([
                    ['years', 'sales']
                ].concat(_data));
                var materialChart = new google.charts.Line(chartDiv);
                materialChart.draw(data, materialOptions);
            },
            function (data, status, headers, config) {
                return 0;
            })


    }
})