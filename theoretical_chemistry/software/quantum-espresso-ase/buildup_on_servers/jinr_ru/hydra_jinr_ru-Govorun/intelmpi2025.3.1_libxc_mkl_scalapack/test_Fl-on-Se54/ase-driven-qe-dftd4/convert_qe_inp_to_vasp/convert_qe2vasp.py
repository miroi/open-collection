import argparse
import sys
from ase.io import read, write

def main():
    # 1. Set up the argument parser
    parser = argparse.ArgumentParser(description='Convert Quantum ESPRESSO input to VASP format.')
    
    # 2. Add flags for input and output
    parser.add_argument('-i', '--input', required=True, help='Path to the QE input file')
    parser.add_argument('-o', '--output', required=True, help='Path for the VASP output file')
    
    # Optional flags to toggle VASP format options
    parser.add_argument('--vasp5', action='store_true', default=True, help='Use VASP 5 format (default: True)')
    parser.add_argument('--direct', action='store_true', default=True, help='Use direct/fractional coordinates (default: True)')

    args = parser.parse_args()

    try:
        # 3. Read and Write using ASE
        structure = read(args.input, format='espresso-in')
        write(args.output, structure, format='vasp', vasp5=args.vasp5, direct=args.direct)
        
        print(f"Done! Successfully converted '{args.input}' to '{args.output}'")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

