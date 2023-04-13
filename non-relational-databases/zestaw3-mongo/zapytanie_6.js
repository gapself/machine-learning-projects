printjson(db.people.insert([{
    "sex" : "Female",
    "first_name" : "Gabriela",
    "last_name" : "Paszkiewicz",
    "job" : "Junior Web Developer",
    "email" : "testgabi@test.test",
    "location" : {
        "city" : "Warszawa",
        "address" : {
            "streetname" : "Fake",
            "streetnumber" : "3210"
        }
    },
    "description" : "bla bla bla",
    "height" : "178",
    "weight" : "57",
    "birth_date" : "1996-03-25T11:51:38Z",
    "nationality" : "Poland",
    "credit" : [
        {
            "type" : "instapayment",
            "number" : "3482509567781672",
            "currency" : "PLN",
            "balance" : "8938.66"
        },
        {
            "type" : "visa-electron",
            "number" : "6379756322338409",
            "currency" : "PLN",
            "balance" : "4280.15"
        },
        {
            "type" : "diners-club-international",
            "number" : "3539516060377020",
            "currency" : "LKR",
            "balance" : "53402.31"
        },
        {
            "type" : "jcb",
            "number" : "5602323447627424",
            "currency" : "CNY",
            "balance" : "43453.86"
        },
        {
            "type" : "jcb",
            "number" : "352984503996014",
            "currency" : "ARS",
            "balance" : "49544.8"
        }
    ]
}]))