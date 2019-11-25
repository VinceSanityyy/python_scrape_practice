var URL = 'https://www.propertyguru.com.sg/property-for-sale?sort=date&order=desc&market=residential&property_type_code%5B%5D=CONDO&property_type_code%5B%5D=APT&property_type_code%5B%5D=WALK&property_type_code%5B%5D=CLUS&property_type_code%5B%5D=EXCON&property_type=N&newProject=all'

$.getJSON(URL, function(data){
	console.log('asdasda');
	console.log(data)
	}
);