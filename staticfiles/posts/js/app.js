// app.js
document.addEventListener("DOMContentLoaded", function () {
    const titles = document.querySelectorAll(".post-title");

    titles.forEach((title) => {
        title.addEventListener("click", function () {
            alert("Siz ushbu postga bosdingiz: " + title.textContent);
        });
    });
});
