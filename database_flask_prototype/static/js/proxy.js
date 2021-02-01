/*
I took the img-upload function from Chenhao's img uploader, then
ported it over to also submit user info. I then realized that we
could just set a few attributes on the HTML form that circumvents
the need for any JQuery. In any case, these are good examples of 
how to use JQuery should we require it in the future - Jonas :)
*/

$(function () {
    $("#profile-upload").on("click", function () {

        var fd = new FormData();
        var name = document.getElementById("profile-form").elements["name"];
        var email = document.getElementById("profile-form").elements["email"];

        fd.append("name", name);
        fd.append("email", email);

        $.ajax({
            url: "/create-account",
            data: fd,
            type: "POST",
            dataType: "json",
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                alert("Profile Created!");
            }
        })
    })
});


$(function () {
    $("#img-upload").on("click", function () {

        var fileObj = document.getElementById("picpath").files[0];
        if (typeof (fileObj) == "undefined" || fileObj.size <= 0) {
            alert("Please choose an image");
            return;
        }
        var formFile = new FormData();
        formFile.append("action", "UploadVMKImagePath");
        formFile.append("file", fileObj);
    
        var data = formFile;
        $.ajax({
            url: "/upload-image",
            data: data,
            type: "POST",
            dataType: "json",
            cache: false,
            processData: false,
            contentType: false,
            success: function (result) {
                alert("Successful Upload!");
            }
        })
    })
});