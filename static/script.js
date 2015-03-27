var app = angular.module("word", [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
    
app.controller("WordController", function($scope, $http, $element) {
    
    $scope.getWord = function() {
        $.ajax({
            url: "/words/getword/",
            type: "GET",
            cache: false
        }).success( function(data) {
            $scope.russian = data.russian;
            $scope.italian = data.italian;
            $scope.show_italian = false;
            $scope.$apply();
        });
    }
    
    $scope.getWord()
});

