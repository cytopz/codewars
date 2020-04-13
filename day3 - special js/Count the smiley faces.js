const countSmileys = arr => arr.filter(str => str.match(/^[:;]{0,1}[-~]{0,1}[)D]$/g)).length
