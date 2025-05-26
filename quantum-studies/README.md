1. Understanding the Bell Algorithm

The Bell State is a maximally entangled two-qubit state:


|\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)


Circuit Construction
	•	Step 1: Apply a Hadamard (H) gate on qubit 0 → Creates superposition:  \frac{|0\rangle + |1\rangle}{\sqrt{2}} 
	•	Step 2: Apply a CNOT (CX) gate with qubit 0 as control and qubit 1 as target → Entangles them into the Bell state.

Quantum Circuit:
  Q0 ───H───■───
            │
  Q1 ───────X───



✔️ Superposition & Entanglement are fundamental to quantum computing
✔️ The Bell Algorithm is the simplest demonstration of quantum correlations
✔️ Amazon Braket’s local simulator is great for testing before using real QPUs



# Logging into AWS and running in a Real Quantum Computer
`aws-sso-util configure populate -u https://codility-aws-sso.awsapps.com/start --sso-region us-east-1 --region us-east-1`
`aws-sso-util run-as -r Eng-evaluations-dev-L3 -a 311929961626 /bin/bash`
