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
        onSet: function (rating) {
            // Send the rating value to the server
            $("input[name='rating']").val(rating);
        },
      });
    });