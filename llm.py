from transformers import pipeline, AutoTokenizer

class LanguageProcessor:
    def __init__(self):
        # English model
        self.en_llm = pipeline(
            'text-generation',
            model='gpt2-medium',
            device='cpu'
        )
        
        # Arabic model
        self.ar_tokenizer = AutoTokenizer.from_pretrained("aubmindlab/aragpt2-base")
        self.ar_llm = pipeline(
            'text-generation',
            model="aubmindlab/aragpt2-base",
            tokenizer=self.ar_tokenizer,
            device='cpu'
        )
    
    def generate_response(self, prompt, lang):
        try:
            if lang == 'ar':
                response = self.ar_llm(
                    prompt,
                    max_length=100,
                    num_return_sequences=1,
                    temperature=0.7
                )
            else:
                response = self.en_llm(
                    prompt,
                    max_length=100,
                    num_return_sequences=1,
                    temperature=0.7
                )
            return response[0]['generated_text'].replace(prompt, "").strip()
        except Exception as e:
            print(f"LLM Error: {e}")
            return "Sorry, I couldn't process that request."
