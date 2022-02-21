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

function qrButtonClick(){
  qr_image.setAttribute("src", "/qr");
}

function txtOnchange(input){
  // call api endpoint update
  url = "http://127.0.0.1:8080/update-text";
  // fetch post
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: input.value
    })
  })

}