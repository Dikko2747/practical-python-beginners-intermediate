def read_scores(path):
    """Yield scores one at a time instead of loading the whole file."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield int(line.strip())


if __name__ == "__main__":
    # Create a small demo file.
    with open("big.txt", "w", encoding="utf-8") as f:
        f.write("70\n82\n65\n")

    total = sum(read_scores("big.txt"))
    print("Total:", total)
