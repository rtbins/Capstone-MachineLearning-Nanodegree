/**
 * @author v.lugovsky
 * created on 16.12.2015
 */
(function () {
  'use strict';

  angular.module('BlurAdmin.pages.dashboard')
    .controller('LineChartCtrl', LineChartCtrl);

  /** @ngInject */
  function LineChartCtrl($scope, baConfig, $element, layoutPaths, $http) {
    var layoutColors = baConfig.colors;
    var id = $element[0].getAttribute('id');
    

    function zoomChart() {
      lineChart.zoomToIndexes(Math.round(lineChart.dataProvider.length * 0.4), Math.round(lineChart.dataProvider.length * 0.55));
    }

    $http.get('http://localhost:5000/stockData/rohit').
    then(function (data, status, headers, config) {
        var d = data["data"]["AAPL"];
        var _data = [];
        for (var key in d) {
          if (d.hasOwnProperty(key)) {
            _data.push({year: key, value: d[key]})
          }
        }

        _data = _.sortBy(_data, function(item){return Date.parse(item.year);})
        
        var lineChart = AmCharts.makeChart(id, {
          type: 'serial',
          theme: 'blur',
          color: layoutColors.defaultText,
          marginTop: 0,
          marginRight: 15,
          dataProvider: _data,
          valueAxes: [{
            axisAlpha: 0,
            position: 'left',
            gridAlpha: 0.5,
            gridColor: layoutColors.border,
          }],
          graphs: [{
            id: 'g1',
            balloonText: 'Apple \n[[value]]',
            bullet: 'round',
            bulletSize: 2,
            lineColor: layoutColors.danger,
            lineThickness: 1,
            negativeLineColor: layoutColors.warning,
            type: 'smoothedLine',
            valueField: 'value'
          }],
          chartScrollbar: {
            graph: 'g1',
            gridAlpha: 0,
            color: layoutColors.defaultText,
            scrollbarHeight: 55,
            backgroundAlpha: 0,
            selectedBackgroundAlpha: 0.05,
            selectedBackgroundColor: layoutColors.defaultText,
            graphFillAlpha: 0,
            autoGridCount: true,
            selectedGraphFillAlpha: 0,
            graphLineAlpha: 0.2,
            selectedGraphLineColor: layoutColors.defaultText,
            selectedGraphLineAlpha: 1
          },
          chartCursor: {
            cursorAlpha: 0,
            valueLineEnabled: false,
            valueLineBalloonEnabled: true,
            valueLineAlpha: 0.5,
            fullWidth: true
          },
          categoryAxis: {
            gridPosition: "start",
            labelRotation: 45
          },
          dataDateFormat: 'YYYY-MM-DD',
          categoryField: 'year',
          
          export: {
            enabled: true
          },
          creditsPosition: 'bottom-right',
          pathToImages: layoutPaths.images.amChart
        });
    
        lineChart.addListener('rendered', zoomChart);
        if (lineChart.zoomChart) {
          lineChart.zoomChart();
        }
      },
      function (data, status, headers, config) {
        return 0;
      })

  }

})();