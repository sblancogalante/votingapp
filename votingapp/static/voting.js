var votingApp = angular.module('votingApp', []);
votingApp.controller('votingController', ['$scope', '$http', function($scope, $http) {
  var voting = this;
  console.log('asd')
  voting.login = function() {
  var loginUrl = '/login';
    $http.post(loginUrl, {'serie': voting.serie, 'numero': voting.numero}).success(function(data, status, headers, config) {
        if (data.msg != '') {
          console.log(data);
          console.log('si');
        } else {
          console.log('asdasd');
        }
    }).error(function(data, status) { // called asynchronously if an error occurs
        // or server returns response with an error status.

    });
}
}
]);