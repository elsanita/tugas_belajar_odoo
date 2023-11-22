/** @odoo-module **/

import ProductScreen from 'point_of_sale.ProductScreen';
import Registries from 'point_of_sale.Registries';

export const CashierProductScreen = (ProductScreen) =>
    class extends ProductScreen {
        setup() {
            super.setup();
            // useListener('click-cashier', this.onClickCashier);
        }
        
        async onClickCashier() {
            // const selectedOrderline = this.env.pos.get_order().get_selected_orderline();
            // if (!selectedOrderline) return;

            // const { confirmed, payload: inputNote } = await this.showPopup('TextAreaPopup', {
            //     startingValue: selectedOrderline.get_customer_note(),
            //     title: this.env._t('Add Customer Note'),
            // });

            // if (confirmed) {
            //     selectedOrderline.set_customer_note(inputNote);
            // }
        }
    };

Registries.Component.extend(ProductScreen, CashierProductScreen);
