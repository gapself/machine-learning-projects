// 3. Listę unikalnych zawodów;

let mapFunction3 = function() {
    emit(this.job, 0);
};

let reduceFunction3 = function(key, value) {
    return 0
};

printjson(db.people.mapReduce(mapFunction3, reduceFunction3, {out: "unique_jobs"}))
printjson(db.unique_jobs.find().toArray())

