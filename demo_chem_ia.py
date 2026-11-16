
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# 1. Teste do RDKit
smiles = "CCO"  # Etanol

mol = Chem.MolFromSmiles(smiles)

if mol is None:
    raise ValueError("SMILES inválido!")

print("\n=== ANÁLISE MOLECULAR ===")
print(f"SMILES: {smiles}")
print(f"Massa molecular: {Descriptors.MolWt(mol):.2f} g/mol")
print(f"LogP: {Descriptors.MolLogP(mol):.2f}")
print(f"TPSA: {Descriptors.TPSA(mol):.2f} Å²")
print(f"HBD: {Lipinski.NumHDonors(mol)}")
print(f"HBA: {Lipinski.NumHAcceptors(mol)}")

# 2. Teste do Ollama + LangChain
print("\n=== TESTE DE INTELIGÊNCIA ARTIFICIAL ===")

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

resposta = llm.invoke([
    HumanMessage(
        content="Explique brevemente o que é LogP na química medicinal."
    )
])

print(resposta.content)
