def calculate_np_ratio(peptide_mass, dna_mass):
    """Calculates the N/P ratio based on given peptide and DNA mass (in µg)."""
    MW_PEPTIDE = 9815  # Molecular weight of peptide (g/mol)
    NUM_LYS_ARG = 21  # Number of lysine and arginine residues
    DNA_PHOSPHATE_WEIGHT = 330  # g/mol per phosphate group in DNA

    nitrogen_moles = peptide_mass / (MW_PEPTIDE / NUM_LYS_ARG)
    phosphate_moles = dna_mass / DNA_PHOSPHATE_WEIGHT

    return nitrogen_moles / phosphate_moles if phosphate_moles > 0 else None

def calculate_peptide_mass(desired_np_ratio, dna_mass):
    """Calculates the required peptide mass (in µg) to achieve the desired N/P ratio."""
    MW_PEPTIDE = 9815  # Molecular weight of peptide (g/mol)
    NUM_LYS_ARG = 21  # Number of lysine and arginine residues
    DNA_PHOSPHATE_WEIGHT = 330  # g/mol per phosphate group in DNA

    phosphate_moles = dna_mass / DNA_PHOSPHATE_WEIGHT
    required_nitrogen_moles = desired_np_ratio * phosphate_moles
    peptide_mass = required_nitrogen_moles * (MW_PEPTIDE / NUM_LYS_ARG)

    return peptide_mass

def calculate_dna_mass(np_ratio, peptide_mass):
    """Calculates the required DNA mass (in µg) to achieve the desired N/P ratio with a given peptide mass."""
    MW_PEPTIDE = 9815  # Molecular weight of peptide (g/mol)
    NUM_LYS_ARG = 21  # Number of lysine and arginine residues
    DNA_PHOSPHATE_WEIGHT = 330  # g/mol per phosphate group in DNA

    nitrogen_moles = peptide_mass / (MW_PEPTIDE / NUM_LYS_ARG)
    required_phosphate_moles = nitrogen_moles / np_ratio
    dna_mass = required_phosphate_moles * DNA_PHOSPHATE_WEIGHT

    return dna_mass

# User selection
print("Welcome to N/P calculator, please choose an option:")
print("1 - Calculate N/P ratio")
print("2 - Calculate peptide mass for a given N/P ratio")
print("3 - Calculate DNA mass for a given N/P ratio")

choice = input("Enter 1, 2, or 3: ").strip()

if choice == "1":
    peptide_mass = float(input("Enter peptide mass (µg): "))
    dna_mass = float(input("Enter DNA mass (µg): "))

    np_ratio = calculate_np_ratio(peptide_mass, dna_mass)
    if np_ratio is not None:
        print(f"N/P Ratio: {np_ratio:.2f}")
    else:
        print("Invalid input: DNA mass must be greater than zero.")

elif choice == "2":
    desired_np_ratio = float(input("Enter N/P ratio: "))
    dna_mass = float(input("Enter DNA mass (µg): "))

    peptide_mass = calculate_peptide_mass(desired_np_ratio, dna_mass)
    print(f"Calculated peptide mass: {peptide_mass:.2f} µg")

elif choice == "3":
    np_ratio = float(input("Enter N/P ratio: "))
    peptide_mass = float(input("Enter peptide mass (µg): "))

    dna_mass = calculate_dna_mass(np_ratio, peptide_mass)
    print(f"Calculated DNA mass: {dna_mass:.2f} µg")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
