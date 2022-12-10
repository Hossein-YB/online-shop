/* Product Quantity */
$(".quantity").append('<div class="dec qtybutton">-</div><div class="inc qtybutton">+</div>');

$(".qtybutton").on("click", function() {
    var $button = $(this);
    var oldValue = $button.parent().find("input").val();
    if ($button.hasClass("inc")) {
        var newVal = parseFloat(oldValue) + 1;
    } else {
        // Don't allow decrementing below zero
        if (oldValue > 1) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 1;
        }
    }
    $button.parent().find("input").val(newVal);
});

/* close btn */

$('.btn-close').on('click', function(e) {
    e.preventDefault();
    var $this = $(this);
    $this.parents('.open').removeClass('open');
    $($overlay).removeClass('overlay-open');
});


$('.tt').toolip('show');

$('.po').popover('show');

$('.tot').toast('show');