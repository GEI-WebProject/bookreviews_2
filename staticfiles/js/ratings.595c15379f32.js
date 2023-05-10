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
        readOnly: false,
        ...rateYoConfig
    });
});