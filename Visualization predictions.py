test_predictions = model.predict(valid_dataset, transformers)
import matplotlib.pyplot as plt
import deepchem as dc
from rdkit import Chem
from rdkit.Chem import Draw
# Visualize predictions
def visualize_predictions(dataset, predictions):
    mols = [Chem.MolFromSmiles(smiles) for smiles in dataset.ids]
    true_values = dataset.y
    predicted_values = predictions.flatten()

    for mol, true_value, predicted_value in zip(mols, true_values, predicted_values):
        print(f"True Value: {true_value}, Predicted Value: {predicted_value}")
        img = Draw.MolToImage(mol)
        plt.imshow(img)
        plt.show()

# Visualize predictions on the test set
visualize_predictions(valid_dataset, test_predictions)
     
