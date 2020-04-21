var events = [
{'Date': new Date(2019,11,11), 'Title': '-30 Benzina' },
{'Date': new Date(2019,11,22), 'Title': '-60 Benzina' },
{'Date': new Date(2019,12,11), 'Title': '-45 Benzina' },
{'Date': new Date(2019,12,23), 'Title': '-20 Benzina' },
{'Date': new Date(2019,12,28), 'Title': '-45 Benzina' },
{'Date': new Date(2020,01,15), 'Title': '-40 Benzina' },
{'Date': new Date(2020,04,04), 'Title': '-30 Benzina' },
{'Date': new Date(2020,03,31), 'Title': '-140 - '},
{'Date': new Date(2020,04,21), 'Title': '-30 - ', 'Color': 'green', 'LinkColor'	: 'green',},
{'Date': new Date(2020,03,10), 'Title': '+1270 -'},
{'Date': new Date(2020,04,19), 'Title': '+132 -'},
{'Date': new Date(2020,04,19), 'Title': '+13233 -'},

{{ calend }}

];

var settings = {};
var element = document.getElementById('caleandar');
caleandar(element, events, settings);