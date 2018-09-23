$(document).ready(function() {

    var form = $(".form-inline");
    calculatingBasketAmount();

    function basketUpdating(product_id, number, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.number = number;
        
        var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val();
        
        data["csrfmiddlewaretoken"] = csrf_token;
        
        if (is_delete) {
            data["is_delete"] = true;
        }
        
        var url = form.attr("action");
        if (url == null) {
            form = $(".clearfix");        
            url = form.attr("action");
        }
        console.log("URL: ", url);

        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 //console.log("DATA: ", data);
                 if (data.products_total_number || data.products_total_number == 0){
                    $('#basket_total_number').text(data.products_total_number);
                    $('.shopping-cart-list').html("");
                    $.each(data.products, function(k, v) {
                        $('.shopping-cart-list').append('<div class= "product product-widget"><li><div class="product-body"><h3 class="product-price">' + v.price_per_item + '<span class="qty"> ' + v.number + ' шт' + '</span></h3><h2 class="product-name"><a href="#">' + v.name + '</a></h2></div><button class="cancel-btn"><i class="fa fa-trash" data-product_id="' + v.id + '"' + '></i></button></li></div>');
                    });
                 }
             },
             error: function() {
                 console.log("the error");
             }
        });
    }



    form.on('submit', function(e) {
        e.preventDefault();
        
        var number = $('#number').val();
        
        if (number == null) {
            number = 1;    
        }
        var submit_btn = $('#submit_btn');
        var product_id = $(this).attr("id")
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');
        var img_url = submit_btn.data('img_url');     

        basketUpdating(product_id, number, is_delete=false);
                
    })

    // Function for deleting items from cart.
    $(document).on('click', '.fa-trash', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        console.log("Product_id_to_delete: ", product_id);
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true);
    });

         function calculatingBasketAmount() {
            var total_order_amount = 0;            
            var shipping = 100;
            $('.total-product-in-basket-amount').each(function() {
                total_order_amount += parseFloat($(this).text());
                $("#sub-total_amount").text(total_order_amount);
                $('#shipping').text(shipping);
            });

            if (total_order_amount == 0) {
                shipping = 0;
                $("#sub-total_amount").text(total_order_amount);
                $('#shipping').text(shipping);
            }

            total_order_amount += shipping;
            
            console.log("total_order_amount_plus_shipping", total_order_amount);

            $('#total_order_amount').text(total_order_amount.toFixed(2));
         }; 

         // Change amount of products on the checkout page.
         $(document).on('change', '.product-in-basket-number', function() {
            var current_number = $(this).val();
            console.log(parseInt(current_number));
            var current_tr = $(this).closest('tr');
            console.log(current_tr);
            var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
            var total_amount = parseFloat(current_number * current_price).toFixed(2);
            current_tr.find('.total-product-in-basket-amount').text(total_amount);
            calculatingBasketAmount();
         });
         
         //calculatingBasketAmount();

          // Delete a product from checkout page.
          $(document).on('click', '.icon-btn', function(e){
              e.preventDefault();
              product_id = $(this).data("product_id");
              console.log("PRODUCT_ID_CHECKOUT", product_id);
              var current_tr = $(this).closest('tr');
              console.log(current_tr);            
              current_tr.html("");
              nmb = 0;
              basketUpdating(product_id, nmb, is_delete=true);
              calculatingBasketAmount();
           });
         
    

});

