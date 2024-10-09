function PreviewImage() {
    let fileReader = new FileReader();
    fileReader.readAsDataURL(document.querySelector("#image").files[0]);

    fileReader.onload = function (fileReaderEvent) {
        let preview = document.querySelector("#preview");
        if (preview == null) {
            const selectionFeedback = document.querySelector("#selectionFeedback");
            selectionFeedback.style.display = "none";

            preview = document.createElement("img");
            preview.setAttribute("id", "preview");
            document.querySelector("#previewHolder").appendChild(preview);

            const cancelButton = document.createElement("input");
            cancelButton.setAttribute("type", "button");
            cancelButton.setAttribute("class", "cancelButton");
            cancelButton.value = "REMOVE IMAGE";
            cancelButton.onclick = function () {
                selectionFeedback.style.display = "block";

                document.querySelector("#image").value = "";
                preview.remove();
                cancelButton.remove();
            }
            document.querySelector("#previewHolder").appendChild(cancelButton);
        }

        preview.src = fileReaderEvent.target.result;
    }
}

document.querySelector("#image").onchange = PreviewImage;