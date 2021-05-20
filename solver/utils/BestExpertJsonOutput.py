import json
import os


def generate(experts, filename):
    data = {"experts": [], "best_experts": []}
    for expert in experts.best():
        data["best_experts"].append({'name': expert.name, 'expertise': expert.expertise})
    for expert in experts:
        data["experts"].append({'name': expert.name, 'expertise': expert.expertise,
                                'reinforce_dominates': [expert_d.name for expert_d in experts if
                                                        expert.reinforce_dominate(expert_d)
                                                        and expert != expert_d]})

    if os.path.isdir(filename):
        filename = os.path.join(filename, 'output.json')

    with open(filename, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))
