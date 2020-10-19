node_list = document.querySelectorAll("[nowrap]");
let fruits = []
for (let checkbox of node_list) {
  fruits.push(checkbox.outerText)
}
fruits.join("\n")
