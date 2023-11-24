odoo.define('tugas_belajar.Orderline', function (require) {
    'use strict';

    const Orderline = require('point_of_sale.Orderline');
    const Registries = require('point_of_sale.Registries');

    const PosCashierNameText = (Orderline) =>
        class extends Orderline {
            get cashierName() {
                return this.props.line.get_cashier_name();
            }
        };

    Registries.Component.extend(Orderline, PosCashierNameText);

    return Orderline;
});
