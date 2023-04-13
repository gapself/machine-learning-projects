// db.people.find().forEach(function(data) {
//     db.people.update({
//         "_id": data._id,
//         "sex": data.sex,
//     }, {
//         "$set": {
//             "weight": parseInt(data.weight),
//             "height": parseInt(data.height)
//         }
//     });
// })

printjson(db.people.aggregate(
    [{$group: {
        _id: '$sex',
        totalWeight: { $sum: '$weight' },
        totalHeight: { $sum: '$height' },
        total_elements: { $sum: 1 }
    }},
    {$project: {
        averWeight: {
            $divide: ['$totalWeight', '$total_elements']
        },
        averHeight: {
            $divide: ['$totalHeight', '$total_elements']
        }
    }}
]).toArray())