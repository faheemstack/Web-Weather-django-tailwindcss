function updateLiveDate() {
  const now = new Date();
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  };
  const formattedDate = now.toLocaleDateString("en-US", options);
  document.getElementById("liveDate").innerHTML = formattedDate;
}
setInterval(updateLiveDate, 1000);
updateLiveDate();


