node_list = document.querySelectorAll("[nowrap]");
let fruits = []
for (let checkbox of node_list) {
  fruits.push(checkbox.outerText)
}
console.log(fruits.join("\n"))
console.log(fruits.length)
