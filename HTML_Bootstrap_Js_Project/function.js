const submit = document.getElementById("register");
submit.addEventListener("click", validate);
function validate(e) {
  e.preventDefault();
  const fullname = document.getElementById("name");
  var nvname = document.getElementById("NotValidFullName");
  var vname = document.getElementById("ValidFullName");
  var nvemail = document.getElementById("NotValidEmail");
  var vemail = document.getElementById("ValidEmail");
  var nvpass = document.getElementById("NotValidPassword");
  var vpass = document.getElementById("ValidPassword");
  var nvconf = document.getElementById("NotValidConf");
  var vconf = document.getElementById("ValidConf");
  var nvconfir = document.getElementById("NotValidconfirm");
  var crosName = document.getElementById("crossName");
  var truName= document.getElementById("trueName");
  var crosEmail = document.getElementById("crossEmail");
  var truEmail= document.getElementById("trueEmail");
  var crosPass = document.getElementById("crossPass");
  var truPass= document.getElementById("truePass");
  var crosConf = document.getElementById("crossConf");
  var truConf= document.getElementById("trueConf");
  if (!fullname.value) {
    nvname.classList.add("d-block");
    crosName.classList.add("d-block");
    vname.classList = "valid-feedback";
    truName.classList.remove("d-block");
  } else {
    
    vname.classList.add("d-block");
    truName.classList.add("d-block");
    nvname.classList = "invalid-feedback";
    crosName.classList.remove("d-block");
  }
  const email = document.getElementById("Email");

  if (!email.value) {
    nvemail.classList.add("d-block");
    crosEmail.classList.add("d-block");
    vemail.classList = "valid-feedback";
    truEmail.classList.remove("d-block");
  } else {
    vemail.classList.add("d-block");
    truEmail.classList.add("d-block");
    nvemail.classList = "invalid-feedback";
    crosEmail.classList.remove("d-block");
  }
  const password = document.getElementById("Pass");
  if (!password.value) {
    nvpass.classList.add("d-block");
    crosPass.classList.add("d-block");
    vpass.classList = "valid-feedback";
    truPass.classList.remove("d-block");
  } else {
    vpass.classList.add("d-block");
    truPass.classList.add("d-block");
    nvpass.classList = "invalid-feedback";
    crosPass.classList.remove("d-block");
  }
  const con_pass = document.getElementById("Conf_Pass");

  if (!con_pass.value || con_pass !== password) {
    nvconf.classList.add("d-block");
    crosConf.classList.add("d-block");
    vconf.classList = "valid-feedback";
    truConf.classList.remove("d-block");
  } else {
    vconf.classList.add("d-block");
    truConf.classList.add("d-block");
    nvconf.classList = "invalid-feedback";
    crosConf.classList.remove("d-block");
  
  }
  const confir = document.getElementById("confirm");
  if (!confir.checked) {
    nvconfir.classList.add("d-block");
  } else {
    nvconfir.classList = "invalid-feedback";
  }
  return true;
}
