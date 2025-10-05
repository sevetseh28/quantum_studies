"""IBM Quantum Runner - A reusable module for running quantum circuits on IBM QPUs."""

import os
from typing import Dict, List, Optional, Union, Tuple, Any
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class IBMQuantumRunner:
    """A class to handle IBM Quantum backend operations."""
    
    def __init__(self, api_key: Optional[str] = None, channel: str = "ibm_quantum_platform"):
        """
        Initialize the IBM Quantum Runner.
        
        Args:
            api_key: IBM Quantum API key. If None, tries to load from environment or saved account.
            channel: IBM Quantum channel ('ibm_quantum_platform' or 'ibm_cloud')
        """
        self.channel = channel
        self.service = None
        self.backend = None
        
        if api_key:
            self._save_account(api_key, channel)
        
        self._initialize_service()
    
    def _save_account(self, api_key: str, channel: str) -> None:
        """Save IBM Quantum account credentials."""
        try:
            QiskitRuntimeService.save_account(
                channel=channel, 
                token=api_key, 
                overwrite=True
            )
            print(f"Account saved successfully with {channel} channel!")
        except Exception as e:
            raise RuntimeError(f"Failed to save account: {e}")
    
    def _initialize_service(self) -> None:
        """Initialize the Qiskit Runtime Service."""
        try:
            self.service = QiskitRuntimeService(channel=self.channel)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize service: {e}")
    
    def list_backends(self, min_qubits: int = 1, operational_only: bool = True) -> List:
        """
        List available quantum backends.
        
        Args:
            min_qubits: Minimum number of qubits required
            operational_only: Only show operational backends
            
        Returns:
            List of available backends
        """
        if not self.service:
            raise RuntimeError("Service not initialized")
        
        backends = self.service.backends(
            simulator=False, 
            operational=operational_only,
            min_num_qubits=min_qubits
        )
        
        print(f"\nAvailable quantum backends (min {min_qubits} qubits):")
        for backend in backends:
            status = backend.status()
            queue_length = getattr(status, 'pending_jobs', 'N/A')
            print(f"- {backend.name}: {backend.num_qubits} qubits, Queue: {queue_length}")
        
        return backends
    
    def select_backend(self, backend_name: str) -> None:
        """
        Select a specific backend.
        
        Args:
            backend_name: Name of the backend to select
        """
        if not self.service:
            raise RuntimeError("Service not initialized")
        
        try:
            self.backend = self.service.backend(backend_name)
            print(f"\nSelected backend: {self.backend.name}")
            print(f"Number of qubits: {self.backend.num_qubits}")
            
            status = self.backend.status()
            print(f"Backend status: {status.status_msg}")
            if hasattr(status, 'pending_jobs'):
                print(f"Queue length: {status.pending_jobs}")
                
        except Exception as e:
            raise RuntimeError(f"Failed to select backend '{backend_name}': {e}")
    
    def run_circuit(
        self, 
        circuit: QuantumCircuit, 
        shots: int = 1024,
        optimization_level: int = 1,
        backend_name: Optional[str] = None,
        plot_results: bool = True,
        title: Optional[str] = None
    ) -> Tuple[Dict[str, int], Any]:
        """
        Run a quantum circuit on the selected backend.
        
        Args:
            circuit: The quantum circuit to run
            shots: Number of shots to execute
            optimization_level: Transpilation optimization level (0-3)
            backend_name: Backend to use (if None, uses currently selected backend)
            plot_results: Whether to plot the histogram
            title: Title for the histogram plot
            
        Returns:
            Result 
        """
        # Select backend if specified
        if backend_name:
            self.select_backend(backend_name)
        
        if not self.backend:
            raise RuntimeError("No backend selected. Use select_backend() first.")
        
        try:
            # Transpile the circuit for the selected backend
            transpiled_circuit = transpile(circuit, self.backend, optimization_level=optimization_level)
            print(f"\nTranspiled circuit depth: {transpiled_circuit.depth()}")
            
            # Create a Sampler primitive
            sampler = SamplerV2(self.backend)
            
            # Run the job
            print(f"\nSubmitting job to {self.backend.name}...")
            job = sampler.run([transpiled_circuit], shots=shots)
            
            print(f"Job ID: {job.job_id()}")
            print("Job status:", job.status())
            
            # Get the result
            result = job.result()
            
            # Get the classic registers names dynamically
            return result
            
        except Exception as e:
            self._print_troubleshooting_info(e)
            raise
    
    def calculate_bell_state_fidelity(self, counts: Dict[str, int]) -> float:
        """
        Calculate Bell state fidelity from measurement counts.
        
        Args:
            counts: Measurement counts dictionary
            
        Returns:
            Fidelity percentage
        """
        total_shots = sum(counts.values())
        bell_state_counts = counts.get('00', 0) + counts.get('11', 0)
        fidelity = bell_state_counts / total_shots * 100
        
        print(f"\nBell state fidelity: {fidelity:.1f}%")
        print(f"Expected outcomes (00, 11): {bell_state_counts}/{total_shots}")
        
        return fidelity
    
    def get_backend_info(self) -> Dict[str, Any]:
        """
        Get detailed information about the current backend.
        
        Returns:
            Dictionary with backend information
        """
        if not self.backend:
            raise RuntimeError("No backend selected")
        
        status = self.backend.status()
        config = self.backend.configuration()
        
        info = {
            'name': self.backend.name,
            'num_qubits': self.backend.num_qubits,
            'status': status.status_msg,
            'pending_jobs': getattr(status, 'pending_jobs', None),
            'basis_gates': config.basis_gates,
            'coupling_map': config.coupling_map,
            'max_shots': config.max_shots,
            'max_experiments': config.max_experiments
        }
        
        return info
    
    def _print_troubleshooting_info(self, error: Exception) -> None:
        """Print troubleshooting information when errors occur."""
        print(f"Error: {error}")
        print("\nTroubleshooting steps:")
        print("1. Verify your IBM Quantum token is valid:")
        print("   - Go to https://quantum.cloud.ibm.com/")
        print("   - Log in and copy your API token from the account settings")
        print("2. Make sure you're using the correct channel:")
        print("   - Use 'ibm_cloud' for IBM Cloud accounts")
        print("   - Use 'ibm_quantum_platform' for IBM Quantum Platform accounts")
        print("3. Check if your token has expired or been regenerated")
        print("4. Ensure qiskit-ibm-runtime is up to date: pip install -U qiskit-ibm-runtime")
        print("\nIf you have a legacy IBM Quantum Experience account, try:")
        print("   QiskitRuntimeService.save_account(channel='ibm_quantum_platform', token=your_token)")


# Convenience functions for quick usage
def run_on_ibm_qpu(
    circuit: QuantumCircuit,
    api_key: str,
    backend_name: str = 'ibm_brisbane',
    shots: int = 1024,
    channel: str = "ibm_quantum_platform"
) -> Tuple[Dict[str, int], Any]:
    """
    Quick function to run a circuit on IBM QPU.
    
    Args:
        circuit: Quantum circuit to run
        api_key: IBM Quantum API key
        backend_name: Name of the backend to use
        shots: Number of shots
        channel: IBM Quantum channel
        
    Returns:
        Tuple of (measurement_counts, job_result)
    """
    runner = IBMQuantumRunner(api_key=api_key, channel=channel)
    return runner.run_circuit(circuit, shots=shots, backend_name=backend_name)


def list_available_backends(api_key: str, min_qubits: int = 1, channel: str = "ibm_quantum_platform") -> List:
    """
    Quick function to list available backends.
    
    Args:
        api_key: IBM Quantum API key
        min_qubits: Minimum number of qubits
        channel: IBM Quantum channel
        
    Returns:
        List of available backends
    """
    runner = IBMQuantumRunner(api_key=api_key, channel=channel)
    return runner.list_backends(min_qubits=min_qubits)