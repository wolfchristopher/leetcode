function hashStringToInt(s, tableSize) {
    let hash = 17;

    for(let i = 0; i < s.length; i++) {
        hash = (13 * hash * s.charCodeAt(i) % tableSize)
    }

    return hash
}

class HashTable {
    table = new Array(2001)

    numsItems = 0
    // loadfactor = this.numItems / this.table.length

    setItem = (key, value) => {
        this.numItems++
        const loadfactor = this.numItems /this.table.length
        
        const index = hashStringToInt(key, this.table.length)
        if (this.table[index]) {
            this.table[index].push([[key, value]])
        } else {
            this.table[index] = [[key, value]]
        }
    }

    getItem = key => {
        const index = hashStringToInt(key, this.table.length)
        if (!this.table[index]) {
            return null
        }

        // O(n)
        return this.table[index].find(x => x[0] === key)[1]
    }

}

const myTable = new HashTable();
myTable.setItem("firstName", "bob")
myTable.getItem("firstName")
console.log(myTable.getItem("firstName"))

