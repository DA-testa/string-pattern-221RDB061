# Nikita Ščipanovs 221RDB061
def read_input():
    input_format = input().upper().rstrip()
    if 'F' in input_format:
        input_file = '06'
        input_file = "tests/" + input_file
        try:
            with open(input_file, "r") as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        except FileNotFoundError:
            return "File not found error"
    elif input_format == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        return "Invalid input format"
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    p_hash = sum(ord(pattern[i]) * pow(101, i) for i in range(p))
    t_hash = sum(ord(text[i]) * pow(101, i) for i in range(p))
    output = []

    for i in range(t - p + 1):
        if p_hash == t_hash:
            if text[i:i+p] == pattern:
                output.append(i)

        if i < t - p:
            t_hash = t_hash - ord(text[i]) * pow(101, 0)
            t_hash = t_hash // 101
            t_hash += ord(text[i+p]) * pow(101, p-1)

    return output

# This part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))