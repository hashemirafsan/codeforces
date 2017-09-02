var a = readline();
var b = a.split("WUB")

var c = []

b.map(function(item) {
  if(item.length > 0) {
    c.push(item)
  }
})

print(c.join(" "));