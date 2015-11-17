var votingApp = angular.module('votingApp', []);
votingApp.controller('votingController', ['$scope', '$http', '$window', function($scope, $http, $window) {
  var voting = this;
  voting.login = function() {

      var loginUrl = '/login';
      var request = $http.post(loginUrl, {'serie': voting.serie, 'numero': voting.numero});
      request.success(function(){
          $window.location.href = '/vote';
      });
}
  voting.vote1 = function() {
      var voteUrl ='/vote'
      var request = $http.post(voteUrl, {'candidato': 1});
      request.success(function(){
          alert('su voto fue registrado!');
          $window.location.href = '/';
      });


  };
  voting.vote2 = function() {
      var voteUrl ='/vote'
      var request = $http.post(voteUrl, {'candidato': 2});
      request.success(function(){
          alert('su voto fue registrado!');
          $window.location.href = '/';
      });


  };
  voting.voteBlank = function() {
      var voteUrl = '/vote'
      var request = $http.post(voteUrl, {'voto en blanco': '1'});
      request.success(function(){
          alert('su voto fue registrado!');
          $window.location.href = '/';
      });
  }
}
]);
