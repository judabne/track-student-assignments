# Track Student Assignments

A script that takes a CSV of student names and updates the number of Leetcode problems they solved.

## Description

This script reads a CSV file containing student names and their Leetcode profile URLs, fetches the number of problems they have solved from Leetcode, and writes the updated data to a new CSV file.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

    pip install requests

### Running the Script

To run the script, use the following command:

    python update_leetcode_stats.py <input_file> <output_file>

- `<input_file>`: Path to the input CSV file containing student names and Leetcode profile URLs.
- `<output_file>`: Path to the output CSV file where the updated data will be saved.

### Input CSV Format

The script is designed for CSVs with the following columns:

- `Nb in List`
- `First Name`
- `Last Name`
- `Link` (Leetcode profile URL)

The script can handle additional columns after the `Link` column.

Example:

    Nb in List,First Name,Last Name,Link,Solved Last Week
    course-Elec-001,John,Doe,https://leetcode.com/u/johndoe/,18
    course-Elec-002,Jane,Smith,https://leetcode.com/u/janesmith/,2
    ...

### Output CSV Format

The output CSV file will have an additional column `Solved Problems` indicating the number of problems solved by each student.

Example:

    Nb in List,First Name,Last Name,Link,Solved Last Week,Solved Problems
    course-Elec-001,John,Doe,https://leetcode.com/u/johndoe/,18,50
    course-Elec-002,Jane,Smith,https://leetcode.com/u/janesmith/,2,10
    ...

## Example

    python update_leetcode_stats.py input.csv output.csv
