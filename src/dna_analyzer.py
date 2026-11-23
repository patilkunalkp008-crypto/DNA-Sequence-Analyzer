# ==========================================
# DNA SEQUENCE ANALYZER
# Project: Computational Biology
# Language: Python
# ==========================================


def clean_sequence(sequence):
    """Convert sequence to uppercase and remove spaces."""
    return sequence.replace(" ", "").upper()


def is_valid_dna(sequence):
    """Check whether the DNA sequence is valid."""

    valid_bases = ["A", "T", "G", "C"]

    if len(sequence) == 0:
        return False

    for base in sequence:
        if base not in valid_bases:
            return False

    return True


def calculate_length(sequence):
    """Calculate the total DNA sequence length."""
    return len(sequence)


def count_nucleotides(sequence):
    """Count each nucleotide."""

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    return counts


def calculate_gc_content(sequence):
    """Calculate GC content as a percentage."""

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage


def calculate_at_content(sequence):
    """Calculate AT content as a percentage."""

    at_count = sequence.count("A") + sequence.count("T")

    at_percentage = (at_count / len(sequence)) * 100

    return at_percentage


def analyze_dna(sequence):
    """Perform complete basic DNA analysis."""

    sequence = clean_sequence(sequence)

    print("\n========== DNA ANALYSIS ==========")

    if not is_valid_dna(sequence):
        print("Error: Invalid DNA sequence.")
        print("Only A, T, G and C are allowed.")
        print("==================================")
        return

    length = calculate_length(sequence)
    counts = count_nucleotides(sequence)
    gc_content = calculate_gc_content(sequence)
    at_content = calculate_at_content(sequence)

    print("DNA Sequence:", sequence)

    print("\nSequence Length:", length)

    print("\nNucleotide Frequencies:")

    for base, count in counts.items():
        percentage = (count / length) * 100
        print(f"{base}: {count} ({percentage:.2f}%)")

    print(f"\nGC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")

    print("\nAnalysis completed successfully!")
    print("==================================")


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("Welcome to DNA Sequence Analyzer")

    dna_sequence = input("\nEnter a DNA sequence: ")

    analyze_dna(dna_sequence)
