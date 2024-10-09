window.addEventListener("load", function () {
    const textarea = document.querySelector("textarea")
    let textRows = textarea.value.split("\n");
    
    let textWidth = textRows[0].length;
    let textHeight = textRows.length - 1;
    let newSize = Math.max(-1/6 * textWidth + 48, 4);
    
    console.log(textWidth, textHeight, newSize);
    
    textarea.style.fontSize = `${newSize}px`;
    textarea.style.lineHeight = `${newSize}px`;
    textarea.rows = textHeight + 1;
    textarea.style.height = `${textarea.rows * newSize}px`;
})