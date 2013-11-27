var metroApp = angular.module('metroApp', []);

metroApp.controller('OffloadListCtrl', function($scope, $http){
	var endpointUrl = 'http://56cf5ae8.ngrok.com/api/v1/incident/?format=json';

	$http.get(endpointUrl).success(function(data){
		$scope.offloads = data.objects;
	});

	$scope.update = function(type) {
		switch( type ) {
			case 'confirmed':
				$http.get(endpointUrl).success(function(data){
					var confirmed = [];
					for( offload in data.objects ) {
						if( data.objects[offload].confirmed ) {
							confirmed.push( data.objects[offload] );
						}
					}
					$scope.offloads = confirmed;
				});
			break;
			case 'uncofirmed':
				$http.get(endpointUrl).success(function(data){
					var uncofirmed = [];
					for( offload in data.objects ) {
						if( !data.objects[offload].confirmed ) {
							uncofirmed.push( data.objects[offload] );
						}
					}
					$scope.offloads = uncofirmed;
				});
			break;
			case 'all':
				$http.get(endpointUrl).success(function(data){
					$scope.offloads = data.objects;
				});
			break;
		}
	}
});