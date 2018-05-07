/**
 * @author v.lugovsky
 * created on 16.12.2015
 */
(function () {
  'use strict';

  angular.module('BlurAdmin.pages', [
 
   'BlurAdmin.pages.dashboard',
   'BlurAdmin.pages.profile'
  ])
      .config(routeConfig);

  /** @ngInject */
  function routeConfig($urlRouterProvider, baSidebarServiceProvider) {
    $urlRouterProvider.otherwise('/dashboard');

    baSidebarServiceProvider.addStaticItem({
      title: 'About',
      icon: 'fa fa-info',
      stateRef: 'profile'
    });
    
  }

})();
