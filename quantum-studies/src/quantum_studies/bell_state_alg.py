import logging
import time
from typing import Literal, Dict
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
    datefmt="%Y-%m-%d %H:%M:%S",
)

class QuantumExperiment:
    """Manages quantum circuit execution on Amazon Braket"""

    def __init__(self, backend: Literal["simulator", "qpu"] = "simulator", shots: int = 1) -> None:
        """
        Initializes the quantum experiment.

        :param backend: "simulator" for local execution or "qpu" for real quantum device.
        :param shots: Number of shots for the experiment.
        """
        self.shots = shots
        self.backend = backend
        self.device = self._get_device()

    def _get_device(self) -> LocalSimulator | AwsDevice:
        """Selects the quantum backend based on settings."""
        if self.backend == "simulator":
            logging.info("Using Local Simulator")
            return LocalSimulator()
        elif self.backend == "aria1":
            logging.info("Using Real Trapped Ion QPU (AWS Braket provided by IonQ)")
            return AwsDevice("arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1")  # 
        elif self.backend == "aquila":
            logging.info("Using Real Neutral Atom QPU QPU (AWS Braket provided by QuEra)")
            return AwsDevice("arn:aws:braket:us-east-1::device/qpu/quera/Aquila")  
        else:
            raise ValueError(f"Invalid backend: {self.backend}. Choose 'simulator' or 'qpu'.")

    def build_bell_circuit(self) -> Circuit:
        """Creates a Bell state quantum circuit."""
        circuit = Circuit()
        circuit.h(0)       # Hadamard gate on qubit 0 (SUPERPOSITION)
        circuit.cnot(0, 1)  # CNOT gate (ENTANGLEMENT)
        return circuit

    def run_experiment(self) -> Dict[str, int]:
        """Executes the quantum circuit on the selected backend."""
        circuit = self.build_bell_circuit()
        logging.info(f"\nQuantum Circuit:\n{circuit}")

        # Execute the circuit
        logging.info(f"Running experiment on {self.backend.upper()} with {self.shots} shot(s)...")
        task = self.device.run(circuit, shots=self.shots)

        # If running on a real QPU, monitor status
        if self.backend == "qpu":
            logging.info("QPU job submitted. Waiting for results...")
            while (state := task.state()) not in {"COMPLETED", "FAILED"}:
                logging.info(f"Current state: {state}... waiting...")
                time.sleep(10)  # Poll every 10 seconds

        # Fetch results
        result = task.result()
        counts = result.measurement_counts
        logging.info("Experiment completed!")
        logging.info(f"Measurement results: {counts}")
        return counts


if __name__ == "__main__":
    # SETTINGS: Change backend to "qpu" to use real quantum hardware
    backend_choice: Literal["simulator", "qpu", "aria1", "aquila"] = "aria1"  # Change to "qpu" for AWS Braket QPU
    shots: int = 1  # Number of runs

    # Run the experiment
    experiment = QuantumExperiment(backend=backend_choice, shots=shots) # $ 0.30 
    results = experiment.run_experiment()