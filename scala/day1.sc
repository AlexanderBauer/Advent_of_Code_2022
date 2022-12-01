// scala -nobootcp -nc day1.sc

// imports
import scala.io.Source

object day1 {
  def main(args: Array[String]): Unit = {

    // initial values
    var elf_calories: Int = 0
    var calories_list = new Array[Int](0)

    val filename = "../inputs/day1.txt"

    for (calories <- Source.fromFile(filename).getLines) {
        if(calories == "") {
          calories_list +:= elf_calories
          elf_calories = 0;
        }
        else {
            elf_calories += calories.toInt
        }
    }

    // solution part one
    val solution_part_one = calories_list.max // 70374

    // solution part two
    // sort list reversed and sum up top 3 values
    val sorted = calories_list.sorted(Ordering[Int].reverse)
    var solution_part_two = 0;
    for ( i <- 0 to 2) {
         solution_part_two += sorted(i);
      }
  }
}
