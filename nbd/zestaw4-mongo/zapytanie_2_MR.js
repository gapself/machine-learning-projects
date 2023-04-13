// Łączną ilość środków pozostałych na kartach kredytowych osób w bazie,
// w podziale na waluty;
let mapFunction2 = function () {
    this.credit.forEach(el => {
        emit(el.currency, parseInt(el.balance));
    });
};

let reduceFunction2 = function (key, values) {
    return Array.sum(values);
};

printjson(db.people.mapReduce(mapFunction2, reduceFunction2, {out: 'results'}))
printjson(db.results.find().toArray())