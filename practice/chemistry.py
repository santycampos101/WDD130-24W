from typing import List, Tuple

def make_periodic_table() -> List[Tuple[str, str, float]]:
    """
    Creates a list of tuples representing the periodic table of elements, where each tuple
    contains the symbol, name, and atomic mass of an element.
    Returns:
        A list of tuples representing the periodic table of elements.
    """
    # implementation of make_periodic_table function
    periodic_table_list = [
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ["Ar", "Argon", 39.948],
        ["As", "Arsenic", 74.9216],
        ["At", "Astatine", 210],
        ["Au", "Gold", 196.966569],
        ["B", "Boron", 10.81],
        ["Ba", "Barium", 137.327],
        ["Be", "Beryllium", 9.0121831],
        ["Bi", "Bismuth", 208.9804],
        ["Br", "Bromine", 79.904],
        ["C", "Carbon", 12.011],
        ["Ca", "Calcium", 40.078],
        ["Cd", "Cadmium", 112.414],
        ["Ce", "Cerium", 140.116],
        ["Cl", "Chlorine", 35.453],
        ["Co", "Cobalt", 58.933194],
        ["Cr", "Chromium", 51.9961],
        ["Cs", "Cesium", 132.90545196],
        ["Cu", "Copper", 63.546],
        ["Dy", "Dysprosium", 162.5],
        ["Er", "Erbium", 167.259],
        ["Eu", "Europium", 151.964],
        ["F", "Fluorine", 18.998403163],
        ["Fe", "Iron", 55.845],
        ["Fr", "Francium", 223],
        ["Ga", "Gallium", 69.723],
        ["Gd", "Gadolinium", 157.25],
        ["Ge", "Germanium", 72.63],
        ["H", "Hydrogen", 1.008],
        ["He", "Helium", 4.002602],
        ["Hf", "Hafnium", 178.49],
        ["Hg", "Mercury", 200.592],
        ["Ho", "Holmium", 164.930328],
        ["I", "Iodine", 126.90447],
        ["In", "Indium", 114.818],
        ["Ir", "Iridium", 192.217],
        ["K", "Potassium", 39.0983],
        ["Kr", "Krypton", 83.798],
        ["La", "Lanthanum", 138.90547],
        ["Li", "Lithium", 6.94],
        ["Lu", "Lutetium", 174.9668],
        ["Mg", "Magnesium", 24.305],
        ["Mn", "Manganese", 54.938044],
        ["Mo", "Molybdenum", 95.95],
        ["N", "Nitrogen", 14.007],
        ["Na", "Sodium", 22.98976928],
        ["Nb", "Niobium", 92.90637],
        ["Nd", "Neodymium", 144.242],
        ["Ne", "Neon", 20.1797],
        ["Ni", "Nickel", 58.6934],
        ["Np", "Neptunium", 237],
        ["O", "Oxygen", 15.999],
        ["Os", "Osmium", 190.23],
        ["P", "Phosphorus", 30.973761998],
        ["Pa", "Protactinium", 231.03588],
        ["Pb", "Lead", 207.2],
        ["Pd", "Palladium", 106.42],
        ["Pm", "Promethium", 145],
        ["Po", "Polonium", 209],
        ["Pr", "Praseodymium", 140.90766],
        ["Pt", "Platinum", 195.084],
        ["Pu", "Plutonium", 244],
        ["Ra", "Radium", 226],
        ["Rb", "Rubidium", 85.4678],
        ["Re", "Rhenium", 186.207],
        ["Rh", "Rhodium", 102.9055],
        ["Rn", "Radon", 222],
        ["Ru", "Ruthenium", 101.07],
        ["S", "Sulfur", 32.06],
        ["Sb", "Antimony", 121.76],
        ["Sc", "Scandium", 44.955908],
        ["Se", "Selenium", 78.96],
        ["Si", "Silicon", 28.085],
        ["Sm", "Samarium", 150.36],
        ["Sn", "Tin", 118.71],
        ["Sr", "Strontium", 87.62],
        ["Ta", "Tantalum", 180.94788],
        ["Tb", "Terbium", 158.92535],
        ["Tc", "Technetium", 98],
        ["Te", "Tellurium", 127.6],
        ["Th", "Thorium", 232.0377],
        ["Ti", "Titanium", 47.867],
        ["Tl", "Thallium", 204.38],
        ["Tm", "Thulium", 168.93422],
        ["U", "Uranium", 238.02891],
        ["V", "Vanadium", 50.9415],
        ["W", "Tungsten", 183.84],
        ["Xe", "Xenon", 131.293],
        ["Y", "Yttrium", 88.90584],
        ["Yb", "Ytterbium", 173.054],
        ["Zn", "Zinc", 65.38],
        ["Zr", "Zirconium", 91.224]
    ]

def compute_molar_mass(formula: str, periodic_table: List[Tuple[str, str, float]]) -> float:
    """
    Computes the molar mass of a chemical formula using the periodic table of elements.
    Args:
        formula: A string representing the chemical formula.
        periodic_table: A list of tuples representing the periodic table of elements.
    Returns:
        The molar mass of the chemical formula in grams per mole.
    """
    # Create a dictionary to store the count of each element in the formula
    elements = {}
    # Iterate over each character in the formula
    for i, char in enumerate(formula):
        if char.isupper():
            # If the character is an uppercase letter, it represents the start of a new element
            if i != 0:
                # If the previous element has not been added to the dictionary, add it with a count of 1
                if prev_element not in elements:
                    elements[prev_element] = 1
                # If the previous element has already been added to the dictionary, increment its count by 1
                elif prev_element in elements:
                    # If the previous element appears again later in the formula (e.g. H2SO4), skip it
                    if prev_element in elements and prev_element in formula[i:]:
                        continue
                    else:
                        elements[prev_element] = 1
            prev_element = char
        elif char.islower():
            # If the character is a lowercase letter, it represents the continuation of the previous element
            prev_element += char
        elif char.isdigit():
            # If the character is a digit, it represents the count of the previous element
            if prev_element in elements:
                elements[prev_element] += int(char) - 1
            else:
                elements[prev_element] = int(char) - 1
    # Add the last element to the dictionary if it hasn't been added yet
    if prev_element not in elements:
        elements[prev_element] = 1
    
    # Compute the molar mass of the formula using the atomic masses from the periodic table
    molar_mass = 0
    for element, count in elements.items():
        atomic_mass = next(item[2] for item in periodic_table if item[0] == element)
        molar_mass += count * atomic_mass
    
    return molar_mass

def main():
    """
    Prompts the user to enter a chemical formula and the mass of a sample in grams, and
    computes the molar mass and number of moles of the substance.
    """
    # Create the periodic table of elements
    periodic_table = make_periodic_table()
    # Prompt the user to enter the chemical formula and sample mass
    formula = input("Enter the chemical formula: ")
    sample_mass = float(input("Enter the mass of the sample in grams: "))
    
    # Compute the molar mass of the formula and the number of moles in the sample
    molar_mass = compute_molar_mass(formula, periodic_table)
    number_of_moles = sample_mass / molar_mass
    
    # Print the results
    print(f"Molar mass of {formula}: {molar_mass:.2f} g/mol")
    print(f"Number of moles in {sample_mass:.2f} g of {formula}: {number_of_moles:.4f} moles")

if __name__ == "__main__":
    main()