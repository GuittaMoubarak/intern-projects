window.onload = function () {
  let btnClose = document.getElementsByClassName("close");
 
  test(btnClose);
  check();
  
};
function newItem() {
  var li = document.createElement("li");
  var inputval = document.getElementById("New").value;
  li.classList.add("item");
  li.addEventListener("click", function () {
    if (this.classList == "item checked") {
      this.classList = "item";
    } else {
      this.classList.add("checked");
    }
  });
  var btn = document.createElement("button");
  btn.className = "close";

  btn.addEventListener("click", function () {
    var div = this.parentElement;
    div.style.display = "none";
  });
  var t = document.createTextNode(inputval);
  var m = document.createTextNode("x");
  btn.appendChild(m);
  li.appendChild(t);
  li.appendChild(btn);
  if (inputval == "") {
    alert("You must enter an item");
  } else {
    document.getElementById("newlist").appendChild(li);
    var enterItem = document.getElementById("New");
    enterItem.value = "";
  }
}
function test(btnClose) {
  console.log(btnClose);
  for (var i = 0; i < btnClose.length; i++) {
    btnClose[i].addEventListener("click", function () {
      this.parentElement.style.display = "none";
    });
  }
}

function check() {
  let listItem = document.getElementsByTagName("li");
  for (let i = 0; i < listItem.length; i++) {
    listItem[i].addEventListener("click", function () {
      if (this.classList == "item checked") {
        this.classList = "item";
      } else {
        this.classList.add("checked");
      }
    });
  }
}

