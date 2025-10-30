"""
Response Collection Helper for Week 2
This script helps me manually log LLM responses as I test each prompt
"""

import json
from datetime import datetime

# Load the prompts I created in Week 1
with open('experiment_prompts.json', 'r') as f:
    prompts = json.load(f)

# Initialize response storage
responses = {
    'metadata': {
        'experiment_date': datetime.now().isoformat(),
        'llms_tested': ['ChatGPT', 'Claude', 'Gemini'],  # Update based on what I actually use
        'responses_per_prompt': 2  # Getting 2 responses per prompt to save time
    },
    'results': {}
}

print("=" * 70)
print("RESPONSE COLLECTION TEMPLATE")
print("=" * 70)
print("\nI'll test each prompt with 2-3 different LLMs")
print("For each prompt, I'll get 2 responses to account for randomness\n")

# Show me what I need to test
prompt_count = 0
for hypothesis_id, hypothesis_data in prompts.items():
    print(f"\n### {hypothesis_id}: {hypothesis_data['hypothesis']} ###")
    
    for condition, prompt_text in hypothesis_data['prompts'].items():
        prompt_count += 1
        prompt_id = f"{hypothesis_id}_{condition}"
        
        print(f"\nPrompt {prompt_count}: {prompt_id}")
        print("-" * 70)
        print(prompt_text)
        print("-" * 70)
        print(f"✅ Test this with: ChatGPT (2x), Claude (2x), Gemini (2x)")
        print()

print("\n" + "=" * 70)
print(f"TOTAL: {prompt_count} prompts to test")
print(f"With 2 LLMs x 2 responses each = {prompt_count * 2 * 2} total responses needed")
print("=" * 70)

# Create template structure for responses
for hypothesis_id, hypothesis_data in prompts.items():
    responses['results'][hypothesis_id] = {
        'hypothesis': hypothesis_data['hypothesis'],
        'ground_truth_countries': hypothesis_data['ground_truth_countries'],
        'conditions': {}
    }
    
    for condition, prompt_text in hypothesis_data['prompts'].items():
        responses['results'][hypothesis_id]['conditions'][condition] = {
            'prompt': prompt_text,
            'llm_responses': {
                'ChatGPT': [],
                'Claude': [],
                'Gemini': []
            }
        }

# Save the template
with open('responses_template.json', 'w') as f:
    json.dump(responses, f, indent=2)

print("\n✅ Response template created: responses_template.json")
print("\nNEXT STEPS:")
print("1. Copy each prompt above")
print("2. Paste into ChatGPT (chat.openai.com) and save response")
print("3. Paste same prompt again to get 2nd response")
print("4. Repeat for Claude and Gemini")
print("5. I'll add all responses to the JSON file as I collect them")
