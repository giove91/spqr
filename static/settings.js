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
    
    $scope.requesting = false;
    $scope.success = true;
    $scope.saved = false;
    $scope.no_words = false;
    
    $scope.saveSettings = function() {
        keywords_ids = []
        for (i=0; i<$scope.chosen_keywords.length; i++) {
            keywords_ids.push($scope.chosen_keywords[i].id);
        }
        $scope.requesting = true;
        
        $.ajax({
            url: "/words/savesettings/",
            type: "POST",
            data: {
                chosen_keywords: keywords_ids,
                filter_type: $scope.filter_type,
            },
            cache: false
        }).success( function(data) {
            if (data == "Error") $scope.success = false;
            else $scope.success = true;
            
            if (data == "0") $scope.no_words = true;
            else $scope.no_words = false;
            
            $scope.requesting = false;
            $scope.saved = true;
            $scope.$apply();
        });
    }
    
});

