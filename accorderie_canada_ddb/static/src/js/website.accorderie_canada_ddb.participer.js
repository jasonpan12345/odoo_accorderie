odoo.define('website.accorderie_canada_ddb.participer.instance', function (require) {
    'use strict';

    require('web_editor.ready');
    let ParticiperForm = require('website.accorderie_canada_ddb.participer');

    let $form = $('#participer_form');
    if (!$form.length) {
        return null;
    }

    let instance = new ParticiperForm();
    return instance.appendTo($form).then(function () {
        return instance;
    });
});

//==============================================================================

odoo.define("website.accorderie_canada_ddb.participer", function (require) {
    const INIT_STATE = "init";
    let ajax = require('web.ajax');
    let core = require('web.core');
    let session = require('web.session');
    let Widget = require('web.Widget');
    let _t = core._t;

    let app = angular.module('AccorderieApp', []);
    app.filter('unsafe', function ($sce) {
        // This allows html generation in view
        return $sce.trustAsHtml;
    });
    app.controller('ParticiperController', function ($scope) {
        $scope.error = "";
        $scope.workflow = {};
        $scope.state = {};
        $scope.stack_breadcrumb_state = [];
        $scope.stack_breadcrumb_inner_state = [];
        $scope.actual_inner_state_name = "";
        $scope.in_multiple_inner_state = false; // true when a state need multiple interaction before show next
        $scope.selected_model = "";
        $scope.selected_model_inner_state = "";

        ajax.rpc("/accorderie_canada_ddb/get_participer_workflow_data/", {}).then(function (data) {
            console.debug("Receive get_participer_workflow_data");
            if (data.error) {
                $scope.error = error;
            } else if (_.isEmpty(data)) {
                $scope.error = "Empty data";
            } else if (!data.workflow.hasOwnProperty(INIT_STATE)) {
                let str_error = "Missing state '" + INIT_STATE + "'.";
                console.error(str_error);
                $scope.error = str_error;
                $scope.workflow = {};
                $scope.state = {};
                $scope.data = {};
            } else {
                $scope.error = "";
                $scope.workflow = data.workflow;
                $scope.state = $scope.workflow[INIT_STATE];
                $scope.data = data.data;
                // Update relation workflow with data
                for (const [key, value] of Object.entries($scope.workflow)) {
                    if (!_.isEmpty(value.data)) {
                        $scope.workflow[key].data = $scope.data[value.data];
                    }
                }
            }

            // Process all the angularjs watchers
            $scope.$digest();
        })

        $scope.is_show_previous = function () {
            return $scope.stack_breadcrumb_state.length
        }

        $scope.is_show_next = function () {
            return !$scope.in_multiple_inner_state
        }

        $scope.click_choix_categorie_de_service = function (option) {
            console.debug(option);
            // copy object state with option, add it to stack
            // EDIT ignore it, previous will ignore this inner state
            // $scope.state = JSON.parse(JSON.stringify($scope.state));
            // // Ignore breadcrumb in this processing
            // $scope.state.breadcrumb_value = "";
            // $scope.state.option = option;
            // $scope.state.last_item = option.title;
            // $scope.stack_breadcrumb_state.push($scope.state);
            if ($scope.in_multiple_inner_state) {
                $scope.stack_breadcrumb_inner_state.push(option);
                $scope.actual_inner_state_name = option.title;
                $scope.update_inner_state(option);
            } else {
                $scope.selected_model = $scope.state.next_id;
            }
        }

        $scope.previous_inner_state_btn = function () {
            console.debug("previous inner state click");
            $scope.error = "";
            if (!_.isEmpty($scope.stack_breadcrumb_state)) {
                $scope.stack_breadcrumb_inner_state.pop();
                $scope.selected_model_inner_state = "";
                if (!_.isEmpty($scope.stack_breadcrumb_state)) {
                    let option = $scope.stack_breadcrumb_inner_state.at(-1);
                    if (!_.isUndefined(option)) {
                        $scope.actual_inner_state_name = $scope.stack_breadcrumb_inner_state.at(-1).title;
                        $scope.update_inner_state(option);
                    } else {
                        $scope.actual_inner_state_name = "";
                    }
                } else {
                    $scope.actual_inner_state_name = "";
                }
            } else {
                console.error("Cannot previous inner state.");
            }
        }

        $scope.previous_btn = function () {
            console.debug("previous click");
            $scope.error = "";
            if (!_.isEmpty($scope.stack_breadcrumb_state)) {
                $scope.stack_breadcrumb_state.pop();
                if (_.isEmpty($scope.stack_breadcrumb_state)) {
                    // Force return to init
                    $scope.state = $scope.workflow[INIT_STATE];
                } else {
                    $scope.state = $scope.stack_breadcrumb_state.at(-1);
                }
                $scope.update_state();
                $scope.selected_model = "";
            } else {
                console.error("Cannot previous when " + INIT_STATE + ".");
            }
        }

        $scope.next_btn = function () {
            console.debug("next click");
            console.debug($scope.selected_model);
            if (!$scope.selected_model.length) {
                console.error("Cannot find selected model");
            } else {
                $scope.state = $scope.workflow[$scope.selected_model];
                $scope.stack_breadcrumb_state.push($scope.state);
                $scope.update_state();
                console.debug($scope.state);
                if (_.isUndefined($scope.state)) {
                    $scope.error = "Cannot find " + $scope.selected_model;
                } else {
                    $scope.error = "";
                }
                $scope.selected_model = "";
            }
        }

        $scope.state_get_data = function () {
            if (!_.isEmpty($scope.stack_breadcrumb_inner_state)) {
                let option = $scope.stack_breadcrumb_inner_state.at(-1);
                // $scope.update_inner_state(option);
                return option.sub_list;
            } else if (!_.isUndefined($scope.state.option)) {
                return $scope.state.option.sub_list;
            } else {
                return $scope.state.data;
            }
        }

        $scope.update_inner_state = function (option) {
            // validate if inner workflow continue, check if contains sub_list
            $scope.in_multiple_inner_state = !_.isUndefined(option.sub_list) && !_.isUndefined(option.sub_list.at(-1).sub_list);
            $scope.selected_model = "";
        }

        $scope.update_state = function () {
            $scope.in_multiple_inner_state = $scope.state.type === "choix_categorie_de_service" && !_.isUndefined($scope.state.data);
            // Force delete stack inner state
            $scope.stack_breadcrumb_inner_state = [];
            $scope.actual_inner_state_name = "";
        }

        $scope.label_breadcrumb = function () {
            let label = "";
            for (let i = 0; i < $scope.stack_breadcrumb_state.length; i++) {
                let state = $scope.stack_breadcrumb_state[i];
                if (!_.isUndefined(state.breadcrumb_value) && !_.isEmpty(state.breadcrumb_value)) {
                    let lst_breadcrumb = state.breadcrumb_value.split(".");
                    for (let j = 0; j < lst_breadcrumb.length; j++) {
                        if (label.length) {
                            label += " > "
                        }
                        label += lst_breadcrumb[j];
                    }
                }
            }
            if (label.indexOf(" > ") === -1) {
                label += " > ..."
            }
            return label;
        }
    });


    // let currentTab = 0; // Current tab is set to be the first tab (0)

    // Catch registration form event, because of JS for attendee details
    let ParticiperForm = Widget.extend({
        start: function () {
            // let self = this;
            // let res = this._super.apply(this.arguments).then(function () {
            //     $('#participer_form .submit_container .submit_btn')
            //         .off('click')
            //         .click(function (ev) {
            //             self.on_click(ev, 1);
            //         });
            // });
            // let prev = this._super.apply(this.arguments).then(function () {
            //     $('#participer_form .submit_container .prev')
            //         .off('click')
            //         .click(function (ev) {
            //             self.on_click(ev, -1);
            //         });
            // });
            // let form_choice = this._super.apply(this.arguments).then(function () {
            //     $('.buttons_form_container > input')
            //         .off('click')
            //         .click(function (ev) {
            //             self.verifRadioChosen()
            //         });
            // });
            // self.showTab(currentTab); // Display the current tab
            // return res;
        },
        // on_click: function (ev, nextPrev) {
        //     ev.preventDefault();
        //     ev.stopPropagation();
        //     this.nextPrev(nextPrev);
        // },
        // // Verify that at least one radio button is chosen on the current tab
        // verifRadioChosen: function () {
        //     let x = document.getElementsByClassName("tab");
        //     let inputName = x[currentTab].getElementsByTagName("input")[0];
        //     let primaryColor = getComputedStyle(document.body).getPropertyValue('--primary');
        //
        //     let inputClick = $("input[name=" + inputName.name + "]:checked");
        //     console.debug(inputClick);
        //     if (inputClick.length > 0) {
        //         document.getElementById("nextBtn").style.backgroundColor = primaryColor;
        //         return true;
        //     }
        //     document.getElementById("nextBtn").style.backgroundColor = "lightgray";
        //     return false;
        // },
        // showTab: function (n) {
        //     this.verifRadioChosen();
        //     // This function will display the specified tab of the form ...
        //     let x = document.getElementsByClassName("tab");
        //     x[n].style.display = "flex";
        //     // ... and fix the Previous/Next buttons:
        //     if (n === 0) {
        //         document.getElementById("prevBtn").style.display = "none";
        //     } else {
        //         document.getElementById("prevBtn").style.display = "inline";
        //     }
        //     if (n === (x.length - 1)) {
        //         document.getElementById("nextBtn").value = "Submit";
        //     } else {
        //         document.getElementById("nextBtn").innerHTML = "Suivant";
        //     }
        // },
        // nextPrev: function (n) {
        //     // TODO update here the sequence, update click event
        //     // This function will figure out which tab to display
        //     let x = document.getElementsByClassName("tab");
        //     // Exit the function if any field in the current tab is invalid:
        //     if (n === 1 && !this.verifRadioChosen()) {
        //         return false;
        //     }
        //     console.debug("click nextPrev, tab # " + currentTab);
        //     console.debug(x);
        //     console.debug(x[currentTab]);
        //     if (currentTab === 2) {
        //         let inputName = x[currentTab].getElementsByTagName("input")[0];
        //         let lst_radio = $("input[name=" + inputName.name + "]:checked");
        //         let self = this;
        //         this.tab_sous_categorie = document.getElementsByClassName("tab_sous_categorie");
        //         let categorie_id = lst_radio[0].value;
        //         ajax.rpc("/accorderie_canada_ddb/type_service_sous_categorie_list/" + categorie_id, {}).then(function (data) {
        //             if (data.error) {
        //                 return;
        //             }
        //
        //             if (_.isEmpty(data)) {
        //                 return;
        //             }
        //
        //             self.tab_sous_categorie[0].innerHTML = data;
        //             $('.buttons_form_container > input')
        //                 .off('click')
        //                 .click(function (ev) {
        //                     self.verifRadioChosen()
        //                 });
        //
        //             // Hide the current tab:
        //             x[currentTab].style.display = "none";
        //             // Increase or decrease the current tab by 1:
        //             currentTab = currentTab + n;
        //
        //             // Otherwise, display the correct tab:
        //             self.showTab(currentTab);
        //         });
        //     } else if (currentTab >= x.length - 1) {
        //         // if you have reached the end of the form... :
        //         //...the form gets submitted:
        //         document.getElementById("participer_form").submit();
        //         return false;
        //     } else {
        //         // Hide the current tab:
        //         x[currentTab].style.display = "none";
        //         // Increase or decrease the current tab by 1:
        //         currentTab = currentTab + n;
        //
        //         // Otherwise, display the correct tab:
        //         this.showTab(currentTab);
        //     }
        // },
    });

    return ParticiperForm;
});