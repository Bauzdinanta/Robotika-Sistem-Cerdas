use rand::Rng;
use std::collections::HashSet;

type Position = (usize, usize);

#[derive(Debug, Clone, Copy)]
enum Action {
    Up,
    Down,
    Left,
    Right,
}

#[derive(Debug, Clone)]
struct Robot {
    position: Position,
    uncertainty: f64, // Ketidakpastian posisi robot (dalam hal ini, semacam noise)
}

impl Robot {
    fn new(start: Position, uncertainty: f64) -> Self {
        Robot {
            position: start,
            uncertainty,
        }
    }

    // Fungsi untuk bergerak dengan memperhitungkan ketidakpastian
    fn move_with_noise(&mut self, action: Action) {
        let mut rng = rand::thread_rng();

        // Memperkenalkan ketidakpastian dalam gerakan
        let noise = rng.gen_range(0.0..self.uncertainty); // Noise dalam rentang [0, uncertainty]
        let move_amount = if noise < 0.5 { 1 } else { 0 };

        match action {
            Action::Up => {
                if move_amount == 1 {
                    self.position.1 = self.position.1.saturating_sub(1);
                }
            }
            Action::Down => {
                self.position.1 += move_amount;
            }
            Action::Left => {
                if move_amount == 1 {
                    self.position.0 = self.position.0.saturating_sub(1);
                }
            }
            Action::Right => {
                self.position.0 += move_amount;
            }
        }
    }

    // Fungsi untuk memeriksa apakah robot telah mencapai tujuan
    fn reached_goal(&self, goal: Position) -> bool {
        self.position == goal
    }
}

#[derive(Debug)]
struct Environment {
    obstacles: HashSet<Position>,
    goal: Position,
}

impl Environment {
    fn new(goal: Position) -> Self {
        Environment {
            obstacles: HashSet::new(),
            goal,
        }
    }

    fn add_obstacle(&mut self, obstacle: Position) {
        self.obstacles.insert(obstacle);
    }

    fn is_free(&self, pos: Position) -> bool {
        !self.obstacles.contains(&pos)
    }
}

fn sample_based_navigation(robot: &mut Robot, environment: &Environment, max_steps: usize) -> Vec<Action> {
    let actions = vec![Action::Up, Action::Down, Action::Left, Action::Right];
    let mut path = Vec::new();

    let mut rng = rand::thread_rng();
    let mut current_position = robot.position;

    for _ in 0..max_steps {
        // Jika robot sudah mencapai tujuan
        if robot.reached_goal(environment.goal) {
            break;
        }

        let mut best_action = None;
        let mut best_position = current_position;
        let mut best_score = f64::NEG_INFINITY;

        // Mengambil sampel acak untuk mencoba beberapa tindakan
        for action in &actions {
            let mut robot_copy = robot.clone();
            robot_copy.move_with_noise(*action);

            // Jika posisi setelah gerakan valid (tidak ada rintangan)
            if environment.is_free(robot_copy.position) {
                // Skor dihitung berdasarkan seberapa dekat dengan tujuan (lebih dekat lebih baik)
                let score = -((robot_copy.position.0 as isize - environment.goal.0 as isize).abs()
                    + (robot_copy.position.1 as isize - environment.goal.1 as isize).abs()) as f64;

                if score > best_score {
                    best_action = Some(*action);
                    best_position = robot_copy.position;
                    best_score = score;
                }
            }
        }

        if let Some(action) = best_action {
            robot.move_with_noise(action);
            path.push(action);
            current_position = robot.position;
        }
    }

    path
}

fn main() {
    let start = (0, 0);
    let goal = (5, 5);
    let uncertainty = 0.3; // Ketidakpastian dalam pergerakan robot (misalnya 30%)

    let mut robot = Robot::new(start, uncertainty);
    let mut environment = Environment::new(goal);

    // Menambahkan beberapa rintangan
    environment.add_obstacle((2, 2));
    environment.add_obstacle((3, 3));

    println!("Robot mulai di posisi: {:?}", robot.position);

    let path = sample_based_navigation(&mut robot, &environment, 20);

    if robot.reached_goal(goal) {
        println!("Robot berhasil mencapai tujuan!");
        println!("Langkah-langkah yang diambil robot:");
        for action in path {
            println!("{:?}", action);
        }
    } else {
        println!("Robot gagal mencapai tujuan.");
    }
}
