use std::collections::{HashSet, HashMap};
use std::thread;
use std::time::Duration;

// Tipe data untuk posisi
type Position = (usize, usize);

// Struktur untuk robot
struct Robot {
    position: Position,
    goal: Position,
}

impl Robot {
    fn new(start: Position, goal: Position) -> Self {
        Robot { position: start, goal }
    }

    // Fungsi untuk memindahkan robot ke tujuan jika memungkinkan
    fn move_towards_goal(&mut self) {
        if self.position.0 < self.goal.0 {
            self.position.0 += 1;
        } else if self.position.0 > self.goal.0 {
            self.position.0 -= 1;
        }

        if self.position.1 < self.goal.1 {
            self.position.1 += 1;
        } else if self.position.1 > self.goal.1 {
            self.position.1 -= 1;
        }

        println!("Robot bergerak ke posisi {:?}", self.position);
    }

    fn reached_goal(&self) -> bool {
        self.position == self.goal
    }
}

// Struktur untuk lingkungan
struct Environment {
    obstacles: HashSet<Position>, // Rintangan yang ada di peta
    events: HashMap<String, Box<dyn Fn()>>, // Daftar event yang dapat dipicu
}

impl Environment {
    fn new() -> Self {
        Environment {
            obstacles: HashSet::new(),
            events: HashMap::new(),
        }
    }

    // Fungsi untuk menambahkan rintangan
    fn add_obstacle(&mut self, position: Position) {
        self.obstacles.insert(position);
        println!("Rintangan ditambahkan di {:?}", position);
    }

    // Fungsi untuk menghapus rintangan
    fn remove_obstacle(&mut self, position: Position) {
        if self.obstacles.remove(&position) {
            println!("Rintangan dihapus di {:?}", position);
        }
    }

    // Fungsi untuk menambahkan event
    fn add_event(&mut self, name: String, event: Box<dyn Fn()>) {
        self.events.insert(name, event);
    }

    // Fungsi untuk memicu event
    fn trigger_event(&self, name: &str) {
        if let Some(event) = self.events.get(name) {
            event();
        }
    }

    // Fungsi untuk memeriksa perubahan yang perlu ditanggapi oleh robot
    fn check_for_changes(&self, robot: &Robot) {
        // Jika robot mencapai tujuannya, robot akan berhenti
        if robot.reached_goal() {
            println!("Robot telah mencapai tujuan!");
            return;
        }

        // Memeriksa apakah ada rintangan di jalur robot
        if self.obstacles.contains(&robot.position) {
            println!("Rintangan terdeteksi di posisi {:?}, robot berhenti!", robot.position);
            return;
        }

        // Memicu event perubahan tujuan jika perlu
        self.trigger_event("goal_reached");
    }
}

fn main() {
    // Membuat lingkungan dan robot
    let mut environment = Environment::new();
    let mut robot = Robot::new((0, 0), (4, 4));

    // Menambahkan beberapa rintangan
    environment.add_obstacle((2, 2));
    environment.add_obstacle((3, 3));

    // Menambahkan event yang memicu jika tujuan tercapai
    environment.add_event("goal_reached".to_string(), Box::new(|| {
        println!("Event: Tujuan telah tercapai!");
    }));

    // Event-driven loop untuk robot
    loop {
        // Memeriksa apakah ada perubahan yang memerlukan respons robot
        environment.check_for_changes(&robot);

        // Jika robot sudah mencapai tujuan, keluar dari loop
        if robot.reached_goal() {
            break;
        }

        // Robot bergerak menuju tujuan
        robot.move_towards_goal();

        // Tunggu sebentar sebelum memeriksa lagi (mensimulasikan penundaan)
        thread::sleep(Duration::from_secs(1));
    }
}
