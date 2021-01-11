node_list = document.querySelectorAll(".name > .hidden-xs.hidden-sm");
let fruits = []
for (let checkbox of node_list) {
  fruits.push("https://github.com/" + checkbox.outerText)
}
console.log(fruits.join("\n"))
console.log(fruits.length)