function copyToClipBoard() {
  /* Get the text field */
  var copyText = document.getElementById("txt-output");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

   /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Đã copy nội dung văn bản vào clipboard");
}
function triggerUpload(){
    document.getElementById("uploadFileInput").click();
}

function showFilePath(input){
    console.log(input);
    if (input.files && input.files[0]) {
        var img = document.getElementById("inputImage");
        img.src = URL.createObjectURL(input.files[0]);
  }
}