console.log("aous");
apps = document.getElementsByClassName("my-card");
for (const div of apps) {
  $(div).hover(
    function () {
      let req_id = "#" + div.id + "_name";
      $(req_id).css("display", "block");
    },
    function () {
      let req_id = "#" + div.id + "_name";
      $(req_id).css("display", "none");
    }
  );
}
