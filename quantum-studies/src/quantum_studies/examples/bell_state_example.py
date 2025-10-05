"""
Simple example script showing how to use the IBMQuantumRunner class.
This can be imported and used in other modules.
"""

from qiskit import QuantumCircuit
from quantum_studies.ibm_qpus import IBMQuantumRunner

def create_bell_state_circuit():
    """Create a Bell state quantum circuit."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)          # Apply Hadamard gate to qubit 0
    qc.cx(0, 1)      # Apply CNOT gate from qubit 0 to qubit 1
    qc.measure_all() # Measure all qubits
    return qc

def run_bell_state_on_ibm(api_key, backend_name='ibm_brisbane', shots=1024):
    """
    Run a Bell state circuit on IBM quantum hardware.
    
    Args:
        api_key: IBM Quantum API key
        backend_name: Name of the IBM backend to use
        shots: Number of measurement shots
        
    Returns:
        Tuple of (counts, fidelity)
    """
    # Create the runner
    runner = IBMQuantumRunner(api_key=api_key)
    
    # Create circuit
    circuit = create_bell_state_circuit()
    
    # Run on quantum hardware
    counts, result = runner.run_circuit(
        circuit=circuit,
        shots=shots,
        backend_name=backend_name,
        plot_results=True,
        title=f"Bell State on {backend_name}"
    )
    
    # Calculate fidelity
    fidelity = runner.calculate_bell_state_fidelity(counts)
    
    return counts, fidelity

def example_multiple_backends(api_key):
    """
    Example showing how to run the same circuit on multiple backends.
    
    Args:
        api_key: IBM Quantum API key
    """
    runner = IBMQuantumRunner(api_key=api_key)
    
    # List available backends
    backends = runner.list_backends(min_qubits=2)
    
    # Create circuit
    circuit = create_bell_state_circuit()
    
    results = {}
    
    # Run on first few available backends (limit to avoid excessive queue time)
    for backend in backends[:3]:  # Limit to first 3 backends
        try:
            print(f"\n{'='*50}")
            print(f"Running on {backend.name}")
            print(f"{'='*50}")
            
            counts, result = runner.run_circuit(
                circuit=circuit,
                shots=1024,
                backend_name=backend.name,
                plot_results=False  # Don't plot to avoid too many plots
            )
            
            fidelity = runner.calculate_bell_state_fidelity(counts)
            results[backend.name] = {
                'counts': counts,
                'fidelity': fidelity,
                'qubits': backend.num_qubits
            }
            
        except Exception as e:
            print(f"Failed to run on {backend.name}: {e}")
    
    # Print summary
    print(f"\n{'='*50}")
    print("SUMMARY OF RESULTS")
    print(f"{'='*50}")
    for backend_name, data in results.items():
        print(f"{backend_name}: {data['fidelity']:.1f}% fidelity ({data['qubits']} qubits)")
    
    return results

if __name__ == "__main__":
    # Example usage (you need to provide your API key)
    API_KEY = "<api_key>"  # Replace with your actual API key
    
    print("Example 1: Single backend execution")
    try:
        counts, fidelity = run_bell_state_on_ibm(API_KEY)
        print(f"Final results: {counts}")
        print(f"Bell state fidelity: {fidelity:.1f}%")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure to replace 'your_api_key_here' with your actual IBM Quantum API key")
    
    # Uncomment to run multiple backends example
    # print("\nExample 2: Multiple backends comparison")
    # results = example_multiple_backends(API_KEY)