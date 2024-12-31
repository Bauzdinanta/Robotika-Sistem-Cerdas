fn main() {
    // Basic if/else statement
    if 1 == 2 {
        println!("Nomornya sama");
    } else {
        println!("Nomornya berbeda");
    }

    // Binding a value to a variable using an if/else statement
    let sunny_day = true;
    let take_jacket = if sunny_day {
        "Jangan ambil jaket"
    } else {
        "Ambil jaket"
    };

    println!("{}", take_jacket);

    // Using multiple if/else statements to evaluate multiple conditional statements
    let num = 100;
    let out_of_range: bool;

    if num < 0 {
        out_of_range = true;
    } else if num == 0 {
        out_of_range = true
    } else if num > 101 {
        out_of_range = true;
    } else {
        out_of_range = false
    }
    println!("{}", out_of_range);
}