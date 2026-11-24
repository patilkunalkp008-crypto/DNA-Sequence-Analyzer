# ==================================================
# DNA SEQUENCE ANALYZER
# Project: Computational Biology
# Version: 2.0
# ==================================================

from pathlib import Path
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. CLEAN DNA SEQUENCE
# --------------------------------------------------

def clean_sequence(sequence):
    """Convert DNA sequence to uppercase and remove spaces."""
    return sequence.replace(" ", "").upper()


# --------------------------------------------------
# 2. VALIDATE DNA SEQUENCE
# --------------------------------------------------

def is_valid_dna(sequence):
    """Check whether the DNA sequence contains valid bases."""
    valid_bases = ["A", "T", "G", "C"]

    if len(sequence) == 0:
        return False

    for base in sequence:
        if base not in valid_bases:
            return False

    return True


# --------------------------------------------------
# 3. CALCULATE SEQUENCE LENGTH
# --------------------------------------------------

def calculate_length(sequence):
    return len(sequence)


# --------------------------------------------------
# 4. COUNT NUCLEOTIDES
# --------------------------------------------------

def count_nucleotides(sequence):
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    return counts


# --------------------------------------------------
# 5. CALCULATE GC CONTENT
# --------------------------------------------------

def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


# --------------------------------------------------
# 6. CALCULATE AT CONTENT
# --------------------------------------------------

def calculate_at_content(sequence):
    at_count = sequence.count("A") + sequence.count("T")
    return (at_count / len(sequence)) * 100


# --------------------------------------------------
# 7. PLOT NUCLEOTIDE FREQUENCY
# --------------------------------------------------

def plot_nucleotide_frequency(counts):

    bases = list(counts.keys())
    frequencies = list(counts.values())

    plt.figure(figsize=(8, 5))

    plt.bar(bases, frequencies)

    plt.title("DNA Nucleotide Frequency")
    plt.xlabel("Nucleotides")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(RESULTS_DIR / "nucleotide_frequency.png")

    plt.show()
    plt.close()


# --------------------------------------------------
# 8. PLOT GC AND AT CONTENT
# --------------------------------------------------

def plot_gc_at_content(gc_content, at_content):

    labels = ["GC Content", "AT Content"]
    values = [gc_content, at_content]

    plt.figure(figsize=(7, 5))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.2f%%",
        startangle=90
    )

    plt.title("GC vs AT Content")

    plt.tight_layout()

    plt.savefig(RESULTS_DIR / "gc_at_content.png")

    plt.show()
    plt.close()


# --------------------------------------------------
# 9. ANALYZE DNA
# --------------------------------------------------

def analyze_dna(sequence):

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

    print("\nDNA Sequence:", sequence)

    print("\nSequence Length:", length)

    print("\nNucleotide Frequencies:")

    for base, count in counts.items():

        percentage = (count / length) * 100

        print(f"{base}: {count} ({percentage:.2f}%)")

    print(f"\nGC Content: {gc_content:.2f}%")

    print(f"AT Content: {at_content:.2f}%")

    print("\nGenerating graphs...")

    plot_nucleotide_frequency(counts)

    plot_gc_at_content(gc_content, at_content)

    print("\nAnalysis completed successfully!")

    print("==================================")


# --------------------------------------------------
# 10. MAIN PROGRAM
# --------------------------------------------------

PROJECT_DIR = Path.cwd()

RESULTS_DIR = PROJECT_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

print("Welcome to DNA Sequence Analyzer")

dna_sequence = input("\nEnter a DNA sequence: ")

analyze_dna(dna_sequence)
