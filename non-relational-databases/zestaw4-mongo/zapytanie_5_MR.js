// Średnia i łączna ilość środków
// na kartach kredytowych kobiet narodowości
// polskiej w podziale na waluty.

let mapFunction5 = function () {
    if (this.nationality == "Poland" && this.sex == "Female") {
        this.credit.forEach(el => {
            emit(el.currency, parseInt(el.balance));
        });
    }
};

let reduceFunction5 = function (key, values) {
    let sumBalance = Array.sum(values);
    let averBalance = sumBalance / values.length;

    return {
        sumBalance, averBalance
    }
};

printjson(db.people.mapReduce(mapFunction5, reduceFunction5, {out: 'results_sum_aver_balance'}))
printjson(db.results_sum_aver_balance.find().toArray())