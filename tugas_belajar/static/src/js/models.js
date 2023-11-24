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
        can_be_merged_with(orderline) {
            if (orderline.get_cashier_name() !== this.get_cashier_name()) {
                return false;
            }
        }
        //@override
        clone() {
            const orderline = super.clone(...arguments);
            orderline.cashier_name = this.cashier_name;
            return orderline;
        }
        //@override
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.cashier_name = this.cashier_name;
            return json;
        }
        //@override
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.cashier_name = json.cashier_name;
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
