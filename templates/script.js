let val_ff;
let val_smoke;
let val_alchl;
let val_xrcs;
let val_age;
let val_dbts;
let val_fh;
let val_haw;
let val_abw;

// ,smoke,alcohol,exercise,age,diabetes,heart_disease,heart_attack_weight,artery_block_weight

const button = document.getElementById('btn')
console.log(button)
button.onclick = function(){
    console.log(val_ff);
}

var a = document.getElementById("fried-food");
function onChange() {
  val_ff = a.value;
  var text = a.options[a.selectedIndex].text;
}
a.onchange = onChange;
onChange();

var e = document.getElementById("alcohol");
function onChange() {
  val_alchl = e.value;
  var text = e.options[e.selectedIndex].text;
}
e.onchange = onChange;
onChange();

var b = document.getElementById("exercise");
function onChange() {
  val_xrcs = b.value;
  var text = b.options[e.selectedIndex].text;
}
b.onchange = onChange;
onChange();

var c = document.getElementById("age");
function onChange() {
  val_age = c.value;
//   var text = e.options[e.selectedIndex].text;
}
c.onchange = onChange;
onChange();

var d = document.getElementById("diabetes");
function onChange() {
  val_dbts = d.value;
  var text = d.options[e.selectedIndex].text;
}
d.onchange = onChange;
onChange();

var g = document.getElementById("family-history");
function onChange() {
  val_dbts = g.value;
  var text = g.options[e.selectedIndex].text;
}
g.onchange = onChange;
onChange();

var h = document.getElementById("smoking");
function onChange() {
  val_dbts = h.value;
  var text = h.options[e.selectedIndex].text;
}
h.onchange = onChange;
onChange();








