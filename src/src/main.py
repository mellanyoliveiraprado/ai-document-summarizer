from dotenv import load_dotenv
from ai_service import GeminiSummarizer

def main():
    load_dotenv()
    summarizer = GeminiSummarizer()
    
    print("=== Processador de Textos com IA ===")
    sample_text = """
    A inteligência artificial generativa revolucionou o desenvolvimento de software.
    Engenheiros agora utilizam modelos de linguagem para automatizar a escrita de testes,
    documentar código e gerar trechos de algoritmos complexos. A integração rápida via APIs
    permite criar soluções escaláveis em poucas horas.
    """
    
    summary = summarizer.summarize(sample_text)
    print("\nResumo Gerado:\n")
    print(summary)

if __name__ == "__main__":
    main()
