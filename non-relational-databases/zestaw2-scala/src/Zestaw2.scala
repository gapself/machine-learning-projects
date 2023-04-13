class KontoBankowe(stanPoczatkowy: Double=0) {
  private var _stanKonta = stanPoczatkowy
  def stanKonta: Double = _stanKonta

  def wplata(wartosc: Double): Double = {
    _stanKonta += wartosc
    _stanKonta
  }

  def wyplata(wartosc: Double): Double = {
    if (_stanKonta - wartosc <= 0) return _stanKonta
    _stanKonta -= wartosc
    _stanKonta
  }
}

case class Osoba(imie: String, nazwisko: String) {
  val podatek = 0

  def przywitanieOsoby(osoba: Osoba): String = {
    val przywitanie = osoba match {
      case Osoba("Gabi", "Paszkiewicz") => "Hello Gabi!"
      case Osoba("Anna", "Kowalska") => "Hello Anna!"
      case _ => "Hello DEFAULTOWE PRZYWITANIE"
    }
    println("Zadanie 3: przywitanie dla imienia " + imie + " ===> " + przywitanie)
    przywitanie
  }
}

trait Student extends Osoba {
  override val podatek = 0
}

trait Pracownik extends Osoba {
  override val podatek = 20
  var pensja = 0
}

trait Nauczyciel extends Pracownik {
  override val podatek = 10
}

object Zestaw2 {
  def main(args: Array[String]): Unit = {

    println("Odpowiedź 1: <input:Środa>: " + exc1("Środa"))
    println("Odpowiedź 1: <input:Niedziela>: " + exc1("Niedziela"))
    println("Odpowiedź 1: <input:Coś>: " + exc1("Coś"))

    val kontoBankowe_1 = new KontoBankowe(200)
    println("Odpowiedź 2: <gdy stan poczatk = 200> " + kontoBankowe_1.stanKonta)
    val kontoBankowe_2 = new KontoBankowe()
    println("Odpowiedź 2: <przy założeniu konta> " + kontoBankowe_2.stanKonta)
    println("Odpowiedź 2: <przy wplacie na konto +50 > " + kontoBankowe_2.wplata(50))
    println("Odpowiedź 2: <przy wyplacie z konta -23 > " + kontoBankowe_2.wyplata(23))

    val osoba_1 = Osoba("Gabi", "Paszkiewicz")
    val osoba_2 = Osoba("Anna", "Kowalska")
    val osoba_3 = Osoba("Adam", "Mickiewicz")

    osoba_1.przywitanieOsoby(osoba_1)
    osoba_2.przywitanieOsoby(osoba_2)
    osoba_3.przywitanieOsoby(osoba_3)

    val numb = 5
    println("Odpowiedź 4: " + exc4(numb,odejmowanie))

    val osoba_student = new Osoba("Ga", "Pasz") with Student
    val osoba_prac = new Osoba("Ann", "Kow") with Pracownik
    val osoba_naucz = new Osoba("Ewa", "Bcd") with Nauczyciel
    val osoba_stud_prac = new Osoba("Tomasz", "Nowak") with Student with Pracownik
    val osoba_prac_stud = new Osoba("Aleks", "Abcowik") with Pracownik with Student

    println(s"Odpowiedź 5: Podatek pracownika: ${osoba_prac.podatek}%")
    println(s"Odpowiedź 5: Podatek nauczyciela: ${osoba_naucz.podatek}%")
    println(s"Odpowiedź 5: Podatek studenta: ${osoba_student.podatek}%")
    println(s"Odpowiedź 5: Podatek studiującego pracownika: ${osoba_stud_prac.podatek}%")
    println(s"Odpowiedź 5: Podatek pracującego studenta: ${osoba_prac_stud.podatek}%")
  }

  def exc1(word: String): String = {
    val workDays = List("Poniedziałek","Wtorek","Środa","Czwartek","Piątek")
    val weekend = List("Sobota","Niedziela")
    word match {
      case a if workDays.contains(a) => "Praca"
      case b if weekend.contains(b) => "Weekend"
      case _ => "Nie ma takiego dnia"
    }
  }

  def exc4(numb: Int, fun_param: (Int) => Int): Int = {
    fun_param(fun_param(fun_param(numb)))
  }

  def odejmowanie(numb4: Int): Int = {
    numb4 - 1
  }
}