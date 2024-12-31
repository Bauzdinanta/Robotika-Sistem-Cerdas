use std::io;

fn main() {
    // Menetapkan posisi awal robot
    let mut robot_position = (0, 0); // Robot mulai di posisi (0, 0)
    let grid_size = (5, 5); // Ukuran grid adalah 5x5

    loop {
        // Mencetak posisi robot saat ini
        println!("Posisi robot saat ini: {:?}", robot_position);

        // Meminta input dari pengguna untuk gerakan
        println!("Masukkan gerakan (w = atas, s = bawah, a = kiri, d = kanan, q = keluar):");

        // Membaca input dari pengguna
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Gagal membaca input");
        let input = input.trim().to_lowercase();

        // Keluar jika pengguna memasukkan 'q'
        if input == "q" {
            println!("Keluar dari program.");
            break;
        }

        // Menggerakkan robot sesuai input
        match input.as_str() {
            "w" => {
                // Gerakan ke atas
                if robot_position.0 > 0 {
                    robot_position.0 -= 1;
                } else {
                    println!("Robot sudah mencapai batas atas!");
                }
            }
            "s" => {
                // Gerakan ke bawah
                if robot_position.0 < grid_size.0 - 1 {
                    robot_position.0 += 1;
                } else {
                    println!("Robot sudah mencapai batas bawah!");
                }
            }
            "a" => {
                // Gerakan ke kiri
                if robot_position.1 > 0 {
                    robot_position.1 -= 1;
                } else {
                    println!("Robot sudah mencapai batas kiri!");
                }
            }
            "d" => {
                // Gerakan ke kanan
                if robot_position.1 < grid_size.1 - 1 {
                    robot_position.1 += 1;
                } else {
                    println!("Robot sudah mencapai batas kanan!");
                }
            }
            _ => {
                println!("Perintah tidak valid. Gunakan w, s, a, d untuk menggerakkan robot, atau q untuk keluar.");
            }
        }
    }
}
