odoo.define('website.accorderie_aide', function (require) {
    "use strict";

    require('bus.BusService');
    let ajax = require('web.ajax');
    let core = require('web.core');
    let session = require('web.session');
    let Widget = require('web.Widget');
    let QWeb = core.qweb;

    // Get existing module
    let app = angular.module('AccorderieApp');

    app.controller('AideController', ['$scope', '$location', '$sce', function ($scope, $location, $sce) {
        $scope._ = _;
        $scope.section = "";
        $scope.error = "";

        // constant
        $scope.default_section = "guide_utilisation";

        $scope.trustSrc = function (src) {
            return $sce.trustAsResourceUrl(src);
        }

        $scope.$on('$locationChangeSuccess', function (object, newLocation, previousLocation) {
            let section = $location.search()["section"];
            if (!_.isEmpty(section)) {
                $scope.section = section;
            } else {
                $scope.section = $scope.default_section;
            }
        });

        let url = "/accorderie_canada_ddb/get_help_data/";
        ajax.rpc(url, {}).then(function (data) {
            console.debug("AJAX receive get_help_data");
            if (data.error) {
                $scope.error = data.error;
            } else if (_.isEmpty(data)) {
                $scope.error = "Empty data - " + url;
            } else {
                // Init controller or call change_state_name(name)
                $scope.error = "";
                $scope.data = data.data;
                console.debug(data.data);
            }

            // Process all the angularjs watchers
            $scope.$digest();
        })

    }])

    let AccorderieAide = Widget.extend({
        start: function () {
        },
    });

    return {
        AccorderieAide: AccorderieAide,
    };

});
