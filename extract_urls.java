urls = []
$$('*').forEach(element => {
  urls.push(element.src)
  urls.push(element.href)
  urls.push(element.url)
}); 
array = Array.from(new Set(urls))
console.log(array.join("\n"))
console.log(array.length)
