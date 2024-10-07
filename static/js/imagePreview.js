function PreviewImage() {
    let fileReader = new FileReader();
    fileReader.readAsDataURL(document.querySelector("#image").files[0]);

    fileReader.onload = function (fileReaderEvent) {
        let preview = document.querySelector("#preview");
        if (preview == null) {
            preview = document.createElement("img");
            preview.setAttribute("id", "preview");
            document.querySelector("#previewHolder").appendChild(preview);
        }

        preview.src = fileReaderEvent.target.result;
    }
}

document.querySelector("#image").onchange = PreviewImage;