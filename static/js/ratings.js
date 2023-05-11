var rateYoConfig = {
    starWidth: "20px"
};

$(function() {
    $(".rateyo-read-only").rateYo({
        readOnly: true,
        ratedFill: "#3DA7F3",
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

        // Set different colors for different ratings
        multiColor: {
            "startColor": "#CFE9FC", // light blue
            "endColor"  : "#3DA7F3" // dark blue
        },
      });
    });