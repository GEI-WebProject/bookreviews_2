var rateYoConfig = {
    starWidth: "20px"
};

$(function() {
    $(".rateyo-read-only").rateYo({
        readOnly: true,
        ...rateYoConfig
    });
});

$(function() {
    $(".rateyo-interactive").rateYo({
        fullStar: true, 
        ...rateYoConfig,
        // Show previous rating or default value
        rating: $("input[name='rating']").val(),

        // When the rating changes, update the hidden input field
        onSet: function (rating) {
            $("input[name='rating']").val(rating);
        },
      });
    });