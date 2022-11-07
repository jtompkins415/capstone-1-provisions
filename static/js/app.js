(function( $ ) {
    $.Shop = function( element ) {
        this.$element = $( element ); // top-level element
        this.init();
    };

    $.Shop.prototype = {
        init: function() {
            // initializes properties and methods
            this.cartPrefix = "provisions-"; // prefix string to be prepended to the cart's name in session storage
            this.cartName = this.cartPrefix + "cart"; // cart's name in session storage
            this.shippingRates = this.cartPrefix + "shipping-rates"; // shipping rates key in session storage
            this.total = this.cartPrefix + "total"; // total key in the session storage
            this.storage = sessionStorage; // shortcut to sessionStorage object

            this.$formAddToCart = this.$element.find( "form.add-to-cart" ); // forms for adding items to the cart
            this.$formCart = this.$element.find( "#shopping-cart" ); // Shopping cart form
            this.$checkoutCart = this.$element.find( "#checkout-cart" ); // checkout form cart
            this.$checkoutOrderForm = this.$element.find( "#checkout-order-form" ); // checkout user details form
            this.$shipping = this.$element.find( "#sshipping" ); // element that displays the shipping rates
            this.$subTotal = this.$element.find( "#stotal" ); // element that displays the subtotal charges
            this.$shoppingCartActions = this.$element.find( "#shopping-cart-actions" ); // cart actions links
            this.$updateCartBtn = this.$shoppingCartActions.find( "#update-cart" ); // update cart button
            this.$emptyCartBtn = this.$shoppingCartActions.find( "#empty-cart" ); // empty cart button
            this.$userDetails = this.$element.find( "#user-details-content" ); // element that displays the user's information
            this.$paypalForm = this.$element.find( "#paypal-form" ); // PayPal form

            this.currency = "&euro;"; // HTML entity of the currency to be displayed in layout
            this.currencyString = "€"; // currency symbol as text string
            this.paypalCurrency = "EUR"; // PayPal's currency code
            this.paypalBusinessEmail = "yourbusiness@email.com"; // your PayPal Business account email address
            this.paypalURL = "https://www.sandbox.paypal.com/cgi-bin/webscr"; // URL of the PayPal form

            // object containing patterns for form validation
            // this.requiredFields = {
            //     expression: {
            //         value: /^([w-.]+)@((?:[w]+.)+)([a-z]){2,4}$/
            //     },

            //     str: {
            //         value: ""
            //     }

            // };

            // public methods invocation

            this.createCart();
            this.handleAddToCartForm();
            this.handleCheckoutOrderForm();
            this.emptyCart();
            this.updatedCart();
            this.displayCart();
            this.deleteProduct();
            this.displayUserDetails();
            this.populatePaypalForm();
            

        },
        createCart: function() {
                if( this.storage.getItem( this.cartName ) == null ) {
            
                    let cart = {};
                    cart.items = [];
            
                    this.storage.setItem( this.cartName, JSON.stringify( cart ) );
                    this.storage.setItem( this.shippingRates, "0" );
                    this.storage.setItem( this.total, "0" );
                    }
            },

        handleAddToCartForm: function() {
                let self = this;
                self.$formAddToCart.each(function() {
                    let $form = $( this );
                    let $product = $form.parent();
                    let price = self._convertString( $product.data( "price" ) );
                    let name =  $product.data( "name" );
            
                    $form.on( "submit", function() {
                        let qty = self._convertString( $form.find( ".qty" ).val() );
                        let subTotal = qty * price;
                        let total = self._convertString( self.storage.getItem( self.total ) );
                        let sTotal = total + subTotal;
                        self.storage.setItem( self.total, sTotal );
                        self._addToCart({
                            product: name,
                            price: price,
                            qty: qty
                        });
                        let shipping = self._convertString( self.storage.getItem( self.shippingRates ) );
                        let shippingRates = self._calculateShipping( qty );
                        let totalShipping = shipping + shippingRates;
            
                        self.storage.setItem( self.shippingRates, totalShipping );
                    });
                });
            },

            deleteProduct: function() {
                let self = this;
                if( self.$formCart.length ) {
                    let cart = this._toJSONObject( this.storage.getItem( this.cartName ) );
                    let items = cart.items;
    
                    $( document ).on( "click", ".pdelete a", function( e ) {
                        e.preventDefault();
                        let productName = $( this ).data( "product" );
                        let newItems = [];
                        for( let i = 0; i < items.length; ++i ) {
                            let item = items[i];
                            let product = item.product;	
                            if( product == productName ) {
                                items.splice( i, 1 );
                            }
                        }
                        newItems = items;
                        let updatedCart = {};
                        updatedCart.items = newItems;
    
                        let updatedTotal = 0;
                        let totalQty = 0;
                        if( newItems.length == 0 ) {
                            updatedTotal = 0;
                            totalQty = 0;
                        } else {
                            for( let j = 0; j < newItems.length; ++j ) {
                                let prod = newItems[j];
                                let sub = prod.price * prod.qty;
                                updatedTotal += sub;
                                totalQty += prod.qty;
                            }
                        }
    
                        self.storage.setItem( self.total, self._convertNumber( updatedTotal ) );
                        self.storage.setItem( self.shippingRates, self._convertNumber( self._calculateShipping( totalQty ) ) );
    
                        self.storage.setItem( self.cartName, self._toJSONString( updatedCart ) );
                        $( this ).parents( "tr" ).remove();
                        self.$subTotal[0].innerHTML = self.currency + " " + self.storage.getItem( self.total );
                    });
                }
            },

            displayCart: function() {
                if( this.$formCart.length ) {
                    let cart = this._toJSONObject( this.storage.getItem( this.cartName ) );
                    let items = cart.items;
                    let $tableCart = this.$formCart.find( ".shopping-cart" );
                    let $tableCartBody = $tableCart.find( "tbody" );
            
                    for( let i = 0; i < items.length; ++i ) {
                        let item = items[i];
                        let product = item.product;
                        let price = this.currency + " " + item.price;
                        let qty = item.qty;
                        let html = "<tr><td class='pname'>" + product + "</td>" + "<td class='pqty'><input type='text' value='" + qty + "' class='qty'/></td>" + "<td class='pprice'>" + price + "</td></tr>";
            
                        $tableCartBody.html( $tableCartBody.html() + html );
                    }
            
                    let total = this.storage.getItem( this.total );
                    this.$subTotal[0].innerHTML = this.currency + " " + total;
                } else if( this.$checkoutCart.length ) {
                    let checkoutCart = this._toJSONObject( this.storage.getItem( this.cartName ) );
                    let cartItems = checkoutCart.items;
                    let $cartBody = this.$checkoutCart.find( "tbody" );
            
                    for( let j = 0; j < cartItems.length; ++j ) {
                        let cartItem = cartItems[j];
                        let cartProduct = cartItem.product;
                        let cartPrice = this.currency + " " + cartItem.price;
                        let cartQty = cartItem.qty;
                        let cartHTML = "<tr><td class='pname'>" + cartProduct + "</td>" + "<td class='pqty'>" + cartQty + "</td>" + "<td class='pprice'>" + cartPrice + "</td></tr>";
            
                        $cartBody.html( $cartBody.html() + cartHTML );
                    }
            
                    let cartTotal = this.storage.getItem( this.total );
                    let cartShipping = this.storage.getItem( this.shippingRates );
                    let subTot = this._convertString( cartTotal ) + this._convertString( cartShipping );
            
                    this.$subTotal[0].innerHTML = this.currency + " " + this._convertNumber( subTot );
                    this.$shipping[0].innerHTML = this.currency + " " + cartShipping;
            
                }
            },

            updatedCart: function() {
                let self = this;
            if( self.$updateCartBtn.length ) {
                self.$updateCartBtn.on( "click", function() {
                    let $rows = self.$formCart.find( "tbody tr" );
                    let cart = self.storage.getItem( self.cartName );
                    let shippingRates = self.storage.getItem( self.shippingRates );
                    let total = self.storage.getItem( self.total );
        
                    let updatedTotal = 0;
                    let totalQty = 0;
                    let updatedCart = {};
                    updatedCart.items = [];
        
                    $rows.each(function() {
                        let $row = $( this );
                        let pname = $.trim( $row.find( ".pname" ).text() );
                        let pqty = self._convertString( $row.find( ".pqty > .qty" ).val() );
                        let pprice = self._convertString( self._extractPrice( $row.find( ".pprice" ) ) );
        
                        let cartObj = {
                            product: pname,
                            price: pprice,
                            qty: pqty
                        };
        
                        updatedCart.items.push( cartObj );
        
                        let subTotal = pqty * pprice;
                        updatedTotal += subTotal;
                        totalQty += pqty;
                    });
        
                    self.storage.setItem( self.total, self._convertNumber( updatedTotal ) );
                    self.storage.setItem( self.shippingRates, self._convertNumber( self._calculateShipping( totalQty ) ) );
                    self.storage.setItem( self.cartName, self._toJSONString( updatedCart ) );
        
                });
            }
        },

        emptyCart: function() {
            let self = this;
            if( self.$emptyCartBtn.length ) {
                self.$emptyCartBtn.on( "click", function() {
                    self._emptyCart();
                });
            }
        },

        handleCheckoutOrderForm: function() {
            let self = this;
            if( self.$checkoutOrderForm.length ) {
                let $sameAsBilling = $( "#same-as-billing" );
                $sameAsBilling.on( "change", function() {
                    let $check = $( this );
                    if( $check.prop( "checked" ) ) {
                        $( "#fieldset-shipping" ).slideUp( "normal" );
                    } else {
                        $( "#fieldset-shipping" ).slideDown( "normal" );
                    }
                });
        
                self.$checkoutOrderForm.on( "submit", function() {
                    let $form = $( this );
                    let valid = self._validateForm( $form );
        
                    if( !valid ) {
                        return valid;
                    } else {
                        self._saveFormData( $form );
                    }
                });
            }
        },

        displayUserDetails: function() {
            if( this.$userDetails.length ) {
                if( this.storage.getItem( "shipping-name" ) == null ) {
                    let name = this.storage.getItem( "billing-name" );
                    let email = this.storage.getItem( "billing-email" );
                    let city = this.storage.getItem( "billing-city" );
                    let address = this.storage.getItem( "billing-address" );
                    let zip = this.storage.getItem( "billing-zip" );
                    let country = this.storage.getItem( "billing-country" );
        
                    let html = "<div class='detail'>";
                        html += "<h2>Billing and Shipping</h2>";
                        html += "<ul>";
                        html += "<li>" + name + "</li>";
                        html += "<li>" + email + "</li>";
                        html += "<li>" + city + "</li>";
                        html += "<li>" + address + "</li>";
                        html += "<li>" + zip + "</li>";
                        html += "<li>" + country + "</li>";
                        html += "</ul></div>";
        
                    this.$userDetails[0].innerHTML = html;
                } else {
                    let name = this.storage.getItem( "billing-name" );
                    let email = this.storage.getItem( "billing-email" );
                    let city = this.storage.getItem( "billing-city" );
                    let address = this.storage.getItem( "billing-address" );
                    let zip = this.storage.getItem( "billing-zip" );
                    let country = this.storage.getItem( "billing-country" );
        
                    let sName = this.storage.getItem( "shipping-name" );
                    let sEmail = this.storage.getItem( "shipping-email" );
                    let sCity = this.storage.getItem( "shipping-city" );
                    let sAddress = this.storage.getItem( "shipping-address" );
                    let sZip = this.storage.getItem( "shipping-zip" );
                    let sCountry = this.storage.getItem( "shipping-country" );
        
                    let html = "<div class='detail'>";
                        html += "<h2>Billing</h2>";
                        html += "<ul>";
                        html += "<li>" + name + "</li>";
                        html += "<li>" + email + "</li>";
                        html += "<li>" + city + "</li>";
                        html += "<li>" + address + "</li>";
                        html += "<li>" + zip + "</li>";
                        html += "<li>" + country + "</li>";
                        html += "</ul></div>";
        
                        html += "<div class='detail right'>";
                        html += "<h2>Shipping</h2>";
                        html += "<ul>";
                        html += "<li>" + sName + "</li>";
                        html += "<li>" + sEmail + "</li>";
                        html += "<li>" + sCity + "</li>";
                        html += "<li>" + sAddress + "</li>";
                        html += "<li>" + sZip + "</li>";
                        html += "<li>" + sCountry + "</li>";
                        html += "</ul></div>";
        
                    this.$userDetails[0].innerHTML = html;
        
                }
            }
        },

        populatePaypalForm: function() {
            let self = this;
            if( self.$paypalForm.length ) {
                let $form = self.$paypalForm;
                let cart = self._toJSONObject( self.storage.getItem( self.cartName ) );
                let shipping = self.storage.getItem( self.shippingRates );
                let numShipping = self._convertString( shipping );
                let cartItems = cart.items;
                let singShipping = Math.floor( numShipping / cartItems.length );
        
                $form.attr( "action", self.paypalURL );
                $form.find( "input[name='business']" ).val( self.paypalBusinessEmail );
                $form.find( "input[name='currency_code']" ).val( self.paypalCurrency );
        
                for( let i = 0; i < cartItems.length; ++i ) {
                    let cartItem = cartItems[i];
                    let n = i + 1;
                    let name = cartItem.product;
                    let price = cartItem.price;
                    let qty = cartItem.qty;
        
                    $( "<div/>" ).html( "<input type='hidden' name='quantity_" + n + "' value='" + qty + "'/>" ).
                    insertBefore( "#paypal-btn" );
                    $( "<div/>" ).html( "<input type='hidden' name='item_name_" + n + "' value='" + name + "'/>" ).
                    insertBefore( "#paypal-btn" );
                    $( "<div/>" ).html( "<input type='hidden' name='item_number_" + n + "' value='SKU " + name + "'/>" ).
                    insertBefore( "#paypal-btn" );
                    $( "<div/>" ).html( "<input type='hidden' name='amount_" + n + "' value='" + self._formatNumber( price, 2 ) + "'/>" ).
                    insertBefore( "#paypal-btn" );
                    $( "<div/>" ).html( "<input type='hidden' name='shipping_" + n + "' value='" + self._formatNumber( singShipping, 2 ) + "'/>" ).
                    insertBefore( "#paypal-btn" );
        
                }
        
            }
        },
//Private methods

    _emptyCart: function(){
        this.storage.clear();
    },

    _formatNumber: function( num, places ) {
        let n = num.toFixed( places );
        return n;
    },

    _convertString: function( numStr ) {
        let num;
        if( /^[-+]?[0-9]+.[0-9]+$/.test( numStr ) ) {
            num = parseFloat( numStr );
        } else if( /^d+$/.test( numStr ) ) {
            num = parseInt( numStr );
        } else {
            num = Number( numStr );
        }
    
        if( !isNaN( num ) ) {
            return num;
        } else {
            console.warn( numStr + " cannot be converted into a number" );
            return false;
        }
    },

    _convertNumber: function( n ) {
        let str = n.toString();
        return str;
    },

    _toJSONObject: function( str ) {
        let obj = JSON.parse( str );
        return obj;
    },

    _addToCart: function( values ) {
        let cart = this.storage.getItem( this.cartName );
        let cartObject = this._toJSONObject( cart );
        let cartCopy = cartObject;
        let items = cartCopy.items;
        items.push( values );
    
        this.storage.setItem( this.cartName, this._toJSONString( cartCopy ) );
    },

    _calculateShipping: function( qty ) {
        let shipping = 0;
        if( qty >= 6 ) {
            shipping = 10;
        }
        if( qty >= 12 && qty <= 30 ) {
            shipping = 20;
        }
    
        if( qty >= 30 && qty <= 60 ) {
            shipping = 30;
        }
    
        if( qty > 60 ) {
            shipping = 0;
        }
    
        return shipping;
    
    },


    _validateForm: function( form ) {
        let self = this;
        let fields = self.requiredFields;
        let $visibleSet = form.find( "fieldset:visible" );
        let valid = true;

        form.find( ".message" ).remove();

    $visibleSet.each(function() {

        $( this ).find( ":input" ).each(function() {
        let $input = $( this );
        let type = $input.data( "type" );
        let msg = $input.data( "message" );

        if( type == "string" ) {
            if( $input.val() == fields.str.value ) {
                $( "<span class='message'/>" ).text( msg ).
                insertBefore( $input );

                valid = false;
            }
        } else {
            if( !fields.expression.value.test( $input.val() ) ) {
                $( "<span class='message'/>" ).text( msg ).
                insertBefore( $input );

                valid = false;
            }
        }

    });
    });

    return valid;
    },

    _saveFormData: function( form ) {
        let self = this;
        let $visibleSet = form.find( "fieldset:visible" );
    
        $visibleSet.each(function() {
            let $set = $( this );
            if( $set.is( "#fieldset-billing" ) ) {
                let name = $( "#name", $set ).val();
                let email = $( "#email", $set ).val();
                let city = $( "#city", $set ).val();
                let address = $( "#address", $set ).val();
                let zip = $( "#zip", $set ).val();
                let country = $( "#country", $set ).val();
    
                self.storage.setItem( "billing-name", name );
                self.storage.setItem( "billing-email", email );
                self.storage.setItem( "billing-city", city );
                self.storage.setItem( "billing-address", address );
                self.storage.setItem( "billing-zip", zip );
                self.storage.setItem( "billing-country", country );
            } else {
                let sName = $( "#sname", $set ).val();
                let sEmail = $( "#semail", $set ).val();
                let sCity = $( "#scity", $set ).val();
                let sAddress = $( "#saddress", $set ).val();
                let sZip = $( "#szip", $set ).val();
                let sCountry = $( "#scountry", $set ).val();
    
                self.storage.setItem( "shipping-name", sName );
                self.storage.setItem( "shipping-email", sEmail );
                self.storage.setItem( "shipping-city", sCity );
                self.storage.setItem( "shipping-address", sAddress );
                self.storage.setItem( "shipping-zip", sZip );
                self.storage.setItem( "shipping-country", sCountry );
    
            }
        });
    }

};

    $(function(){
        const shop = new $.Shop("#site")
    });

})( jQuery );