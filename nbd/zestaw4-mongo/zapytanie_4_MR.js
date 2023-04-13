// Średnie, minimalne i maksymalne BMI
// (waga/wzrost^2) dla osób w bazie, w podziale
// na narodowości;

// Średnią wagę i wzrost osób w bazie z podziałem na płeć (tzn. osobno mężczyzn, osobno kobiet);

let mapFunction4 = function() {
    emit(this.nationality, {height: parseInt(this.height), weight: parseInt(this.weight)});
};

let reduceFunction4 = function(key, value) {
    let sumBmi = 0;
    let maxBmi = 0;
    let minBmi = Infinity;

    value.forEach(x => {
        let newBmi = ((x.weight/Math.pow(x.height,2))*10000)
        sumBmi += newBmi

        if (newBmi > maxBmi) {
            maxBmi = newBmi
        }

        if (newBmi < minBmi) {
            minBmi = newBmi
        }

    });

    return {
        averBmi: sumBmi / value.length,
        maxBmi: maxBmi,
        minBmi: minBmi
    }
};

printjson(db.people.mapReduce(mapFunction4, reduceFunction4, {out: "result_bmi"}))
printjson(db.result_bmi.find().toArray())

