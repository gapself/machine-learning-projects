import scala.annotation.tailrec

object Zestaw1 {

  def main(args: Array[String]) {
    val days = List("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")

    exc1_a(days)
    exc1_b(days)
    exc1_c(days)
    exc2_a(days)
    exc2_b(days)
    exc3(days)
    println("Odpowiedź 4a: " + exc4_a(days))
    println("Odpowiedź 4b: " + exc4_b(days))
    println("Odpowiedź 4c: " + exc4_c(days))

    val prods = Map(
      "tshirt" -> 50,
      "dress" -> 100,
      "belt" -> 150,
    )
    val prod_after_discount = {
      prods map { case (key, value) => (key, value * 0.9) }
    }
    println("Odpowiedź 5: " + prod_after_discount)

    println("Odpowiedź 6:")
    exc6(100,"nbd",true)

    val exc7_list = List(1,2,3)
    val exc7_map = Map (1-> 'A', 2-> 'B', 3-> 'C')
    val exc7_some_value = exc7_list.find(_ > 2)
    val exc7_none_value = exc7_list.find(_ > 3)
    val exc7_some_key = exc7_map.get(2)
    val exc7_none_key = exc7_map.get(4)
    println("Odpowiedź 7: Wartość option==some wyszukana po kluczu w mapie: " + exc7_some_key + ". Wartość option==None wyszukana po kluczu w mapie: " + exc7_none_key )

    val exc8_list = List(1,0,5,-100,199,2,0,5,6,7)
    println("Odpowiedź 8: " + exc8(exc8_list))

    val exc9_list = List(1,2,3,4,5,6)
    println("Odpowiedź 9: " + exc9(exc9_list))

    val exc10_list = List(1,2,3,4,5,6,20,-5,-6,0,13,12)
    println("Odpowiedź 10: " + exc10(exc10_list))
  }

  def exc1_a(days: List[String]) {
    var newString = ""
    for (el <- days) {
      if (newString != "")
        newString += "," + el
        else
        newString += el
    }
    println("Odpowiedź 1a: " + newString)
  }

  def exc1_b(days: List[String]) {
    var newString = ""
    for (el <- days) {
      if (el.startsWith("P"))
        if (newString != "")
          newString += "," + el
        else
          newString += el
    }
    println("Odpowiedź 1b: " + newString)
  }

  def exc1_c(days: List[String]) {
    var id = 0
    var newString = ""
    while (id < days.length) {
      if (newString != "")
        newString += "," + days(id)
      else
        newString += days(id)
      id += 1
    }
    println("Odpowiedź 1c: " + newString)
  }

  // RECURSION
  def exc2_a(days: List[String]) {
    val id = 0
    def joinDaysTogether(id: Int): String = {
      val startDay =
        if (id == days.length - 1) days(id)
        else if (id == days.length) return ""
        else days(id) + ","

      startDay + joinDaysTogether(id + 1)
    }
    println("Odpowiedź 2a: " + joinDaysTogether(id))
  }

  def exc2_b(days: List[String]) {
    val id = 0
    def joinDaysTogether(id: Int): String = {
      val startDay =
        if (id == days.length - 1) days.reverse(id)
        else if (id == days.length) return ""
        else days.reverse(id) + ","
      startDay + joinDaysTogether(id + 1)
    }
    println("Odpowiedź 2b: " + joinDaysTogether(id))
  }

  // TAIL RECURSION
  def exc3(days: List[String]): Unit = {
    val id = 0
    val newString = ""
    @tailrec
    def joinDaysTogether(id: Int, newString: String ): String = {
      val startDay =
        if (id == days.length - 1) days(id)
        else if (id == days.length) return newString
        else days(id) + ","
      joinDaysTogether(id +1, newString + startDay)
    }
    println("Odpowiedź 3: " + joinDaysTogether(id,newString))
  }

  def exc4_a(days: List[String]): String = {
    days.foldLeft("") {
      (all, res) =>
        if (res == days.last) all + res
        else all + res + ","
    }
  }

  def exc4_b(days: List[String]): String = {
    days.foldRight("") {(all, res) => {
      all + "," + res
    }}.dropRight(1)
  }

  def exc4_c(days: List[String]): String = {
    days.foldRight("") {(all, res) => {
      all + "," + res
    }}.dropRight(1)
  }

  def exc6(tup: (Int, String, Boolean)) = {
    println(tup._1)
    println(tup._2)
    println(tup._3)
  }

  // BŁĘDNE, bo może być 0,0 --> i wtedy co?:)
  def exc8(exc8_list: List[Int]):List[Int] = {
    val id = 0
    val valueToRemove = 0
    def deleteZeroValues(id:Int, list: List[Int]):List[Int] = {
      if (id >= list.length) return list
      val (list_1, list_2) = list.splitAt(id)

      if (list(id) == 0)
        deleteZeroValues(id+1, list_1 ++ list_2.tail)
      else
        deleteZeroValues(id+1, list)
    }
    deleteZeroValues(id, exc8_list)
  }

  def exc9(list: List[Int]): List[Int] = {
    list.map(_ + 1)
  }

  def exc10(exc10_list: List[Int]):List[Int] = {
    exc10_list.filter(x => x >= -5 && x <= 12).map (x => x.abs)
  }
}