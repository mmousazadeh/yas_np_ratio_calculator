import streamlit as st

# Function to calculate N/P ratio
def calculate_np_ratio(peptide_mass, dna_mass):
    """Calculates the N/P ratio based on given peptide and DNA mass (in µg)."""
    MW_PEPTIDE = 9815  # Molecular weight of peptide (g/mol)
    NUM_LYS_ARG = 21  # Number of lysine and arginine residues
    DNA_PHOSPHATE_WEIGHT = 330  # g/mol per phosphate group in DNA

    if dna_mass == 0:
        return None  # Avoid division by zero

    nitrogen_moles = peptide_mass / (MW_PEPTIDE / NUM_LYS_ARG)
    phosphate_moles = dna_mass / DNA_PHOSPHATE_WEIGHT

    return nitrogen_moles / phosphate_moles

# Function to calculate required peptide mass
def calculate_peptide_mass(desired_np_ratio, dna_mass):
    MW_PEPTIDE = 9815
    NUM_LYS_ARG = 21
    DNA_PHOSPHATE_WEIGHT = 330

    phosphate_moles = dna_mass / DNA_PHOSPHATE_WEIGHT
    required_nitrogen_moles = desired_np_ratio * phosphate_moles
    return required_nitrogen_moles * (MW_PEPTIDE / NUM_LYS_ARG)

# Function to calculate required DNA mass
def calculate_dna_mass(np_ratio, peptide_mass):
    MW_PEPTIDE = 9815
    NUM_LYS_ARG = 21
    DNA_PHOSPHATE_WEIGHT = 330

    nitrogen_moles = peptide_mass / (MW_PEPTIDE / NUM_LYS_ARG)
    required_phosphate_moles = nitrogen_moles / np_ratio
    return required_phosphate_moles * DNA_PHOSPHATE_WEIGHT

# Streamlit UI
st.title("🔬 N/P Ratio Calculator")
st.write("This tool helps calculate N/P ratio, required peptide mass, or required DNA mass.")

# User selection
option = st.radio("Choose a calculation:", ["Calculate N/P ratio", "Calculate required peptide mass", "Calculate required DNA mass"])

if option == "Calculate N/P ratio":
    peptide_mass = st.number_input("Enter peptide mass (µg)", min_value=0.0)
    dna_mass = st.number_input("Enter DNA mass (µg)", min_value=0.0)

    if st.button("Calculate"):
        np_ratio = calculate_np_ratio(peptide_mass, dna_mass)
        if np_ratio is not None:
            st.success(f"N/P Ratio: {np_ratio:.2f}")
        else:
            st.error("DNA mass must be greater than zero.")

elif option == "Calculate required peptide mass":
    desired_np_ratio = st.number_input("Enter desired N/P ratio", min_value=0.0)
    dna_mass = st.number_input("Enter DNA mass (µg)", min_value=0.0)

    if st.button("Calculate"):
        peptide_mass = calculate_peptide_mass(desired_np_ratio, dna_mass)
        st.success(f"Required peptide mass: {peptide_mass:.2f} µg")

elif option == "Calculate required DNA mass":
    np_ratio = st.number_input("Enter desired N/P ratio", min_value=0.0)
    peptide_mass = st.number_input("Enter peptide mass (µg)", min_value=0.0)

    if st.button("Calculate"):
        dna_mass = calculate_dna_mass(np_ratio, peptide_mass)
        st.success(f"Required DNA mass: {dna_mass:.2f} µg")
