$().ready(function() {

    var form = $("#contact-form");
    form.submit(function(e) {
        var submitButton = $("#submit-id-submit");
        submitButton.attr('disabled', true);
        var waitMessage = $("#wait-message");
        waitMessage.prepend('<span>Sending message, please wait... </span>');
        $.post(
            form.attr('action'),
            form.serializeArray(),
            function(data) {
                if(data.is_valid){
                    form.empty();
                    $('#captcha-instructions').hide();
                    $('#thank-you-message').html(data.html);
                } else {
                    submitButton.attr('disabled', false);
                    form.html(data.html);
                }
                waitMessage.empty();
            }
        );
        e.preventDefault();
    });
});
