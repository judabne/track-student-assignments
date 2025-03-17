import csv
import requests
import sys

def get_solved_problems_count(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('totalSolved', 'N/A')
    return 'N/A'

def extract_username_from_url(url):
    if url:
        return url.rstrip('/').split('/')[-1]
    return None

if len(sys.argv) != 3:
    print("Usage: python update_leetcode_stats.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

success_count = 0
failure_count = 0
no_username = 0

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    header.append('Solved Problems')
    writer.writerow(header)
    
    for row in reader:
        first_name = row[1]
        last_name = row[2]
        leetcode_url = row[3]
        username = extract_username_from_url(leetcode_url)
        print(f"Updating for {first_name}{last_name}:")
        if username:
            solved_problems = get_solved_problems_count(username)
            if solved_problems != 'N/A':
                success_count += 1
                print(f"\t{solved_problems} problems solved.")
            else:
                failure_count += 1
                print(f"\tFailed to update.")
        else:
            solved_problems = 'N/A'
            no_username += 1
            print(f"\tNo username for {first_name}{last_name}.")
        row.append(solved_problems)
        writer.writerow(row)

print(f"Updated CSV file has been saved as {output_file}")
print(f"Total succeeded: {success_count}")
print(f"Total failed: {failure_count}")
print(f"No username: {no_username}")
