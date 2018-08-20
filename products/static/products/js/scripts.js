$(document).ready(function() {
    
    var form = $('#form_buying_product');
    
    function basketUpdating(product_id, number, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.number = number;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        
        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
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
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');
        var img_url = submit_btn.data('img_url');     

        basketUpdating(product_id, number, is_delete=false);
                
       // $( '.fa-trash').on('click', function(e) {
            //$(this).closest('li').remove();
            //console.log("delete");
         //   e.preventDefault();
           // number = 0;
            //product_id = $(this).data('product_id');
            //basketUpdating(product_id, number, is_delete=true);
        //});
    })

         $(document).on('click', '.fa-trash', function(e){
             console.log("delete function");
             e.preventDefault();
             product_id = $(this).data("product_id");
             console.log(product_id);
             nmb = 0;
             basketUpdating(product_id, nmb, is_delete=true)
     });

         function calculatingBasketAmount() {
            var total_order_amount = 0
            $('.total-product-in-basket-amount').each(function() {
                total_order_amount += parseFloat($(this).text());
            });
            $('#total_order_amount').text(total_order_amount.toFixed(2));
         }; 

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
         
         calculatingBasketAmount();

});

