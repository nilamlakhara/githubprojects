# Name: Neelam
# File Handling Program

# Open input file and read all lines
with open("input.txt", "r") as f:
    lines = f.readlines()

# Count total number of lines
print("Total number of lines:", len(lines))

# Extract first two lines
first_two = lines[:2]

# Write first two lines into output file
with open("output.txt", "w") as f:
    f.writelines(first_two)

print("First two lines written successfully to output.txt")