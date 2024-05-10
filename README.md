# Scheduler

Scheduler is a command-line tool built with Python and Click library that allows users to manage their tasks efficiently.

## Features

- Add tasks with customizable name, description, and priority.
- Delete tasks by their index in the task list.
- List tasks with optional filtering by priority.

## Requirements

- Python 3.x
- Click 8.1.7
- Colorama 0.4.6

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/debghs/scheduler.git
    ```

2. Navigate to the project directory:

    ```
    cd scheduler
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Adding a Task:**

    ```
    python main.py add-task
    ```

    Follow the prompts to enter the task name, description, and choose a priority.

   Or use,
   
    ```
    python main.py add-task --name "task name" --desc "task description" "priority"
    ```
    Replace the fields with your data.

3. **Deleting a Task:**

    ```
    python main.py del-task <index>
    ```

    Replace `<index>` with the index of the task you want to delete.

4. **Listing Tasks:**

    ```
    python main.py task-list
    ```

    Use the optional `-p` flag followed by the priority (o, l, m, h, c) to filter tasks by priority.

## Priorities

Tasks can be assigned one of the following priorities:

- **o (optional):** Indicates an optional task.
- **l (low):** Indicates a low-priority task.
- **m (moderate):** Indicates a moderate-priority task.
- **h (high):** Indicates a high-priority task.
- **c (critical):** Indicates a critical-priority task.

## Contributing

Contributions are welcome! If you have any ideas for new features, find any bugs, or want to improve the code, feel free to open an issue or submit a pull request.
