odoo.define('website.accorderie_aide', function (require) {
    "use strict";

    require('bus.BusService');
    let core = require('web.core');
    let session = require('web.session');
    let Widget = require('web.Widget');
    let QWeb = core.qweb;

    // Get existing module
    let app = angular.module('AccorderieApp');

    app.controller('AideController', ['$scope', '$location', function ($scope, $location) {
        $scope._ = _;
        $scope.section = "";

        // constant
        $scope.default_section = "guide_utilisation";

        $scope.$on('$locationChangeSuccess', function (object, newLocation, previousLocation) {
            let section = $location.search()["section"];
            if (!_.isEmpty(section)) {
                $scope.section = section;
            } else {
                $scope.section = $scope.default_section;
            }
        });
    }])

    let AccorderieAide = Widget.extend({
        start: function () {
        },
    });

    return {
        AccorderieAide: AccorderieAide,
    };

});
