var app = angular.module("settings", [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
    
app.controller("SettingsController", function($scope, $http, $element) {
    
    $scope.addKeyword = function(keyword) {
        index = $scope.available_keywords.indexOf(keyword);
        $scope.available_keywords.splice(index, 1);
        $scope.chosen_keywords.push(keyword);
    };
    
    $scope.removeKeyword = function(keyword) {
        index = $scope.chosen_keywords.indexOf(keyword);
        $scope.chosen_keywords.splice(index, 1);
        $scope.available_keywords.push(keyword);
    };
    
    $scope.saveSettings = function() {
        keywords_ids = []
        for (i=0; i<$scope.chosen_keywords.length; i++) {
            keywords_ids.push($scope.chosen_keywords[i].id);
        }
        
        $.ajax({
            url: "/words/savesettings/",
            type: "POST",
            data: {
                chosen_keywords: keywords_ids,
            },
            cache: false
        }).success( function(data) {
        });
    }
    
});

