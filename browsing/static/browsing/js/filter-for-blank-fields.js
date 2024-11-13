document.addEventListener("DOMContentLoaded", function () {
  var form = document.querySelector("form");
  form.addEventListener("submit", function () {
    var inputs = form.querySelectorAll("input, select");
    inputs.forEach(function (input) {
      if (input.value.length === 0) {
        input.disabled = true;
        var nextElement = input.nextElementSibling;
        if (nextElement) {
          nextElement.disabled = true;
        }
      }
    });
  });
});
