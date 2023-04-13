db.people.find().forEach( function (x) {
    x.credit.forEach(el => {
        el.balance = parseInt(el.balance );
    });
    db.people.save(x);
});

printjson(db.people.aggregate([
    { $unwind : "$credit" },
    { $group: { _id: "$credit.currency" , totalBalance: {$sum: "$credit.balance"}}}
]).toArray())


/* db.people.aggregate([
    { $unwind : "$credit" },
    { $addFields: {convertedBalance: { $toDecimal: "$credit.balance" }}},
    { $group: { _id: "$credit.currency" , totalBalance: {$sum: "$convertedBalance"}}}
]) */