myApp.controller('lineChartCtrl', function ($scope, $http) {

    $scope.options = {
        chart: {
            type: 'lineChart',
            height: 450,
            margin: {
                top: 20,
                right: 20,
                bottom: 40,
                left: 55
            },
            x: function (d) {
                console.log(d)
                return d.x;
            },
            y: function (d) {
                return d.y;
            },
            useInteractiveGuideline: true,
            dispatch: {
                stateChange: function (e) {
                    console.log("stateChange");
                },
                changeState: function (e) {
                    console.log("changeState");
                },
                tooltipShow: function (e) {
                    console.log("tooltipShow");
                },
                tooltipHide: function (e) {
                    console.log("tooltipHide");
                }
            },
            xAxis: {
                axisLabel: 'Time (ms)',
                tickFormat: function (d) {
                    console.log('x:' + d);
                    return d3.time.format('%m/%d/%y')(new Date(d))
                },
            },
            yAxis: {
                axisLabel: 'Voltage (v)',
                tickFormat: function (d) {
                    console.log(':' + d);
                    return d3.format('.02f')(d);
                },
                axisLabelDistance: -10
            },
            callback: function (chart) {
                console.log("!!! lineChart callback !!!");
            }
        },
        title: {
            enable: true,
            text: 'Title for Line Chart'
        },
        subtitle: {
            enable: true,
            text: 'Subtitle for simple line chart. Lorem ipsum dolor sit amet, at eam blandit sadipscing, vim adhuc sanctus disputando ex, cu usu affert alienum urbanitas.',
            css: {
                'text-align': 'center',
                'margin': '10px 13px 0px 7px'
            }
        },
        caption: {
            enable: true,
            html: '<b>Figure 1.</b> Lorem ipsum dolor sit amet, at eam blandit sadipscing, <span style="text-decoration: underline;">vim adhuc sanctus disputando ex</span>, cu usu affert alienum urbanitas. <i>Cum in purto erat, mea ne nominavi persecuti reformidans.</i> Docendi blandit abhorreant ea has, minim tantas alterum pro eu. <span style="color: darkred;">Exerci graeci ad vix, elit tacimates ea duo</span>. Id mel eruditi fuisset. Stet vidit patrioque in pro, eum ex veri verterem abhorreant, id unum oportere intellegam nec<sup>[1, <a href="https://github.com/krispo/angular-nvd3" target="_blank">2</a>, 3]</sup>.',
            css: {
                'text-align': 'justify',
                'margin': '10px 13px 0px 7px'
            }
        }
    };


    /*Random Data Generator */
    $scope.sinAndCos = function () {

        $http.get('http://localhost:5000/stockData/rohit').
        then(function (data, status, headers, config) {
                var stock = [];
                data = data["data"]
                for (var s in data) {
                    for (var date in data[s]) {
                        stock.push({
                            x: date,
                            y: data[s][date]
                        })
                    }
                }
                $scope.data = [{
                    values: stock,
                    key: 'AAPL',
                    color: '#2ca02c'
                }]
            },
            function (data, status, headers, config) {
                return 0;
            })

        /*
        var sin = [],
            sin2 = [],
            cos = [];

        //Data is represented as an array of {x,y} pairs.
        for (var i = 0; i < 100; i++) {
            sin.push({
                x: i,
                y: Math.sin(i / 10)
            });
            sin2.push({
                x: i,
                y: i % 10 == 5 ? null : Math.sin(i / 10) * 0.25 + 0.5
            });
            cos.push({
                x: i,
                y: .5 * Math.cos(i / 10 + 2) + Math.random() / 10
            });
        }

        //Line chart data should be sent as an array of series objects.
        return [{
                values: cos,
                key: 'Cosine Wave',
                color: '#2ca02c'
            },
            {
                values: sin2,
                key: 'Another sine wave',
                color: '#7777ff' //,
                //area: true //area - set to true if you want this line to turn into a filled area chart.
            }
        ];
        */
    };


    $scope.sinAndCos();
})