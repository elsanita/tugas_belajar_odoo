// odoo.define('appschef.modal_penawaran', function (require) {
//     'use strict';
    
//     var publicWidget = require('web.public.widget');
//     const Dialog = require('web.Dialog');
//     const {_t, qweb} = require('web.core');
//     const session = require('web.session');
    
// publicWidget.registry.penawaran = publicWidget.Widget.extend({
//     selector: '.o_portal_details',
//     events: {
//         'change select[name="country_id"]': '_onCountryChange',
//     },

//     /**
//      * override
//      */
//     // start: function () {
//     //     var def = this._super.apply(this, arguments);

//     //     this.$state = this.$('select[name="state_id"]');
//     //     this.$stateOptions = this.$state.filter(':enabled').find('option:not(:first)');
//     //     this._adaptAddressForm();

//     //     return def;
//     // },

//     //--------------------------------------------------------------------------
//     // Private
//     //--------------------------------------------------------------------------

//     /**
//      * private
//      */
//     // _adaptAddressForm: function () {
//     //     var $country = this.$('select[name="country_id"]');
//     //     var countryID = ($country.val() || 0);
//     //     this.$stateOptions.detach();
//     //     var $displayedState = this.$stateOptions.filter('[data-country_id=' + countryID + ']');
//     //     var nb = $displayedState.appendTo(this.$state).show().length;
//     //     this.$state.parent().toggle(nb >= 1);
//     // },

//     //--------------------------------------------------------------------------
//     // Handlers
//     //--------------------------------------------------------------------------

//     /**
//      * private
//      */
//     // _onCountryChange: function () {
//     //     this._adaptAddressForm();
//     // },
// })
// });