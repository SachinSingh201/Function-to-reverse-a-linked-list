# Function-to-reverse-a-linked-list
Reverse a linked list with the help of this code.



---

# Linked List Implementation in Python

This project contains a Python implementation of a **singly linked list** data structure. It includes methods to insert a node at the head of the list, reverse the linked list, and display the total number of nodes.

## Features

- **Node Class**: Represents an individual node in the linked list, with attributes for storing data and a reference to the next node.
- **Linked List Class**:
  - `insert_head(value)`: Adds a new node with the given value to the head of the linked list.
  - `reverse_linked_list()`: Reverses the linked list.
  - `__len__()`: Prints the total number of nodes in the linked list.

## How to Use

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-folder>
   ```

3. Run the Python script in your preferred Python environment:
   ```bash
   python <script_name>.py
   ```

4. Implement the linked list operations in your main function by calling the methods from the `Linked_list` class.

## Example Usage

Here's an example of how you can use the code:

```python
# Create a linked list
ll = Linked_list()

# Insert elements at the head
ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)

# Reverse the linked list
ll.reverse_linked_list()

# Get the total number of nodes
ll.__len__()
```

## Output

- Adds nodes to the linked list.
- Reverses the linked list.
- Displays the total number of nodes.

## Improvements

Future enhancements may include:
- Method to delete nodes from the list.
- Method to search for a specific value.
- Support for doubly linked lists.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

