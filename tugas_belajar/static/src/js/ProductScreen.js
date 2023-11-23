odoo.define('tugas_belajar.ProductScreen', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");

    const Update = (ProductScreen) =>
        class extends ProductScreen {
            setup() {
                super.setup();
                useListener('click-cashier', this.onClickCashier);
            }
            
            async onClickCashier() {
                const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
                if (!selectedOrderline) return;

                const { confirmed, payload: inputCashierName } = await this.showPopup('TextAreaPopup', {
                    // startingValue: selectedOrderline.get_cashier_name(),
                    startingValue: selectedOrderline.get_customer_note(),
                    title: this.env._t('Add Cashier Name'),
                });

                if (confirmed) {
                    // selectedOrderline.set_cashier_name(inputCashierName);
                    selectedOrderline.set_customer_note(inputCashierName);
                }
            }
        };

    Registries.Component.extend(ProductScreen, Update);

    return ProductScreen;
});
