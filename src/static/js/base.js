$(document).ready(function() {

    /*
    * Sign up button handler in index.html
    * If clicked, redirect to signup page
    */
    $("#sign_up_btn").click(function() {
        // Signup button clicked
        $("#sign_up_btn").click(function() {
            window.location.href = "/signup";
        })
    })

    /**
     * Full Name Validator in signup.html
     * It checkes if full name is passed or not
    */
   $("#fullname").blur(function() {
    const fullname = $("#fullname").val();

    /**
     * Check if full name is empty or not
     */
    if (fullname.trim() == "") {
        const divFullname = $("#div_fullname");
        divFullname.find('.invalid-feedback').remove();
        divFullname.append(`<div class="invalid-feedback">Full Name can't be empty.</div>`);
        $("#fullname").addClass("is-invalid");
    } else {
        $("#div_fullname").find('.invalid-feedback').remove();
        $("#fullname").removeClass("is-invalid");
        $("#fullname").addClass("is-valid")
    }
    
    })

    /**
     * Email validator in signup.html
     * It checks if the email is passed or not
     */
    $("#email").blur(function() {
        const email = $("#email").val();
        if (email.trim() == "") {
        const divEmail = $("#div_email");
        divEmail.find('.invalid-feedback').remove();
        divEmail.append(`<div class="invalid-feedback">Email can't be empty.</div>`);
        $("#email").addClass("is-invalid");
    } else {
        $("#div_email").find('.invalid-feedback').remove();
        $("#email").removeClass("is-invalid");
    }
    })
});
