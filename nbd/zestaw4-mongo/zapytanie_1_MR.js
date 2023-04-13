// Średnią wagę i wzrost osób w bazie z podziałem na płeć (tzn. osobno mężczyzn, osobno kobiet);

let mapFunction = function() {
    emit(this.sex, {height: parseInt(this.height), weight: parseInt(this.weight)});
};

let reduceFunction = function(key, value) {
    let sumHeights = 0;
    let sumWeights = 0;

    value.forEach(x => {
        sumHeights += x.height;
        sumWeights += x.weight;
    });

    return {
        averWeight: sumWeights / value.length,
        averHeight: sumHeights / value.length
    }
};

printjson(db.people.mapReduce(mapFunction, reduceFunction, {out: "result_aver_weights_heights"}))
printjson(db.result_aver_weights_heights.find().toArray())

