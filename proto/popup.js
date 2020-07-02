document.addEventListener("DOMContentLoaded", () => {
  const ul = document.querySelector("#js-history-list");
  let html = "";
  const query = {
    text: "",
  };
  chrome.history.search(query, (results) => {
    results.forEach((result) => {
      html +=
        "<li>" +
        '<a href="' +
        result.url +
        '" target="_blank">' +
        result.title +
        "</a>" +
        "<br>" +
        '<a href="https://twitter.com/intent/tweet?url=' +
        result.url +
        '" target="_blank">tw</a>' +
        "</li>";
    });
    ul.innerHTML = html;
  });
});
