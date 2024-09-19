import subprocess

# Path to the ner.sh script in the current directory
ner_script = "./ner.sh"

# Input and output file paths (corrected to point to the parent directory)
wikipedia_input = "../wikipedia.txt"
fanwiki_input = "../fanwiki.txt"
wikipedia_output = "../stanford-wikipedia.txt"
fanwiki_output = "../stanford-fanwiki.txt"

# Command to run Stanford NER on wikipedia.txt
wikipedia_command = f"bash {ner_script} {wikipedia_input} > {wikipedia_output}"

# Command to run Stanford NER on fanwiki.txt
fanwiki_command = f"bash {ner_script} {fanwiki_input} > {fanwiki_output}"

# Execute the commands
subprocess.run(wikipedia_command, shell=True, check=True)
subprocess.run(fanwiki_command, shell=True, check=True)

print(f"NER tagging completed. Outputs saved to {wikipedia_output} and {fanwiki_output}.")
