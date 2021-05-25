'use strict';
$.support.cors = true;
$.ajax({
  url: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
  dataType: 'text',
  success: function(csv) {
    for (var db = [], lns = csv.split('\n'), i = 1; i < lns.length - 1; i++) {
      db.push(lns[i].split(','));
    }
    var rates = [
      ['Australia', 0],
      ['Belgium', 0],
      ['Canada', 0],
      ['China', 0],
      ['Denmark', 0],
      ['France', 0],
      ['Germany', 0],
      ['Japan', 0],
      ['Netherlands', 0],
      ['Singapore', 0],
      ['Sweden', 0],
      ['Switzerland', 0],
      ['United Kingdom', 0],
      ['United States', 0],
      ['World', 0],
    ];
    var last14DRate = function(arr, pop) {
      return (arr[arr.length - 1] - arr[arr.length - 15]) / pop * 1e5;
    };
    for (i = 0; i < db.length; i++) {
      rates[14][1] += last14DRate(db[i], 7874965732);
      if (db[i][1] === 'Australia') {
        rates[0][1] += last14DRate(db[i], 25788217);
      } else if (db[i][1] === 'Belgium') {
        rates[1][1] += last14DRate(db[i], 11632334);
      } else if (db[i][1] === 'Canada') {
        rates[2][1] += last14DRate(db[i], 38067913);
      } else if (db[i][1] === 'China' || db[i][1] === 'Taiwan*') {
        rates[3][1] += last14DRate(db[i], 1476282301);
      } else if (db[i][1] === 'Denmark' && db[i][0] === '') {
        rates[4][1] += last14DRate(db[i], 5813302);
      } else if (db[i][1] === 'France') {
        rates[5][1] += last14DRate(db[i], 68325350);
      } else if (db[i][1] === 'Germany') {
        rates[6][1] += last14DRate(db[i], 83900471);
      } else if (db[i][1] === 'Japan') {
        rates[7][1] += last14DRate(db[i], 126050796);
      } else if (db[i][1] === 'Netherlands') {
        rates[8][1] += last14DRate(db[i], 17514951);
      } else if (db[i][1] === 'Singapore') {
        rates[9][1] += last14DRate(db[i], 5896684);
      } else if (db[i][1] === 'Sweden') {
        rates[10][1] += last14DRate(db[i], 10160159);
      } else if (db[i][1] === 'Switzerland') {
        rates[11][1] += last14DRate(db[i], 8715494);
      } else if (db[i][1] === 'United Kingdom' && db[i][0] === '') {
        rates[12][1] += last14DRate(db[i], 68207114);
      } else if (db[i][1] === 'US') {
        rates[13][1] += last14DRate(db[i], 336130735);
      }
    }
    rates.sort(function(a, b) {
      return b[1] - a[1];
    });
    for (i = 0; i < 15; i++) {
      document.getElementById('categ' + i).innerHTML = rates[i][0];
      document.getElementById('bar' + i).style.width =
        Math.max(0, rates[i][1] / rates[0][1] * 200) + 'px';
      document.getElementById('data' + i).innerHTML = rates[i][1].toFixed(2);
    }
  },
  error: function() {
    alert('Failed to get data!');
  }
});
