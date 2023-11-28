odoo.define('tugas_belajar.models', function (require) {
    "use strict";

    const { Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const PosCashierNameOrderline = (Orderline) => class PosCashierNameOrderline extends Orderline {
        constructor() {
            super(...arguments);
            this.cashier_name = this.cashier_name || "";
        }
        //@override
        //THIS FUNCTION IS REQUIRED TO SAVE VALUE INTO .PY MODEL
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.cashier_name = this.cashier_name;
            return json;
        }
        set_cashier_name(cashier_name) {
            this.cashier_name = cashier_name;
        }
        get_cashier_name() {
            return this.cashier_name;
        }
    }
    
    Registries.Model.extend(Orderline, PosCashierNameOrderline);
});
