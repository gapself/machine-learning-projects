db.people.find().forEach( function (x) {
    x.credit.forEach(el => {
        el.balance = parseInt(el.balance );
    });
    db.people.save(x);
});

printjson(db.people.aggregate([{
    $match: {
        sex: "Female",
        nationality: "Poland"
    }}, {
    $unwind: "$credit",
    }, {
    $group: {
        _id: "$credit.currency",
        totalBalance: { $sum: "$credit.balance"},
        averBalance: { $avg: "$credit.balance"}
    }}
]).toArray())