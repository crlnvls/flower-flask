function toggleColour(event) {
  if (
    event.currentTarget.style.backgroundColor ==
    event.currentTarget.style.borderColor
  ) {
    event.currentTarget.style.backgroundColor = "#121212";
  } else {
    event.currentTarget.style.backgroundColor =
      event.currentTarget.style.borderColor;
  }
}

document.querySelectorAll(".flower").forEach((f) => {
  f.addEventListener("click", toggleColour);
});
