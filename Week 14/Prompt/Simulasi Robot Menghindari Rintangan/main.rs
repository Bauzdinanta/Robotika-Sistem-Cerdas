use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
struct Node {
    position: (usize, usize),
    g: usize, // Biaya dari titik awal ke node ini
    h: usize, // Perkiraan biaya dari node ini ke tujuan (heuristik)
}

impl Node {
    fn new(position: (usize, usize), g: usize, h: usize) -> Self {
        Node { position, g, h }
    }

    // Fungsi untuk menghitung f(n) = g(n) + h(n)
    fn f(&self) -> usize {
        self.g + self.h
    }
}

// Membandingkan dua node berdasarkan nilai f(n)
impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        other.f().cmp(&self.f()) // Membalikkan urutan untuk menggunakan BinaryHeap sebagai Min-Heap
    }
}

// Membandingkan dua node berdasarkan nilai f(n)
impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// Fungsi untuk menghitung jarak Manhattan (heuristik A*)
fn manhattan_distance(start: (usize, usize), goal: (usize, usize)) -> usize {
    (start.0 as isize - goal.0 as isize).abs() as usize + (start.1 as isize - goal.1 as isize).abs() as usize
}

fn find_path(grid: Vec<Vec<i32>>, start: (usize, usize), goal: (usize, usize)) -> Option<Vec<(usize, usize)>> {
    let directions = vec![
        (0, 1),  // kanan
        (1, 0),  // bawah
        (0, isize::MAX),  // kiri
        (isize::MAX, 0)  // atas
    ];

    let mut open_set = BinaryHeap::new();
    let mut came_from: HashMap<(usize, usize), (usize, usize)> = HashMap::new();
    let mut g_score: HashMap<(usize, usize), usize> = HashMap::new();
    let mut f_score: HashMap<(usize, usize), usize> = HashMap::new();

    open_set.push(Node::new(start, 0, manhattan_distance(start, goal)));
    g_score.insert(start, 0);
    f_score.insert(start, manhattan_distance(start, goal));

    while let Some(current_node) = open_set.pop() {
        let current_pos = current_node.position;

        // Jika kita sampai di tujuan, rekonstruksi jalur
        if current_pos == goal {
            let mut path = Vec::new();
            let mut current = goal;

            while let Some(&previous) = came_from.get(&current) {
                path.push(current);
                current = previous;
            }
            path.push(start);
            path.reverse();
            return Some(path);
        }

        // Cek semua tetangga (arah gerakan)
        for &(dx, dy) in &directions {
            let neighbor = (current_pos.0.wrapping_add(dx as usize), current_pos.1.wrapping_add(dy as usize));

            // Pastikan tetangga berada dalam batas matriks dan bukan rintangan
            if neighbor.0 < grid.len() && neighbor.1 < grid[0].len() && grid[neighbor.0][neighbor.1] != 1 {
                let tentative_g_score = g_score[&current_pos] + 1;

                // Jika jalur lebih baik ditemukan
                if tentative_g_score < *g_score.get(&neighbor).unwrap_or(&usize::MAX) {
                    came_from.insert(neighbor, current_pos);
                    g_score.insert(neighbor, tentative_g_score);
                    f_score.insert(neighbor, tentative_g_score + manhattan_distance(neighbor, goal));
                    open_set.push(Node::new(neighbor, tentative_g_score, manhattan_distance(neighbor, goal)));
                }
            }
        }
    }

    None // Tidak ada jalur ditemukan
}

fn main() {
    // Matriks grid dengan 0 sebagai jalan bebas dan 1 sebagai rintangan
    let grid = vec![
        vec![0, 0, 0, 0, 0],
        vec![0, 1, 1, 0, 0],
        vec![0, 0, 0, 1, 0],
        vec![0, 1, 0, 0, 0],
        vec![0, 0, 0, 0, 0],
    ];

    let start = (0, 0);  // Titik awal
    let goal = (4, 4);   // Titik tujuan

    match find_path(grid, start, goal) {
        Some(path) => {
            println!("Jalur ditemukan:");
            for step in path {
                println!("Langkah ke: {:?}", step);
            }
        },
        None => {
            println!("Tidak ada jalur yang ditemukan");
        }
    }
}
