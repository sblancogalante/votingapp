var votingApp = angular.module('votingApp', []);
votingApp.controller('votingController', ['$scope', '$http', '$window', function($scope, $http, $window) {
  var voting = this;
  voting.login = function() {

      var loginUrl = '/login';
      var request = $http.post(loginUrl, {'serie': voting.serie, 'numero': voting.numero});
      request.success(function(){
          $window.location.href = '/caca';
      });
}
}
]);
