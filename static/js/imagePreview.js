function PreviewImage() {
    const imageInput = document.querySelector("#image");

    let fileReader = new FileReader();
    fileReader.readAsDataURL(imageInput.files[0]);

    fileReader.onload = function (fileReaderEvent) {
        let preview = document.querySelector("#preview");
        if (preview == null) {
            const previewHolder = document.querySelector("#previewHolder");

            // Disable selection feedback
            const selectionFeedback = document.querySelector("#selectionFeedback");
            selectionFeedback.style.display = "none";

            // Create preview image
            preview = document.createElement("img");
            preview.setAttribute("id", "preview");
            previewHolder.appendChild(preview);

            // Create and initialize cancel button
            const cancelButton = document.createElement("input");
            cancelButton.setAttribute("type", "button");
            cancelButton.setAttribute("class", "cancelButton");
            cancelButton.value = "REMOVE IMAGE";
            cancelButton.onclick = function () {
                // Show selection feedback again
                selectionFeedback.style.display = "block";

                // Remove all unnecessary elements
                imageInput.value = "";
                preview.remove();
                cancelButton.remove();
            }
            previewHolder.appendChild(cancelButton);
        }

        preview.src = fileReaderEvent.target.result;
    }
}

document.querySelector("#image").onchange = PreviewImage;