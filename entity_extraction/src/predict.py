import config
import torch
import numpy as np
import find_compounds
import model
import sys

#Load saved weights in order to predict new data
model = model.init_model()
model.load_state_dict(torch.load(config.MODEL_PATH))
model.cuda();
tag_values = config.tag_values
publications_filename = config.publications_filename

test_sentence = """
In the current work, we investigated the in vitro biochemical mechanism of Caffeic Acid Phenylethyl Ester (CAPE) toxicity and eight hydroxycinnamic/caffeic acid derivatives in vitro, using tyrosinase enzyme as a molecular target in human SK-MEL-28 melanoma cells. Enzymatic reaction models using tyrosinase/O(2) and HRP/H(2)O(2) were used to delineate the role of one- and two-electron oxidation. Ascorbic acid (AA), NADH and GSH depletion were used as markers of quinone formation and oxidative stress in CAPE induced toxicity in melanoma cells. Ethylenediamine, an o-quinone trap, prevented the formation of o-quinone and oxidations of AA and NADH mediated by tyrosinase bioactivation of CAPE. The IC(50) of CAPE towards SK-MEL-28 melanoma cells was 15muM. Dicoumarol, a diaphorase inhibitor, and 1-bromoheptane, a GSH depleting agent, increased CAPE's toxicity towards SK-MEL-28 cells indicating quinone formation played an important role in CAPE induced cell toxicity. Cyclosporin-A and trifluoperazine, inhibitors of the mitochondrial membrane permeability transition pore (PTP), prevented CAPE toxicity towards melanoma cells. We further investigated the role of tyrosinase in CAPE toxicity in the presence of a shRNA plasmid, targeting tyrosinase mRNA. Results from tyrosinase shRNA experiments showed that CAPE led to negligible anti-proliferative effect, apoptotic cell death and ROS formation in shRNA plasmid treated cells. Furthermore, it was also found that CAPE selectively caused escalation in the ROS formation and intracellular GSH (ICG) depletion in melanocytic human SK-MEL-28 cells which express functional tyrosinase. In contrast, CAPE did not lead to ROS formation and ICG depletion in amelanotic C32 melanoma cells, which do not express functional tyrosinase. These findings suggest that tyrosinase plays a major role in CAPE's selective toxicity towards melanocytic melanoma cell lines. Our findings suggest that the mechanisms of CAPE toxicity in SK-MEL-28 melanoma cells mediated by tyrosinase bioactivation of CAPE included quinone formation, ROS formation, intracellular GSH depletion and induced mitochondrial toxicity.
"""


def predict(test_sentence,model,tag_values):
    tokenized_sentence = config.tokenizer.encode(test_sentence)
    input_ids = torch.tensor([tokenized_sentence]).cuda()
    
    with torch.no_grad():
        output = model(input_ids)
    label_indices = np.argmax(output[0].to('cpu').numpy(), axis=2)
    
    # join bpe split tokens
    tokens = config.tokenizer.convert_ids_to_tokens(input_ids.to('cpu').numpy()[0])
    new_tokens, new_labels = [], []
    for token, label_idx in zip(tokens, label_indices[0]):
        if token.startswith("##"):
            new_tokens[-1] = new_tokens[-1] + token[2:]
        else:
            new_labels.append(tag_values[label_idx])
            new_tokens.append(token)
    
    for token, label in zip(new_tokens, new_labels):
        print("{}\t{}".format(label, token))
    
    for tok,lab in zip(new_tokens,new_labels):
      if lab == 1:
        print(tok,lab)

predict(test_sentence,model,tag_values)

sys.exit()

description_list = find_compounds.retrieve_classified_publications(publications_filename)

comps_found = find_compounds.find_compounds(description_list,model,tag_values)

print(comps_found)