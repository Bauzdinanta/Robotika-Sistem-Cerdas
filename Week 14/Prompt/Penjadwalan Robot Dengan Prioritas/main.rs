use std::collections::BinaryHeap;
use std::cmp::Reverse;

#[derive(Debug, Eq, PartialEq)]
struct Task {
    priority: usize, // Prioritas lebih rendah = lebih tinggi prioritasnya
    description: String,
}

impl Task {
    fn new(priority: usize, description: &str) -> Self {
        Task {
            priority,
            description: description.to_string(),
        }
    }
}

// Membuat BinaryHeap dengan Reverse untuk menjamin prioritas tertinggi berada di depan
impl Ord for Task {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        // Prioritas lebih rendah dianggap lebih tinggi
        other.priority.cmp(&self.priority)
    }
}

impl PartialOrd for Task {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

fn main() {
    let mut task_queue = BinaryHeap::new();

    // Menambahkan tugas dengan prioritas
    task_queue.push(Task::new(3, "Periksa sensor"));
    task_queue.push(Task::new(1, "Bersihkan area"));
    task_queue.push(Task::new(2, "Perbarui perangkat lunak"));
    task_queue.push(Task::new(5, "Kalibrasi robot"));

    // Robot menyelesaikan tugas berdasarkan urutan prioritas
    while let Some(task) = task_queue.pop() {
        println!("Menjalankan tugas: {} (Prioritas: {})", task.description, task.priority);
    }
}
