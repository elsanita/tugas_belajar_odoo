odoo.define("appschef.penawaran", function (require) {
    "use strict";

	var rpc = require('web.rpc')
	var publicWidget = require('web.public.widget')

	console.log("JS RUNNING")

	publicWidget.registry.Offer = publicWidget.Widget.extend({
        selector: '#btn_submit_offer',
	    events: {
	        click: '_submitOffer'
	    },

        _submitOffer: function(e){
			// console.log("function running")
			var invoice_id = window.location.pathname.split('/')
			invoice_id = invoice_id[invoice_id.length - 1]
			var arrayOffer = []

			var input = document.querySelectorAll("#offering-view div.child-view")

			for(const data of input){
				// console.log(data)

				var productId = data.getElementsByClassName('product_id')[0].value
				var offering = data.getElementsByClassName('offering')[0].value
				
				arrayOffer.push({
					'productId': productId,
					'offering': offering
				})
			}

			console.log(arrayOffer)

            this._rpc({
				model: 'account.move',
				method: 'save_offer',
				kwargs: {
					'invoice_id': parseInt(invoice_id),
					'data_offering': arrayOffer,
			},
			}).then()
        },
    });
});