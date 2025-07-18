from suggest import suggest_commit_message

if __name__ == "__main__":
    print("Enter your PR description (end with an empty line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    
    pr_description = "\n".join(lines)
    print("\nGenerating commit message...\n")
    commit_msg = suggest_commit_message(pr_description)
    print("💡 Suggested Commit Message:\n")
    print(commit_msg)
